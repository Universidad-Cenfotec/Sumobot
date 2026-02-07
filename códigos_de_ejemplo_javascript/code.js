/**
 * @file code.js
 * @description
 * Control principal de un robot seguidor de línea con detección de obstáculos
 * usando la IdeaBoard (Espruino).
 *
 * El programa utiliza `setInterval` como loop principal, facilitando
 * la lectura y el paralelismo con el concepto de `while True` en Python.
 *
 * Requisitos:
 *  - ideaboard.js
 *  - Módulo ultrasónico HC-SR04
 *
 * @author Emanuel Mena
 * @version 1.0.0
 */

const ib = require("ideaboard").connect();

/* ------------------------------------------------------------------
 * Ultrasonido (HC-SR04)
 * ------------------------------------------------------------------*/

/**
 * Última distancia medida por el sensor ultrasónico (cm).
 * -1 indica que aún no hay lectura válida.
 * @type {number}
 */
let lastDistCm = -1;

/**
 * Sensor ultrasónico frontal.
 */
const sonar = require("HC-SR04").connect(D25, D26, function (dist) {
  lastDistCm = dist;
});

/* ------------------------------------------------------------------
 * Sensores infrarrojos (línea)
 * ------------------------------------------------------------------*/

/**
 * Sensores infrarrojos analógicos (izq → der).
 */
const infrarrojos = [
  new ib.AnalogIn(D36),
  new ib.AnalogIn(D39),
  new ib.AnalogIn(D34),
  new ib.AnalogIn(D35)
];

/**
 * Convierte un arreglo de bits a un entero.
 * Ejemplo: [1,0,1,0] → 10
 *
 * @param {number[]} bits
 * @returns {number}
 */
function arreglo_a_entero(bits) {
  let valor = 0;
  for (let i = 0; i < bits.length; i++) {
    valor = (valor << 1) | (bits[i] ? 1 : 0);
  }
  return valor;
}

/**
 * Lee los sensores infrarrojos y devuelve su estado binario.
 *
 * @param {ib.AnalogIn[]} sensores
 * @param {number} [valor_critico=10000]
 * @returns {number[]} 1 = negro, 0 = blanco
 */
function leer_sensores(sensores, valor_critico) {
  valor_critico = valor_critico ?? 10000;
  return sensores.map(s => (s.value < valor_critico ? 1 : 0));
}

/**
 * Devuelve el estado combinado de la línea.
 *
 * @param {ib.AnalogIn[]} sensores
 * @param {number} valor_critico
 * @returns {number}
 */
function line_status(sensores, valor_critico) {
  return arreglo_a_entero(leer_sensores(sensores, valor_critico));
}

/* ------------------------------------------------------------------
 * Control de movimiento
 * ------------------------------------------------------------------*/

function stopMotors() {
  ib.pixel = [0, 0, 0];
  ib.motor_1.throttle = 0;
  ib.motor_2.throttle = 0;
}

function forward(speed) {
  ib.pixel = [0, 255, 0];
  ib.motor_1.throttle = speed;
  ib.motor_2.throttle = speed;
}

function backward(speed) {
  ib.pixel = [150, 255, 0];
  ib.motor_1.throttle = -speed;
  ib.motor_2.throttle = -speed;
}

function left(speed) {
  ib.pixel = [50, 55, 100];
  ib.motor_1.throttle = -speed;
  ib.motor_2.throttle = speed;
}

function right(speed) {
  ib.pixel = [50, 55, 100];
  ib.motor_1.throttle = speed;
  ib.motor_2.throttle = -speed;
}

function randomTurn(speed) {
  const dir = Math.random() < 0.5 ? -1 : 1;
  ib.pixel = [255, 0, 0];
  ib.motor_1.throttle = -dir * speed;
  ib.motor_2.throttle = dir * speed;
}

/* ------------------------------------------------------------------
 * Loop principal
 * ------------------------------------------------------------------*/

/**
 * Umbral de detección de línea.
 */
const LINE_THRESHOLD = 2950;

/**
 * Estado del robot.
 * Evita que el loop principal interrumpa acciones en curso.
 */
let busy = false;

/**
 * Iteración principal del robot.
 * Se ejecuta periódicamente por `setInterval`.
 */
function loop() {
  if (busy) return;

  const status = line_status(infrarrojos, LINE_THRESHOLD);
  console.log("Line status:", status);

  // Línea centrada → avanzar
  if (status === 0) {
    forward(0.5);
    return;
  }

  // Línea parcialmente detectada
  if (status >= 1 && status <= 3) {
    forward(1);
    return;
  }

  // Línea perdida → maniobra de recuperación
  busy = true;
  stopMotors();

  setTimeout(function () {
    backward(0.3);
    setTimeout(function () {
      randomTurn(0.3);
      setTimeout(function () {
        stopMotors();
        busy = false;
      }, 800);
    }, 800);
  }, 300);
}

/* ------------------------------------------------------------------
 * Inicio del programa
 * ------------------------------------------------------------------*/

/**
 * Delay inicial equivalente a `sleep(3)` en Python.
 */
setTimeout(function () {
  console.log("Rutina Iniciada");

  /**
   * Loop principal (equivalente a while True).
   * Se ejecuta cada 50 ms.
   */
  setInterval(loop, 50);

}, 3000);

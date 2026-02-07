/**
 * @file batalla.js
 * @description
 * Modo combate para Sumobot usando IdeaBoard (Espruino).
 *
 * El robot pelea en un dojo circular:
 *  - Sensores IR detectan el borde blanco (¡no caer!)
 *  - Sensor ultrasónico detecta al enemigo al frente
 *
 * El loop principal usa `setInterval`, similar a `while True` en Python.
 *
 * Requiere:
 *  - ideaboard.js
 *  - Módulo HC-SR04
 *
 * @author Emanuel Mena
 * @version 1.0.0
 */

const ib = require("ideaboard").connect();

/* ------------------------------------------------------------------
 * Sensor ultrasónico
 * ------------------------------------------------------------------*/

/**
 * Última distancia medida al frente (cm).
 * -1 = sin lectura válida
 * @type {number}
 */
let enemyDist = -1;

const sonar = require("HC-SR04").connect(D25, D26, function (dist) {
  enemyDist = dist;
});

/* ------------------------------------------------------------------
 * Sensores infrarrojos (borde del dojo)
 * Blanco = peligro
 * ------------------------------------------------------------------*/

const irSensors = [
  new ib.AnalogIn(D36),
  new ib.AnalogIn(D39),
  new ib.AnalogIn(D34),
  new ib.AnalogIn(D35)
];

/**
 * Umbral para detectar blanco (borde del dojo).
 * Ajustar según iluminación y superficie.
 */
const WHITE_THRESHOLD = 3000;

/**
 * Devuelve true si algún sensor detecta blanco.
 *
 * @returns {boolean}
 */
function dojoEdgeDetected() {
  for (let i = 0; i < irSensors.length; i++) {
    if (irSensors[i].value > WHITE_THRESHOLD) {
      return true;
    }
  }
  return false;
}

/* ------------------------------------------------------------------
 * Movimiento
 * ------------------------------------------------------------------*/

function stop() {
  ib.pixel = [0, 0, 0];
  ib.motor_1.throttle = 0;
  ib.motor_2.throttle = 0;
}

function attack(speed) {
  ib.pixel = [255, 0, 0]; // rojo = ataque
  ib.motor_1.throttle = speed;
  ib.motor_2.throttle = speed;
}

function retreat(speed) {
  ib.pixel = [255, 255, 0]; // amarillo = peligro
  ib.motor_1.throttle = -speed;
  ib.motor_2.throttle = -speed;
}

function spin(speed) {
  ib.pixel = [0, 0, 255]; // azul = búsqueda
  ib.motor_1.throttle = speed;
  ib.motor_2.throttle = -speed;
}

/* ------------------------------------------------------------------
 * Estados
 * ------------------------------------------------------------------*/

/**
 * Evita que el loop principal interrumpa maniobras críticas.
 */
let busy = false;

/* ------------------------------------------------------------------
 * Loop principal de combate
 * ------------------------------------------------------------------*/

/**
 * Distancia máxima para considerar enemigo cercano (cm).
 */
const ENEMY_RANGE = 40;

/**
 * Iteración principal del combate.
 */
function battleLoop() {
  if (busy) return;

  /* 1. PRIORIDAD ABSOLUTA: no caer del dojo */
  if (dojoEdgeDetected()) {
    busy = true;
    console.log("⚠️ BORDE DETECTADO");

    retreat(0.6);
    setTimeout(function () {
      spin(0.5);
      setTimeout(function () {
        stop();
        busy = false;
      }, 600);
    }, 500);

    return;
  }

  /* 2. Enemigo detectado → atacar */
  if (enemyDist !== -1 && enemyDist <= ENEMY_RANGE) {
    console.log("👊 ENEMIGO A LA VISTA:", enemyDist, "cm");
    attack(1.0);
    return;
  }

  /* 3. Nada detectado → buscar */
  console.log("🔍 BUSCANDO ENEMIGO");
  spin(0.3);
}

/* ------------------------------------------------------------------
 * Inicio del combate
 * ------------------------------------------------------------------*/

/**
 * Delay inicial tipo "listos... ya!"
 */
console.log(">>>Protocolo 1: Enlazar con Piloto<<<");

setTimeout(function() {
    console.log(">>>Protocolo 2: Cumplir la Misión<<<");
}, 1000);

setTimeout(function() {
    console.log(">>>Protocolo 3: Proteger al Piloto<<<");
}, 2000);

setTimeout(function() {
    console.log(">>>MODO BATALLA ACTIVADO<<<");
    
    /**
     * Loop principal del sumobot
     * Se inicia justo después del último mensaje
     */
    setInterval(battleLoop, 40);
    
}, 3000);
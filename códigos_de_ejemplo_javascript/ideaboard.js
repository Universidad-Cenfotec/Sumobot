/**
 * @file ideaboard.js
 * @description
 * Port de `ideaboard.py` (CircuitPython) por Bentley Born para la
 * IdeaBoard de CRCibernética, adaptado a JavaScript usando Espruino.
 *
 * Este módulo expone una API similar a CircuitPython para facilitar
 * el control de motores, servos, entradas/salidas digitales,
 * entradas analógicas y el NeoPixel integrado.
 *
 * @author Emanuel Mena
 * @version 1.0.0
 * @date 2026-02-06
 */

const neopixel = require("neopixel");

// -----------------------------
// Helpers
// -----------------------------

/**
 * Limita un valor dentro de un rango.
 *
 * @param {number} x Valor de entrada
 * @param {number} a Límite inferior
 * @param {number} b Límite superior
 * @returns {number} Valor limitado entre `a` y `b`
 */
function clamp(x, a, b) {
  return x < a ? a : x > b ? b : x;
}


/**
 * Mapea un valor desde un rango a otro.
 *
 * @param {number} x Valor a mapear
 * @param {number} inMin Mínimo del rango de entrada
 * @param {number} inMax Máximo del rango de entrada
 * @param {number} outMin Mínimo del rango de salida
 * @param {number} outMax Máximo del rango de salida
 * @returns {number} Valor mapeado al nuevo rango
 */
function map_range(x, inMin, inMax, outMin, outMax) {
  if (inMax === inMin) return outMin;
  return outMin + ((x - inMin) * (outMax - outMin)) / (inMax - inMin);
}


// Rainbow colorwheel
function colorwheel(pos) {
  pos = ((pos % 256) + 256) % 256;
  if (pos < 85) {
    return [pos * 3, 255 - pos * 3, 0];
  } else if (pos < 170) {
    pos -= 85;
    return [255 - pos * 3, 0, pos * 3];
  } else {
    pos -= 170;
    return [0, pos * 3, 255 - pos * 3];
  }
}

// NeoPixel en Espruino usa GRB. (por alguna razón)
// Para "hacerlo igual" a CircuitPython (RGB), convertimos a GRB al enviar.
function rgbToGrb(rgb) {
  const r = clamp(rgb[0] | 0, 0, 255);
  const g = clamp(rgb[1] | 0, 0, 255);
  const b = clamp(rgb[2] | 0, 0, 255);
  return new Uint8Array([g, r, b]);
}

/**
 * Controlador de motor DC usando dos pines PWM.
 * Permite controlar dirección y velocidad con un valor de -1 a 1.
 */
class DCMotor {

    /**
   * @param {Pin} pinA Pin PWM para giro positivo
   * @param {Pin} pinB Pin PWM para giro negativo
   * @param {Object} [opts] Opciones de configuración
   * @param {number} [opts.freq=50] Frecuencia PWM en Hz
   */
  constructor(pinA, pinB, opts) {

    opts = opts || {};
    this.pinA = pinA;
    this.pinB = pinB;
    this.freq = opts.freq || 50;
    this._throttle = 0;

    pinMode(this.pinA, "output");
    pinMode(this.pinB, "output");

    //Inicializa PWM una vez para reservar canal
    analogWrite(this.pinA, 0, { freq: this.freq });
    analogWrite(this.pinB, 0, { freq: this.freq });

    this.stop("coast");

    return this;
  }

    /**
   * Velocidad del motor.
   * Rango: -1 (máxima reversa) a 1 (máximo avance).
   *
   * @type {number}
   */
  get throttle() {
    return this._throttle;
  }


    /**
   * @param {number} value Valor entre -1 y 1
   */
  set throttle(value) {

    const t = clamp(+value || 0, -1, 1);
    this._throttle = t;

    const mag = Math.abs(t);

    if (mag === 0) {
      this.stop("coast");
      return;
    }

    if (t > 0) {
      digitalWrite(this.pinB, 0);
      analogWrite(this.pinA, mag, { freq: this.freq });
    } else {
      digitalWrite(this.pinA, 0);
      analogWrite(this.pinB, mag, { freq: this.freq });
    }
  }

  stop(mode) {
    mode = mode || "coast";
    if (mode === "brake") {
      digitalWrite(this.pinA, 1);
      digitalWrite(this.pinB, 1);
    } else {
      digitalWrite(this.pinA, 0);
      digitalWrite(this.pinB, 0);
    }
    this._throttle = 0;
  }
}

/**
 * Control de servo estándar por PWM.
 * Compatible con servos de 0 a 180 grados.
 */
class Servo {

    /**
   * @param {Pin} pin Pin PWM
   * @param {number} [freq=50] Frecuencia en Hz
   * @param {number} [min_pulse=500] Pulso mínimo en microsegundos
   * @param {number} [max_pulse=2500] Pulso máximo en microsegundos
   */
  constructor(pin, freq, min_pulse, max_pulse) {

    this.pin = pin;
    this.freq = freq || 50;
    this.min_pulse = min_pulse == null ? 500 : min_pulse;
    this.max_pulse = max_pulse == null ? 2500 : max_pulse;
    this._angle = 0;

    pinMode(this.pin, "output");
    this.angle = 0;
    return this;
  }

  get angle() {
    return this._angle;
  }

  set angle(deg) {
    const a = clamp(+deg || 0, 0, 180);
    this._angle = a;

    // Convertir ángulo a pulso (us)
    const pulseUs = this.min_pulse + (a / 180) * (this.max_pulse - this.min_pulse);

    // En Espruino analogWrite duty es 0..1
    // periodo = 1/freq segundos => en microsegundos:
    const periodUs = 1e6 / this.freq;
    const duty = clamp(pulseUs / periodUs, 0, 1);

    analogWrite(this.pin, duty, { freq: this.freq });
  }
}

/**
 * Entrada digital con soporte para resistencias pull-up y pull-down.
 */
class DigitalIn {
  /**
   * @param {Pin} pin Pin digital
   * @param {"UP"|"DOWN"|"input_pullup"|"input_pulldown"|null} pull Tipo de resistencia
   */
  constructor(pin, pull) {
    this.pin = pin;
    if (pull === "UP" || pull === "input_pullup") {
      pinMode(pin, "input_pullup")
    } else if (pull === "DOWN" || pull === "input_pulldown") {
      pinMode(pin, "input_pulldown")
    } else {
      pinMode(pin, "input")
    }

    return this;
  }
  get value() {
    return !!digitalRead(this.pin);
  }
}

class DigitalOut {
  constructor(pin) {
    this.pin = pin;
    pinMode(pin, "output");
    this._value = 0;
    digitalWrite(pin, 0);
    return this;
  }
  get value() {
    return this._value;
  }
  set value(v) {
    this._value = v ? 1 : 0;
    digitalWrite(this.pin, this._value);
  }
}

/**
 * Entrada analoga cruda de un pin.
 */
class AnalogIn {
  /**
   * 
   * @param {Pin} pin Pin de entrada analoga
   */
  constructor(pin) {
    this.pin = pin;
    return this;
  }
  
  // Emula CircuitPython: 0..65535, ya que Espruino maneja la lectura como un 
  // float entre 0 y 1 con cambios decimales
  get value() {
    return (analogRead(this.pin) * 65535) | 0;
  }

  // Útil para debug
  get raw() {
    return analogRead(this.pin); // 0..1
  }
}

/**
 * Salida de Voltages analogas a pines compatibles.
 */
class AnalogOut {
  /**
   * En placas con DAC, analogWrite produce voltaje DAC.
   * En otras, será PWM filtrable.
   * @param {Pin} pin 
   * @param {Object} [opts.freq=100] objeto con frequencia deseada en pines pwm
   */
  constructor(pin, opts) {
    opts = opts || {};
    this.pin = pin;
    this.freq = opts.freq || 1000;
    pinMode(pin, "output");
    this.value = 0;
    return this;
  }
  set value(v) {
    const x = clamp(+v || 0, 0, 65535);
    analogWrite(this.pin, x / 65535, { freq: this.freq });
  }
}

/**
 * Representa la placa IdeaBoard de CRCibernética.
 * Expone una API similar a CircuitPython para facilitar el aprendizaje
 * y la portabilidad de código educativo.
 */
class IdeaBoard {

  /**
   */
  constructor() {

    this.UP = "UP";
    this.DOWN = "DOWN";

    // Exponer subclases “igual” que en Python (ib.Servo(...))
    this.Servo = Servo;
    this.DigitalIn = DigitalIn;
    this.DigitalOut = DigitalOut;
    this.AnalogIn = AnalogIn;
    this.AnalogOut = AnalogOut;

    // NeoPixel
    this.neoPixelPin = D2;
    this._brightness = clamp(0.3, 0, 1);
    this._pixel = [0, 0, 0];
    this.pixel = [0, 0, 0];

    // Motores 
    const motorFreq = 50;
    this.motor_1 = new DCMotor(
      D12,
      D14,
      { freq: motorFreq }
    );
    this.motor_2 = new DCMotor(
      D13,
      D15,
      { freq: motorFreq }
    );

    this.map_range = map_range;
  }

    /**
   * Color actual del NeoPixel.
   * @type {number[]}
   */
  get pixel() {
    return this._pixel.slice();
  }
  /**
   * Brillo global del NeoPixel.
   * Rango válido: 0.0 a 1.0
   *
   * @type {number}
   */
  get brightness() {

    if (!Array.isArray(color) || color.length !== 3) {
      throw new Error("pixel debe ser [r,g,b] con 3 enteros (0..255)");
    }
    const r = clamp(color[0] | 0, 0, 255);
    const g = clamp(color[1] | 0, 0, 255);
    const b = clamp(color[2] | 0, 0, 255);

    this._pixel = [r, g, b];

    const br = this._brightness;
    const out = [(r * br) | 0, (g * br) | 0, (b * br) | 0];

    neopixel.write(this.neoPixelPin, rgbToGrb(out));
  }

  // Brightness 0..1
  get brightness() {
    return this._brightness;
  }

  set brightness(newBrightness) {
    const b = clamp(+newBrightness || 0, 0, 1);
    this._brightness = b;
    // re-escribe el color actual con nuevo brillo
    this.pixel = this._pixel;
  }

  // arcoiris: setter recibe n=0..255
  get arcoiris() {
    return this.pixel;
  }

  set arcoiris(n) {
    const c = colorwheel(n | 0);
    this.pixel = c;
  }
}

/**
 * Inicializa y devuelve una instancia de IdeaBoard.
 *
 * @returns {IdeaBoard} Instancia lista para usar
 */
exports.connect = function () {
  return new IdeaBoard();
}

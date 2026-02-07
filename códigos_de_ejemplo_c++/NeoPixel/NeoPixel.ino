//Fiorella Pérez López.
//Universidad Cenfotec.

#include <Adafruit_NeoPixel.h>

#define LED_PIN    2          // Pin donde está conectado el LED NeoPixel
#define NUM_LEDS   1          // Número de LEDs (solo uno)

Adafruit_NeoPixel strip(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);

String comando = "";          // Variable para guardar lo que escribe el usuario

void setup() {
  Serial.begin(115200);         // Inicia la comunicación serial
  strip.begin();              // Inicializa la tira de LEDs
  strip.show();               // Apaga todos los LEDs al inicio

  Serial.println("Escribe un color: rojo, verde, azul, amarillo, celeste, lila o blanco.");
  Serial.println("También puedes escribir STOP para apagar el LED y detener el programa.");
}

void loop() {
  if (Serial.available()) {
    comando = Serial.readStringUntil('\n'); // Lee hasta que se presione ENTER
    comando.trim();                         // Elimina espacios en blanco
    comando.toLowerCase();                  // Convierte a minúsculas

    if (comando == "rojo") {
      setColor(255, 0, 0);
    } else if (comando == "verde") {
      setColor(0, 255, 0);
    } else if (comando == "azul") {
      setColor(0, 0, 255);
    } else if (comando == "amarillo") {
      setColor(255, 255, 0);
    } else if (comando == "celeste") {
      setColor(0, 255, 255);
    } else if (comando == "lila") {
      setColor(255, 0, 255);
    } else if (comando == "blanco") {
      setColor(255, 255, 255);
    } else if (comando == "stop") {
      apagarLed();
      Serial.println("Programa detenido.");
      while (true); // Detiene el programa
    } else {
      Serial.println("Comando no reconocido. Intenta con: rojo, verde, azul, amarillo, celeste, lila, blanco o STOP.");
    }
  }
}

// Función para encender el LED con un color RGB
void setColor(uint8_t r, uint8_t g, uint8_t b) {
  strip.setPixelColor(0, strip.Color(r, g, b)); // Asigna el color
  strip.show();                                 // Muestra el color
}

// Función para apagar el LED
void apagarLed() {
  strip.setPixelColor(0, strip.Color(0, 0, 0)); // Apaga el LED
  strip.show();
}

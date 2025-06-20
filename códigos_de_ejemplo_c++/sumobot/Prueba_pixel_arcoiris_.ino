//Fiorella Pérez López.
//Universidad Cenfotec.

#include <Adafruit_NeoPixel.h> // Librería para controlar tiras de LEDs NeoPixel

// Define el pin de datos donde se conecta el LED y el número de LEDs
#define LED_PIN  2            // Pin digital 2 conectado al LED
#define NUM_LEDS 1            // Solo hay un LED NeoPixel

// Crea un objeto llamado 'strip' para controlar el LED
Adafruit_NeoPixel strip(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);

// Variable para guardar comandos escritos por el usuario desde el monitor serial
String comando = "";

/*
  Función que genera colores del arcoíris según una posición (0-255)
  Esta función se usa para crear un efecto de transición suave entre colores
*/
uint32_t Wheel(byte WheelPos) {
  if (WheelPos < 85) {
    // De rojo a verde
    return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
  } else if (WheelPos < 170) {
    WheelPos -= 85;
    // De verde a azul
    return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  } else {
    WheelPos -= 170;
    // De azul a rojo
    return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  }
}

void setup() {
  Serial.begin(9600);        // Inicia la comunicación con el monitor serial a 9600 baudios
  strip.begin();             // Inicializa el LED NeoPixel
  strip.show();              // Apaga el LED al comenzar (pone el color a negro)
  Serial.println("Escribe STOP para detener el programa."); // Instrucción para el usuario
}

void loop() {
  // Verifica si hay algún dato disponible en el monitor serial
  if (Serial.available()) {
    comando = Serial.readStringUntil('\n'); // Lee el texto hasta que se presione ENTER
    comando.trim(); // Elimina espacios en blanco o saltos de línea

    if (comando == "STOP") { // Si el usuario escribió "STOP"
      Serial.println("Programa detenido."); // Muestra mensaje
      while (true); // Se detiene el programa para siempre
    }
  }

  // Muestra un efecto de arcoíris en el LED
  for (int i = 0; i < 256; i++) {
    uint32_t color = Wheel(i);     // Obtiene un color del arcoíris
    strip.setPixelColor(0, color); // Asigna ese color al LED (posición 0)
    strip.show();                  // Actualiza el LED con ese color
    delay(20);                     // Espera 10 milisegundos para hacer la transición suave
  }
}



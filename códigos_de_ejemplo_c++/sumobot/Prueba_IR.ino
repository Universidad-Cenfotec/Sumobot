#include <Adafruit_NeoPixel.h>

// Pines analógicos conectados a los sensores infrarrojos
const int sen1 = 27;
const int sen2 = 33;
const int sen3 = 32;
const int sen4 = 35;

// Arreglo para facilitar el manejo de los sensores
int sensores[] = {sen1, sen2, sen3, sen4};

// Valor umbral para diferenciar entre blanco y negro
const int valor_critico = 1000;

// Configuración del NeoPixel
#define LED_PIN     2       // Pin al que está conectado el NeoPixel
#define NUM_LEDS    1       // Número de LEDs (solo uno en este caso)

Adafruit_NeoPixel strip(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);

// Variable para detener el programa si el usuario escribe "STOP"
bool detenido = false;

void setup() {
  Serial.begin(9600);  // Inicia la comunicación serial
  delay(1000);         // Breve pausa para estabilidad

  strip.begin();       // Inicializa el LED NeoPixel
  strip.show();        // Apaga el LED al inicio

  Serial.println("Escribe STOP para detener el programa.");
}

void loop() {
  // Si el programa está detenido, no hace nada
  if (detenido) {
    return;
  }

  // Revisa si el usuario ha escrito algo por el monitor serial
  if (Serial.available()) {
    String comando = Serial.readStringUntil('\n');  // Lee el texto hasta un salto de línea
    comando.trim();  // Elimina espacios innecesarios

    if (comando.equalsIgnoreCase("STOP")) {
      Serial.println("Programa detenido.");
      strip.setPixelColor(0, 0, 0, 0);  // Apaga el LED
      strip.show();                     // Actualiza el LED
      detenido = true;                 // Cambia el estado para detener el loop
      return;
    }
  }

  // Arreglo para guardar las lecturas (no se usa mucho en este caso, pero es útil si luego lo necesitas)
  int estado_sensores[4];

  Serial.println("Lecturas de sensores:");

  // Lee cada sensor uno por uno
  for (int i = 0; i < 4; i++) {
    int lectura = analogRead(sensores[i]);  // Lee el valor analógico
    estado_sensores[i] = lectura;           // Guarda la lectura (opcional)

    // Imprime la lectura por serial
    Serial.print("Sensor ");
    Serial.print(i + 1);
    Serial.print(": ");
    Serial.print(lectura);
    Serial.print(" - ");

    // Si la lectura es mayor al umbral, se interpreta como NEGRO
    if (lectura > valor_critico) {
      Serial.println("NEGRO");
      strip.setPixelColor(0, strip.Color(255, 0, 0));        // Rojo para negro
    } else {
      Serial.println("BLANCO");
      strip.setPixelColor(0, strip.Color(150, 150, 255));    // Azul claro para blanco
    }

    strip.show();   // Muestra el color en el LED
    delay(700);     // Espera un poco para que el color sea visible
  }

  Serial.println();  // Línea en blanco para separar ciclos
  delay(1000);       // Espera antes de la próxima ronda de lectura
}


// Tomás de Camino Beck & Jeffry Valverde 
// Escuela de Sistemas Inteligentes
// Universidad Cenfotec

// Definición de pines para motores y sensores
#define A_IN1 13  // Motor A, dirección 1
#define A_IN2 15  // Motor A, dirección 2
#define B_IN1 12  // Motor B, dirección 1
#define B_IN2 14  // Motor B, dirección 2

#define TRIG_PIN 26   // Pin TRIG del sensor ultrasónico
#define ECHO_PIN 25   // Pin ECHO del sensor ultrasónico

#define SENSOR_1 35   // Sensor IR 1
#define SENSOR_2 34   // Sensor IR 2
#define SENSOR_3 39   // Sensor IR 3
#define SENSOR_4 36   // Sensor IR 4

#define THRESHOLD 500 // Umbral para detección en sensores IR

// Variables para la medición de distancia
float duration, distance;

// Configura los motores con velocidades específicas
void setMotors(int speedA1, int speedA2, int speedB1, int speedB2) {
  analogWrite(A_IN1, speedA1);  // Velocidad en Motor A (dirección 1)
  analogWrite(A_IN2, speedA2);  // Velocidad en Motor A (dirección 2)
  analogWrite(B_IN1, speedB1);  // Velocidad en Motor B (dirección 1)
  analogWrite(B_IN2, speedB2);  // Velocidad en Motor B (dirección 2)
}

// Realiza un movimiento oscilatorio (izquierda-derecha) n veces
void wiggle(float t, int n, int speed) {
  for (int i = 0; i < n; i++) {
    setMotors(0, speed, speed, 0); // Gira hacia la izquierda
    delay(t * 1000);               // Espera t segundos
    setMotors(speed, 0, 0, speed); // Gira hacia la derecha
    delay(t * 1000);               // Espera t segundos
    stop();                        // Detiene los motores
    delay(t * 1000);               // Pausa entre ciclos
  }
}

// Avanza hacia adelante por un tiempo t con una velocidad dada
void forward(float t, int speed) {
  setMotors(speed, 0, speed, 0); // Ambos motores avanzan
  delay(t * 1000);               // Espera t segundos
  stop();                        // Detiene el robot
}

// Retrocede por un tiempo t con una velocidad dada
void backward(float t, int speed) {
  setMotors(0, speed, 0, speed); // Ambos motores retroceden
  delay(t * 1000);               // Espera t segundos
  stop();                        // Detiene el robot
}

// Gira a la izquierda por un tiempo t con una velocidad dada
void left(float t, int speed) {
  setMotors(0, speed, speed, 0); // Gira a la izquierda
  delay(t * 1000);               // Espera t segundos
  stop();                        // Detiene el robot
}

// Gira a la derecha por un tiempo t con una velocidad dada
void right(float t, int speed) {
  setMotors(speed, 0, 0, speed); // Gira a la derecha
  delay(t * 1000);               // Espera t segundos
  stop();                        // Detiene el robot
}

// Detiene ambos motores
void stop() {
  setMotors(0, 0, 0, 0); // Apaga ambos motores
}

// Realiza un giro aleatorio hacia la izquierda o derecha
void randomTurn(float t, int speed) {
  int dir = random(0, 2); // Genera 0 (izquierda) o 1 (derecha)
  if (dir == 0) {
    left(t, speed);       // Gira a la izquierda
  } else {
    right(t, speed);      // Gira a la derecha
  }
}

// Mide la distancia hacia adelante con el sensor ultrasónico
float lookForward() {
  stop();                         // Detiene el robot para medir
  digitalWrite(TRIG_PIN, LOW);    // Asegura que TRIG esté en LOW
  delayMicroseconds(2);           
  digitalWrite(TRIG_PIN, HIGH);   // Envía pulso TRIG
  delayMicroseconds(10);          // Duración del pulso
  digitalWrite(TRIG_PIN, LOW);    // Finaliza el pulso
  duration = pulseIn(ECHO_PIN, HIGH); // Mide la duración del pulso ECHO
  distance = (duration * 0.0343) / 2; // Convierte duración a distancia en cm
  delay(200);                     
  return distance;                // Retorna la distancia medida
}

// Realiza un escaneo girando hacia la izquierda hasta encontrar un objeto
bool scan() {
  stop();                         // Detiene el robot
  int maxCount = 10;              // Máximo número de intentos
  int count = 0;                  // Contador de intentos
  float dist = lookForward();     // Mide la distancia inicial
  while (count < maxCount && (dist > 30 || dist == -1)) {
    left(0.2, 150);               // Gira a la izquierda
    count++;                      // Incrementa el contador
    dist = lookForward();         // Mide nuevamente
    stop();                       // Detiene el robot
  }
  return (count < maxCount);      // Devuelve true si encuentra algo
}

// Avanza verificando constantemente los sensores IR
void forwardCheck(float t, int speed) {
  int d = int(t / 0.1); // Divide el tiempo en pasos de 0.1 segundos
  for (int i = 0; i < d; i++) {
    // Lee los valores de los sensores IR
    int sensorValue1 = analogRead(SENSOR_1);
    int sensorValue2 = analogRead(SENSOR_2);
    int sensorValue3 = analogRead(SENSOR_3);
    int sensorValue4 = analogRead(SENSOR_4);

    // Si algún sensor detecta un obstáculo
    if (sensorValue1 > THRESHOLD || sensorValue2 > THRESHOLD || 
        sensorValue3 > THRESHOLD || sensorValue4 > THRESHOLD) {
      stop();                     // Detiene el robot
      delay(300);                 
      backward(1, 150);           // Retrocede
      randomTurn(1, 150);         // Gira aleatoriamente
      return;                     // Sale de la función
    }
    forward(0.1, speed);          // Avanza por 0.1 segundos
  }
  stop();                         // Detiene el robot           
}

// Configuración inicial
void setup() {
  pinMode(TRIG_PIN, OUTPUT); // Configura TRIG como salida
  pinMode(ECHO_PIN, INPUT);  // Configura ECHO como entrada
  pinMode(A_IN1, OUTPUT);    // Pines de motores como salida
  pinMode(A_IN2, OUTPUT);
  pinMode(B_IN1, OUTPUT);
  pinMode(B_IN2, OUTPUT);

  Serial.begin(115200);          
}

// Ciclo principal
void loop() {
  if (scan()) {                   // Si encuentra un camino libre
    delay(200);                  
    forwardCheck(0.5, 200);       // Intenta avanzar
  } else {                        // Si no encuentra camino libre
    delay(200);                   
    randomTurn(1, 200);           // Gira aleatoriamente
    forwardCheck(0.5, 200);       // Intenta avanzar nuevamente
  }
  delay(200);
}
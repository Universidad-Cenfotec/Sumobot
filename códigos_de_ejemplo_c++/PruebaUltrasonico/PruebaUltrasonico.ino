// Universidad CENFOTEC
// Robot con evasión de obstáculos a 10 cm
//Mariana Cubero

// Pines de los motores
const int motorA_IN1 = 12;
const int motorA_IN2 = 14;
const int motorB_IN1 = 13;
const int motorB_IN2 = 15;

// Pines del sensor ultrasónico
const int trigPin = 25;  // TRIG conectado a GPIO25 (I025)
const int echoPin = 26;  // ECHO conectado a GPIO26 (I026)

// Umbral de detección (cm)
const float DISTANCIA_UMBRAL = 10.0;

void setup() {
  // Inicializar motores
  pinMode(motorA_IN1, OUTPUT);
  pinMode(motorA_IN2, OUTPUT);
  pinMode(motorB_IN1, OUTPUT);
  pinMode(motorB_IN2, OUTPUT);

  // Inicializar sensor ultrasónico
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  Serial.begin(115200);
  Serial.println("Iniciando robot con evasión de obstáculos...");
}

void loop() {
  float distancia = medirDistanciaCM();

  Serial.print("Distancia: ");
  Serial.print(distancia);
  Serial.println(" cm");

  if (distancia > 0 && distancia < DISTANCIA_UMBRAL) {
    Serial.println("¡Obstáculo detectado! Retrocediendo...");
    atras();
    delay(1000);

    Serial.println("Girando para evitar obstáculo...");
    girarDerecha();
    delay(1000); // Ajusta para dar una vuelta completa si lo deseas

    Serial.println("Reanudando avance...");
  } else {
    adelante();
  }

  delay(100);
}

// ---------------- FUNCIONES DE MOVIMIENTO ----------------

void adelante() {
  digitalWrite(motorA_IN1, HIGH);
  digitalWrite(motorA_IN2, LOW);
  digitalWrite(motorB_IN1, HIGH);
  digitalWrite(motorB_IN2, LOW);
}

void atras() {
  digitalWrite(motorA_IN1, LOW);
  digitalWrite(motorA_IN2, HIGH);
  digitalWrite(motorB_IN1, LOW);
  digitalWrite(motorB_IN2, HIGH);
}

void parar() {
  digitalWrite(motorA_IN1, LOW);
  digitalWrite(motorA_IN2, LOW);
  digitalWrite(motorB_IN1, LOW);
  digitalWrite(motorB_IN2, LOW);
}

void girarDerecha() {
  digitalWrite(motorA_IN1, HIGH);
  digitalWrite(motorA_IN2, LOW);
  digitalWrite(motorB_IN1, LOW);
  digitalWrite(motorB_IN2, HIGH);
}

// ---------------- SENSOR ULTRASÓNICO ----------------

float medirDistanciaCM() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duracion = pulseIn(echoPin, HIGH, 30000); // Timeout de 30 ms

  if (duracion == 0) {
    return -1; // No se detectó eco
  }

  float distancia = duracion * 0.0343 / 2.0;
  return distancia;
}
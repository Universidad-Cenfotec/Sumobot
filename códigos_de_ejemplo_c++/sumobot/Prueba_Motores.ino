//CODIGO PRUEBA DE MOTOTES C++

//Universidad CENFOTEC 
//Mariana Cubero

// Pines del Motor A
const int motorA_IN1 = 12;
const int motorA_IN2 = 14;

// Pines del Motor B
const int motorB_IN1 = 13;
const int motorB_IN2 = 15;

void setup() {
  // Configura los pines como salidas
  pinMode(motorA_IN1, OUTPUT);
  pinMode(motorA_IN2, OUTPUT);
  pinMode(motorB_IN1, OUTPUT);
  pinMode(motorB_IN2, OUTPUT);

  Serial.begin(115200);
  Serial.println("Iniciando control de motores...");
}

void loop() {
  // Adelante
  Serial.println("Adelante");
  adelante();
  delay(2000);

  // Parar
  // Aún es necesario parar antes de cambiar dirección de un motor!
  // Al igual que en CircuitPython el programa crashea si no lo haces
  // Pero aquí no se paran los motores cuando crashea!
  Serial.println("Parar");
  parar();
  delay(2000);

  // Atrás
  Serial.println("Atras");
  atras();
  delay(2000);

  Serial.println("Parar");
  parar();
  delay(2000);

  // Giro a la izquierda
  Serial.println("Girar izquierda");
  girarIzquierda();
  delay(1500);  // Ajusta este tiempo según el robot para que dé 1 vuelta

  Serial.println("Parar");
  parar();
  delay(2000);

  // Giro a la derecha
  Serial.println("Girar derecha");
  girarDerecha();
  delay(1500);  // Ajusta este tiempo según el robot

 
}

// Funciones de movimiento
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

void girarIzquierda() {
  digitalWrite(motorA_IN1, LOW);
  digitalWrite(motorA_IN2, HIGH);  // Motor A va atrás

  digitalWrite(motorB_IN1, HIGH);
  digitalWrite(motorB_IN2, LOW);   // Motor B va adelante
}

void girarDerecha() {
  digitalWrite(motorA_IN1, HIGH);
  digitalWrite(motorA_IN2, LOW);   // Motor A va adelante

  digitalWrite(motorB_IN1, LOW);
  digitalWrite(motorB_IN2, HIGH);  // Motor B va atrás
}
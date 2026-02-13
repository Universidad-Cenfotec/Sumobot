//CODIGO PRUEBA DE MOTORES C++

//Universidad CENFOTEC 
//Mariana Cubero

// Pines del Motor 1
const int motorA_IN1 = 12;
const int motorA_IN2 = 14;

// Pines del Motor 2
const int motorB_IN1 = 13;
const int motorB_IN2 = 15;


float speed = -1;

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
  moveMotor1(1);
  delay(2000);
  moveMotor1(0);
  delay(2000);
  moveMotor1(-1);
  delay(2000);
  moveMotor1(0);
  delay(2000);
  moveMotor1(0.5);
  delay(2000);
  moveMotor1(0);
  delay(2000);
  moveMotor1(-0.5);
  delay(2000);
  moveMotor1(0);
  delay(2000);
}


int motorMap(float value, float fromLow, float fromHigh, float toLow, float toHigh){
  return (int) toLow + (value - fromLow) * (toHigh - toLow) / (fromHigh - toLow);
}

bool moveMotor1(float s){
  if (s > 1 || s < -1){
    return false;
  } else if (s > 0){
    analogWrite(motorA_IN1,motorMap(s, 0, 1, 0, 255));
    digitalWrite(motorA_IN2, LOW);
  } else if (s < 0){
    digitalWrite(motorA_IN1, LOW);
    analogWrite(motorA_IN2,motorMap(s, -1, 0, 0, 255));
  } else {
    digitalWrite(motorA_IN1, LOW);
    digitalWrite(motorA_IN2, LOW);
  }

  return true;
}
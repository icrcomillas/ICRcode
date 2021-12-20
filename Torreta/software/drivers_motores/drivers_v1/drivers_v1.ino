#define Pin_1_driver 2
#define Pin_2_driver 3

void setup() {
  //Se configuran los pines como salida
  pinMode(Pin_1_driver,OUTPUT);
  pinMode(Pin_2_driver,OUTPUT);
  
  //Se establece la velocidad del puerto serial
  Serial.begin(115200);
  while(!Serial.available()){
    
  }
}

void loop() {
 //se ejecuta el código mientras el puerto serial se mantenga abierto
 while(Serial.available()>0){
      String data = Serial.readStringUntil(")");
      /*El formato de mensajes que se van a recibir es:
       * (MOTOR,angulo,MOTOR2,angulo)
       */
      int  yaw = data[3]-'0';
      int tilt = data[7] -'0';
      moverYaw(yaw);
      moverTilt(tilt);
 }

}
void moverYaw(int angulo){
  
}
void moverTilt(int angulo){
  
}

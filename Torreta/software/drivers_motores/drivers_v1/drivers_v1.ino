#include "DRV8825.h"

#define MODE0 10
#define MODE1 11
#define MODE2 12

//Pines de control
#define MOTOR_STEPS 200
#define RPM 120

#define DIR_YAW 5
#define STEP_YAW 2  //x
#define DIR_TILT 6  
#define STEP_TILT 3 //y
#define SLEEP 13 // optional (just delete SLEEP from everywhere if not used)

DRV8825 Tilt(MOTOR_STEPS, DIR_TILT, STEP_TILT, SLEEP, MODE0, MODE1, MODE2);
DRV8825 Yaw(MOTOR_STEPS, DIR_YAW, STEP_YAW, SLEEP, MODE0, MODE1, MODE2);

void setup() {
    /*
     * Microstepping mode: 1, 2, 4, 8, 16 or 32 (where supported by driver)
     * Mode 1 is full speed.
     * Mode 32 is 32 microsteps per step.
     * The motor should rotate just as fast (at the set RPM),
     * but movement precision is increased, which may become visually apparent at lower RPMs.
     */
    pinMode(DIR_YAW,OUTPUT);
    pinMode(STEP_YAW,OUTPUT);
    pinMode(DIR_TILT,OUTPUT);
    pinMode(STEP_TILT,OUTPUT);

    
    Yaw.begin(RPM);
    // if using enable/disable on ENABLE pin (active LOW) instead of SLEEP uncomment next line
    // stepper.setEnableActiveState(LOW);
    Yaw.enable();
    Tilt.begin(RPM);
    Tilt.enable();
    
    Yaw.setMicrostep(1);  
    Tilt.setMicrostep(1);  
  
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
       * YAW,angulo(3 posiciones),Dir,TILT,angulo(3 posiciones),Dir)
       * YAW y TILT no se envían, es unicamente para saber el orden de recepción
       */

     // Lectura de los valores del Strig de datos
      String stringYaw;
      String stringTilt; 
      //Datos del yaw
      stringYaw.concat(data[0]-'0');
      stringYaw.concat(data[1]-'0');
      stringYaw.concat(data[2]-'0');
      //Datos del tilt
      stringTilt.concat(data[6]-'0');
      stringTilt.concat(data[7]-'0');
      stringTilt.concat(data[8]-'0');

      //direcciones
      int dirYaw = data[4]-'0';
      int dirTilt = data[9]-'0';
      
      // Se convierte a Int
      int  yaw = stringYaw.toInt();
      int tilt = stringTilt.toInt();
      // Se mueven los motores
      moverYaw(yaw,dirYaw);
      moverTilt(tilt,dirTilt);
 }

}
void moverYaw(int angulo,int direccion){ 
  //Se establece la dirección
  if(direccion == 0){
    angulo = -1*angulo;
  }else{
    angulo = angulo;
  }
   Yaw.rotate(angulo);     // forward revolution + reverse -
}
void moverTilt(int angulo, int direccion){
  //Se establece la dirección
  if(direccion == 0){
    angulo = -1*angulo;
  }else{
    angulo = angulo;
  }
   
   Tilt.rotate(angulo);     // forward revolution + reverse -
}

/*
  Test ejecutado exitosamente.
  Si el giro es en sentido horario la secuencia es:
  (A B)
  (0 0)
  (0 1)
  (1 1)
  (1 0)

  Si el giro es en sentido anti-horario la secuencia es:
  (A B)
  (0 0)
  (1 0)
  (1 1)
  (0 1)

*/



#define ENC_IZQ_A 3
#define ENC_IZQ_B 2
int enc_izq_a=0;
int enc_izq_b=0;

void setup() {
  pinMode(ENC_IZQ_A, INPUT);
  pinMode(ENC_IZQ_B, INPUT);
  
  Serial.begin(1200);
  Serial.print("HOLA");
}

void loop() {
  
  enc_izq_a= digitalRead(ENC_IZQ_A);
  enc_izq_b= digitalRead(ENC_IZQ_B);

  /*Serial.print(enc_izq_a);
  Serial.print(" ");
  Serial.print(enc_izq_b);
  Serial.println(" ");*/

  Serial.println((enc_izq_a<<1)| enc_izq_b);
  
}

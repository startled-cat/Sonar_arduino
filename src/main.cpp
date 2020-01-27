
#include "Arduino.h"
#include <CheapStepper.h>

#define DEBUG 0

#define BAUD_RATE 38400

#define STEP_H_IN1 8
#define STEP_H_IN2 9
#define STEP_H_IN3 10
#define STEP_H_IN4 11

#define STEP_V_IN1 4
#define STEP_V_IN2 5
#define STEP_V_IN3 6
#define STEP_V_IN4 7

#define STEP_H_RPM 12
#define STEP_V_RPM 12

#define GREEN_LED 13
#define RED_LED 12

#define BLUE1 14
#define BLUE2 15
#define BLUE3 16

#define STEPS_FOR_ROTATION 4076

#define TRIGGRER 3
#define ECHO 2
#define SONAR_STOPTIME 150



union uint_buffer {
    unsigned int i;
    unsigned char c[2];
};

union ulong_buffer {
    unsigned long l;
    unsigned char a[4];
};


void sonar(byte, unsigned int, unsigned int);
unsigned long measure();

void blink_led(byte, unsigned int, byte);
void led_on(byte);
void led_off(byte);



// initialize the stepper library
CheapStepper myStepperH(STEP_H_IN1, STEP_H_IN2, STEP_H_IN3, STEP_H_IN4);
CheapStepper myStepperV(STEP_V_IN1, STEP_V_IN2, STEP_V_IN3, STEP_V_IN4);

bool moveClockwise = true;
bool moveClockwiseV = true;
byte measurements = 3;

unsigned int h_step = 200;
unsigned int v_step = 100;
bool h_move_direction = true;
bool v_move_direction = true;
int h_starting_pos = 0;
int v_starting_pos = 0;

void setup() {
  //setup leds
  pinMode(GREEN_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);
  pinMode(BLUE1, OUTPUT);
  pinMode(BLUE2, OUTPUT);
  pinMode(BLUE3, OUTPUT);

  led_on(GREEN_LED);
  led_on(RED_LED);
  led_on(BLUE1);
  led_on(BLUE2);
  led_on(BLUE3);
  delay(500);
  //

  myStepperH.setRpm(STEP_H_RPM);
  myStepperV.setRpm(STEP_V_RPM);
  
  myStepperH.set4076StepMode();
  myStepperV.set4076StepMode();
  h_starting_pos = myStepperH.getStep();
  v_starting_pos = myStepperV.getStep();



  Serial.begin(BAUD_RATE);
  while (!Serial) {
    blink_led(RED_LED, 1000, 10); // wait for serial port to connect. Needed for native USB port only
  }
  if (Serial.available() > 0) {
    char inByte = Serial.read();
    Serial.write(inByte);
  }
  
  delay(100);
  led_off(RED_LED);
  led_off(GREEN_LED);
  led_off(BLUE1);
  led_off(BLUE2);
  led_off(BLUE3);
}

void loop() {
  
  //odbierz dane dot pomiaru
  //1b - ilosc pomiarow na jednej pozycji
  //2b - krok poziomy
  //2b - krok pionowy // if == -1 then pomiar 2d

  //int h_step = 1;//krok poziomy silnika (w krokach silnika, a nie stopniach)
  //int v_step = 1;//krok pionowego silnika (w krokach silnika, a nie stopniach)
//
  //int how_many_measurements = 180 / h_step + 90 / v_step; //ilosc wszystkich pomiarow do zrobienia

  bool got_parameters = false;
  //while(!got_parameters){
  //getting number of measurements

  while(Serial.available() == 0){
    blink_led(GREEN_LED, 100, 1);
  }
  
  if (Serial.available() >= 1) {
    measurements = (byte)Serial.read();
    //Serial.write(1);
    got_parameters = true;
    if(measurements == (byte)2){
      led_on(GREEN_LED);
      led_on(BLUE1);
      delay(1000);
      led_off(GREEN_LED);
    }else{
      led_on(RED_LED);
      blink_led(BLUE1, 500, 3);
      led_off(RED_LED);
    } 
  }

  //getting h step
  if (Serial.available() >= 2) {
    char* buffer = (char*)calloc(3, sizeof(char));
    byte len = Serial.readBytes(buffer, 2);
    if(len == 2){
      //read 2b
      //convert to int
    
      union uint_buffer b;
      b.c[0] = buffer[0];
      b.c[1] = buffer[1];
      h_step = b.i;

      if(h_step == (unsigned int)185){
        led_on(GREEN_LED);
        led_on(BLUE2);
        got_parameters = true;
        delay(1000);
        led_off(GREEN_LED);
      }else{
        led_on(RED_LED);
        blink_led(BLUE2, 500, 3);
        got_parameters = false;
        led_off(RED_LED);

      }

    }else{
      
    }
    free(buffer);
  }

  //getting v step
  if (Serial.available() >= 2) {
    char* buffer = (char*)calloc(3, sizeof(char));
    byte len = Serial.readBytes(buffer, 2);
    if(len == 2){
      //read 2b
      //convert to int
      union uint_buffer b;
      b.c[0] = buffer[0];
      b.c[1] = buffer[1];
      v_step = b.i;

      if(v_step == (unsigned int)105){
        led_on(GREEN_LED);
        led_on(BLUE3);
        delay(1000);
        got_parameters = true;
        led_off(GREEN_LED);

      }else{
        led_on(RED_LED);
        blink_led(BLUE3, 500, 3);
        got_parameters = false;
        led_off(RED_LED);
      }
    }else{
      got_parameters = false;
    }
    free(buffer);
  }




  
  blink_led(RED_LED, 100, 10);

  

  //just for testing

  //Serial.println(measurements);
  //Serial.println(h_step);
  //Serial.println(v_step);

  if(1){

    do{
      //while pomiar not finished
      
      for(int curr_h_step = 0; curr_h_step < STEPS_FOR_ROTATION / 2 - 1; curr_h_step += h_step){

        if(DEBUG) Serial.println("moving horizontally by h_step)");

        myStepperH.move(h_move_direction, h_step);

        if(DEBUG) Serial.println("envoking sonar()");
        led_on(GREEN_LED);
        sonar(measurements, myStepperH.getStep(), myStepperV.getStep());
        led_off(GREEN_LED);
        delay(500);

      }

      if(DEBUG) Serial.println("changing horizontal direction");

      h_move_direction = !h_move_direction;
      //move one step up
      if(DEBUG) Serial.println("moving vertically up");
      myStepperV.move(v_move_direction, v_step);
    }while(!(myStepperV.getStep() != 0 && myStepperV.getStep() >= (STEPS_FOR_ROTATION / 6)));

    
    if(myStepperV.getStep() != 0 && myStepperV.getStep() >= (STEPS_FOR_ROTATION / 6)){
      //pomiar done, bo back to starting position
      if(DEBUG) Serial.println("pomiar done, resetting position ... ");
      myStepperH.moveTo(h_move_direction, h_starting_pos);
      myStepperV.moveTo(!v_move_direction, v_starting_pos);
      
      h_move_direction = !h_move_direction;
      //v_move_direction = !v_move_direction;
      //Serial.write()
      union ulong_buffer l;
      l.l = (unsigned long)0;
      Serial.write(l.a[0]);
      Serial.write(l.a[1]);
      Serial.write(l.a[2]);
      Serial.write(l.a[3]);
      //Serial.print(" h pos : ");
      Serial.write(1);
      Serial.write(1);
      //Serial.print(" v pos : ");
      Serial.write(1);
      Serial.write(1);
      Serial.println();
      //Serial.write(69);  
      while(true){
        int x = 1;
        int y = 7;
        x = y * x;
        blink_led(GREEN_LED, 1000, 1);
        // blink_led(RED_LED, 1000, 1);
      }
    }
  }else{
    //got wrong parameters

    while(false){
      unsigned long value = 4294967295;
      Serial.write(value);
      Serial.write(value >> 8);
      Serial.write(value >> 16);
      Serial.write(value >> 24);
      Serial.write(365);
      Serial.write(365 >> 8);
      Serial.write(366);
      Serial.write(366 >> 8);


      Serial.println();
      blink_led(BLUE1, 500, 1);
      blink_led(BLUE2, 500, 1);
      blink_led(BLUE3, 500, 1);
    }
  }
  




  // for(int i=0;i<4076;i++){
	//  if(i%220==0){
  //         sonar(measurements, i, 0);
  //     }
	//  // if(i==2148){
	//   if(i==2038){
	// 	  moveClockwise=!moveClockwise;
	//   }
	//   myStepperH.step(moveClockwise);
	// //  if(i%1019==0){
	// // 	 moveClockwiseV=!moveClockwiseV;
	// //  }
	// //	myStepperV.step(moveClockwiseV);
  // }
  // moveClockwise=!moveClockwise;
 
}

void sonar(byte measurements, unsigned int h_pos, unsigned int v_pos){
  unsigned long m[measurements];
  unsigned long avg = 0;
  for (byte i = 0; i < measurements; i++) {
		unsigned long temp = measure();
    m[i] = temp;
		// if (temp < 15*58) {
		// 	i--;
		// 	continue;
		// }else {
		// 	m[i] = temp;
		// }
    avg += temp;
		delay(SONAR_STOPTIME);
	}
  avg = avg / measurements;

	//Serial.print("avg : "); 

  union ulong_buffer l;
  l.l = (unsigned long)avg;
  Serial.write(l.a[0]);
  Serial.write(l.a[1]);
  Serial.write(l.a[2]);
  Serial.write(l.a[3]);
	//Serial.print(" h pos : ");
  h_pos += 32;
  Serial.write(h_pos);
  Serial.write(h_pos >> 8);
  h_pos -= 32;
  //Serial.print(" v pos : ");
  v_pos += 32;
  Serial.write(v_pos);
  Serial.write(v_pos >> 8);
  v_pos -= 32;
  Serial.println();
 // Serial.write(69); 
  
}

unsigned long measure() { 
	digitalWrite(TRIGGRER, LOW); //setting the high status on 2 uS pulse inicjalizujacy - see the documentation 
	delayMicroseconds(2); 
	digitalWrite(TRIGGRER, HIGH); //setting the high position for 10 uS pulse inicjalizujacy - see the documentation 
	delayMicroseconds(15); 
	digitalWrite(TRIGGRER, LOW); 
	digitalWrite(ECHO, HIGH); 
	//width of the reflected pulse in the uS divided by 58 is the distance in centimeters - see the documentation 
	return pulseIn(ECHO, HIGH);
} 

void blink_led(byte pin, unsigned int length, byte times){
  while(times--){
    digitalWrite(pin, HIGH);
    delay(length);
    digitalWrite(pin, LOW);
    delay(length);
  }
}

void led_on(byte pin){
  digitalWrite(pin, HIGH);
}

void led_off(byte pin){
  digitalWrite(pin, LOW);
}


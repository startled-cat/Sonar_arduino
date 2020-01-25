
#include "Arduino.h"
#include <CheapStepper.h>



#define STEP_H_IN1 8
#define STEP_H_IN2 9
#define STEP_H_IN3 10
#define STEP_H_IN4 11

#define STEP_V_IN1 4
#define STEP_V_IN2 5
#define STEP_V_IN3 6
#define STEP_V_IN4 7

#define STEPS_FOR_ROTATION 4076

#define TRIGGRER 3
#define ECHO 2
#define SONAR_STOPTIME 100

unsigned long measure();
void sonar(int measurements, int h_pos, int v_pos);


// initialize the stepper library on pins 8 through 11:
CheapStepper myStepperH(STEP_H_IN1, STEP_H_IN2, STEP_H_IN3, STEP_H_IN4);
CheapStepper myStepperV(STEP_V_IN1, STEP_V_IN2, STEP_V_IN3, STEP_V_IN4);

bool moveClockwise = true;
bool moveClockwiseV = true;
unsigned long moveStartTime = 0; // this will save the time (millis()) when we started each new move
int measurements = 1;

int h_step = 200;
int v_step = 100;
bool h_move_direction = true;
bool v_move_direction = true;
int h_starting_pos = 0;
int v_starting_pos = 0;

void setup() {
  // initialize the serial port:
  //Serial.begin(BAUD_RATE);

  myStepperH.setRpm(5);
  myStepperV.setRpm(5);

  Serial.begin(115200);
  //Serial.print("stepper H RPM: "); Serial.print(myStepperH.getRpm());
  //Serial.print("stepper V RPM: "); Serial.print(myStepperV.getRpm());

  //Serial.print("stepper delay (micros): "); Serial.print(myStepperH.getDelay());
  //Serial.print("stepper delay (micros): "); Serial.print(myStepperV.getDelay());

  //Serial.println();
  myStepperH.set4076StepMode();
  myStepperV.set4076StepMode();
  h_starting_pos = myStepperH.getStep();
  v_starting_pos = myStepperV.getStep();
}

void loop() {
  
  //odbierz dane dot pomiaru
  //2b - krok poziomy
  //2b - krok pionowy // if == -1 then pomiar 2d
  //1b - ilosc pomiarow na jednej pozycji

  //int h_step = 1;//krok poziomy silnika (w krokach silnika, a nie stopniach)
  //int v_step = 1;//krok pionowego silnika (w krokach silnika, a nie stopniach)
//
  //int how_many_measurements = 180 / h_step + 90 / v_step; //ilosc wszystkich pomiarow do zrobienia
  //int tab[how_many_measurements];


  //int stepsLeft = myStepperH.getStepsLeft();
  //Serial.println("stepper h position : " + myStepperH.getStep());
  //Serial.println("stepper v position : " + myStepperV.getStep());
  //Serial.println();



  //delay(1000);

  for(int curr_h_step = 0; curr_h_step < STEPS_FOR_ROTATION / 2; curr_h_step += h_step){

    Serial.println("moving horizontally by h_step)");

    myStepperH.move(h_move_direction, h_step);

    Serial.println("envoking sonar()");

    sonar(measurements, myStepperH.getStep(), myStepperV.getStep());

    //delay(500);
  }

  Serial.println("changing horizontal direction");

  h_move_direction = !h_move_direction;
  //move one step up
  Serial.println("moving vertically up");
  myStepperV.move(v_move_direction, v_step);

  
  if(myStepperV.getStep() != 0 && myStepperV.getStep() >= (STEPS_FOR_ROTATION / 4)){
    //pomiar done, bo back to starting position
    Serial.println("pomiar done, resetting position ... ");
    myStepperH.moveTo(h_move_direction, h_starting_pos);
    myStepperV.moveTo(!v_move_direction, v_starting_pos);
    
    h_move_direction = !h_move_direction;
    //v_move_direction = !v_move_direction;
    while(false){
      int x = 1;
      int y = 7;
      x = y * x;
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

void sonar(int measurements, int h_pos, int v_pos){
  unsigned long m[measurements];
  for (int i = 0; i < measurements; i++) {
		unsigned long temp = measure();
		if (temp < 15*58) {
			//i--;
			continue;
		}else {
			m[i] = temp;
		}
		delay(SONAR_STOPTIME);
	}

  unsigned long avg = 0;

	for (int i = 0; i < measurements; i++) {
    avg += m[i];
	}

  avg = avg / measurements;

	Serial.print("avg : "); Serial.print(avg); 
	Serial.print(" h pos : ");Serial.print(h_pos);
  Serial.print(" v pos : ");Serial.print(v_pos);
  Serial.println(); 
  
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
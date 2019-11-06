#include <Servo.h>
#include "Arduino.h"

#define SERVO_STOPTIME 50
#define SONAR_STOPTIME 100

#define RED_LED 2
#define SERVO 3
#define MOSFET 4
#define TRIGGRER 7
#define ECHO 6

#define MEASUREMENTS 3

Servo myservo;
int pos = 0;
int inc = 1;
unsigned long m[MEASUREMENTS];

unsigned long measure();
void print();
void print_all();

void setup() {
	Serial.begin(9600); //inicjalizaja monitor serial port 
	myservo.attach(SERVO); 
	
	//pinMode(MOSFET, OUTPUT);
	pinMode(RED_LED, OUTPUT);
	pos = 190;//myservo.read();
	
	
}

void loop() {
	if(pos > 180){
		myservo.write(0);
		digitalWrite(RED_LED,HIGH);
		delay(1000);
		int bytes = 0;
		do{
			bytes = Serial.read();
			Serial.write(bytes);
		}while(bytes <= 0);
		digitalWrite(RED_LED,LOW);
		pos = 0;
	}
	
	myservo.write(pos);  
	delay(SERVO_STOPTIME);    
	
	for(int i = 0; i < MEASUREMENTS; i++){
		unsigned long temp = measure();
		if(temp < 15*58){
			i--;
			continue;
		}else{
			m[i] = temp;
		}
		
	}
	
	print();

	pos += inc;
	/*
	if(pos >= 180){
		inc = -1;

	}else if(pos <= 0){
		inc = 1;
	}
	*/
	
	//delay(50);
  
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
void print(){
	Serial.print(pos); 
	for(int i = 0; i < MEASUREMENTS; i++){
		Serial.print(",");
		Serial.print(m[i]);
	}
	Serial.println(); 
}

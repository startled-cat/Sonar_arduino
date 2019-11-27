#include <Servo.h>
#include "Arduino.h"

#define SERVO_STOPTIME 200
#define SONAR_STOPTIME 100

#define RED_LED 2
#define SERVO 3
#define MOSFET 4
#define TRIGGRER 7
#define ECHO 6

Servo myservo;
int pos = 0;
int BigInc = 30;
int SmallInc = 1;
int dec = 0;
int CountJumps = 0;
int volatile Measurements = 1;
bool GetNumber = true;

unsigned long measure();
void print(int Measurements, unsigned long m[]);
void print_all();

void setup() {
	Serial.begin(9600); //inicjalizaja monitor serial port 
	myservo.attach(SERVO); 
	
	//pinMode(MOSFET, OUTPUT);
	pinMode(RED_LED, OUTPUT);
	pos = 0;//190;//myservo.read();
}

void loop() {
	if (GetNumber) {
		while (!Serial.available()) {}
		char UserInput = Serial.read();

		if (UserInput == '2' || UserInput == '3') {
			Measurements = UserInput - '0';
		}

		GetNumber = false;
	}

	unsigned long m[Measurements];

	myservo.write(pos);  
	delay(SERVO_STOPTIME); 	
	delay(700);  
	for (int i = 0; i < Measurements; i++) {
		
		unsigned long temp = measure();
		if (temp < 15*58) {
			i--;
			continue;
		} else {
			m[i] = temp;
		}
		delay(200);
	}
	
	print(Measurements, m);

	if (pos >= 180) {
		myservo.write(0);
		digitalWrite(RED_LED,HIGH);
		delay(1000);
		int bytes = 0;
		do {
			bytes = Serial.read();
			Serial.write(bytes);
		} while(bytes <= 0);
		digitalWrite(RED_LED,LOW);
		pos = 0;
	}	

	pos += BigInc;
	CountJumps++; 

	if (CountJumps > 5) {
		pos = 0;
		pos += SmallInc;
		SmallInc += 1;
		CountJumps = 0;
	}
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

void print(int Measurements, unsigned long m[]) {
	Serial.print(pos); 
	for (int i = 0; i < Measurements; i++) {
		Serial.print(",");
		Serial.print(m[i]);
	}
	Serial.println(); 
}

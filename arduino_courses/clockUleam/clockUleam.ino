#include<LiquidCrystal.h>



//const int d4=2,d5=3,d6=4,d7=5,rs=6,en=7;
//LiquidCrystal lcd(rs,en,d4,d5,d6,d7);
int led2=2;
int led3=3;
int led4=4;
int led5=5;
int led6=6;


void setup() {
  pinMode(led2, OUTPUT);    // sets the digital pin 2 as output#
  pinMode(led3, OUTPUT);    // sets the digital pin 3 as output#
  pinMode(led4, OUTPUT);    // sets the digital pin 4 as output#

  pinMode(led5, OUTPUT);    // sets the digital pin 5 as output#
  pinMode(led6, OUTPUT);    // sets the digital pin 6 as output#


}

void loop() {
  digitalWrite(led2, HIGH); // sets the digital pin 13 on
  delay(200);            // waits for a second
  digitalWrite(led2, LOW);  // sets the digital pin 13 off
  delay(200);            // waits for a second

  digitalWrite(led3, HIGH); // sets the digital pin 13 on
  delay(200);            // waits for a second
  digitalWrite(led3, LOW);  // sets the digital pin 13 off
  delay(200);            // waits for a second

  digitalWrite(led4, HIGH); // sets the digital pin 13 on
  delay(200);            // waits for a second
  digitalWrite(led4, LOW);  // sets the digital pin 13 off
  delay(200);            // waits for a second



  digitalWrite(led5, HIGH); // sets the digital pin 13 on
  delay(200);            // waits for a second
  digitalWrite(led5, LOW);  // sets the digital pin 13 off
  delay(200);            // waits for a second


  digitalWrite(led6, HIGH); // sets the digital pin 13 on
  delay(200);            // waits for a second
  digitalWrite(led6, LOW);  // sets the digital pin 13 off
  delay(200); 

  
}

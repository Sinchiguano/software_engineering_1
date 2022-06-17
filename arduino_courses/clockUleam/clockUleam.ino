#include<LiquidCrystal.h>



//Crear el objeto LCD con los números correspondientes (rs, en, d4, d5, d6, d7)
LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

//initializing  the variables
int hrs=10;
int mins=0;
int sec=0;
//varible for checking the time
int TIME=0;



const int bhrs=0;
const int bmins=0;
int state1=0;
int state2=0;

void setup() {
  //mode for the push buttons
  pinMode(bhrs, INPUT_PULLUP);
  pinMode(bmins, INPUT_PULLUP);
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);


}
/////////////////////////////////
void loop()
{
lcd.setCursor(0,0);
sec=sec+1;

//displaying the time
lcd.print("Time:");
lcd.print(hrs);
lcd.print(":");
lcd.print(mins);
lcd.print(":");
lcd.print(sec);
lcd.print(" AM");


//checking for the AM and PM as the status changes after 12 o'clocl

delay(800);
//lcd.clear();

////////////////////////////
if (sec==60) {
  sec=0;
  mins=mins+1;
  delay(10);
  lcd.clear();
}
if (mins==60) {
  mins=0;
  hrs=hrs+1;
  delay(10);
  lcd.clear();
}
if (hrs==13) {
  hrs=0;
}
lcd.setCursor(0,1);
lcd.print("ULEAM>>El CARMEN");

//read the state of the buttons for hours setting
  if (state1==1) {
    hrs=hrs+1;
  }
}



/*
// set up the LCD's number of columns and rows:

lcd.begin(16, 2);

// Print a message to the LCD.

lcd.print("hello, world!");; // sets the digital pin 13 on
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
*/

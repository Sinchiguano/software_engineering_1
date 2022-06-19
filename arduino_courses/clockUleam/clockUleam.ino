#include<LiquidCrystal.h>



//Crear el objeto LCD con los números correspondientes (rs, en, d4, d5, d6, d7)
LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

//initializing  the variables
int hrs=12;
int mins=0;
int sec=0;
//varible for checking the time
int TIME=0;



const int bhrs=2;
const int bmins=3;
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



//checking for the AM and PM as the status changes after 12 o'clocl
if (TIME >=12) lcd.print(" AM");
if (TIME <=11) lcd.print(" PM");
if (TIME==24)  TIME=0;
delay(800);
lcd.clear();
////////////////////////////
if (sec==60) {
  sec=0;
  mins=mins+1;
}
if (mins==60) {
  mins=0;
  hrs=hrs+1;
  TIME=TIME+1;
}
if (hrs==13) {
  hrs=0;
}
lcd.setCursor(0,1);
lcd.print("ULEAM>>El CARMEN");

//read the state of the buttons for hours setting
state1=digitalRead(bhrs);
  if (state1==0) {
    hrs=hrs+1;
    TIME=TIME+1;
    if (TIME <=11)  lcd.print(" PM");
    if (TIME==24)  TIME=0;
    if (hrs==13) hrs=1;
  }
state2=digitalRead(bmins);
if (state2==0) {
  sec=0;
  mins=mins+1;
}





}



/*


if (state1==0) {
  hrs=hrs+1;
  if (TIME==12) {
    lcd.print(" PM");
  }
  if (TIME==24) {
    TIME=0;
  }
  if (hrs=13) {
    hrs=1;
  }
}


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

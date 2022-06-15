#include<LiquidCrystal.h>


//const int rs,en,d4,d5,d6,d7;
const int d4=2,d5=3,d6=4,d7=5;
const int rs=6,en=7;
LiquidCrystal lcd(rs,en,d4,d5,d6,d7);



// make some custom characters:
byte heart[8] = {
  0b00000,
  0b01010,
  0b11111,
  0b11111,
  0b11111,
  0b01110,
  0b00100,
  0b00000
};

void setup() {
 
  lcd.begin(16,2);//setup numbers and rows of my LCD
  //lcd.print("Hello World");
  //initialize the serial communications
  Serial.begin(9600);

    // create a new character
  lcd.createChar(0, heart);


    // Print a message to the lcd.
  lcd.print("I ");
  lcd.write(byte(0)); // when calling lcd.write() '0' must be cast as a byte
  lcd.print(" Arduino! ");
  lcd.write((byte)1);
  

}

void loop() {
  // read the potentiometer on A0:
  int sensorReading = analogRead(A0);
  // map the result to 200 - 1000:
  int delayTime = map(sensorReading, 0, 1023, 200, 1000);
  // set the cursor to the bottom row, 5th position:
  lcd.setCursor(4, 1);
  // draw the little man, arms down:
  lcd.write(3);
  delay(delayTime);
  lcd.setCursor(4, 1);
  // draw him arms up:
  lcd.write(4);
  delay(delayTime);



}

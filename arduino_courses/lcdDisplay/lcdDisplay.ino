#include<LiquidCrystal.h>


//const int rs,en,d4,d5,d6,d7;
const int d4=2,d5=3,d6=4,d7=5;
const int rs=6,en=7;
LiquidCrystal lcd(rs,en,d4,d5,d6,d7);


void setup() {
  // put your setup code here, to run once:
  lcd.begin(16,2);
  lcd.print("Hello World");
  

}

void loop() {
  // put your main code here, to run repeatedly:


  lcd.setCursor(0,1);
  lcd.print(millis()/1000);


}

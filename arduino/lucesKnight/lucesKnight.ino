#include<LiquidCrystal.h>



//const int d4=2,d5=3,d6=4,d7=5,rs=6,en=7;
//LiquidCrystal lcd(rs,en,d4,d5,d6,d7);


int timer=20;
void setup() {

for(int thisPin=2;thisPin<8;thisPin++){
  
  
  pinMode(thisPin,OUTPUT);
  }

}

void loop() 
{
for(int thisPin=2;thisPin<8;thisPin++){
  digitalWrite(thisPin,HIGH);
  delay(timer);
  digitalWrite(thisPin,LOW);
  delay(timer);
  }
for(int thisPin=6;thisPin>2;thisPin--){
  digitalWrite(thisPin,HIGH);
  delay(timer);
  digitalWrite(thisPin,LOW);
  delay(timer);
  }

  


  
}

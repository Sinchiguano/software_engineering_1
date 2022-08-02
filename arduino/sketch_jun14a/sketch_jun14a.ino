
int pinArray[]={2,3,4,5,6};
int timer=60;


void setup() {
  // put your setup code here, to run once:


  for (int i=0;i<6;i++)
  {
    pinMode(pinArray[i],OUTPUT);
    }


}

void loop() {
  // put your main code here, to run repeatedly:

for(int i=0;i<6;i++){
digitalWrite(pinArray[i],HIGH);  
delay(timer);
digitalWrite(pinArray[i],LOW);  
delay(timer*2);
  }

for(int p=5;p>=0;p--){
digitalWrite(pinArray[p],HIGH);  
delay(timer);
digitalWrite(pinArray[p],LOW);  
delay(timer*2);
  }


}

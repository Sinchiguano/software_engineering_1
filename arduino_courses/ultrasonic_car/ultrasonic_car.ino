

//#define echo_Pin 3
//#define trig_Pin 2


//define variables
//ultrasonic variables
long timePulse;
int distance;
const int trig_Pin=2;
const int echo_Pin=3;
//motor variable
int in1=4;//motor1
int in2=5;//motor1
int in3=6;//motor2
int in4=7;//motor2


void setup() {
  // put your setup code here, to run once:
pinMode(trig_Pin, OUTPUT);// set teh trigger as output
pinMode(echo_Pin,INPUT);//set echo as input

//serial communication
Serial.begin(9600);
Serial.println("Ultrasonic Sensor");
Serial.println("With Arduino UNO");


//motor setup
pinMode(in1,OUTPUT);
pinMode(in2,OUTPUT);
pinMode(in3,OUTPUT);
pinMode(in4,OUTPUT);


}

void loop() {
  // clears the trigger condition
digitalWrite(trig_Pin,LOW);
delayMicroseconds(2);
//set the trigger pin HIGH
digitalWrite(trig_Pin,HIGH);
delayMicroseconds(10);
digitalWrite(trig_Pin,LOW);
//read the echo pin in microseconds
timePulse=pulseIn(echo_Pin,HIGH);
//compute the distance with the basic equation
distance=timePulse*0.034/2;
Serial.print("Distance: ");
Serial.print(distance);
Serial.println(" cm");


  //script to command the car forward
  if (distance>19) {
    digitalWrite(in1,HIGH);
    digitalWrite(in2,LOW);
    digitalWrite(in3,HIGH);
    digitalWrite(in4,LOW);
  }
  if (distance<18) {
    //STOP MOTORS
    digitalWrite(in1,LOW);
    digitalWrite(in2,LOW);
    digitalWrite(in3,LOW);
    digitalWrite(in4,LOW);

    delay(500);

    //MOVE BACKWARD
    digitalWrite(in1,LOW);
    digitalWrite(in2,HIGH);
    digitalWrite(in3,LOW);
    digitalWrite(in4,HIGH);

    //STOP MOTORS
    digitalWrite(in1,LOW);
    digitalWrite(in2,LOW);
    digitalWrite(in3,LOW);
    digitalWrite(in4,LOW);

    delay(100);

    //TURN RIGHT THE CAR
    digitalWrite(in1,HIGH);
    digitalWrite(in2,LOW);
    digitalWrite(in3,LOW);
    digitalWrite(in4,LOW);
    delay(500);
   }

}

/*************************************************************

  This is a simple demo of sending and receiving some data.
  Be sure to check out other examples!
 *************************************************************/

// Template ID, Device Name and Auth Token are provided by the Blynk.Cloud
// See the Device Info tab, or Template settings

#define BLYNK_TEMPLATE_ID "TMPLqP9NcMDT"
#define BLYNK_DEVICE_NAME "homeAutomation"
#define BLYNK_AUTH_TOKEN "vsAF-tthi-Dmvned1EkXoWnrUZVzzLqc"

// Comment this out to disable prints and save space
#define BLYNK_PRINT Serial


#include <WiFi.h>
#include <WiFiClient.h>
#include <BlynkSimpleEsp32.h>


//VARIABLES DECLARATION
/********************/
// Your WiFi credentials.
// Set password to "" for open networks.
char ssid[] = "Hostal_Guayaquil_3";
char pass[] = "16081987";
char auth[] = BLYNK_AUTH_TOKEN;
#define GPIO_D15 15
#define GPIO_D2 2
#define GPIO_D4 4
#define GPIO_D5 5
#define GPIO_D18 18


#define GPIO_D22 22
#define GPIO_D23 23

// Relay State
bool toggleState_1 = LOW; //Define integer to remember the toggle state for relay 1

// We make these values volatile, as they are used in interrupt context
volatile bool pinChanged = false;
volatile int  pinValue   = 0;

// This function is called every time the Virtual Pin 0 state changes
BLYNK_WRITE(V0)
{
  // Set incoming value from pin V0 to a variable
  int value = param.asInt();

  // Update state
  Blynk.virtualWrite(V0, value);
  if(param.asInt() == 1){
    digitalWrite(GPIO_D15,HIGH);
  }
  else
  {
    digitalWrite(GPIO_D15,LOW);
  }
}


BLYNK_WRITE(V1)
{
  // Set incoming value from pin V0 to a variable
  int value = param.asInt();

  // Update state
  Blynk.virtualWrite(V1, value);
  if(param.asInt() == 1){
    digitalWrite(GPIO_D2,HIGH);
  }
  else
  {
    digitalWrite(GPIO_D2,LOW);
  }
}

BLYNK_WRITE(V2)
{
  // Set incoming value from pin V0 to a variable
  int value = param.asInt();

  // Update state
  Blynk.virtualWrite(V2, value);
  if(param.asInt() == 1){
    digitalWrite(GPIO_D4,HIGH);
  }
  else
  {
    digitalWrite(GPIO_D4,LOW);
  }
}

BLYNK_WRITE(V3)
{
  // Set incoming value from pin V0 to a variable
  int value = param.asInt();

  // Update state
  Blynk.virtualWrite(V3, value);
  if(param.asInt() == 1){
    digitalWrite(GPIO_D5,HIGH);
  }
  else
  {
    digitalWrite(GPIO_D5,LOW);
  }
}

BLYNK_WRITE(V4)
{
  // Set incoming value from pin V0 to a variable
  int value = param.asInt();

  // Update state
  Blynk.virtualWrite(V4, value);
  if(param.asInt() == 1){
    digitalWrite(GPIO_D18,HIGH);
  }
  else
  {
    digitalWrite(GPIO_D18,LOW);
  }
}

void CHECKPIN() {
  // Invert state, since button is "Active LOW"
  pinValue = !digitalRead(GPIO_D22);

  // Mark pin value changed
  pinChanged = true;
}

void setup()
{
  pinMode(GPIO_D15,OUTPUT);
  pinMode(GPIO_D2,OUTPUT);
  pinMode(GPIO_D4,OUTPUT);
  pinMode(GPIO_D5,OUTPUT);
  pinMode(GPIO_D18,OUTPUT);

  pinMode(GPIO_D22,INPUT_PULLUP);
  //pinMode(GPIO_D23,INPUT_PULLUP);
  attachInterrupt(GPIO_D22, CHECKPIN, CHANGE);
  //attachInterrupt(GPIO_D23, ISR_D23, FALLING);

  // Debug console
  Serial.begin(115200);
  Blynk.begin(auth, ssid, pass);
}

void loop()
{
  Blynk.run();

  if (pinChanged)
  {
      // Process the value
      if (pinValue)
      {
        digitalWrite(GPIO_D15,HIGH);
      } else
      {
        digitalWrite(GPIO_D15,LOW);
      }

    // Clear the mark, as we have processed the value
    pinChanged = false;
    }


}



//more information
//https://randomnerdtutorials.com/getting-started-with-esp32/
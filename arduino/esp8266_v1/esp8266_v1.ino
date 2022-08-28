/* Comment this out to disable prints and save space */
#define BLYNK_PRINT Serial

/* Fill-in your Template ID (only if using Blynk.Cloud) */
#define BLYNK_TEMPLATE_ID "TMPLm013-3K-"
#define BLYNK_DEVICE_NAME "OTHERONE"
#define BLYNK_AUTH_TOKEN "4GXW0GFWrHYBqOR3PIgMCH5Lfm4fLQhC"

#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

// You should get Auth Token in the Blynk App.
// Go to the Project Settings (nut icon).
char auth[] = BLYNK_AUTH_TOKEN;
#define GPIO_D0 16
#define GPIO_D1 5
#define GPIO_D2 4
#define GPIO_D3 0
#define GPIO_D4 2

// Your WiFi credentials.
char ssid[] = "MIKROTIK";
char pass[] = "saori2021";

//char ssid[] = "Hostal_Guayaquil_3";
//char pass[] = "16081987";

//char ssid[] = ".:Wifi-Uleam:.";
//char pass[] = "U13aM.2022";


// This function is called every time the Virtual Pin 0 state changes
BLYNK_WRITE(V1)
{
  // Set incoming value from pin V0 to a variable
  int value = param.asInt();
  //Serial.println(param.asInt());

  // Update state
  Blynk.virtualWrite(V1, value);
  if(param.asInt() == 1){
    digitalWrite(GPIO_D1,HIGH);
  }
  else
  {
    digitalWrite(GPIO_D1,LOW);
  }
}

BLYNK_WRITE(V2)
{
  // Set incoming value from pin V0 to a variable
  int value = param.asInt();
  //Serial.println(param.asInt());

  // Update state
  Blynk.virtualWrite(V2, value);
  if(param.asInt() == 1){
    digitalWrite(GPIO_D2,HIGH);
  }
  else
  {
    digitalWrite(GPIO_D2,LOW);
  }
}


BLYNK_WRITE(V3)
{
  // Set incoming value from pin V0 to a variable
  int value = param.asInt();
  //Serial.println(param.asInt());

  // Update state
  Blynk.virtualWrite(V3, value);
  if(param.asInt() == 1){
    digitalWrite(GPIO_D3,HIGH);
  }
  else
  {
    digitalWrite(GPIO_D3,LOW);
  }
}


BLYNK_WRITE(V4)
{
  // Set incoming value from pin V0 to a variable
  int value = param.asInt();
  //Serial.println(param.asInt());

  // Update state
  Blynk.virtualWrite(V4, value);
  if(param.asInt() == 1){
    digitalWrite(GPIO_D4,HIGH);
  }
  else
  {
    digitalWrite(GPIO_D4,LOW);
  }
}

void setup()
{
  pinMode(GPIO_D0,OUTPUT);
  pinMode(GPIO_D1,OUTPUT);
  pinMode(GPIO_D2,OUTPUT);
  pinMode(GPIO_D3,OUTPUT);
  pinMode(GPIO_D4,OUTPUT);
  // Debug console
  Serial.begin(115200);
  Blynk.begin(auth, ssid, pass);
}

void loop()
{
  Blynk.run();
}

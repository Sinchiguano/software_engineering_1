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


void setup()
{
  pinMode(GPIO_D15,OUTPUT);
  // Debug console
  Serial.begin(115200);

  Blynk.begin(auth, ssid, pass);
}

void loop()
{
  Blynk.run();

}

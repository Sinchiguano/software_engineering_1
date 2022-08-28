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
char auth[] = "4GXW0GFWrHYBqOR3PIgMCH5Lfm4fLQhC";

// Your WiFi credentials.
// Set password to "" for open networks.
char ssid[] = "MIKROTIK";
char pass[] = "saori2021";

void setup()
{
  // Debug console
  Serial.begin(9600);

  Blynk.begin(auth, ssid, pass);
}

void loop()
{
  Blynk.run();
}

#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

ESP8266WebServer server(80);

const char* ssid = "robotica"; //Enter Wi-Fi SSID
const char* password =  "robotica"; //Enter Wi-Fi Password


int led1Pin = D10;
int led2Pin = D11;

int led3Pin = D12;
int led4Pin = D13;



bool LED1status = LOW;
bool LED2status = LOW;
bool LED3status = LOW;
bool LED4status = LOW;


void setup() {
  Serial.begin(115200); //Begin Serial at 115200 Baud
  WiFi.begin(ssid, password);  //Connect to the WiFi network
  pinMode(led1Pin,OUTPUT);
  pinMode(led2Pin,OUTPUT);
  pinMode(led3Pin,OUTPUT);
  pinMode(led4Pin,OUTPUT);

  while (WiFi.status() != WL_CONNECTED) {  //Wait for connection
      delay(500);
      Serial.println("Waiting to connect...");
  }

  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());  //Print the local IP

  server.on("/", handle_index); //Handle Index page// front page or main web page

  server.on("/led1on", handle_led1on);
  server.on("/led1off", handle_led1off);

  server.on("/led2on", handle_led2on);
  server.on("/led2off", handle_led2off);

  server.on("/led3on", handle_led3on);
  server.on("/led3off", handle_led3off);

  server.on("/led4on", handle_led4on);
  server.on("/led4off", handle_led4off);

  server.begin(); //Start the server
  Serial.println("Server listening");
}

void loop()
{
  server.handleClient(); //Handling of incoming client requests
  if(LED1status)
  {digitalWrite(led1Pin, HIGH);}
  else
  {digitalWrite(led1Pin, LOW);}

  if(LED2status)
  {digitalWrite(led2Pin, HIGH);}
  else
  {digitalWrite(led2Pin, LOW);}
  if(LED3status)
  {digitalWrite(led3Pin, HIGH);}
  else
  {digitalWrite(led3Pin, LOW);}

  if(LED4status)
  {digitalWrite(led4Pin, HIGH);}
  else
  {digitalWrite(led4Pin, LOW);}
}

void handle_index() {
  //Print Hello at opening homepage
  LED1status = LOW;
  LED2status = LOW;
  LED3status = LOW;
  LED4status = LOW;
  //Serial.println("GPIO7 Status: OFF | GPIO6 Status: OFF");
  server.send(200, "text/html", SendHTML(false,LED2status,LED3status,LED4status));
}

void handle_led1on() {
  LED1status = HIGH;
  Serial.println("GPIO5 Status: ON");
  server.send(200, "text/html", SendHTML(true,LED2status,LED3status,LED4status));
}

void handle_led1off() {
  LED1status = LOW;
  Serial.println("GPIO5 Status: OFF");
  server.send(200, "text/html", SendHTML(false,LED2status,LED3status,LED4status));
}
/////////////////////////////////////
void handle_led2on() {
  LED2status = HIGH;
  Serial.println("GPIO6 Status: ON");
  server.send(200, "text/html", SendHTML(LED1status,true,LED3status,LED4status));
}

void handle_led2off() {
  LED2status = LOW;
  Serial.println("GPIO6 Status: OFF");
  server.send(200, "text/html", SendHTML(LED1status,false,LED3status,LED4status));
}
/////////////////////////////////////
void handle_led3on() {
  LED3status = HIGH;
  Serial.println("GPIO7 Status: ON");
  server.send(200, "text/html", SendHTML(LED1status,LED2status,true,LED4status));
}

void handle_led3off() {
  LED3status = LOW;
  Serial.println("GPIO7 Status: OFF");
  server.send(200, "text/html", SendHTML(LED1status,LED2status,false,LED4status));
}
/////////////////////////////////////
void handle_led4on() {
  LED4status = HIGH;
  Serial.println("GPIO8 Status: ON");
  server.send(200, "text/html", SendHTML(LED1status,LED2status,LED3status,true));
}

void handle_led4off() {
  LED4status = LOW;
  Serial.println("GPIO8 Status: OFF");
  server.send(200, "text/html", SendHTML(LED1status,LED2status,LED3status,false));
}

String SendHTML(bool led1stat,bool led2stat,bool led3stat,bool led4stat){
  String ptr = "<!DOCTYPE html> <html>\n";
  ptr +="<head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, user-scalable=no\">\n";
  ptr +="<title>LED Control</title>\n";
  ptr +="<style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}\n";
  ptr +="body{margin-top: 50px;} h1 {color: #444444;margin: 50px auto 30px;} h3 {color: #444444;margin-bottom: 50px;}\n";
  ptr +=".button {display: block;width: 80px;background-color: #1abc9c;border: none;color: white;padding: 13px 30px;text-decoration: none;font-size: 25px;margin: 0px auto 35px;cursor: pointer;border-radius: 4px;}\n";
  ptr +=".button-on {background-color: #1abc9c;}\n";
  ptr +=".button-on:active {background-color: #16a085;}\n";
  ptr +=".button-off {background-color: #34495e;}\n";
  ptr +=".button-off:active {background-color: #2c3e50;}\n";
  //ptr +="p {font-size: 14px;color: #888;margin-bottom: 10px;}\n";
  ptr +="p {font-size: 12px;color: #888;margin-bottom: 8px;}\n";
  ptr +="</style>\n";
  ptr +="</head>\n";
  ptr +="<body>\n";
  ptr +="<h1>ULEAM Ext El Carmen</h1>\n";
  //ptr +="<h2>Software Engineering</h2>\n";
  //ptr +="<h3>Using Station Mode (STA)</h3>\n";
  ptr +="<h2>ROBOTICS CLUB</h2>\n";
  ptr +="<h3>CONTROL DE LUCES EN VIVIENDA</h3>\n";
  ptr +="<h4>CESAR SINCHIGUANO</h4>\n";
  ptr +="<h5>MSc in Robotics and Cybernetics</h5>\n";

  if(led1stat)
  {ptr +="<p>DORMITORIO MASTER Status: ON</p><a class=\"button button-off\" href=\"/led1off\">OFF</a>\n";}
  else
  {ptr +="<p>DORMITORIO MASTER Status: OFF</p><a class=\"button button-on\" href=\"/led1on\">ON</a>\n";}

  if(led2stat)
  {ptr +="<p>SANITARIO Status: ON</p><a class=\"button button-off\" href=\"/led2off\">OFF</a>\n";}
  else
  {ptr +="<p>SANITARIO Status: OFF</p><a class=\"button button-on\" href=\"/led2on\">ON</a>\n";}

  if(led3stat)
  {ptr +="<p>VENTILADOR Status: ON</p><a class=\"button button-off\" href=\"/led3off\">OFF</a>\n";}
  else
  {ptr +="<p>VENTILADOR Status: OFF</p><a class=\"button button-on\" href=\"/led3on\">ON</a>\n";}

  if(led4stat)
  {ptr +="<p>CARGADOR Status: ON</p><a class=\"button button-off\" href=\"/led4off\">OFF</a>\n";}
  else
  {ptr +="<p>CARGADOR Status: OFF</p><a class=\"button button-on\" href=\"/led4on\">ON</a>\n";}

  ptr +="</body>\n";
  ptr +="</html>\n";

  return ptr;
}

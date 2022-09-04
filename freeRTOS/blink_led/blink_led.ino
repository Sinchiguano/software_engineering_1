//use only 1 core for demo purposes

#if CONFIG_FREERTOS_UNICORE
static const BaseType_t app_cpu=0
#else
static const BaseType_t app_cpu=1;
#endif


//pins

static const int GPIO_15=15;
static const int GPIO_2=2;
static const int GPIO_4=4;
static const int GPIO_5=5;
static const int GPIO_18=18;



static const int rate15=250;
static const int rate2=350;
static const int rate5=450;
static const int rate4=650;



// our task:  blink an led
void toggleGPIO15(void *parameter)
{
  while(1)
  {
    digitalWrite(GPIO_15,HIGH);
    vTaskDelay(rate15/portTICK_PERIOD_MS);
    digitalWrite(GPIO_15,LOW);
    vTaskDelay(rate15/portTICK_PERIOD_MS);//portTICK_PERIOD_MS 1ms
    }
}
void toggleGPIO2(void *parameter)
{
  while(1)
  {
    digitalWrite(GPIO_2,LOW);
    vTaskDelay(rate2/portTICK_PERIOD_MS);
    digitalWrite(GPIO_2,HIGH);
    vTaskDelay(rate2/portTICK_PERIOD_MS);//portTICK_PERIOD_MS 1ms
    }
}
void toggleGPIO4(void *parameter)
{
  while(1)
  {
    digitalWrite(GPIO_4,HIGH);
    vTaskDelay(rate4/portTICK_PERIOD_MS);
    digitalWrite(GPIO_4,LOW);
    vTaskDelay(rate4/portTICK_PERIOD_MS);//portTICK_PERIOD_MS 1ms
    }
}
void toggleGPIO5(void *parameter)
{
  while(1)
  {
    digitalWrite(GPIO_5,LOW);
    vTaskDelay(rate5/portTICK_PERIOD_MS);
    digitalWrite(GPIO_5,HIGH);
    vTaskDelay(rate5/portTICK_PERIOD_MS);//portTICK_PERIOD_MS 1ms
    }
}
void setup() {
  // put your setup code here, to run once:
  pinMode(GPIO_15,OUTPUT);
  pinMode(GPIO_2,OUTPUT);
  pinMode(GPIO_4,OUTPUT);
  pinMode(GPIO_5,OUTPUT);
  //pinMode(GPIO_18,OUTPUT);

  //Task to run forever
  xTaskCreatePinnedToCore(
                  toggleGPIO15,//functon to be called
                  "Toggle Task_1",//name of task
                  1024,//stack size in bytes
                  NULL,//paramer to pass to funciton
                  1,//Task priority (0 lowest priority) 24
                  NULL, //task handle
                  app_cpu);//run on one core for demo purposes ESP32 only

  xTaskCreatePinnedToCore(
                  toggleGPIO2,//funciton to be called
                  "Toggle Task_2",//name of task
                  1024,//stack size in bytes
                  NULL,//paramer to pass to funciton
                  1,//Task priority (0 lowest priority) 24
                  NULL, //task handle
                  app_cpu);//run on one core for demo purposes ESP32 only

xTaskCreatePinnedToCore(
                toggleGPIO4,//functon to be called
                "Toggle Task_3",//name of task
                1024,//stack size in bytes
                NULL,//paramer to pass to funciton
                1,//Task priority (0 lowest priority) 24
                NULL, //task handle
                app_cpu);//run on one core for demo purposes ESP32 only

xTaskCreatePinnedToCore(
                toggleGPIO5,//funciton to be called
                "Toggle Task_4",//name of task
                1024,//stack size in bytes
                NULL,//paramer to pass to funciton
                1,//Task priority (0 lowest priority) 24
                NULL, //task handle
                app_cpu);//run on one core for demo purposes ESP32 only
}

void loop() {
  // put your main code here, to run repeatedly:
}

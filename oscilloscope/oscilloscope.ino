#define LED_GREEN 8
#define LED_RED 9
#define LED_BLUE 10
#define LED_A    3
#define CHANNEL_1 5
#define CHANNEL_2 6
#define CHANNEL_3 7

#define CHANNEL_A 0
#define CHANNEL_V 1
#define DELAY 500

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_GREEN, OUTPUT);
  pinMode(LED_RED, OUTPUT);
  pinMode(LED_BLUE, OUTPUT);
  pinMode(CHANNEL_1, INPUT);
  pinMode(CHANNEL_2, INPUT);
  pinMode(CHANNEL_3, INPUT);
  pinMode(CHANNEL_A, INPUT);
  pinMode(CHANNEL_V, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

  int channel_1 = digitalRead(CHANNEL_1);
  int channel_2 = digitalRead(CHANNEL_2);
  int channel_3 = digitalRead(CHANNEL_3);

  int channel_a = analogRead(CHANNEL_A);
  int channel_v = analogRead(CHANNEL_V);
  
  digitalWrite(LED_GREEN, channel_1);
  output("channel_1", channel_1);
  
  digitalWrite(LED_RED, channel_2);
  output("channel_2", channel_2);
   
  digitalWrite(LED_BLUE, channel_3);
  output("channel_3", channel_3);

  analogWrite(LED_A, channel_a);
  output("channel_a", channel_a);

  int voltage = (channel_v * (5.0 / 1023.0)) * 1000;
  output("channel_v", voltage);
  
  delay(DELAY);
  
}

void output(String channel, int value){
  float t = millis() / 1000.0;
  Serial.println("{\"channel\":\"" + channel + "\", \"value\":" + String(value) + ",\"time\":" + String(t) + "}"); 
}



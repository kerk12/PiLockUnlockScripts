void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(2, HIGH);
  digitalWrite(LED_BUILTIN, LOW);
  if (Serial.available() > 0){
    String content = "";
    char character;

    while(Serial.available()) {
        character = Serial.read();
        content.concat(character);
        delay(10);
    }

    if (content == "ENABLE") {
      digitalWrite(2, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
      delay(5000);
    }
  }
}

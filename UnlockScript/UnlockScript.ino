// The pin the relay is attached to.
const int RELAY_PIN = 2;
// How many seconds to keep the relay turned on.
const int DELAY = 5;

void setup() {
  // Setup everything...
  Serial.begin(9600);
  pinMode(RELAY_PIN, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // The Relay is active low, so write high to it in order to disable it.
  digitalWrite(RELAY_PIN, HIGH);
  digitalWrite(LED_BUILTIN, LOW);

  // If the serial port is available, read each character and concatenate it to a string.
  if (Serial.available() > 0){
    String content = "";
    char character;

    while(Serial.available()) {
        character = Serial.read();
        content.concat(character);
        delay(10); // Add a 10ms delay in order to receive the characters correctly.
    }

    // Finally, check the string, if it reads "ENABLE", turn on the relay, wait for 5 seconds, then turn it off.
    if (content == "ENABLE") {
      digitalWrite(RELAY_PIN, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
      delay(DELAY * 1000);
    }
  }
}

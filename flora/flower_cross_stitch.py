// Pin D7 has an LED connected on FLORA.
// give it a name:
int pins[6] = {1, 0, 2, 3, 9, 10} ;
// the setup routine runs once when you press reset:
void setup() {
// initialize the digital pin as an output.
 for (int i = 0; i <= 12; i++) {
    pinMode(i, OUTPUT);
 }
}
// the loop routine runs over and over again forever:
void loop() {
  for (int i = 0; i <= 5; i++) {
    for (int j=0; j<=5; j++){
      digitalWrite(pins[j], HIGH); // turn the LED on (HIGH is the voltage level)
      delay(1000); // wait for a second
      digitalWrite(pins[j], LOW); // turn the LED off by making the voltage LOW
    }
  }
   for (int i = 0; i <= 12; i++) {
    for (int j=0; j<=5; j++){
      digitalWrite(pins[j], HIGH); // turn the LED on (HIGH is the voltage level)
    }
  }
  delay(10000000); // wait for a second
}

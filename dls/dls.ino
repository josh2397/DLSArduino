#include "Queue.hpp"

void setup() {
    
    Queue queue(5);
    queue.size();

    pinMode(LED_BUILTIN, HIGH);
    for (int i = 0; i < 10; i++) {
        digitalWrite(LED_BUILTIN, HIGH);
        delay(500);
        digitalWrite(LED_BUILTIN, LOW);
        delay(500);
    }
}

void loop() {
    
}

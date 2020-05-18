#include "Queue.hpp"

class DLS {
private:
    char CI[4] = "";
    String inputString = "";
    Queue queue;
public:

    DLS::DLS (Queue _queue) {
        queue = _queue;
    }

    void DLS::eventLoop(){
        for (;;) {

        }
    }
    
    void DLS::readSerial(){
        // Serial.println("Reading Serial Date");
        while (Serial.available() ) {
            char inChar = (char)Serial.read();

            inputString += inChar;


            if (inputString[inputString.length() - 1] == '\n') {
                Serial.print(inputString);
                inputString = "";
                Serial.println("End");
                break;
            }
          https://forum.arduino.cc/index.php?topic=73372.0
        }
    }
};


void setup() {

    pinMode(LED_BUILTIN, HIGH);
    for (int i = 0; i < 3; i++) {
        digitalWrite(LED_BUILTIN, HIGH);
        delay(500);
        digitalWrite(LED_BUILTIN, LOW);
        delay(500);
    }

    Serial.begin(9600);
    
    Serial.println("Arduino is running");

}

Queue _queue(5);
DLS dls(_queue);

void loop() { 
    
}

void serialEvent() {
    dls.readSerial();
}

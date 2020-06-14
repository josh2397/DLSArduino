#include "Queue.hpp"
#include "Instruction.hpp"

class DLS {
private:
    char CI[4] = "";
    String inputString = "";
    char inputChar[30] = "";

    Queue queue;
    Instruction instruction;

public:

    DLS::DLS (Queue _queue) {
        queue = _queue;
    }

    void DLS::eventLoop(){
        for (;;) {

        }
    }
    
    void DLS::readSerial(){
      
        while (Serial.available() > 0 ) {

            char inChar = (char)Serial.read();
            
            if (inChar == '\n') {
              queue.enqueue(inputString);
              Serial.print(queue.peek());
              Serial.println(queue.size());
              
              inputString = "";
              break;
            }
            
            inputString += inChar;
        }
    }
};


void setup() {

//    pinMode(LED_BUILTIN, HIGH);
//    for (int i = 0; i < 3; i++) {
//        digitalWrite(LED_BUILTIN, HIGH);
//        delay(500);
//        digitalWrite(LED_BUILTIN, LOW);
//        delay(500);
//    }

    Serial.begin(9600);
    
    Serial.println("Arduino is running");
}

Queue _queue(10);
DLS dls(_queue);

void loop() { 
    
}

void serialEvent() {
    dls.readSerial();
}

#include <stdio.h>
// #include "arduino.h"
// #include "serial.h"
// Include other necessary arduino libraries



// Define Pins
#define IR_1 7 /* define IR sensor 1 to be at Pin 7 */
#define IR_2 8 /* define IR sensor 2 to be at Pin 8 */


#define WARNING "Note: above numbers are subject to change based on sensor; need to take readings to derive relationship"

void setup()
{
 // Serial.begin(9600); // set the data rate in bits per second for data transmission
}

float find_distance_from_voltage(float voltage) {
    /* Voltage is given by 
    y [mV] = 137500 x [m^-1] + 1125
    */
   float x = (voltage - 1125)/137500; // 1/distance
   printf(WARNING);
   return 1/x;
}

float read_from_IR(int pin) {
    return pin;
}

void main() {
    float dist, voltage;
    while (1) {
        voltage = read_from_IR(IR_1);
        dist = find_distance_from_voltage(voltage);
    }
}

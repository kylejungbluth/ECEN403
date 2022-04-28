/*******************************************************************************
  Main Source File

  Company:
    Microchip Technology Inc.

  File Name:
    main.c

  Summary:
    This file contains the "main" function for a project.

  Description:
    This file contains the "main" function for a project.  The
    "main" function calls the "SYS_Initialize" function to initialize the state
    machines of all modules in the system
 *******************************************************************************/

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stddef.h>                     // Defines NULL
#include <stdbool.h>                    // Defines true
#include <stdlib.h>                     // Defines EXIT_FAILURE
#include "definitions.h"                // SYS function prototypes
#include <xc.h>
#include <stdio.h>

#define SYS_FREQ 48000000               // system frequency set at 48 MHz
#define _XTAL_FREQ 48000000             // internal frequency set at 48 MHz

#define steps 200                       // 1.8 degrees per step, 200 steps per revolution

#define cw 0                            // define clockwise as char 0
#define ccw 1                           // define counter clockwise as char 1

// on board led
#define board_led PORTAbits.RA0

// motor 1
#define direction1 PORTBbits.RB12   
#define pulse1 PORTBbits.RB13
#define button1_L PORTBbits.RB6
#define button1_R PORTBbits.RB7
// motor 2
#define direction2 PORTBbits.RB14 
#define pulse2 PORTBbits.RB15
#define button2_L PORTBbits.RB8
#define button2_R PORTBbits.RB9
// confirm button
#define confirm PORTBbits.RB10

#define input1 PORTAbits.RA2
#define output1 PORTBbits.RB4

#define input2 PORTAbits.RA3
#define output2 PORTAbits.RA4


// delay function in microseconds
void delay_us(unsigned int us) {
    // convert microseconds into how many clock ticks it will take
    us *= SYS_FREQ / 1000000 / 2; // core timer updates every 2 ticks
    _CP0_SET_COUNT(0); // set core timer count to 0
    while(us > _CP0_GET_COUNT()); // wait until core timer reaches number we calculated
}

// delay function in milliseconds
void delay_ms(int ms) {
    delay_us(ms * 1000); // micro to milli second conversion
}

void initialize() {
    // set all ports to be digital, not analog
    ANSELA = 0;
    ANSELB = 0;
    
    // set on board LED as output
    TRISAbits.TRISA0 = 0; 
    PORTAbits.RA0 = 0;
    
    // input and output pins to Raspberry Pi
    TRISAbits.TRISA2 = 1;   // input 1
    TRISAbits.TRISA3 = 1;   // input 2
    TRISBbits.TRISB4 = 0;   // output 1
    TRISAbits.TRISA4 = 0;   // output 2
    
    PORTAbits.RA2 = 0;
    PORTAbits.RA3 = 0;
    PORTBbits.RB4 = 0;
    PORTAbits.RA4 = 0;
    
    
    // set ports B 6through B19 as inputs from buttons
    TRISBbits.TRISB6 = 1;   // determines direction of motor rotation
    TRISBbits.TRISB7 = 1;   // determines speed and movement on motor
    TRISBbits.TRISB8 = 1;
    TRISBbits.TRISB9 = 1;
    PORTBbits.RB6 = 0;
    PORTBbits.RB7 = 0;
    PORTBbits.RB8 = 0;
    PORTBbits.RB9 = 0;
    
    // set ports RB12 through RB15 as outputs for direction and drive
    TRISBbits.TRISB12 = 0;
    TRISBbits.TRISB13 = 0;
    TRISBbits.TRISB14 = 0;
    TRISBbits.TRISB15 = 0;
    PORTBbits.RB12 = 0;
    PORTBbits.RB13 = 0;
    PORTBbits.RB14 = 0;
    PORTBbits.RB15 = 0;
    
    // initialize all ports as 0
    PORTA = 0;
    PORTB = 0;
}

// function to flash on board led for 1 second
void onboardled() {
    // flashes on board led every second
    PORTAbits.RA0 = 1;
    delay_ms(1000);
    PORTAbits.RA0 = 0;
    delay_ms(1000);
}

void motor1_pulse() {
    for(int i = 0; i < (55); i++) {    // adjusted condition to rotate more/less
        pulse1 = 1;
        delay_ms(3);
        pulse1 = 0;
        delay_ms(3);
    } 
}

void motor1_fulldrive(char direction) {
    if(direction == cw) {
       direction1 = 1;  // set motor to rotate in clockwise direction
       motor1_pulse();
    }
    if(direction == ccw) {
        direction1 = 0;  // set motor to rotate in clockwise direction
        motor1_pulse();
    }
}

void motor1_calib() {
    if(button1_L) {
            direction1 = cw;
            while(button1_L) {
                pulse1 = 1;
                delay_ms(2);
                pulse1 = 0;
                delay_ms(2);
            }
        }
    if(button1_R) {
        direction1 = ccw;
        while(button1_R) {
            pulse1 = 1;
            delay_ms(2);
            pulse1 = 0;
            delay_ms(2);
        }
    }
}

void motor2_pulse() {
    for(int i = 0; i < (steps/4); i++) {
        pulse2 = 1;
        delay_ms(3);
        pulse2 = 0;
        delay_ms(3);
    } 
}

void motor2_fulldrive(char direction) {
    if(direction == cw) {
       direction2 = 1;  // set motor to rotate in clockwise direction
       motor2_pulse();
    }
    if(direction == ccw) {
        direction2 = 0;  // set motor to rotate in clockwise direction
        motor2_pulse();
    }
}

void motor2_calib() {
    if(button2_L) {
            direction2 = cw;
            while(button2_L) {
                pulse2 = 1;
                delay_ms(2);
                pulse2 = 0;
                delay_ms(2);
            }
        }
    if(button2_R) {
        direction2 = ccw;
        while(button2_R) {
            pulse2 = 1;
            delay_ms(2);
            pulse2 = 0;
            delay_ms(2);
        }
    }
}

void calibration() {
    if(button1_L || button1_R) {
        motor1_calib();
    }
    if(button2_L || button2_R) {
        motor2_calib();
    }
}

int main ()
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    
    // initializing all pins
    initialize(); 
    
    bool centered = false;
    while(centered == false) {
            board_led = 1;
            calibration();
            if(confirm) {
                centered = true;
                board_led = 0;
                delay_ms(1000);
                break;
            }
        }
    
    while ( true ) {
        SYS_Tasks ( );
        // use with communication_test.py 
        /*
        if(button1_L) {
            output1 = 1;
            delay_ms(1000);
            output1 = 0;
        }
        if(button1_R) {
            output2 = 1;
            delay_ms(1000);
            output2 = 0;
        }
        */ 
        
        if(input1) {
            motor1_fulldrive(cw);
            delay_ms(500);
            output1 = 1;
            delay_ms(2000);
            output1 = 0;
        }
        
        if(input2) {
            motor2_fulldrive(cw);
            delay_ms(500);
            output2 = 1;
            delay_ms(2000);
            output2 = 0;
        }
        
        /*
        while(current1 < required1 || current2 < required2) {
            if(current1 < required1 && current2 < required2) {
                board_led = 1;
                motor1_fulldrive(ccw);
                delay_ms(1000);
                motor2_fulldrive(cw);
                current1++;
                current2++;
                board_led = 0;
                delay_ms(1000);
                continue;
            }
            // if one of the two nutrients is below the required levels
            else if(current1 >= required1 || current2 >= required2) {
                if(current1 < required1) { // if nutrient 1 is below required level
                    board_led = 1;
                    motor1_fulldrive(ccw); // dispense nutrient 1
                    current1++; // increase nutrient 1 current level by 1
                    board_led = 0;
                    delay_ms(1000);
                    continue; // restart loop
                }
                else if(current2 < required2) { // if nutrient 2 is below required level
                    board_led = 1;
                    motor2_fulldrive(cw); // dispense nutrient 2
                    current2++; // increase nutrient 2 current level by 1
                    board_led = 0;
                    delay_ms(1000);
                    continue; // restart loop
                }
            }
        }
        */ 
        // reset everything back to 0
        PORTA = 0;
        PORTB = 0;
    }
    
    
    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/


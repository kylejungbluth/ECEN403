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
#include <stdio.h>
#define SYS_FREQ 48000000               // Running at 48 MHz
#define BAUDRATE 115200                 // baud rate at 115200 Hz

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

// function to flash on board led for 1 second
void onboardled() {
    // flashes on board led every second
    PORTAbits.RA0 = 1;
    delay_ms(1000);
    PORTAbits.RA0 = 0;
    delay_ms(1000);
}

/*
void UART_Init() {
    int pbClk;
    pbClk = SYS_FREQ / 2; // 48 MHz / 2
    
    U1MODE = 0; // set UART 1 off prior to setting it up
    U1MODEbits.BRGH = 0; // want standard speed
    U1BRG = pbClk / (16 * 115200) - 1;
    U1STA = 0; // disable TX and RX pins, clear all flags
    U1STAbits.UTXEN = 1; // enable TX pin
    U1STAbits.URXEN = 1; // enable RX pin
    U1MODEbits.PDSEL = 0;
    U1MODEbits.STSEL = 0;
    U1MODEbits.ON = 1;
}

void _mon_putc (char c) {
    while(U1STAbits.UTXBF);
    U1TXREG = c;
}
*/

// rotate RB6 to open at 0 degrees
void bot1Rotate0() {
    unsigned int i;
    for(i = 0; i < 50; i++) {
        PORTBbits.RB6 = 1;
        delay_us(800);
        PORTBbits.RB6 = 0;
        delay_us(19200);
    }
}

// rotate RB7 to open at 0 degrees
void top1Rotate0() {
    unsigned int i;
    for(i = 0; i < 50; i++) {
        PORTBbits.RB7 = 1;
        delay_us(800);
        PORTBbits.RB7 = 0;
        delay_us(19200);
    }
}

// rotate RB6 to close at 90 degrees
void bot1Rotate90() {
    unsigned int i;
    for(i = 0; i < 50; i++) {
        PORTBbits.RB6 = 1;
        delay_us(1500);
        PORTBbits.RB6 = 0;
        delay_us(18500);
    }
}

// rotate RB7 to close at 90 degrees
void top1Rotate90() {
    unsigned int i;
    for(i = 0; i < 50; i++) {
        PORTBbits.RB7 = 1;
        delay_us(1500);
        PORTBbits.RB7 = 0;
        delay_us(18500);
    }
}

// rotate RB8 to open at 0 degrees
void bot2Rotate0() {
    unsigned int i;
    for(i = 0; i < 50; i++) {
        PORTBbits.RB8 = 1;
        delay_us(800);
        PORTBbits.RB8 = 0;
        delay_us(19200);
    }
}

// rotate RB9 to open at 0 degrees
void top2Rotate0() {
    unsigned int i;
    for(i = 0; i < 50; i++) {
        PORTBbits.RB9 = 1;
        delay_us(800);
        PORTBbits.RB9 = 0;
        delay_us(19200);
    }
}

// rotate RB8 to open at 90 degrees
void bot2Rotate90() {
    unsigned int i;
    for(i = 0; i < 50; i++) {
        PORTBbits.RB8 = 1;
        delay_us(1500);
        PORTBbits.RB8 = 0;
        delay_us(18500);
    }
}

// rotate RB9 to open at 90 degrees
void top2Rotate90() {
    unsigned int i;
    for(i = 0; i < 50; i++) {
        PORTBbits.RB9 = 1;
        delay_us(1500);
        PORTBbits.RB9 = 0;
        delay_us(18500);
    }
}

// dispensing nutrient function for nutrient 1
void dispensing1() {
    bot1Rotate0();  // bottom open
    delay_ms(750);  // wait
    bot1Rotate90(); // bottom close
    delay_ms(750);  // wait        
    top1Rotate0();  // top open
    delay_ms(750);  // wait
    top1Rotate90(); // top close
    delay_ms(750);  // wait
}

// dispensing nutrient function for nutrient 2
void dispensing2() {
    bot2Rotate0();
    delay_ms(750);
    bot2Rotate90();
    delay_ms(750);        
    top2Rotate0();
    delay_ms(750);
    top2Rotate90();
    delay_ms(750);
}

int main ()
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    
    // set all ports to be digital, not analog
    ANSELA = 0;
    ANSELB = 0;
    
    // initializing RPB2 = U1RX 
    // U1RXR = 0b0100;
    // TRISBbits.TRISB2 = 1; // make RPB2/RB2 an input
    // RPB3R = 0b0001; // make RPB3/RB3 an output, RPB3 = U1TX
        
    // set on board LED as output
    TRISAbits.TRISA0 = 0;
    
    // set RB6 and RB7 as output for servo motor
    TRISBbits.TRISB6 = 0;
    TRISBbits.TRISB7 = 0;
    TRISBbits.TRISB8 = 0;
    TRISBbits.TRISB9 = 0;
    
    // UART_Init();
    
    // printf("Hello World!");
    
    // printing method 
    /*
    char c;
    c = 'A';
    U1TXREG = c;
    */
    
    /*
    while ( true ) {
        SYS_Tasks ( );
        onboardled();
        // UART2_Write(&buffer[0], sizeof(buffer));
        // printf("TEST");
    }
    */
    
    int required1 = 5;
    int current1 = 0;
    int required2 = 7;
    int current2 = 0;
    
    
    while (current1 < required1 || current2 < required2) {
        SYS_Tasks ( );
        // on board led lights up, indicating dispensing
        PORTAbits.RA0 = 1;
        // if both nutrients are below required levels
        if(current1 < required1 && current2 < required2) {
            dispensing1(); // dispensing nutrient 1
            dispensing2(); // dispensing nutrient 2
            current1++; // increase nutrient 1 current level by 1
            current2++; // increase nutrient 2 current level by 1
            continue; // continue with next iteration of loop
        }
        // if one of the two nutrients is below the required levels
        else if(current1 >= required1 || current2 >= required2) {
            if(current1 < required1) { // if nutrient 1 is below required level
                dispensing1(); // dispense nutrient 1
                current1++; // increase nutrient 1 current level by 1
                continue; // restart loop
            }
            else if(current2 < required2) { // if nutrient 2 is below required level
                dispensing2(); // dispense nutrient 2
                current2++; // increase nutrient 2 current level by 1
                continue; // restart loop
            }
        }
        else {
            break; // code shouldn't reach here
        }
    }
    
    while(true) {
        onboardled(); // once finished, on board led will continue to flash
    }
    
    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/


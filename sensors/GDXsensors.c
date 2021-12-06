#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


int main() {
   /* my first program in C */
   //gdx = gdx.gdx();

// This code uses the gdx functions to collect data from your Go Direct sensors. 
    //gdx.open_usb();
    //gdx.select_sensors([[3],[4]]);


    double measurements[]= {0,0};
    double sumnum[] = {0,0};

    while(1) {
            //define period per start function in gdx.h. set to 1000 for 1 sample per second
            //gdx.start(period=1000);
            //printf("entered while");

            //reset both sumnum values to 0
            sumnum[0]= 0;
            sumnum[1]=0;
            

            //each time take 10 measurements then average them out
            for (int i=0; i<10; i++) {
                    //measurements = gdx.read();

                    //break if no measurements where found at input
                    /*if (measurements[0]== 0 && measurements[0] == 0){
                        printf("Error reading values from sensors, check sensor connections!\n");
                        break;
                        } */
                    float a = 5.0;
                    
                    //add the 10 recordings into sumnum to use for average
                    sumnum[0] += measurements[0];
                    sumnum[1] += measurements[1];
                   
                    //print average of the 10 measurements
                    //printf("ammonium: %f\n" , sumnum[0]/10);
                    //printf("calcium: %f\n" ,sumnum[1]/10);
                    printf("Magnesium: %f\n", (1+ ((float)rand() / (float)(RAND_MAX)) * a));
                    printf("phosphorus: %f\n", (1+ ((float)rand()/(float)(RAND_MAX)) * a));
                        
            //dx.stop();

            //take measurements every 5 minutes (300 seconds)
            sleep(3);
            }
    }

    //gdx.close();
}
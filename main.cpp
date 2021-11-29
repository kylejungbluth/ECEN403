#include <Arduino.h>
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <WiFiClient.h>
#include <WiFi.h>
#include <HTTPClient.h>

//website password:404team17
//db password: @<dB2rYHc{mLi<yW
//db username: id18016886_modeluser
//db name: id18016886_modeldb
//https://ecen404-team17.000webhostapp.com/
#define HOST "ecen404-team17.000webhostapp.com"

const char *ssid = "RamRanch";
const char *password = "redcream211";

const char *ntpServer = "pool.ntp.org";
const long gmtOffset_sec = 0;
const int daylightOffset_sec = 3600;

static int *model;

double ammonium;
double magnesium;
double calcium;
double phosphorus;

struct Models
{
    String name;
    double ammonium;
    double magnesium;
    double calcium;
    double phosphorus;
};

struct Models Model1;
struct Models Model2;
static struct Models *CurrentModel;

void set_global_values();
void sensor_1(struct Models CurrentModel);
void sensor_2(struct Models CurrentModel);
void sensor_3(struct Models CurrentModel);
void sensor_4(struct Models CurrentModel);
void nutrient_absorption();
void update_ML(int random);
void open_actuator_1();
void close_actuator_1();
void open_actuator_2();
void close_actuator_2();
void open_actuator_3();
void close_actuator_3();
void open_actuator_4();
void close_actuator_4();
void printDouble(double val, unsigned int precision);
void printLocalTime();

void setup()
{
    Serial.begin(115200);
    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, password); //try to connect with wifi
    configTime(gmtOffset_sec, daylightOffset_sec, ntpServer);
    printf("Current Time : ");
    printLocalTime();
    delay(5000);
    Serial.println("\n++++ ESP Feedback Loop - Kyle Jungbluth ++++");
    Serial.print("Connecting to: ");
    Serial.print(ssid);
    while (WiFi.status() != WL_CONNECTED)
    {
        printf(".");
        delay(500);
    }

    Serial.println("\nConnected to " + String(ssid));
    Serial.print("IP Address is : ");
    Serial.println(WiFi.localIP()); //print local IP address

    set_global_values();
    Serial.println("\nSet global values: ");
    Serial.print("Model 1 Ammonium: ");
    printDouble(Model1.ammonium, 10);
    Serial.print("Model 1 Magnesium: ");
    printDouble(Model1.magnesium, 10);
    Serial.print("Model 2 Ammonium: ");
    printDouble(Model2.ammonium, 10);
    Serial.print("Model 2 Magnesium: ");
    printDouble(Model2.magnesium, 10);
    Serial.println();

    ammonium = 2;
    magnesium = 1.8;
    calcium = 4;
    phosphorus = 6;
    Serial.println("Initial Nutrient Levels: ");
    Serial.print("Ammonium: ");
    printDouble(ammonium, 10);
    Serial.print("Magnesium: ");
    printDouble(magnesium, 10);
    Serial.println();

    time_t t;
    srand((unsigned)time(&t));
}

void loop()
{
    if (WiFi.status() == WL_CONNECTED)
    {
        WiFiClient WifiClient;
        HTTPClient http;

        http.begin(WifiClient, "http://ecen404-team17.000webhostapp.com/dbreadlast.php"); // Connect to host where MySQL databse is hosted
        int httpCode = http.GET();
        if (httpCode > 0)
        {
            // HTTP header has been send and Server response header has been handled
            Serial.printf("[HTTP] Database GET... code: %d\n", httpCode);

            // file found at server
            if (httpCode == HTTP_CODE_OK || httpCode == HTTP_CODE_MOVED_PERMANENTLY)
            {
                String payload = http.getString();
                Serial.println(payload);
                String stringchar = payload.substring(46, 47);
                int temp = stringchar.toInt();
                model = &temp;
                update_ML(*model);
                Serial.println("Current Model: " + (*CurrentModel).name);
            }
        }
        else
        {
            Serial.println("[HTTP] Error: Database GET Failed.");
        }
        http.end();
        Serial.println();
        nutrient_absorption();
        sensor_1((*CurrentModel));
        sensor_2((*CurrentModel));
        time_t mytime = time(NULL);
        char *time_str = ctime(&mytime);
        time_str[strlen(time_str) - 1] = '\0';
        printf("Current Time : ");
        printLocalTime();
        Serial.println("--------------------------------------");
        delay(5000);
    }
}

void set_global_values()
{
    //initiate nutrient values for each model
    Model1.name = "Model 1";
    Model1.ammonium = .75;
    Model1.magnesium = .5;
    Model1.calcium = .5;
    Model1.phosphorus = .9;

    Model2.name = "Model 2";
    Model2.ammonium = 1.4;
    Model2.magnesium = 1.2;
    Model2.calcium = 1.8;
    Model2.phosphorus = 1.9;
}

void sensor_1(struct Models CurrentModel)
{
    //check current nutrient levels to DB level and release extra if lower
    if (ammonium < (CurrentModel).ammonium)
    {
        //actuator.release()
        //open_actuator_1();
        //close_actuator_1();
        ammonium += .5;
        Serial.print("Ammonium Nutrient Level: ");
        printDouble(ammonium, 100);
        Serial.print("Ammonium ML Level: ");
        printDouble((CurrentModel).ammonium, 10);
        Serial.println("Release Ammonium.\n");
    }
    else
    {
        Serial.print("Ammonium Nutrient Level: ");
        printDouble(ammonium, 100);
        Serial.print("Ammonium ML Level: ");
        printDouble((CurrentModel).ammonium, 10);
        Serial.println("Don't Release Ammonium.\n");
    }
}

void sensor_2(struct Models CurrentModel)
{
    //check current nutrient levels to DB level and release extra if lower
    if (magnesium < (CurrentModel).magnesium)
    {
        //actuator.release()
        //open_actuator_2();
        //close_actuator_1();
        magnesium += .5;
        Serial.print("Magnesium Nutrient Level: ");
        printDouble(magnesium, 100);
        Serial.print("Magnesium ML Level: ");
        printDouble((CurrentModel).magnesium, 10);
        Serial.println("Release Magnesium.");
    }
    else
    {
        Serial.print("Magnesium Nutrient Level: ");
        printDouble(magnesium, 100);
        Serial.print("Magnesium ML Level: ");
        printDouble((CurrentModel).magnesium, 10);
        Serial.println("Don't Release Magnesium.");
    }
}

// void sensor_3(struct Models CurrentModel)
// {
//     if (calcium < CurrentModel.calcium)
//     {
//         //actuator.release()
//         //open_actuator_3();
//         //close_actuator_3();
//         calcium += .5;
//         printf("Nutrient Level: %f", calcium);
//         printf(" ML Level: %f", CurrentModel.calcium);
//         printf(" Release Magnesium.\n");
//     }
//     else
//     {
//         printf("Nutrient Level: %f", calcium);
//         printf(" ML Level: %f", CurrentModel.calcium);
//         printf(" Don't Release Magnesium.\n");
//     }
// }

// void sensor_4(struct Models CurrentModel)
// {
//     if (phosphorus < CurrentModel.phosphorus)
//     {
//         //actuator.release()
//         //open_actuator_4();
//         //close_actuator_4();
//         phosphorus += .5;
//         printf("Nutrient Level: %f", phosphorus);
//         printf(" ML Level: %f", CurrentModel.phosphorus);
//         printf(" Release Magnesium.\n");
//     }
//     else
//     {
//         printf("Nutrient Level: %f", phosphorus);
//         printf(" ML Level: %f", CurrentModel.phosphorus);
//         printf(" Don't Release Magnesium.\n");
//     }
// }

void nutrient_absorption()
{
    //simulates nutrient absorbtion by subtracting small amount of nutrient
    ammonium -= .05;
    magnesium -= .05;
    calcium -= .05;
    phosphorus -= .05;
}

void update_ML(int model)
{
    //update current model to int model pulled from DB
    if (model == 0)
    {
        CurrentModel = &Model1;
    }
    else
    {
        CurrentModel = &Model2;
    }
}

void printDouble(double val, unsigned int precision)
{
    // prints val with number of decimal places determine by precision
    // NOTE: precision is 1 followed by the number of zeros for the desired number of decimial places
    // example: printDouble( 3.1415, 100); // prints 3.14 (two decimal places)

    Serial.print(int(val)); //prints the int part
    Serial.print(".");      // print the decimal point
    unsigned int frac;
    if (val >= 0)
        frac = (val - int(val)) * precision;
    else
        frac = (int(val) - val) * precision;
    int frac1 = frac;
    while (frac1 /= 10)
        precision /= 10;
    precision /= 10;
    while (precision /= 10)
        Serial.print("0");

    Serial.println(frac, DEC);
}

void printLocalTime()
{
    //prints local time
    struct tm timeinfo;
    if (!getLocalTime(&timeinfo))
    {
        Serial.println("Failed to obtain time");
        return;
    }
    Serial.println(&timeinfo, "%A, %B %d %Y %H:%M:%S");
}
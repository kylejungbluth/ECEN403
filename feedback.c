#include <time.h>
#include <stdio.h>
#include <stdlib.h>
//#include <unistd.h>
#include <dos.h>
#include <Windows.h>

double ammonium;
double magnesium;
double calcium;
double phosphorus;

struct Models {
	double ammonium;
	double magnesium;
	double calcium;
	double phosphorus;
};

struct Models Model1;
struct Models Model2;
struct Models CurrentModel;

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

int main() {

	set_global_values();

	ammonium = 2;
	magnesium = 1.8;
	calcium = 4;
	phosphorus = 6;

	CurrentModel = Model1;

	time_t t;
	srand((unsigned)time(&t));

	while (TRUE) {
		printf("Entering Loop\n");
		printf("sleeping\n");
		Sleep(2000);
		printf("done sleeping\n");
		nutrient_absorption();
		int random = rand() % 2;
		printf("Machine Model Output: %i\n", random);
		update_ML(random);
		sensor_1(CurrentModel);
		sensor_2(CurrentModel);
		
	}
	return 0;
}

void set_global_values() {
	Model1.ammonium = .75;
	Model1.magnesium = .5;
	Model1.calcium = .5;
	Model1.phosphorus = .9;

	Model2.ammonium = 1.4;
	Model2.magnesium = 1.2;
	Model2.calcium = 1.8;
	Model2.phosphorus = 1.9;
}

void sensor_1(struct Models CurrentModel) {
	if (ammonium < CurrentModel.ammonium) {
		//actuator.release()
		//open_actuator_1();
		//close_actuator_1();
		ammonium += .5;
		printf("Nutrient Level: %f", ammonium);
		printf(" ML Level: %f", CurrentModel.ammonium);
		printf(" Release Ammonium.\n");
	}
	else {
		printf("Nutrient Level: %f", ammonium);
		printf(" ML Level: %f", CurrentModel.ammonium);
		printf(" Don't Release Ammonium.\n");
	}
}

void sensor_2(struct Models CurrentModel) {
	if (magnesium < CurrentModel.magnesium) {
		//actuator.release()
		//open_actuator_2();
		//close_actuator_1();
		magnesium += .5;
		printf("Nutrient Level: %f", magnesium);
		printf(" ML Level: %f", CurrentModel.magnesium);
		printf(" Release Magnesium.\n");
	}
	else {
		printf("Nutrient Level: %f", magnesium);
		printf(" ML Level: %f", CurrentModel.magnesium);
		printf(" Don't Release Magnesium.\n");
	}
}

void sensor_3(struct Models CurrentModel) {
	if (calcium < CurrentModel.calcium) {
		//actuator.release()
		//open_actuator_3();
		//close_actuator_3();
		calcium += .5;
		printf("Nutrient Level: %f", calcium);
		printf(" ML Level: %f", CurrentModel.calcium);
		printf(" Release Magnesium.\n");
	}
	else {
		printf("Nutrient Level: %f", calcium);
		printf(" ML Level: %f", CurrentModel.calcium);
		printf(" Don't Release Magnesium.\n");
	}
}

void sensor_4(struct Models CurrentModel) {
	if (phosphorus < CurrentModel.phosphorus) {
		//actuator.release()
		//open_actuator_4();
		//close_actuator_4();
		phosphorus += .5;
		printf("Nutrient Level: %f", phosphorus);
		printf(" ML Level: %f", CurrentModel.phosphorus);
		printf(" Release Magnesium.\n");
	}
	else {
		printf("Nutrient Level: %f", phosphorus);
		printf(" ML Level: %f", CurrentModel.phosphorus);
		printf(" Don't Release Magnesium.\n");
	}
}

void nutrient_absorption() {
	ammonium -= .05;
	magnesium -= .05;
	calcium -= .05;
	phosphorus -= .05;
}

void update_ML(int random) {
	if (random == 0)
		CurrentModel = Model1;
	else
		CurrentModel = Model2;
}
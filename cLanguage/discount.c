#include <stdio.h>


float saleNewFunction(float price);


int main(int argc, char const *argv[])
{
	

	float regular;
	float sale;
	int percentOff;
	printf("Enter the regular price: \n");
	scanf("%f", &regular);
	printf("Enter the percent off: \n");
	scanf("%f", &percentOff);

	printf("Floating-Point Number is : %f \n",regular);

	sale=regular*.85;
	printf("Sale Price: %.2f \n",sale);


	float saleNew=saleNewFunction(regular);

	printf("Sale newPrice: %.2f \n",saleNew);


	return 0;
}

float saleNewFunction(float price)
{
	return price*0.85;
}

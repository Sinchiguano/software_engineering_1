#include <stdio.h>


#define SIZE_MAX 80


int main(void)
{
//int x = atoi(gets("X: "));
//int y=atoi(gets("Y: "));

/*
char inputVariables[SIZE_MAX];
int intStakeholder1;
int intStakeholder2;
printf("Entre X: \n");
scanf("%d \n",&intStakeholder1);
printf("Enter Y: \n");
scanf("%d \n",&intStakeholder2);
printf("%d %d \n",intStakeholder1,intStakeholder2 );
*/

char strVar1[2];
char strVar2[2];
printf("Enter X: ");
gets(strVar1);
printf("Enter Y: ");
gets(strVar2);
int intVar1=atoi(strVar1);
int intVar2=atoi(strVar2);
printf("The sum is: %d\n",intVar1+intVar2 );
}

#include <stdio.h>

const int SIZE = 5;

int main(int argc, char const *argv[])
{
	int numbers[7]={4,8,1,2,0,3,9};
	
	//Linear Search
	int count=sizeof numbers;
	for (int i = 0; i < count; ++i)
	{
		printf("The number is %d - %d \n",i,numbers[i]);
		/* code */
		if (numbers[i]==0)
		{
			printf("Found...\n");
			printf("  ");
			printf("");
			/* code */
		}
	}

	char names[7][7]={"cesar","juan","pedro","julio","pepe","lucas","pedro"};
	
	//Linear Search
	
	for (int i = 0; i < count; ++i)
	{
		//printf("The number is %s - %s \n",i,numbers[i]);
		/* code */
		if (strcmp (names[i],"lucas"))
		{
			printf("Found...\n");
			printf("  ");
			printf("");
			break;
			/* code */
		}
	}




	return 0;
}
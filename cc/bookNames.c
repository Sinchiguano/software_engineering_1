#include <stdio.h>
#include <string.h>



typedef struct people
{
	char name[2][12];
	char number[2][12];
	int countSize;

};



int main(int argc, char const *argv[])
{
	/* code */
	char numbers[2][12]={"0967712084","0990296602"};
	//type of variable [] numbers of strings [] size of the value
	char names[2][9]={"Cesar","Augusto"};

	int count=sizeof numbers;
	for (int i = 0; i <count; ++i)
	{
		if (strcmp(names[i],"cesar"))
		{
			printf("found: %s \n",numbers[i]);
			break;
			/* code */
		}
		/* code */
	}

/*

	people[0].name="Cesar";
	people[0].number="0967712084";

	people[1].name="Juan";
	people[1].number="099029084";


	for (int i = 0; i <people.countSize; ++i)
	{
		if (strcmp(people[i].name,"cesar"))
		{
			printf("found: %s \n",people[i].number);
			break;
			
		}
	
	}	

*/
	return 0;
}
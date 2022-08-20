#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	int list[3];// put information on the stack



	list[0]=1;
	list[1]=2;
	list[2]=3;
	int count=3;
	for (int i = 0; i < count; ++i)
	{
		printf("%i\n",list[i] );
	}



	int *listTmp=malloc(3*sizeof(int));//put the information on the heat

	if (listTmp==NULL)
	{
		return 1;
	}

	listTmp[0]=1;
	listTmp[1]=2;
	listTmp[2]=3;

	for (int i = 0; i < 4; ++i)
	{
		printf("#############################\n" );
	}



	int *listTmp1=malloc(4*sizeof(int));//put the information on the heat

	if (listTmp1==NULL)
	{
		free (listTmp);
		return 1;
	}

	for (int i = 0; i < 3; ++i)
	{
		listTmp1[i]=listTmp[i];
	}
	listTmp1[3]=4;


	for (int i = 0; i < 4; ++i)
	{
		printf("%i\n",listTmp1[i] );
	}



	return 0;
}
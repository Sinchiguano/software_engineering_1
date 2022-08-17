#include <stdio.h>


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

	


	return 0;
}
#include <stdio.h>
#include <string.h>



void draw(int n);


int main(int argc, char const *argv[])
{
	int height=0;
	printf("height: \n");
	scanf("%d", &height);

	draw(height);



	return 0;
}


void draw(int n)
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < i+1; j++)
		{
			printf("#");
		}
	printf("\n");
	}

}
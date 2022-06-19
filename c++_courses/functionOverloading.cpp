#include <iostream>








void printNumber(int x);
void printNumber(float x);




int factorialFinder(int tmp);


int main(int argc, char const *argv[])
{
	int a=45;
	float b=32.4896;


	printNumber(a);
	printNumber(b);

	std::cout<<"Factorial number: "<<factorialFinder(5)<<std::endl;





	return 0;
}
int factorialFinder(int tmp)
{
	if (tmp==1)
	{
		return 1;
	}else{
		return tmp*factorialFinder(tmp-1);
	}
}


void printNumber(int x)
{
	std::cout<<"I am printing integer: "<<x<<std::endl;
}





void printNumber(float x)
{
	std::cout<<"I am printing a float: "<<x<<std::endl;
}

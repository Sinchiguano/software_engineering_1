#include <iostream>




int main(int argc, char const *argv[])
{
	int number=5;
	int fact=1;
	
	for (int i = 1; i <=number; ++i)
	{
		fact=fact*i;
	}
	std::cout<<"The factorial number of "<<number<<" is: "<<fact<<std::endl;
	return 0;
}
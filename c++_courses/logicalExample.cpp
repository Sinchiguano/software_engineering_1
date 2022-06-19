#include <iostream>
#include <cstdlib>

#include<ctime>



int main(int argc, char const *argv[])
{
	int age=21;
	int money=500;
	if (age>=21 && money>=500)
	{
		std::cout<<"you are allowed to go inside"<<std::endl;

	}
		if (age>21 || money>=500)
	{
		std::cout<<"you are allowed to go inside"<<std::endl;

	}

	int count=10;
	srand(time(0));
	for (int i = 0; i < count; ++i)
	{
		std::cout<<1+(rand()%6)<<std::endl;
	}
	



	return 0;



}
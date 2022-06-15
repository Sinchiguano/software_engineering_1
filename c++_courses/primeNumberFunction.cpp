#include <iostream>


bool check_prime(int tmp);

int main(int argc, char const *argv[])
{
	/* code */
	int low, high;
	int tmp;

	std::cout<<"Enter two numbers (intervals): "<<std::endl;
	std::cin>>low>>high;
	//std::cout<<low<<" "<<high<<std::endl;
	//std::cin>>tmp;

	while(low<high){
		std::cout<<low<<std::endl;

		if (check_prime(low))
		{
			std::cout<<"is prime number"<<std::endl;
		}
		else
		{
			std::cout<<"is not a prime number"<<"\n"<<std::endl;
		}

		low++;
	}


	return 0;
}

bool check_prime(int tmp)
{
	bool flag=true;

	if (tmp==0 || tmp ==1)
	{
		flag=false;
	}

	for (int i = 2; i < tmp; ++i)
	{
		if (tmp%i==0)
		{
			flag=false;
			break;
		}
	}
	return flag;

}
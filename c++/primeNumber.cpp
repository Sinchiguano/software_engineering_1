#include <iostream>






int main(int argc, char const *argv[])
{

	bool is_prime=true;
	int n;

	std::cout<<"Enter a number to be checked: ";
	std::cin>>n;

	
	std::cout<<"Your Number is: "<<n<<"\n";

    if (n==0||n==1) {
        is_prime=false;
    }



	for (int i = 2; i < n; ++i)
	{
		/* code */
		if (n%2==0)
		{
			/* code */
			is_prime=false;
			break;	
		}

	}
	if (is_prime)
	{
		/* code */
		std::cout<<"It is a prime number"<<std::endl;
	}
	else{
		std::cout<<"It is not a prime number"<<std::endl;
	}
	return 0;
}
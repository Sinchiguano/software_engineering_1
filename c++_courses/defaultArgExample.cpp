#include <iostream>


int volume(int l=1, int w=1, int h=1);


int tuna=25;



//unary scope resolution operator

int main(int argc, char const *argv[])
{
	int tuna =23;

	std::cout<<volume(2,2)<<std::endl;
	std::cout<<::tuna<<std::endl;


	return 0;
}


int volume(int l, int w, int h)
{

	return l*w*h;

}
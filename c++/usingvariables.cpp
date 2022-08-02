#include<iostream>


int main()
{
    int thisisanumber;

    std::cout<<"Please enter a number: \n";
    std::cin>>thisisanumber;
    std::cin.ignore();
    std::cout<<"You entered: "<<thisisanumber<<"\n";
    std::cin.get();
}
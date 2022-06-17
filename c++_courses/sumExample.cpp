#include <iostream>


int main(int argc, char const *argv[]) {




  int age, ageTotal, numberPeople;
  age=0;
  ageTotal=0;
  numberPeople=0;
  std::cout<<"Enter first persons age or -1 to quit"<<std::endl;
  std::cin>>age;

  while (age!=-1) {
    /* code */
    ageTotal=ageTotal+age;
    numberPeople++;
    std::cout<<"Enter the next age or -1 to quit"<<std::endl;
    std::cin>>age;

  }
  std::cout<<"Number de people enter: "<<ageTotal<<std::endl;
  std::cout<<numberPeople<<std::endl;
  std::cout<<"Average age: "<<ageTotal/numberPeople<<std::endl;
  return 0;
}

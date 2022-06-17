#include <iostream>




int main(int argc, char const *argv[]) {
  int age=21;


  switch (age) {
    case 16:
      std::cout<<"I am allowed to go inside"<<std::endl;
      break;
    case 25:
      std::cout<<"you are not allowed to go inside"<<std::endl;
      break;
    default:
      std::cout<<"sorry you get nothing"<<std::endl;
      

  }
  return 0;
}

#include <iostream>



int main(int argc, char const *argv[]) {
  /* code */
 int counter =0;
 //int container[]={};
int total=0;
int number=0;
  while (counter<3) {
    std::cin >> number;
    total=total+number;
    counter++;

    /* code */
  }

  std::cout<<"Total: "<< total<< std::endl;

  return 0;
}
/*

int counter =0;
int container[]={};

 while (counter<3) {
   std::cin >> container[counter];
   counter++;

 }
 int total=0;
 for (size_t i = 0; i < 3; i++) {

   total=total+container[i];
 }
 std::cout<<"Total: "<< total<< std::endl;


*/

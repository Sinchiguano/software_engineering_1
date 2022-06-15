#include<iostream>


class exampleClass{
    public:
        void coolSaying(){
            std::cout<<"Hello from a class"<<std::endl;
        }

    private:

};


int main()
{
    exampleClass exampleObject;
    exampleObject.coolSaying();



    return 0;
}
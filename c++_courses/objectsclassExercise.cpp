#include<iostream>
#include<string>
//#include<>






class objectsclassExercise
{
public:
	void setName(std::string x){
		name=x;

	};

	objectsclassExercise(std::string z){
		setName(z);


		//std::cout<<"this will get printed automatically"<<std::endl;
	};
	//~objectsclassExercise();

	std::string getName(){
		return name;
	};
private:
	std::string name;

	
};


int main(int argc, char const *argv[])
{
	/* code */

	objectsclassExercise oc("Cesar Sinchiguano");
	//oc.setName("Sir Cesar");
	std::cout<<oc.getName()<<std::endl;


	objectsclassExercise oc2("juan chiriboga");
	//oc.setName("Sir Cesar");
	std::cout<<oc2.getName()<<std::endl;




	return 0;
}






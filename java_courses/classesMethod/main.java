
import java.util.Scanner;


public class main{

	public static void main(String[] args) 
	{
		Scanner input= new Scanner(System.in);
		simpleClass simpleObject=new simpleClass();

		//System.out.println("Enter your name her: ");
		//String name =input.nextLine();
		//simpleObject.message(name);



		System.out.println("Enter the name of first gf here: ");
		String tmp=input.nextLine();
		simpleObject.setName(tmp);
		simpleObject.saying();
	}



}
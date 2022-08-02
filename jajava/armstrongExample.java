import java.util.Scanner;
import java.lang.Math;



class Main{

    static boolean isArmstrong(int n){
        int temp = n;
        int digits=0;
        //gets the number of digits
        while(temp>0){

            temp=temp/10;
            digits++;
        }
        
        temp = n;
        int last, sum;
        sum=0;
        last=0;
        System.out.println(digits);
        while (temp>0){
            //determine the last digits from the number
            last = temp%10;
            //compute the power of a number up to the digit times and add 
            //the resultant to the sum variable 
            sum+=(Math.pow(last,digits));
            //remove the last digit
            temp=temp/10;
        }
        
        System.out.println(n);
        System.out.println(sum);
        if (n==sum) {
            return true;            
        } else {
            return false;            
        }
    }






    public static void main(String[] args) {
        
        int number;
        Scanner sc=new Scanner(System.in);
        
        System.out.print("Enter the number ");
        //read data from the user
        number=sc.nextInt();


 /*
        Scanner tmp=new Scanner(System.in);
        double number1,number2,answer;

        System.out.println("Enter the first number: ");
        number1=tmp.nextDouble();
        System.out.println("Enter the second number: ");
        number2=tmp.nextDouble();
        answer=number1+number2;
        System.out.println(answer);

 */
       
        if (isArmstrong(number)) {
            System.out.print("Armstrong");
            
        } else {
            System.out.print("Not Armstrong");
            
        }
        

    }


  
}
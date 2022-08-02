/**
 * averageApplication
 */


import java.util.Scanner;


public class averageApplication {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int total =0;
        int grade;
        int average;
        int counter=0;
        while(counter < 3){

            grade=input.nextInt();
            total=total+grade;
            counter++;
        }
        System.out.println(total);
        System.out.println(total/counter);
    }
    

}
//    System.out.println(fact);
//    System.out.println(fact);

class FactorialClass
{
    public static void main(String[] args) {
        int fact=1;
        int number=5;
        for (int j = 1; j <= number; j++) {
            fact=fact*j;
        }
        System.out.println("Factorial of "+number+"is: "+fact);

    }
    
}
/**
 * ifstatementExample
 */
public class ifstatementExample {

    public static void main(String[] args) {
        int age=50;

        if (age<50) {
            System.out.println("You are young");
        }else{
            System.out.println("You ar old");
            if (age>75) {
                System.out.println("You are really old!");
            }else{
                System.out.println("do not worry, you are not really that old");
            }
        }
    }
}
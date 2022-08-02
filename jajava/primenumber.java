class PrimeExample{
    public static void main(String[] args) {
        int i,m=0,flag=0;
        int n=3;//it is the number to be check
        boolean is_prime=true;

        if (n==0||n==1) {
            is_prime=false;
        }



        for (i=2;i<n;n++) {
            if (n%2==0) {
                is_prime=false;
                break;             
            }
        }
        if (is_prime) {
        System.out.println("is a prime number");          
        } else {
        System.out.println("is not a prime number");
            
        }



    }
}
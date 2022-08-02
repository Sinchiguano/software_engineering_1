

class apples{

    public static void main(String[] args) {
        
        //a=p(1+r)^n
        double amount;
        double principal=10000;
        double rate=.01;


        for (int day = 0; day < 20; day++) {
            amount=principal*Math.pow(1+rate, day);
            System.out.println(day+"  "+amount);
            
        }







        //for (int i = 0; i < 18; i+=2) {
        //    System.out.println(i);
        //}
        
       
    }




}
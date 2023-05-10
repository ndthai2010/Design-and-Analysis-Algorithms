import java.util.Scanner;

public class SumOfDigits{

    public static int sumDigits(int num){
        if(num == 0){
            return 0;
        }else{
            return num % 10 + sumDigits(num / 10);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Number: ");
        sc.close();
            int num = sc.nextInt();
        System.out.print("Sum digits of " + num + " is " + sumDigits(num));
    }
}
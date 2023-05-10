import java.util.Scanner;

public class StringReverse {
    
    public static String reverse(String s){
        if(s.isEmpty())
            return s;
        return reverse(s.substring(1)) + s.charAt(0);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Original: ");
            String s = sc.nextLine();
        sc.close();
        System.out.print("The reverse string is:" + reverse(s));
    }
}

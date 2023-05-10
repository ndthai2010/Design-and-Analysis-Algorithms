
public class PrimeList {
    
    public static boolean isPrime(int num){
        if (num < 2) 
            return false;
        for(int i = 2; i * i <= num; i++){
            if(num % i == 0){
                return false;
            }
        }
        return true;
    }

    public static void listPrime(int num, int prime){
        if(prime < num){
            if(isPrime(prime)){
                System.out.print(prime + " ");
            }
            listPrime(num, prime + 1);
        }
    }

    public static void main(String[] args) {
        int num = 20;
        System.out.println("Prime numbers less than " + num + " are: ");
        listPrime(num, 2);
    }
}

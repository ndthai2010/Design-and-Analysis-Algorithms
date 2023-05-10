public class ListNPrimes {
    
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

    public static void listPrimes(int num, int prime, int count){
        if(count == num){
            return;
        }

        if(isPrime(prime)){
            System.out.print(prime + " ");
            count++;
        }

        listPrimes(num, prime + 1, count);
    }

    public static void main(String[] args) {
        int num = 5;
        System.out.println("First " + num + " primes are: ");
        listPrimes(num, 2, 0);
    }
}

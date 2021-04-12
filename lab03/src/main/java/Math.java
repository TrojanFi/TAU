public class Math {
    public int numberA,numberB,numberC;
    public int[] array = new int[6];

    public int dividing(int a,int b, int c) {
        try {
            numberA = a;
            numberB = b;
            numberC = c;
            return a/b/c;
        } catch (ArithmeticException arithmeticException) {
            System.out.println("You cant divide by 0 you know that ?!?");
        }
        return 0;
    }

    public boolean primeNumber(int a){

        boolean isPrimeNumber = true;
        for (int i = 2; i <= a / 2; ++i) {
            if (a % i == 0) {
                isPrimeNumber = false;
                break;
            }
        }
        if(isPrimeNumber){
            System.out.println(a + " is a prime number");
            return true;
        }
        else{
            System.out.println(a + " is not a prime number");
            return false;
        }
    }

    public int[] dice(int a){
        for(int i = 0; i < 6; i++){
            array[i] = a++;
        }
        return array;
    }

    public int signsSum(char a, char b){
        return a + b;
    }

    public boolean signsComparison(char a, char b){
        return a > b;
    }

    public boolean stringComparison(String text01, String text02){
        return text01.length() > text02.length();
    }

    public int stringLengthDifference(String text01, String text02){
        return text01.length() - text02.length();
    }
}

public class Exercicio2 {
    static void Fibonacci(int N) {
        int num1 = 0, num2 = 1;
        int contador = 0;

        while (contador < N) {
            System.out.print(num1 + " ");

            int num3 = num2 + num1;
            num1 = num2;
            num2 = num3;
            contador = contador + 1;

            //Verificar sé o número de entrada faz parte da sequência de Fibonacci
            if (N == num1){
                System.out.printf("(%d)\nNúmero %d pertence a sequência de Fibonacci!", num1, num1);
                break;
            }
        }
    }
    public static void main(String[] args){

        int N = 21;

        Fibonacci(N);
    }
}

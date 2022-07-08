public class Exercicio2 {
    static void Fibonacci(int N) {
        int num1 = 0, num2 = 1;
        int contador = 0;

        while (contador < N) {
            System.out.print(num1 + " ");

            //Verificar sé o número de entrada faz parte da sequência de Fibonacci
            if (N == num1){
                System.out.printf("(%d)\n\nNúmero %d PERTENCE a sequência de Fibonacci!\n", num1, num1);
                break;
            }
            else if (num1 > N) {
                System.out.printf("\n\nO número %d NÃO pertence a sequência de Fibonacci\n", num1);
                break;
            }

            int num3 = num2 + num1;
            num1 = num2;
            num2 = num3;
            contador = contador + 1;

        }
    }
    public static void main(String[] args){

        int N = 21;

        Fibonacci(N);
    }
}

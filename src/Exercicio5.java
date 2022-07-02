public class Exercicio5 {
    public static void main(String[] args){

        String nome = "Renan Rhaldney Mello";

        char[] invertido = nome.toCharArray();

        for (int i = invertido.length - 1; i >= 0; i--){

            System.out.print(invertido[i]);

        }

    }
}

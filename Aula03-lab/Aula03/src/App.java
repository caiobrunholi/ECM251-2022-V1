import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        System.out.println("Caio");
        System.out.print("teste");
        System.out.println("Agora Vai!");
        //ler do teclado
        Scanner scanner = new Scanner(System.in);
        System.out.println("Informe 2 numeros");
        double n1, n2;
        n1 = scanner.nextDouble();
        n2 = scanner.nextDouble();
        System.out.println("Soma:" + (n1+n2));
    }
}

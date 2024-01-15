package JavaPOO;
import java.util.Scanner;
public class BoraSomar {

	public static void main(String[] args) {
		int a;
		int b;
		int c;
		int soma1;
		int soma2;
		int multi1;
		int multi2;
		Scanner entrada = new Scanner(System.in);
		System.out.print("Digite um valor: ");
		a = entrada.nextInt();
		System.out.print("Digite um valor: ");
		b = entrada.nextInt();
		System.out.print("Digite um valor: ");
		c = entrada.nextInt();

		
		SomarMetodos calculo = new SomarMetodos();
		soma1 = calculo.somar(a, b);
		System.out.println(soma1);
		soma2 = calculo.somar(a, b, c);
		System.out.println(soma2);
		multi1 = calculo.multiplicar(a, b);
		System.out.println(multi1);
		multi2 = calculo.multiplicar(a, b, c);
		System.out.println(multi2);
	}

}

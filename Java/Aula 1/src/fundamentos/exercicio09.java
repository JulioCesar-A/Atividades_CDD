package fundamentos;
import java.util.Scanner;
public class exercicio09 {

	public static void main(String[] args) {
		double n1;
		Scanner entrada = new Scanner(System.in);
		
		System.out.println("Digite um numero: ");
		n1 = entrada.nextDouble();
		
		if(n1 > 0) {
			System.out.println("Seu numero e positivo");
		}
		else {
			if (n1 < 0) {
				System.out.print("Seu numero e negativo");
			}
			else {
				System.out.println("Esse numero e zero");
				}
			}
		

	}

}

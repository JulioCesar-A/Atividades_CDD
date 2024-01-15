package fundamentos;
import java.util.Scanner;
public class exercicio10 {

	public static void main(String[] args) {
		double n1;
		double n2;
		double n3;
		
		Scanner entrada = new Scanner(System.in);
		System.out.print("Digite o primeiro numero: ");
		n1 = entrada.nextDouble();
		System.out.print("Digite o segundo numero: ");
		n2 = entrada.nextDouble();
		System.out.print("Digite o terceiro numero: ");
		n3 = entrada.nextDouble();
		
		if (n1 > n2){
			if (n1 > n3) {
				if (n2 > n3) {
					System.out.print("Maior: " + n1 + " Menor: " + n3 );
				}
				else {
					System.out.print("Maior: " + n1 + " Menor: " + n2 );
				}
			}
			else {
				System.out.print("Maior: " + n3 + " Menor: " + n2 );
			}
		}
		else {
			if (n2 > n3) {
				if (n3 > n1){
					System.out.print("Maior: " + n2 + " Menor: " + n1 );
				}
				else {
					System.out.print("Maior: " + n3 + " Menor: " + n2 );
				}
			}
			else {
				System.out.print("Maior: " + n3 + " Menor: " + n1 );

			}
			}
}
}
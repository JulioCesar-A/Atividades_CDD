package fundamentos;
import java.util.Scanner;
public class exercicio12 {

	public static void main(String[] args) {
		float nota1;
		float nota2;
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite a primeira nota: ");
		nota1 = entrada.nextFloat();
		System.out.println("Digite a segunda nota: ");
		nota2 = entrada.nextFloat();
		
		float media = (nota1 + nota2)/2;
		
		System.out.println("Media desse aluno(a): " + media);
	}

}

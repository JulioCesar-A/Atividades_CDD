package arrays;
import java.util.Scanner;
public class exercicio_04 {

	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		double notasAl[] = new double [5];
		double soma = 0;
		
		for(int x = 0 ; x < notasAl.length; x++) {
			System.out.printf("Digite a nota do aluno: ");
			notasAl[x] = entrada.nextDouble();
		}
		
		for(double x : notasAl) {
			soma += x;
		}
		double media = soma / notasAl.length;
		System.out.print("Media da turma: " + media);
	}

}

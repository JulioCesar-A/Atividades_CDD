package repeticoes;
import java.util.Scanner;
public class exercicio02 {
public static void main (String[]args) {
	int contAluno = 0;
	float soma = 0;
	Scanner entrada = new Scanner(System.in);
	System.out.println("Digite a quantidade de alunos: ");
	int totAluno = entrada.nextInt();	
	while (contAluno < totAluno) {
		contAluno++;
		System.out.println("Digite a nota do aluno " + contAluno + ": ");
		float nota = entrada.nextFloat();
		soma = soma + nota;
	}
	float media = soma/totAluno;
	System.out.println("A media da sala e: " + media);
}
}
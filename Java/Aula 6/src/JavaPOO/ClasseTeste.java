package JavaPOO;

public class ClasseTeste {

	public static void main(String[] args) {
		ClassePessoa aluno01 = new ClassePessoa();
		aluno01.nome = "Wellington";
		System.out.println(aluno01.nome);
		aluno01.comer();
		
		/*O objeto aluno01 da classe ClassePessoa está 
		  inserindo o valor "Wellington" no atributo "nome" e 
		  executando o método "comer" */
	}

	}

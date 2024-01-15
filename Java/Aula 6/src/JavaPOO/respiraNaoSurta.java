package JavaPOO;

public class respiraNaoSurta {

	public static void main(String[] args) {
		int idadep01;
		double valorp01;
		String nomep01;
		boolean estadop01;
		JavaMetodos pessoa01 = new JavaMetodos();
		
		idadep01 = pessoa01.idade(); 		
		valorp01 = pessoa01.valor(); 		
		nomep01 = pessoa01.nome(); 		
		estadop01 = pessoa01.estado(); 		
		
		System.out.printf("A idade do aluno %s é %d", nomep01,idadep01);
		
/*Boa prática: NÃO realizar o print das informações
 *do objeto da seguinte forma: System.out.println(pessoa01.método());  */
	}

}

package JavaPOO;

public class Carro {
	/*início da classe Carro*/
	
	/*private encapsula os atributos*/
	String cor;
	double preco;
	String modelo;
	
	public Carro() {
/*Recebe nenhum parâmetro*/
	}
	
	public Carro(String modelo, double preco) {
	/*Construtor com 2 parâmetros*/
		
		/*o this cola os valores aos objetos quando eles são criados */
		
		this.cor = "Preta";
		
		this.modelo = modelo;
		this.preco = preco;
		
	/*os atributos modelo e preco recebem os argumentos modelo e preco*/
	}
	public Carro (String cor, String modelo, double preco) {
		/*Construtor com 3 parâmetros*/
		
		
		this.cor = cor;
		this.modelo = modelo;
		this.preco = preco;
	}
	
}

package JavaPOO;

public class concessionaria {

	public static void main(String[] args) {
		
		Carro C1 = new Carro();
		Carro C2 = new Carro("Fuscao", 120000);
		Carro C3 = new Carro("Amalelo", "Celta", 1200);
		
		
		C1.modelo = "C3";
		C1.cor = "marrom";
		C1.preco = 1000;
	}
}


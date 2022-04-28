public class Carro extends Veiculo{
    private String marca;
    private String modelo;

    public Carro(String tipo, int id, String marca, String modelo) {
        super(tipo, id);
        this.marca = marca;
        this.modelo = modelo;
    }
}

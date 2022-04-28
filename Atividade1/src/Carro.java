public class Carro extends Veiculo{
    private String marca;
    private String modelo;

    public Carro(String tipo, int id, String marca, String modelo) {
        super(tipo, id);
        this.setMarca(marca);
        this.setModelo(modelo);
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    @Override
    public String toString() {
        return "Carro [tipo="+tipo+", id="+id+", marca=" + marca + ", modelo=" + modelo + "]";
    }
}

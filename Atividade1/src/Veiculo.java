public class Veiculo {
    protected String tipo;
    protected int id;

    // Consrutor de Classe
    public Veiculo(String tipo, int id) {
        this.tipo = tipo;
        this.id = id;
    }

    public String getTipo() {
        return tipo;
    }
    public void setTipo(String tipo) {
        this.tipo = tipo;
    }
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    
    public void testar(){
        System.out.println("[id=" + id + ", tipo=" + tipo + "]");
    }

    @Override
    public String toString() {
        return "Veiculo [id=" + id + ", tipo=" + tipo + "]";
    }
}

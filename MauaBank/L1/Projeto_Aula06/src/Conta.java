public class Conta{
    //Atributos da nossa classe
    private int numero;
    private double saldo;
    private Cliente cliente;

    public Conta(Cliente cliente, int numero){
        this.numero = numero;
        this.cliente = cliente;
        saldo = 0;
    }

    //Métodos da classe 
    public String vizualizarSaldo(){
        return String.format("R$ %.2f", saldo);
    }

    public boolean depositar(double valor){
        if(valor < 0) return false;

        this.saldo += valor;
        return true;
    }

    public boolean sacar(double valor){
        if (valor > saldo) return false;
        if (valor < 0) return false;
        this.saldo -= valor;
        return true;
    }

    public boolean transferirDinheiro(double valor, Conta destino){
        if(!this.sacar(valor)) return false;
        if(!destino.depositar(valor)) return false;
        return true;
    }

    public String toString(){
        return "Conta Numero:" + numero + 
        "\nSaldo:" + vizualizarSaldo() + 
        "\nCliente:" + cliente.getNome();
    }
}
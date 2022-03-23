public class Conta{
    //Atributos da nossa classe
    private int numero;
    private double saldo;

    //Métodos da classe 

    public void vizualizarSaldo(){
        System.out.println("Saldo atual na conta " + numero + ": R$" + saldo);
    }

    public boolean depositar(double valor){
        // if(valor > 0){
        //     this.saldo = this.saldo + valor;
        //     return true;
        // }else{
        //     return false;
        // }
        if(valor < 0) return false;

        this.saldo += valor;
        return true;
    }

    public boolean sacar(double valor){
        // if(valor<=saldo){
        //     this.saldo = this.saldo - valor;
        // }
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
}
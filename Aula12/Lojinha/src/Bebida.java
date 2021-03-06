public class Bebida extends Produto{
    public final EnumCategoriaBebida categoria;
    public final EnumTemeperatura temperatura;

    public Bebida(double preco, String nome, int quantidade, String descricao, EnumCategoriaBebida categoria,
            EnumTemeperatura temperatura) {
        super(preco, nome, quantidade, descricao);
        this.categoria = categoria;
        this.temperatura = temperatura;
    }

    @Override
    public double gerarDesconto() {
        return getPreco()*0.9;
    }
    
}

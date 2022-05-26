public class App {
    public static void main(String[] args) throws Exception {
        Produto cornDog = new Comida(12.5, "CornDog", 5, "Um cachorrro quente meio errado", EnumCategoriaComida.COREANA, EnumAlergicos.GLUTEM, EnumPimenta.SUAVE);

        Produto acaiMoleza = new Bebida(10.5, "Açai do Moleza", 1, "Real nova fonte de energia", EnumCategoriaBebida.ENERGETICO, EnumTemeperatura.FRIO);

        System.out.println("Preços Regulares:");
        System.out.println(cornDog.getNome() + ":R$"+cornDog.getPreco());
        System.out.println(acaiMoleza.getNome()+":R$"+acaiMoleza.getPreco());

        System.out.println("Preços com Desconto:");
        System.out.println(cornDog.getNome() + ":R$"+precoComDesconto(cornDog));
        System.out.println(acaiMoleza.getNome()+":R$"+precoComDesconto(acaiMoleza));
    }

    public static String precoComDesconto(IGerarDesconto produto){
        return "R$"+produto.gerarDesconto();
    }
}

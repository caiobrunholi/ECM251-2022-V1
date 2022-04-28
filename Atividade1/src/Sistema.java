public class Sistema {
    public void run(){
        Veiculo carro = new Carro("carro", 1000);
        Veiculo moto = new Moto("moto", 20000);
        Veiculo bicicleta = new Bicicleta("bicicleta", 30000);
        Veiculo patinete = new Patinete("patinete", 40000);

        Usuario senna = new Usuario("Senna", 111111111, "airton@mclaren.com", carro);
        Usuario mcqueen = new Usuario("McQueen", 22222222, "bullit@universal.com", moto);
        Usuario eleanor = new Usuario("Eleanor", 333333333, "mustang@60seconds.com", bicicleta);
        Usuario mate = new Usuario("Mate", 444444444, "towmatter@cars.com", patinete);
        
        // carro.testar();
        // System.out.println(senna.getVeiculo());
    }

}

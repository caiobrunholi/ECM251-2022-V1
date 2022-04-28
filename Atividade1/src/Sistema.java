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
        // senna.veiculo.testar();

        trocar(senna, mcqueen);
    }

    public void trocar (Usuario u1, Usuario u2){
        System.out.println("Troca entre: " + u1.getNome() + " e " + u2.getNome());
        System.out.println(u1);
        System.out.println(u2);
        Veiculo veiculoU1 = u1.veiculo;
        Veiculo veiculoU2 = u2.veiculo;
        u1.setVeiculo(veiculoU2);
        u2.setVeiculo(veiculoU1);
        System.out.println("Troca Realizada!");
        System.out.println(u1);
        System.out.println(u2);
        u1.veiculo.testar();
        u2.veiculo.testar();
    }

}

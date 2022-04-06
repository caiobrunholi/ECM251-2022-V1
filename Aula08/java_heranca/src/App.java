public class App {
    public static void main(String[] args) throws Exception {
        Ninja jiraya = new Ninja("Jiraya", "Familia", new String[]{"Corte Vertical", "Corte Horizontal"});
        System.out.println("Treinamento:"+jiraya.train());
        System.out.println(jiraya);
    }
}
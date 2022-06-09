import java.util.ArrayList;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello Hackers");

        ArrayList<Membro> AllMembers = new ArrayList<Membro>();
        
    }

    public static void mudarTurno(EnumTurno turno, ArrayList<Membro> AllMembers){
        for (Membro member : AllMembers){
            member.setTurno(turno);
        }
    }

    public void mandarMensagem(ArrayList<Membro> AllMembers){
        for (Membro member : AllMembers){
            member.mandarMensagem();
        }

    }
}




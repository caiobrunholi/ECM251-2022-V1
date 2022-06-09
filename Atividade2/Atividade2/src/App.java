import java.util.ArrayList;

public class App {
    private static EnumTurno turnoAtual = EnumTurno.REGULAR;
    public static EnumTurno getTurnoAtual() {
        return turnoAtual;
    }

    public static void setTurnoAtual(EnumTurno turnoAtual) {
        App.turnoAtual = turnoAtual;
    }

    public static void main(String[] args) throws Exception {
        System.out.println("Hello Hackers");
        System.out.println("");
        System.out.println(turnoAtual);
        System.out.println("");


        ArrayList<Membro> AllMembers = new ArrayList<Membro>();
        AllMembers.add(new BigBrothers("B1aL", "pedro.bial@globo.br", EnumFuncao.BIGBROTHER, turnoAtual));
        AllMembers.add(new MobileMembers("B4t1ma", "feira_da_fruta@gmail.com", EnumFuncao.MOBILEMEMBER, turnoAtual));
        AllMembers.add(new HeavyLifters("7heR0kc", "dwayne.johnson@gmail.com", EnumFuncao.HEAVYLIFTER, turnoAtual));
        AllMembers.add(new ScriptGuys("100MoL3z4", "adivinha@maua.br", EnumFuncao.SCRIPTGUY, turnoAtual));
        AllMembers.add(new ScriptGuys("BuGzBunn11", "bugsbunny@warnerbros.com", EnumFuncao.SCRIPTGUY, turnoAtual));

        postarMensagem(AllMembers);

        mudarTurno(EnumTurno.EXTRA, AllMembers);
        System.out.println("");
        System.out.println(turnoAtual);
        System.out.println("");

        postarMensagem(AllMembers);

        mudarTurno(EnumTurno.REGULAR, AllMembers);
        System.out.println("");
        System.out.println(turnoAtual);
        System.out.println("");
        
        removerMembro("7heR0kc", AllMembers);
        removerMembro("BuGzBunn11", AllMembers);

        postarMensagem(AllMembers);


        System.out.println("");
        System.out.println("");
        System.out.println("Goodbye! Keep Running and don't Crash!"); 
    }

    public static void mudarTurno(EnumTurno turno, ArrayList<Membro> AllMembers){
        setTurnoAtual(turno);
        for (Membro member : AllMembers){
            member.setTurno(turno);
        }
    }

    public static void postarMensagem(ArrayList<Membro> AllMembers){
        for (Membro member : AllMembers){
            member.mandarMensagem();
        }

    }

    public static void removerMembro(String userName, ArrayList<Membro> AllMembers){
        int i = 0;
        for (Membro member : AllMembers){
            if(member.getUserName().equals(userName)){
                System.out.println(member.getUserName()+"="+userName);
            }
            if(member.getUserName().equals(userName)){
            }else{
                // i++;
            }
        }
        System.out.println("index a ser removido: "+i);
        // AllMembers.remove(i);
    }
}




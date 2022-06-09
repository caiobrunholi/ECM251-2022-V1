public class ScriptGuys extends Membro{
    public ScriptGuys(String userName, String email, EnumFuncao funcao, EnumTurno turno) {
        super(userName, email, funcao, turno);
        //TODO Auto-generated constructor stub
        setRegularMessage(regularMessage);
        setExtraMessage(extraMessage);
    }
    private final String regularMessage = "Prazer em ajudar novos amigos de codigo!";
    private final String extraMessage = "QU3Ro_S3us_r3curs0s.py";
    
}

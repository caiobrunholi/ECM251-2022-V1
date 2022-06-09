public abstract class Membro implements IMandarMensagem{
    private String userName;
    private String email;
    private EnumFuncao funcao;
    private EnumTurno turno;
    private String regularMessage;
    private String extraMessage;

    public String getExtraMessage() {
        return extraMessage;
    }

    public String getRegularMessage() {
        return regularMessage;
    }
    
    public Membro(String userName, String email, EnumFuncao funcao, EnumTurno turno) {
        this.userName = userName;
        this.email = email;
        this.funcao = funcao;
        this.turno = turno;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public EnumFuncao getFuncao() {
        return funcao;
    }

    public void setFuncao(EnumFuncao funcao) {
        this.funcao = funcao;
    }

    public EnumTurno getTurno() {
        return turno;
    }

    public void setTurno(EnumTurno turno) {
        this.turno = turno;
    }

    public void mandarMensagem(){
        if(this.getTurno().equals(EnumTurno.REGULAR)){
            System.out.println("Membro: "+getUserName()+" Funcao: "+getFuncao()+" Mensagem: "+getRegularMessage());
        }else{
            System.out.println("Membro: "+getUserName()+" Funcao: "+getFuncao()+" Mensagem: "+getExtraMessage());
        }
    }
}
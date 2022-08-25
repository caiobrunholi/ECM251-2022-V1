from traceback import print_stack

# Código para escrever dados em um arquivo
try:      
    arquivo = open("data/sistemas.txt", "a")
    continuar = True
    while continuar:
        os_name = input("Diga um OS (vazio para sair):")
        if not os_name:
            continuar = False
            continue
        arquivo.write(os_name+'\n')
    arquivo.close()
except FileNotFoundError:
    print("Caminho nao existe")
except Exception:
    print("Algo nao esperado occorreu:")
    print_stack()
finally:
    print("Chegamso no final")

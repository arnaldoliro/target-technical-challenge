# Primeiramente eu iria ligar o interrupitor A e deixaria ele ligado por cerca de 10 minutos, após isso apagaria ele e ligava o interrupitor B então iria verificar as salas
# se a primeira sala que eu entrasse estivesse com a lâmpada ligada, ela faria referência com o interrupitor B
# Então a próxima sala que eu entrar eu verificaria a temperatura da lampada tocando nela, se estivesse quente faz referência com o interrupitor A e se estivesse fria, com o C

Lampadas = X, Y, Z
Interrupitores = A, B, C

# Primeiro passo:
# Ligar o interrupitor A por 10 min
ligar_por_10_min(A)

# Segundo passo:
# Apagar o Interrupitor A e ligar o interrupitor B
apagar(A)
ligar(B)

# Terceiro passo:
# Verificar a primeira sala
def verificar_salas():
    if X == acesa: # Se a lampada estiver acesa a lampada X = Interrupitor B // Então posso verificar a próxima sala
        print(X = B)

    elif X == apagada: # Se a lâmpada estiver apagada...

        tocar_na_lampada(lampada) # Eu toco nela...
        if lampada == quente: # Se ela estiver quente, a lâmpada X = Interrupitor A
            print('X = A')
        elif lampada == fria: # Se ela estiver fria, a lâmpada X = Interrupitor C
            print('X = C')

# Obtendo qualquer uma das respostas, só preciso verificar a próxima sala e ver se ela satisfaz algum dos casos que sobraram =)


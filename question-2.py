#Função para validar e contar as letras
def count_letters(string):

    count = string.lower().count('a')

    if count > 0:
        print(f"Existem {count} letras 'a' na string '{string}' ")
    else:
        print (f"Não existe letra 'a' na string '{string}'")

string = input("Insira uma string: ")

count_letters(string)
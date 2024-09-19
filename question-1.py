# Função para executar e verificar o número na sequência de Fibonacci
def num_is_fibonacci(num):
    if num < 0:
        return False
    
    a, b = 0, 1

    while b <= num:
        if b == num:
            return True

        a, b = b, a + b
    
    return False

# Função para arredondar números


# Função para fazer os testes
def test_function():
    try:
        num = int(input("Insira um número: "))
        
        if num_is_fibonacci(num):
            print(f"{num} faz parte da sequência de Finonacci")
        elif num == 0:
            print(f"{num} faz parte da sequência de Finonacci")
        else:
            print(f"{num} não faz parte da sequência de Finonacci")
    except ValueError:
        print("A entrada precisa ser um número inteiro")

test_function()
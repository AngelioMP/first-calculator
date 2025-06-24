import os

def input_numbers():
    number1 = int(input("Digite um número: "))
    os.system("cls")
    number2 = int(input("Digite outro número: "))
    os.system("cls")
    return number1, number2

def message_return(message):
    os.system("cls")
    print(message)
    print()
    input("Digite uma tecla para voltar à calculadora.. ")
    os.system("cls")
    main()

def message_options():
    os.system("cls")
    print("CALCULADORA")
    print()
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    print()

def func_calculos(number1, number2):
    type_calculator = int(input("Selecione uma das opções acima: "))
    
    if type_calculator == 1:
        resultado = number1 + number2
    elif type_calculator == 2:
        resultado = number1 - number2
    elif type_calculator == 3:
        resultado = number1 * number2
    elif type_calculator == 4:
        try:
            resultado = number1 / number2
        except ZeroDivisionError:
            message_return("Não é possível dividir por zero.")
    elif type_calculator == 5:
        print()
        print("Fechando Calculadora")
        print()
        os.system('cls')
        return
    else:
        message_return("Essa opção não é válida")
    message_return(f"O resultado do seu cálculo é: {resultado}")

def messages_calculator():
    number1, number2 = input_numbers()
    message_options()
    func_calculos(number1, number2)
def main():
    try:
        messages_calculator()
    except ValueError:
        message_return("Digite apenas números.")
main()
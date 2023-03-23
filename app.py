from calculadoraDeOperacoes import CalculadoradeOperacoes

class App:

    #Cria uma instância da classe Calculadora de Operações
    calculadoraObj = CalculadoradeOperacoes()

    while True:    
        try:
            #Recebe a expressão via linha de comando e faz o split
            expressaoCompleta = input("Digite uma expressão no formato -> 'valor1 operação valor2'.\nExemplo: 10 / 2 :\n ")
            valor1, operacao, valor2 = expressaoCompleta.split()

            #Convertendo para float
            valor1 = float(valor1)
            valor2 = float(valor2)

            retorno = calculadoraObj.calculaResultado(valor1, valor2, operacao)
            
            if (retorno == False):
                continue
            else:
                print(retorno)
                break

        except ValueError:
            print("A expressão digitada é inválida\n\n")
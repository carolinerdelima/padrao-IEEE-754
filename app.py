from calculadoraDeOperacoes import CalculadoradeOperacoes

class App:

    #Cria uma instância da classe Calculadora de Operações
    calculadoraObj = CalculadoradeOperacoes()

    while True:    
        try:
            #Recebe a expressão via linha de comando e faz o split
            expressaoCompleta = input("\nDigite uma expressão no formato -> 'valor1 operação valor2'.\nExemplo: 10 / 2 :\n ")
            valor1, operacao, valor2 = expressaoCompleta.split()

            if (expressaoCompleta == 'sair'):
                break

            #Convertendo para float
            valor1 = float(valor1)
            valor2 = float(valor2)

            retorno = calculadoraObj.calculaResultado(valor1, valor2, operacao)
            print("O resultado da operação é: {}".format(retorno))

            #Mostrando a configuração de bits das duas variáveis e do resultado
            print("\nAqui está a configuração de bits das variáveis e do resultado:")
            print("Valor1 -> {}:".format(valor1), calculadoraObj.floatParaBinario(valor1))
            print("Valor2 -> {}:".format(valor2),calculadoraObj.floatParaBinario(valor2))
            
            if (retorno != None):
                print("Resultado-> {}:".format(retorno), calculadoraObj.floatParaBinario(float(retorno)))

        except ValueError:
            print("A expressão digitada é inválida\n\n")
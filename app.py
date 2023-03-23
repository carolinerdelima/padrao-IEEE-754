from calculadoraDeOperacoes import CalculadoradeOperacoes

class App:

    #Cria uma instância da classe Calculadora de Operações
    calculadoraObj = CalculadoradeOperacoes()

    while True:    
        try:
            #Recebe a expressão via linha de comando e faz o split
            expressaoCompleta = input("\nDigite uma expressão no formato -> 'valor1 operação valor2'.\nExemplo: 10 / 2 :\n ")
            if (expressaoCompleta == 'sair'):
                break

            valor1, operacao, valor2 = expressaoCompleta.split()

            #Convertendo para float
            valor1 = float(valor1)
            valor2 = float(valor2)

            retorno = calculadoraObj.calculaResultado(valor1, valor2, operacao)
            
            #Tratamento dos retornos
            if retorno is None:
                print("A expressão digitada é inválida\n\n")
                continue
            elif isinstance(retorno, str):
                print(retorno)
            else:
                print(retorno)

                # Mostrando a configuração de bits das duas variáveis e do resultado
                print("\nAqui está a configuração de bits das variáveis e do resultado:")
                print("Valor1:", calculadoraObj.floatParaBinario(valor1))
                print("Valor2:",calculadoraObj.floatParaBinario(valor2))
                print("Resultado:", calculadoraObj.floatParaBinario(retorno))

        except CalculadoradeOperacoes.IEEE754Exception as e:
            print("Resultado: {}".format(e.args[0]))
            print("Exception: {}".format(e.args[1]))
            break
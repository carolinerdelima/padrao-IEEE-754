import math
import struct

class CalculadoradeOperacoes:

    class IEEE754Exception(Exception):
        pass

    def calculaResultado(self, valor1, valor2, operacao):
        self.verificaIntervaloPontoFlutuante(valor1)
        self.verificaIntervaloPontoFlutuante(valor2)

        try:
            if operacao == '+':
                resultado = valor1 + valor2
            elif operacao == '-':
                resultado = valor1 - valor2
            elif operacao == '*':
                resultado = valor1 * valor2
            elif operacao == '/':
                resultado = valor1 / valor2
                if math.isnan(resultado):
                    return "Not a Number."
                elif math.isinf(resultado):
                    if resultado > 0:
                        return "+infinito"
                    else:
                        return "-infinito"
            else:
                return ("A operação informada não foi reconhecida.")

            return self.verificaResultadosEspeciais(resultado)

        except ZeroDivisionError:
            print("Exception ZeroDivisionError: Divisão por zero encontrada na expressão: {} {} {}".format(valor1, operacao, valor2))
            resultado = float('inf')
            if resultado > 0:
                return "+ infinito"
            else:
                return "- infinito"

        except CalculadoradeOperacoes.IEEE754Exception as e:
            print("Resultado: {}. Erro: {}".format(e.args[0], e.args[1]))
            print("Exception: Ocorreu um erro IEEE754Exception na expressão: {} {} {}".format(valor1, operacao, valor2))

        except ValueError as e:
            print(e.args[0])

    #Verifica se aquele valor está no intervalo permitido para representação em ponto flutuante
    @staticmethod
    def verificaIntervaloPontoFlutuante(valor):
        if valor < -math.pow(2, 127) or valor > math.pow(2, 127):
            raise ValueError("Valor fora do intervalo permitido para representação em ponto flutuante de 32 bits. Valor: " + str(valor))
        else:
            return valor


    @staticmethod
    def verificaResultadosEspeciais(resultado):
        #self.verificaIntervaloPontoFlutuante(resultado)

        #Usa a biblioteca para validar se o resultado é infinito
        if math.isnan(resultado):
            return "Not a Number."
        elif math.isinf(resultado):
            if resultado > 0:
                return "+infinito"
            else:
                return "-infinito"
        else:
            return resultado


    @staticmethod
    def floatParaBinario(valorFloat):
        try:
            #Converte o float para uma string de bytes
            aux = struct.pack('>f', valorFloat)

            #Converte a string de bytes para uma sequência de bits
            bits = ''.join('{:08b}'.format(c) for c in aux)

            #Verifica underflow e overflow
            tamanho_float_bits = struct.calcsize('f') * 8
            if len(bits) < tamanho_float_bits:
                print("Exception UNDERFLOW: Houve underflow na conversão para binário.")
            elif len(bits) > tamanho_float_bits:
                print("Exception OVERFLOW: Houve overflow na conversão para binário.")

            return bits
        except OverflowError:
            print("Exception OVERFLOW: O resultado é maior do que o maior número representável.")

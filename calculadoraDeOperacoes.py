import math
import struct

class CalculadoradeOperacoes:

    #Serve basicamente para tratar as Exceptions do padrão IEEE-754
    class IEEE754Exception(Exception):
        pass

    def calculaResultado(self, valor1, valor2, operacao):

        resultadoReal = None

        try:
            self.verificaIntervaloPontoFlutuante(valor1)
            self.verificaIntervaloPontoFlutuante(valor2)

            if operacao == '+':
                resultado = valor1 + valor2
            elif operacao == '-':
                resultado = valor1 - valor2
            elif operacao == '*':
                resultado = valor1 * valor2
            elif operacao == '/':
                resultado = valor1 / valor2
            else:
                return ("A operação informada não foi reconhecida.")

            resultadoReal = self.verificaResultadosEspeciais(resultado)

        except FloatingPointError as error:
            print("Erro de ponto flutuante: {}".format(str(error)))
            raise error

        except OverflowError:
            print("Exception OVERFLOW: O resultado é maior do que o maior número representável.")
            raise self.IEEE754Exception(resultado, "OVERFLOW")

        except ValueError as e:
            print(e.args[0])
            return None
        
        finally:
            print("O resultado da operação é: {}".format(resultadoReal))
            return resultadoReal

    #Verifica se aquele valor está no intervalo permitido para representação em ponto flutuante
    @staticmethod
    def verificaIntervaloPontoFlutuante(valor):
        if valor < -math.pow(2, 127) or valor > math.pow(2, 127):
            raise ValueError("Valor fora do intervalo permitido para representação em ponto flutuante de 32 bits. Valor:" + str(valor))
        else:
            return valor


    @staticmethod
    def verificaResultadosEspeciais(resultado):
        #self.verificaIntervaloPontoFlutuante(resultado)

        #Usa a biblioteca para validar se o resultado é infinito
        if math.isinf(resultado):
            if resultado > 0:
                return "O resultado é: + infinito"
            else:
                return "O resultado é: - infinito"
        elif math.isnan(resultado):
            return "Exception NAN: O resultado é: Not a Number."
        else:
            return resultado


    @staticmethod
    def floatParaBinario(valorFloat):
        #Converte o float para uma string de bytes
        aux = struct.pack('>f', valorFloat)

        #Converte a string de bytes para uma sequência de bits
        bits = ''.join('{:08b}'.format(c) for c in aux)
        return bits
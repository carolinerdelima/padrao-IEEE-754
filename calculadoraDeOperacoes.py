import math
import struct

class CalculadoradeOperacoes:

    @staticmethod
    def verificaInfinito(resultado):
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

        #Verifica underflow e overflow
        tamanho_float_bits = struct.calcsize('f') * 8
        if len(bits) < tamanho_float_bits:
            print("Exception UNDERFLOW: Houve underflow na conversão para binário.")
        elif len(bits) > tamanho_float_bits:
            print("Exception OVERFLOW: Houve overflow na conversão para binário.")

        return bits

    def calculaResultado(self, valor1, valor2, operacao):
        try:
            if operacao == '+':
                resultado = valor1 + valor2
            elif operacao == '-':
                resultado = valor1 - valor2
            elif operacao == '*':
                resultado = valor1 * valor2
            elif operacao == '/':
                resultado = valor1 / valor2
            else:
                return False

            resultadoReal = self.verificaInfinito(resultado)
            print("O resultado é:", resultadoReal)

            #Mostrando a configuração de bits das duas variáveis e do resultado
            print("\nAqui está a configuração de bits das variáveis e do resultado:")
            print("Valor1:", self.floatParaBinario(valor1))
            print("Valor2:",self.floatParaBinario(valor2))
            print("Resultado:", self.floatParaBinario(resultado))

        except ZeroDivisionError:
            print("Exception DIVBYZERO: Não é possível dividir por zero.")
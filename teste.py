# Importações padrão do Python
import textwrap
from abc import ABC, abstractmethod  # Não usado no momento, mas mantido para possível uso futuro
from datetime import datetime         # Também não utilizado, mas pode ser útil depois

# Classe que representa o investimento
class Investimento:
    def __init__(self):
        # Inicializa os atributos com valores padrão
        self._valor_investido = 0.0  # Armazena o valor do investimento feito pelo usuário
        self._tempo = 0              # Armazena o tempo de investimento em meses

        # Taxas de rendimento mensais para cada tipo de investimento
        self._taxa_cdb = 0.015       # CDB rende 1,5% ao mês
        self._taxa_cdi = 0.012       # CDI rende 1,2% ao mês
        self._taxa_selic = 0.010     # Selic rende 1,0% ao mês
        self._taxa_poupanca = 0.005  # Poupança rende 0,5% ao mês

    def definir_investimento(self, valor, tempo):
        """
        Método usado para definir os dados do investimento com base na entrada do usuário.
        Também faz validação simples dos valores.
        """
        if valor <= 0 or tempo <= 0:
            raise ValueError("Valor e tempo devem ser positivos.")
        self._valor_investido = valor
        self._tempo = tempo

    @property
    def cdb(self):
        """
        Calcula o valor final de um investimento em CDB usando juros compostos:
        Fórmula: Valor Final = Valor Inicial * (1 + taxa) ** tempo
        """
        return self._valor_investido * (1 + self._taxa_cdb) ** self._tempo

    # As demais propriedades ainda não foram implementadas, apenas placeholders
    @property  
    def CDI(self): 
        return None
    
    @property  
    def Selic(self): 
        return None
    
    @property  
    def poupanca(self): 
        return None


# Função que exibe o menu principal ao usuário
def menu():
    print("[1] - CDB")
    print("[2] - CDI")
    print("[3] - Selic")
    print("[4] - Poupança")
    print("[5] - SAIR")
    print("="*70)
    opcao = input("Para prosseguir, escolha uma opção válida: ")
    return opcao  # Retorna a opção digitada pelo usuário


# Função que recebe e retorna o valor a ser investido
def valor_investido():
    valor = input("Insira o valor que deseja investir: ")
    return float(valor)  # Converte o valor digitado em número decimal (float)


# Função que recebe e retorna o tempo de investimento
def meses_investido():
    meses = input("Por quanto tempo você deseja deixar rendendo? (em meses) ")
    return int(meses)  # Converte a entrada em número inteiro


# Criação da instância da classe Investimento antes do loop principal
investimento = Investimento()

# Loop principal do programa
while True:
    opcao = menu()  # Mostra o menu e recebe a escolha do usuário

    # Se o usuário escolher a opção 1 (CDB)
    if opcao == "1":
        valor = valor_investido()     # Pergunta o valor a ser investido
        tempo = meses_investido()     # Pergunta o tempo de investimento

        # Define os valores no objeto de investimento
        investimento.definir_investimento(valor, tempo)

        # Realiza o cálculo de retorno para CDB
        retorno = investimento.cdb

        # Exibe as informações formatadas para o usuário
        print(f"\nValor investido: R$ {valor:.2f}")
        print(f"Tempo: {tempo} meses")
        print(f"Retorno estimado em CDB: R$ {retorno:.2f}\n")

    # As demais opções ainda não foram implementadas
    elif opcao == "2":
        print("Opção CDI selecionada.")
    elif opcao == "3":
        print("Opção Selic selecionada.")
    elif opcao == "4":
        print("Opção Poupança selecionada.")
    elif opcao == "5":
        print("Saindo...")  # Finaliza o programa
        break
    else:
        print("Opção inválida. Tente novamente.")  # Trata entradas incorretas

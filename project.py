import textwrap
from abc import ABC, abstractmethod
from datetime import datetime 

class Investimento:
    def __init__(self):
        # Inicializa os valores padrão
        self._valor_investido = 0.0
        valor_investido = 0
        self._taxa_cdb = 0.015  # Exemplo de 1,5% ao mês
        self._taxa_cdi = 0.012  # Exemplo de 1,2% ao mês
        self._taxa_selic = 0.010  # Exemplo de 1% ao mês
        self._taxa_poupanca = 0.005  # Exemplo de 0,5% ao mês

    @property
    def cdb(self):
       return self._valor_investido * (1 + self._taxa_cdb) ** valor_investido
    
    @property  
    def CDI(self): 
        return self._cdi
    
    @property  
    def Selic(self): 
        return self._selic
    
    @property  
    def poupanca(self): 
        return self._poupanca

# Comentário de teste para pull request

def menu():
    print("[1] - CDB")
    print("[2] - CDI")
    print("[3] - Selic")
    print("[4] - Poupança")
    print("[5] - SAIR")
    print("="*70)
    opcao = input("Para prosseguir, escolha uma opção válida: ")
    return opcao

def valor_investido():
    valor = input("Insira o valor que deseja investir: ")
    return float(valor)  # Convertendo para float para realizar cálculos depois

def meses_investido():
    meses = input("Por quanto tempo você deseja deixar rendendo? (em meses) ")
    return int(meses)  # Convertendo para inteiro para cálculo do tempo

while True:
    opcao = menu()  # Chama o menu
    if opcao == "1":
        valor = valor_investido()  # Chama a função para capturar o valor
        tempo = meses_investido()  # Chama a função para capturar o tempo
        print(f"Valor: {valor}, Tempo: {tempo} meses")
    elif opcao == "2":
        print("Opção CDI selecionada.")
    elif opcao == "3":
        print("Opção Selic selecionada.")
    elif opcao == "4":
        print("Opção Poupança selecionada.")
    elif opcao == "5":
        print("Saindo...")
        break  # Encerra o programa
    else:
        print("Opção inválida. Tente novamente.")

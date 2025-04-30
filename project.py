import textwrap
from abc import ABC, abstractmethod
from datetime import datetime 

class Investimento:
    def __init__(self):
        # Inicializa sem taxas, pois serão informadas pelo usuário
        self._cdb = 0.0
        self._cdi = 0.0
        self._selic = 0.0
        self._poupanca = 0.0

    @property  
    def CDB(self): 
        return self._cdb
    
    @property  
    def CDI(self): 
        return self._cdi
    
    @property  
    def Selic(self): 
        return self._selic
    
    @property  
    def poupanca(self): 
        return self._poupanca


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

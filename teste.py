class Investimento:
    def __init__(self):
        self._valor_investido = 0.0
        self._tempo = 0
        self._taxa_cdb = 0.015
        self._taxa_cdi = 0.012
        self._taxa_selic = 0.010
        self._taxa_poupanca = 0.005

    def definir_investimento(self, valor, tempo):
        if valor <= 0 or tempo <= 0:
            raise ValueError("Valor e tempo devem ser positivos.")
        self._valor_investido = valor
        self._tempo = tempo

    @property
    def cdb(self):
        return self._valor_investido * (1 + self._taxa_cdb) ** self._tempo

    @property
    def cdi(self):
        return self._valor_investido * (1 + self._taxa_cdi) ** self._tempo

    @property
    def selic(self):
        return self._valor_investido * (1 + self._taxa_selic) ** self._tempo

    @property
    def poupanca(self):
        return self._valor_investido * (1 + self._taxa_poupanca) ** self._tempo



# Função que exibe o menu principal ao usuário
def menu():
    print("="*70)
    print("   *** SIMULADOR DE INVESTIMENTOS ***   ".center(70))
    print("="*70)

    print("\nEscolha uma opção para simulação de investimento:")
    print("-"*70)
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
    if opcao == "1":
        valor = valor_investido()     # Pergunta o valor a ser investido
        tempo = meses_investido()     # Pergunta o tempo de investimento

        investimento.definir_investimento(valor, tempo) # Define os valores no objeto de investimento

        retorno = investimento.cdb # Realiza o cálculo de retorno para CDB

        print(f"\nValor investido: R$ {valor:.2f}")# Exibe as informações formatadas para o usuário
        print(f"Tempo: {tempo} meses")
        print(f"Retorno estimado em CDB: R$ {retorno:.2f}\n")  #:.2f Indica o resultado em 2 casas decimais, f de número flutuante

    elif opcao == "2":
        valor = valor_investido()
        tempo = meses_investido()

        investimento.definir_investimento(valor, tempo)
        retorno = investimento.cdb
        
        print(f"\nValor investido: R$ {valor:.2f}")
        print(f"Tempo: {tempo} meses")
        print(f"Retorno estimado em CDB: R$ {retorno:.2f}\n")

    elif opcao == "3":
        print("Opção Selic selecionada.")
    elif opcao == "4":
        print("Opção Poupança selecionada.")
    elif opcao == "5":
        print("Saindo...")  # Finaliza o programa
        break
    else:
        print("Opção inválida. Tente novamente.")  # Trata entradas incorretas

class Investimento:
    def __init__(self):
        # Inicializa sem taxas, pois serão informadas pelo usuário
        self.CDB = 0.0
        self.CDI = 0.0
        self.Selic = 0.0
        self.poupanca = 0.0

    def set_taxas(self):
        # Solicita ao usuário as taxas de cada tipo de investimento
        self.CDB = float(input("Digite a taxa de rendimento do CDB (em % ao mês): ")) / 100
        self.CDI = float(input("Digite a taxa de rendimento do CDI (em % ao mês): ")) / 100
        self.Selic = float(input("Digite a taxa de rendimento da Selic (em % ao mês): ")) / 100
        self.poupanca = float(input("Digite a taxa de rendimento da Poupança (em % ao mês): ")) / 100

    def calcular_rendimento(self, investimento_escolhido, valor_investido, meses):
        # Calcula o rendimento com base no investimento escolhido
        if investimento_escolhido == "CDB":
            rendimento = valor_investido * (1 + self.CDB) ** meses
        elif investimento_escolhido == "CDI":
            rendimento = valor_investido * (1 + self.CDI) ** meses
        elif investimento_escolhido == "Selic":
            rendimento = valor_investido * (1 + self.Selic) ** meses
        elif investimento_escolhido == "poupanca":
            rendimento = valor_investido * (1 + self.poupanca) ** meses
        else:
            print("Investimento não reconhecido")
            return None
        return rendimento

    def investir(self):
        # Solicita os inputs ao usuário
        print("Escolha um modelo de investimento: CDB, CDI, Selic, Poupança")
        investimento_escolhido = input("Qual investimento você deseja fazer? ").strip()

        if investimento_escolhido not in ["CDB", "CDI", "Selic", "poupanca"]:
            print("Opção inválida! Tente novamente.")
            return
        
        valor_investido = float(input("Qual o valor a ser investido? R$ "))
        meses = int(input("Por quantos meses você quer investir? "))
        
        # Calcula o rendimento
        rendimento = self.calcular_rendimento(investimento_escolhido, valor_investido, meses)
        
        if rendimento:
            print(f"O rendimento do seu investimento em {investimento_escolhido} será de R$ {rendimento:.2f}")


# Exemplo de uso
objetos = Investimento()
objetos.set_taxas()  # Definir as taxas de investimento
objetos.investir()   # Realizar o cálculo do rendimento com base nas taxas fornecidas

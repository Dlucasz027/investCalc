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
    
    def _calcular_imposto(self, retorno_bruto):
        if self._tempo <= 180:
            aliquota_ir = 0.225
        elif self._tempo <= 360:
            aliquota_ir = 0.20
        elif self._tempo <= 720:
            aliquota_ir = 0.175
        else:
            aliquota_ir = 0.15
        
        # Cálculo do valor líquido após desconto de IR
        retorno_liquido = retorno_bruto * (1 - aliquota_ir)
        return retorno_liquido

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

def valor_investido():
    while True:
        valor = input("Insira o valor que deseja investir: ")
        if valor.replace('.', '', 1).isdigit() and valor.count('.') <= 1:  # Garante que se houver mais de um ponto( . ) ele vai ser removido / isdigit() garante que vai ser somente números
            valor = float(valor)
            if valor <= 0:
                print("O valor deve ser maior que zero. Tente novamente.")
            else:
                return valor
        else:
            print("Erro: O valor deve ser um número válido. Tente novamente.")

def meses_investido():
    while True:
        meses = input("Por quanto tempo você deseja deixar rendendo? (em meses) ")
        if meses.isdigit(): 
            meses = int(meses)
            if meses <= 0:
                print("O tempo deve ser maior que zero. Tente novamente.")
            else:
                return meses
        else:
            print("Erro: O tempo deve ser um número válido. Tente novamente.")

investimento = Investimento()  # Instância da classe Investimento antes do loop principal

while True:
    opcao = menu() 
    if opcao == "1":
        valor = valor_investido()   
        tempo = meses_investido()     

        investimento.definir_investimento(valor, tempo) # Chama o método da instância Investimento e passando valores

        retorno_bruto = investimento.cdb # Acessando a propriedade com o decorador, busca o cáculo de lá
        retorno_liquido = investimento._calcular_imposto(retorno_bruto) # Acessa a função para calcular imposto na classe investimentos

        lucro_bruto = retorno_bruto - valor
        lucro_liquido = retorno_liquido - valor
        
        print(f"\nValor investido: R$ {valor:.2f}")
        print(f"Tempo: {tempo} meses")

        print(f"\n📈 Retorno BRUTO (sem IR): R$ {retorno_bruto:.2f}")
        print(f"💰 Lucro BRUTO: R$ {lucro_bruto:.2f}")

        print(f"\n✅ Retorno LÍQUIDO (com IR): R$ {retorno_liquido:.2f}")
        print(f"🏦 Lucro LÍQUIDO: R$ {lucro_liquido:.2f}\n")

    elif opcao == "2":
        valor = valor_investido()   
        tempo = meses_investido()     

        investimento.definir_investimento(valor, tempo)
        retorno_bruto = investimento.cdi
        retorno_liquido = investimento._calcular_imposto(retorno_bruto)

        lucro_bruto = retorno_bruto - valor
        lucro_liquido = retorno_liquido - valor
        
        print(f"\nValor investido: R$ {valor:.2f}")
        print(f"Tempo: {tempo} meses")

        print(f"\n📈 Retorno BRUTO (sem IR): R$ {retorno_bruto:.2f}")
        print(f"💰 Lucro BRUTO: R$ {lucro_bruto:.2f}")

        print(f"\n✅ Retorno LÍQUIDO (com IR): R$ {retorno_liquido:.2f}")
        print(f"🏦 Lucro LÍQUIDO: R$ {lucro_liquido:.2f}\n")


    elif opcao == "3":
        valor = valor_investido()
        tempo = meses_investido()

        investimento.definir_investimento(valor, tempo)
        retorno = investimento.selic
        
        print(f"\nValor investido: R$ {valor:.2f}")
        print(f"\nRetorno estimado com o investimento aplicado na taxa Selic: R$ {retorno:.2f}")
        print(f"Rendimento (lucro obtido): R$ {retorno - valor:.2f}\n")

    elif opcao == "4":
        valor = valor_investido()
        tempo = meses_investido()

        investimento.definir_investimento(valor, tempo)
        retorno = investimento.poupanca
        
        print(f"\nValor investido: R$ {valor:.2f}")
        print(f"\nRetorno estimado com o pior investimento do mundo, a Poupança: R$ {retorno:.2f}")
        print(f"Rendimento (lucro obtido bruto): R$ {retorno - valor:.2f}\n\n")

    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")

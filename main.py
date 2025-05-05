class Investimento:
    def __init__(self):
        self._valor_investido = 0.0
        self._tempo = 0
        self._taxa_cdb = 0.015  # taxa base (100%)
        self._taxa_cdi = 0.012  # taxa base (100%)
        self._taxa_selic = 0.010
        self._taxa_poupanca = 0.005
        self._ajuste_cdb = 1.0
        self._ajuste_cdi = 1.0

    def definir_investimento(self, valor, tempo): 
        if valor <= 0 or tempo <= 0:
            raise ValueError("Valor e tempo devem ser positivos.")
        self._valor_investido = valor
        self._tempo = tempo

    def ajustar_cdb(self, porcentagem):
        if porcentagem < 100:
            print("⚠️ O valor informado é menor que 100%. Usando padrão de 100%.")
            self._ajuste_cdb = 1.0
        else:
            self._ajuste_cdb = porcentagem / 100

    def ajustar_cdi(self, porcentagem):
        if porcentagem < 100:
            print("⚠️ O valor informado é menor que 100%. Usando padrão de 100%.")
            self._ajuste_cdi = 1.0
        else:
            self._ajuste_cdi = porcentagem / 100

    @property
    def cdb(self):
        taxa_final = self._taxa_cdb * self._ajuste_cdb
        return self._valor_investido * (1 + taxa_final) ** self._tempo

    @property
    def cdi(self):
        taxa_final = self._taxa_cdi * self._ajuste_cdi
        return self._valor_investido * (1 + taxa_final) ** self._tempo

    @property
    def selic(self):
        return self._valor_investido * (1 + self._taxa_selic) ** self._tempo

    @property
    def poupanca(self):
        return self._valor_investido * (1 + self._taxa_poupanca) ** self._tempo
    
    def _calcular_imposto(self, retorno_bruto):
        dias = self._tempo * 30  # Converte meses em dias, pois o imposto muda dependendo da quantidade de dias investido

        if dias <= 180:  #180 dias = 22,5% (Adaptado para meses com self._tempo, assumindo que o mês tem 30 dias)
            aliquota_ir = 0.225  
        elif dias <= 360:  #181 a 360 dias = 20%
            aliquota_ir = 0.20
        elif dias <= 720:  #361 a 720 dias = 17%
            aliquota_ir = 0.175
        else:
            aliquota_ir = 0.15 #Acima de 720 dias
        
        # Cálculo do valor líquido após desconto de IR
        rendimento = retorno_bruto - self._valor_investido
        imposto = rendimento * aliquota_ir
        retorno_liquido = retorno_bruto - imposto
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
        
        try:
            porcentagem = float(input("Informe a porcentagem do CDB (mínimo 100, ex: 110 para 110%): "))
        except ValueError:
            print("Entrada inválida. Usando padrão de 100%.")
            porcentagem = 100
        
        investimento.definir_investimento(valor, tempo)
        investimento.ajustar_cdb(porcentagem)

        retorno_bruto = investimento.cdb
        retorno_liquido = investimento._calcular_imposto(retorno_bruto)

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

        try:
            porcentagem = float(input("Informe a porcentagem do CDI (mínimo 100, ex: 110 para 110%): "))
        except ValueError:
            print("Entrada inválida. Usando padrão de 100%.")
            porcentagem = 100

        investimento.definir_investimento(valor, tempo)
        investimento.ajustar_cdi(porcentagem)

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
        print(f"\nRetorno estimado com o investimento aplicado na Poupança: R$ {retorno:.2f}")

    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")


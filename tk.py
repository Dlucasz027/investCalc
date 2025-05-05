import customtkinter as ctk

class Investimento:
    def __init__(self):
        self._valor_investido = 0.0
        self._tempo = 0
        self._taxa_cdb = 0.015
        self._taxa_cdi = 0.012
        self._taxa_selic = 0.010
        self._taxa_poupanca = 0.005
        self._ajuste_cdb = 1.0
        self._ajuste_cdi = 1.0

    def definir_investimento(self, valor, tempo):
        self._valor_investido = valor
        self._tempo = tempo

    def ajustar_cdb(self, porcentagem):
        self._ajuste_cdb = porcentagem / 100 if porcentagem >= 100 else 1.0

    def ajustar_cdi(self, porcentagem):
        self._ajuste_cdi = porcentagem / 100 if porcentagem >= 100 else 1.0

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
        dias = self._tempo * 30
        if dias <= 180:
            aliquota_ir = 0.225
        elif dias <= 360:
            aliquota_ir = 0.20
        elif dias <= 720:
            aliquota_ir = 0.175
        else:
            aliquota_ir = 0.15

        rendimento = retorno_bruto - self._valor_investido
        imposto = rendimento * aliquota_ir
        return retorno_bruto - imposto

# INTERFACE COM CUSTOMTKINTER
def calcular_investimento():
    try:
        valor = float(entry_valor.get())
        tempo = int(entry_tempo.get())
        tipo = combo_tipo.get()
        porcentagem = float(entry_porcentagem.get()) if entry_porcentagem.get() else 100

        investimento = Investimento()
        investimento.definir_investimento(valor, tempo)

        if tipo == "CDB":
            investimento.ajustar_cdb(porcentagem)
            bruto = investimento.cdb
            liquido = investimento._calcular_imposto(bruto)
        elif tipo == "CDI":
            investimento.ajustar_cdi(porcentagem)
            bruto = investimento.cdi
            liquido = investimento._calcular_imposto(bruto)
        elif tipo == "Selic":
            bruto = liquido = investimento.selic
        elif tipo == "Poupança":
            bruto = liquido = investimento.poupanca
        else:
            output_box.configure(state="normal")
            output_box.delete("1.0", "end")
            output_box.insert("end", "Selecione um tipo de investimento.")
            output_box.configure(state="disabled")
            return

        lucro_bruto = bruto - valor
        lucro_liquido = liquido - valor

        output_box.configure(state="normal")
        output_box.delete("1.0", "end")
        output_box.insert("end",
            f"Retorno BRUTO: R$ {bruto:.2f}\n"
            f"Lucro BRUTO: R$ {lucro_bruto:.2f}\n\n"
            f"Retorno LÍQUIDO: R$ {liquido:.2f}\n"
            f"Lucro LÍQUIDO: R$ {lucro_liquido:.2f}"
        )
        output_box.configure(state="disabled")

    except ValueError:
        output_box.configure(state="normal")
        output_box.delete("1.0", "end")
        output_box.insert("end", "Erro: Preencha todos os campos corretamente.")
        output_box.configure(state="disabled")

def limpar_resultado():
    output_box.configure(state="normal")
    output_box.delete("1.0", "end")
    output_box.configure(state="disabled")

# LAYOUT DA INTERFACE
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Calculadora de Investimentos")
app.geometry("500x600")

titulo = ctk.CTkLabel(app, text="Calculadora de Investimentos", font=("Arial", 24))
titulo.pack(pady=(30, 10))

# Campos de entrada
entry_valor = ctk.CTkEntry(app, placeholder_text="Valor Investido (R$)")
entry_valor.pack(pady=10)

entry_tempo = ctk.CTkEntry(app, placeholder_text="Tempo (em meses)")
entry_tempo.pack(pady=10)

combo_tipo = ctk.CTkComboBox(app, values=["CDB", "CDI", "Selic", "Poupança"])
combo_tipo.pack(pady=10)
combo_tipo.set("Selecione o tipo")

entry_porcentagem = ctk.CTkEntry(app, placeholder_text="Porcentagem (ex: 110 para 110%)")
entry_porcentagem.pack(pady=10)

# Botão de calcular
btn_calcular = ctk.CTkButton(app, text="Calcular", command=calcular_investimento)
btn_calcular.pack(pady=20)

# Campo de resultado (Textbox)
output_box = ctk.CTkTextbox(app, width=400, height=180)
output_box.pack(pady=10)
output_box.configure(state="disabled")

# Botão de limpar resultados
btn_limpar = ctk.CTkButton(app, text="Limpar Resultado", command=limpar_resultado)
btn_limpar.pack(pady=10)

app.mainloop()

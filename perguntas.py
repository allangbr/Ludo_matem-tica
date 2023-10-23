import tkinter as tk
from Ludo import *
from tkinter import messagebox

# Questões e respostas


questoes = [
    {
        "pergunta": "1. Qual é a forma geral de uma função afim?",
        "opcoes": ["a) y = ax^2 + b", "b) y = ax + b", "c) y = x^2 + a", "d) y = x - b"],
        "resposta_correta": 1
    },
    {
        "pergunta": "2. O que é necessário para que uma função afim seja crescente?",
        "opcoes": ["a) O coeficiente angular (a) deve ser positivo.", "b) O coeficiente angular (a) deve ser negativo.",
                    "c) O coeficiente linear (b) deve ser positivo.", "d) O coeficiente linear (b) deve ser negativo."],
        "resposta_correta": 0
    },
    {
        "pergunta": "3. O que é necessário para que uma função afim seja crescente?",
        "opcoes": ["a) O coeficiente angular (a) deve ser positivo.", "b) O coeficiente angular (a) deve ser negativo.",
                    "c) O coeficiente linear (b) deve ser positivo.", "d) O coeficiente linear (b) deve ser negativo."],
        "resposta_correta": 0
    }
        
    # Adicione o resto das questões
]

class QuizApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Quiz de Python")

        self.pergunta_atual = 0
        self.respostas = []

        self.label_pergunta = tk.Label(janela, text="")
        self.label_pergunta.pack()
        
        self.var_resposta = tk.IntVar()
        self.opcoes = []
        for i in range(4):
            opcao = tk.Radiobutton(janela, text="", variable=self.var_resposta, value=i)
            opcao.pack()
            self.opcoes.append(opcao)
        
        self.botao_proxima = tk.Button(janela, text="Próxima Pergunta", command=self.proxima_pergunta)
        self.botao_proxima.pack()

        self.atualizar_pergunta()

    def atualizar_pergunta(self):
        if self.pergunta_atual < len(questoes):
            questao_atual = questoes[self.pergunta_atual]
            self.label_pergunta.config(text=questao_atual["pergunta"])
            self.var_resposta.set(-1)  # Limpa a seleção
            for i in range(4):
                self.opcoes[i].config(text=questao_atual["opcoes"][i])
        else:
            self.exibir_resultado()

    def proxima_pergunta(self):
        resposta = self.var_resposta.get()
        if resposta == -1:
            messagebox.showerror("Erro", "Por favor, selecione uma resposta.")
            return

        self.respostas.append(resposta)
        self.pergunta_atual += 1
        self.atualizar_pergunta()

    def exibir_resultado(self):
        pontuacao = sum([1 if r == q["resposta_correta"] else 0 for r, q in zip(self.respostas, questoes)])
        messagebox.showinfo("Resultado", f"Sua pontuação é: {pontuacao}/{len(questoes)}")
        self.janela.destroy()

janela = tk.Tk()
app = QuizApp(janela)
janela.mainloop()

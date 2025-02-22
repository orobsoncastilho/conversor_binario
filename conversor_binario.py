import tkinter as tk
from tkinter import scrolledtext
import pyperclip  # Para copiar o resultado

def texto_para_binario():
    texto = entrada.get()  # Obtém o texto digitado
    if texto.strip():  # Verifica se o campo não está vazio
        binario = ' '.join(format(ord(c), '08b') for c in texto)  # Converte para binário
        saida_texto.insert(tk.END, binario + "\n")  # Adiciona o resultado na área de saída
        saida_texto.see(tk.END)  # Mantém o scroll no final

def copiar_texto():
    texto = saida_texto.get("1.0", tk.END).strip()  # Pega todo o texto da área de saída
    pyperclip.copy(texto)  # Copia para a área de transferência

def limpar():
    entrada.delete(0, tk.END)  # Apaga o campo de entrada
    saida_texto.delete("1.0", tk.END)  # Apaga o campo de saída

# Criando a janela
janela = tk.Tk()
janela.title("Conversor de Texto para Binário")
janela.geometry("500x400")

# Rótulo e campo de entrada
entrada_label = tk.Label(janela, text="Digite uma palavra:")
entrada_label.pack(pady=5)

entrada = tk.Entry(janela, width=40)
entrada.pack(pady=5)

# Botões
botao_converter = tk.Button(janela, text="Converter", command=texto_para_binario)
botao_converter.pack(pady=5)

botao_copiar = tk.Button(janela, text="Copiar Resultado", command=copiar_texto)
botao_copiar.pack(pady=5)

botao_limpar = tk.Button(janela, text="Limpar", command=limpar)  # Agora limpa tudo
botao_limpar.pack(pady=5)

# Área de saída (scrolled text)
saida_texto = scrolledtext.ScrolledText(janela, width=60, height=10)
saida_texto.pack(pady=5)

# Rodando a interface
janela.mainloop()

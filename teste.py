"""
Este módulo contém funções para processar arquivos Excel.
Ele é usado para carregar, limpar e exibir planilhas financeiras.
"""
from tkinter import filedialog
import tkinter as tk
import pandas as pd

def buscar_arquivo(banco):
    """Busca e carrega um arquivo Excel ou CSV."""
    arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo Excel",
        filetypes=[("Arquivos Suportados", "*.xlsx *.xls *.csv")]
    )
    motor = ""
    rotulos =""
    if banco == 'bb':
        motor = 'openpyxl'
        rotulos = 2
    elif banco == 'safra':
        motor = 'xlrd'
        rotulos = 10
    elif banco == 'infinity' or banco == 'nubank':
        motor = 'xlrd'
        rotulos = 0

    if  arquivo and arquivo.endswith(('.xlsx', '.xls')):
        print(f"Arquivo selecionado: {arquivo}")
        try:
            df = pd.read_excel(arquivo, engine = motor, header = rotulos)
            print(df.head())  # Mostra as 5 primeiras linhas como exemplo
            remover_linhas(df,arquivo,banco)
        except ImportError as e:
            print(f"Ocorreu um erro ao buscar o arquivo: {e}")
    elif arquivo and arquivo.endswith('.csv'):
        print(f"Arquivo selecionado: {arquivo}")
        try:
            df = pd.read_csv(arquivo)
            print(df.head())  # Mostra as 5 primeiras linhas como exemplo
            remover_linhas(df,arquivo,banco)
        except ImportError as e:
            print(f"Ocorreu um erro ao buscar o arquivo: {e}")
    elif arquivo:
        print("Nenhum arquivo selecionado.")

def remover_linhas(df2,caminho,banco):
    """Remove linhas desnecessárias."""
    remover = ''
    coluna = ''
    #array de linhas a remor da tabela do banco do brasil
    if banco == 'bb':
        remover = ['Saldo Anterior           ', 'BB Rende Fácil           ',
                   'S A L D O                ','BB Rende Fácil           ']
        coluna = 'Historico'
    elif banco == 'safra':
        remover = ['SALDO TOTAL','SALDO APLIC AUTOMATICA','SALDO CONTA CORRENTE',
                   'APLICACAO CDB AUTOMATICO','RESGATE DE RENDA FIXA']
        coluna = 'Lançamento'
    elif banco == 'infinity' or banco == 'nubank':
        edit = df2
        transforma_em_numero(df2,caminho,banco)

    #conta o tamanho do array bb_remover
    contar = len(remover)

    #loop para remover as linhas
    for i in range(contar):
        if i == 0:
            edit = df2[df2[coluna] != remover[i]]
        else:
            edit = edit[edit[coluna] != remover[i]]
    transforma_em_numero(edit,caminho,banco)

#limpa o campo de valor para ser reconhecido como número
def transforma_em_numero(edit,caminho,banco):
    """Limpa o campo de valor para ser reconhecido como número."""   
    coluna=""
    if banco == 'bb':
        coluna = 'Valor R$ '
    elif banco == 'safra':
        coluna = 'Valor'
    else:
        #coluna = 'Valor'
        salvar(edit,caminho,banco)

    edit[coluna] = (
    edit[coluna]
    .astype(str)
    .str.replace('.', '', regex=False)        # Remove milhar
    .str.replace(',', '.', regex=False)       # Ajusta separador decimal
    .str.replace(r'[^\d.-]', '', regex=True)  # Remove qualquer caractere estranho
    .astype(float)
    )

    salvar(edit,caminho,banco)

def salvar(edit,caminho,banco):
    """Salva o DataFrame em um novo arquivo Excel."""
    # exclui as colunas desnecessárias
    if banco == 'bb':
        edit.drop(['observacao','Data balancete','Agencia Origem',
                   'Lote','Numero Documento','Cod. Historico'], axis=1, inplace=True)
    elif banco == 'safra':
        edit.drop(['Situação','Nº Documento','Saldo',], axis=1, inplace=True)
    elif banco == 'infinity':
        edit.drop(['Moeda'], axis=1, inplace=True)
    elif banco == 'nubank':
        edit.drop(['Identificador'], axis=1, inplace=True)

    # Salva o DataFrame em um novo arquivo Excel
    edit.to_excel(caminho+'_modificado.xlsx', sheet_name="Planilha1", index=False)
    tk.messagebox.showinfo("Sucesso", "Arquivo modificado com sucesso!")


root = tk.Tk()
root.title("Carregar Arquivo Excel")
root.geometry("400x200")
texto = tk.Label(root, text="Selecione o arquivo (xls ou xlsx):")
texto.grid(row=0, column=0, columnspan=4, pady=10)

#banco do brasil
botao1 = tk.Button(root, text="BB", command=lambda: buscar_arquivo('bb'), width=10 )
botao1.grid(row=1, column=0)

#safrapay
botao2 = tk.Button(root, text="SAFRAPAY", command=lambda: buscar_arquivo('safra'),width=10)
botao2.grid(row=1, column=1)

#infinity
botao3 = tk.Button(root, text="INFINITY", command=lambda: buscar_arquivo('infinity'),width=10)
botao3.grid(row=1, column=2)

#infinity
botao4 = tk.Button(root, text="NUBANK", command=lambda: buscar_arquivo('nubank'),width=10)
botao4.grid(row=1, column=3)

#botão de fechar
button_fechar = tk.Button(root, text="Fechar", command=root.quit, width=10)
button_fechar.grid(row=2, column=0)

root.mainloop()

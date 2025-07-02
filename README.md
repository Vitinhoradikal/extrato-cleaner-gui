# Extrato Cleaner GUI

Um aplicativo simples em Python com interface gráfica (Tkinter) para processar, limpar e padronizar extratos bancários dos principais bancos em formatos `.xls`, `.xlsx` e `.csv`.

## 🧾 O que este projeto faz

Este sistema foi criado para facilitar a limpeza e conversão de extratos bancários, removendo linhas irrelevantes e padronizando valores numéricos. Ele gera um novo arquivo Excel pronto para uso em análises financeiras ou contábeis.

### Bancos Suportados:
- Banco do Brasil (BB)
- SafraPay
- InfinityPay
- Nubank

---

## 💻 Interface

A interface gráfica é feita com `Tkinter`, simples e intuitiva. Basta clicar no botão correspondente ao banco, escolher o arquivo desejado e o sistema fará o resto.

![exemplo da interface](screenshot.png) <!-- Opcional: substitua ou remova -->

---

## 📦 Funcionalidades

- Importa arquivos `.xls`, `.xlsx` ou `.csv`
- Limpa linhas desnecessárias específicas de cada banco
- Converte valores monetários para `float` (R$ → número)
- Remove colunas irrelevantes
- Exporta novo arquivo `.xlsx` com o sufixo `_modificado`
- Mensagens de sucesso ou erro com `tk.messagebox`

---

## 🚀 Como executar

### Requisitos

- Python 3.7+
- Pandas
- openpyxl
- xlrd (até versão 1.2.0)  
- tkinter (já vem com o Python padrão)

### Instalação de dependências

```bash
pip install pandas openpyxl xlrd==1.2.0
Executar o sistema
bash
Copiar
Editar
python teste.py
📁 Estrutura esperada dos arquivos de entrada
Cada banco tem uma estrutura diferente. O sistema espera que os campos estejam nos formatos comuns exportados por seus sites/aplicativos.

Exemplo para BB:

ruby
Copiar
Editar
Data | Historico | Valor R$ | ...
🛠️ Futuras melhorias
Exportar também em .csv

Adicionar suporte para mais bancos (ex: Inter, C6)

Filtros de data ou tipo de operação

Geração de relatórios ou gráficos simples

📜 Licença
Este projeto é livre para uso pessoal. Para uso comercial, verifique a licença aplicável.

👨‍💻 Autor
Desenvolvido por Vitor Lúcio Machado.

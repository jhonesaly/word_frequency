import PyPDF2
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import os

# Baixe os recursos necessários do NLTK
nltk.download('punkt')
nltk.download('stopwords')

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def process_text(text, ignore_words):
    # Tokenize o texto
    words = word_tokenize(text, language='portuguese')

    # Remova as stopwords e palavras ignoradas
    stop_words = set(stopwords.words('portuguese'))
    filtered_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words and word.lower() not in ignore_words]

    return filtered_words

def load_ignore_words(ignore_file_path):
    try:
        with open(ignore_file_path, 'r', encoding='utf-8') as file:
            ignore_words = [word.strip().lower() for word in file.read().split(',')]
        return ignore_words
    except FileNotFoundError:
        print(f'O arquivo de ignore "{ignore_file_path}" não foi encontrado.')
        return []

def generate_csv_and_plot(word_list, csv_path):
    # Gere a análise de frequência
    word_freq = Counter(word_list)

    # Crie um DataFrame e salve em um arquivo CSV (todas as palavras)
    df = pd.DataFrame(list(word_freq.items()), columns=['Palavra', 'Frequência'])
    df = df.sort_values(by='Frequência', ascending=False)

    # Salve o DataFrame em um arquivo CSV específico para cada PDF
    df.to_csv(csv_path, index=False)

    # Limite o DataFrame às 20 palavras mais frequentes
    df_top_20 = df.head(20)

    # Crie um gráfico de barras (apenas as 20 palavras mais frequentes)
    df_top_20.plot(kind='bar', x='Palavra', y='Frequência', legend=False)
    plt.title('Análise de Frequência de Palavras (Top 20)')
    plt.xlabel('Palavra')
    plt.ylabel('Frequência')
    plt.show()

if __name__ == '__main__':
    # Caminho para a pasta que contém os arquivos PDF
    input_folder = 'input/'

    # Carregue as palavras a serem ignoradas
    ignore_words = load_ignore_words('ignore.txt')

    # Lista todos os arquivos na pasta input
    pdf_files = [file for file in os.listdir(input_folder) if file.endswith('.pdf')]

    # Processa cada arquivo PDF na pasta input
    for pdf_file in pdf_files:
        # Caminho completo do arquivo PDF
        pdf_path = os.path.join(input_folder, pdf_file)

        # Extraia texto do PDF
        text = extract_text_from_pdf(pdf_path)

        # Processamento de texto
        processed_text = process_text(text, ignore_words)

        # Gere um nome de arquivo CSV único com base no nome do arquivo PDF
        csv_file = os.path.splitext(pdf_file)[0] + '_output.csv'
        csv_path = os.path.join('output/', csv_file)

        # Gere CSV e gráfico para cada arquivo PDF
        generate_csv_and_plot(processed_text, csv_path)
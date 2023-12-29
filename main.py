import PyPDF2
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

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

def generate_csv_and_plot(word_list):
    # Gere a análise de frequência
    word_freq = Counter(word_list)

    # Crie um DataFrame e salve em um arquivo CSV
    df = pd.DataFrame(list(word_freq.items()), columns=['Palavra', 'Frequência'])

    # Classifique o DataFrame em ordem decrescente de frequência
    df = df.sort_values(by='Frequência', ascending=False)

    # Limite o DataFrame às 20 palavras mais frequentes
    df = df.head(20)

    # Salve o DataFrame em um arquivo CSV
    df.to_csv('output/output.csv', index=False)

    # Crie um gráfico de barras
    df.plot(kind='bar', x='Palavra', y='Frequência', legend=False)
    plt.title('Análise de Frequência de Palavras (Top 20)')
    plt.xlabel('Palavra')
    plt.ylabel('Frequência')
    plt.show()

if __name__ == '__main__':
    # Substitua 'seu_arquivo.pdf' pelo caminho do seu arquivo PDF
    pdf_path = 'input/origin.pdf'

    # Carregue as palavras a serem ignoradas
    ignore_words = load_ignore_words('ignore.txt')

    # Extraia texto do PDF
    text = extract_text_from_pdf(pdf_path)

    # Processamento de texto
    processed_text = process_text(text, ignore_words)

    # Gere CSV e gráfico
    generate_csv_and_plot(processed_text)

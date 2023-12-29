# word_frequency

Este projeto em Python realiza a análise de frequência de palavras em arquivos PDF. Ele extrai o texto do PDF, remove palavras irrelevantes, como stopwords e palavras personalizadas definidas em um arquivo `ignore.txt`, gera um arquivo CSV com a frequência de todas as palavras e cria um gráfico de barras mostrando as 20 palavras mais frequentes para cada PDF na pasta input.

## Pré-requisitos

- Python 3.x

Instale as bibliotecas necessárias executando o seguinte comando:

```bash
pip install -r requirements.txt
```

Além disso, certifique-se de baixar os recursos necessários do NLTK executando:

```bash
python -m nltk.downloader punkt stopwords
```

## Como Usar

1. Clone o repositório:

```bash
git clone https://github.com/jhonesaly/word_frequency.git
cd word_frequency
```

2. Coloque seus arquivos PDF na pasta `input`.

3. Edite o arquivo `ignore.txt` para adicionar palavras personalizadas que devem ser ignoradas na análise.

4. Execute o script:

```bash
python word_frequency.py
```

1. Verifique os resultados completos na pasta `output` e o gráfico será exibido no console.

## Estrutura do Projeto

- `input`: Pasta para armazenar o arquivo PDF de entrada.
- `output`: Pasta para armazenar os resultados (CSV e gráficos).
- `ignore.txt`: Arquivo contendo palavras personalizadas a serem ignoradas.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

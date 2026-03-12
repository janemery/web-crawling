# 🕷️ Web Crawling – Perguntas Bíblicas (JW.org)

![Python](https://img.shields.io/badge/python-3.11-blue)
![Scrapy](https://img.shields.io/badge/scrapy-2.8-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

## Descrição

Este projeto utiliza **Scrapy** para coletar automaticamente **perguntas bíblicas** do site [JW.org](https://www.jw.org/pt/ensinos-biblicos/perguntas/).

O spider percorre várias páginas, extrai dados estruturados e salva em **CSV ou JSON** para análise estatística.

---

## Estrutura do Projeto

```text
web_crawling/
│
├── scrapy.cfg
├── web_crawling/
│   ├── __init__.py
│   ├── items.py          # Define PerguntaItem
│   ├── pipelines.py      # Enriquecimento dos dados
│   ├── settings.py       # Configurações do Scrapy
│   └── spiders/
│       ├── __init__.py
│       └── perguntas_spider.py  # Spider com paginação
```

---

## Funcionalidades

* Coleta de **título, categoria e link** das perguntas bíblicas
* Enriquecimento de dados via pipeline:

  * Tamanho do título
  * Número de palavras no título
  * Subcategoria simples por palavra-chave (`Deus`, `Jesus`, `Bíblia`, `Outros`)
* Paginação automática (10+ páginas)
* Exportação de dados em **CSV ou JSON**

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seuusuario/web_crawling.git
cd web_crawling
```

Crie e ative um ambiente virtual:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / Mac
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Como rodar o Spider

1. Navegue até a pasta do projeto (onde está `scrapy.cfg`)

2. Gerar CSV:

```bash
scrapy crawl perguntas -o perguntas.csv
```

3. Gerar JSON:

```bash
scrapy crawl perguntas -o perguntas.json
```

> O spider percorre todas as páginas com perguntas, respeitando o `robots.txt` e o `DOWNLOAD_DELAY`.

---

## Exemplo de saída

| titulo                             | categoria | link                                                               | subcategoria | titulo_len | palavras |
| ---------------------------------- | --------- | ------------------------------------------------------------------ | ------------ | ---------- | -------- |
| Quem é Deus?                       | Deus      | [https://www.jw.org/pt/pergunta1](https://www.jw.org/pt/pergunta1) | Deus         | 11         | 3        |
| O que a Bíblia ensina sobre Jesus? | Bíblia    | [https://www.jw.org/pt/pergunta2](https://www.jw.org/pt/pergunta2) | Jesus        | 27         | 6        |

---

## Análise de Dados

No **notebook Python**, você pode:

```python
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_csv("perguntas.csv")

# Contagem por categoria
df['categoria'].value_counts().plot(kind='bar')

# Nuvem de palavras
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(" ".join(df['titulo']))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
```

---

## Autor

* Nome: Jane Ferreira 
* Curso: MBA – Unifor
* Módulo: Web Crawling, Scraping e Coleta de Dados Automatizada


Quer que eu faça isso?

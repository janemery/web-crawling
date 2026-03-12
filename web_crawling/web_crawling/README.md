# Atividade Prática 03 – Web Crawling & Scraping com Scrapy

## Descrição

Este projeto tem como objetivo coletar informações automaticamente da web utilizando **Scrapy**.  
O spider foi configurado para navegar pelas **10 primeiras páginas** do site [Books to Scrape](http://books.toscrape.com/) e extrair os seguintes campos de cada livro:

- `titulo` – título do livro  
- `preco` – preço em libras (£), convertido para float  
- `disponibilidade` – status de estoque  

Os dados coletados são exportados para **CSV** e podem ser analisados posteriormente.

---

## Estrutura do Projeto
web_crawling/
├── scrapy.cfg
├── web_crawling/
│ ├── init.py
│ ├── items.py
│ ├── middlewares.py
│ ├── pipelines.py
│ ├── settings.py
│ └── spiders/
│ └── livros_spider.py
├── livros.csv
└── analise.ipynb

---

## Requisitos

- Python 3.8+  
- Scrapy  
- pandas (para análise)  
- matplotlib (para gráficos)

> É recomendado usar um **ambiente virtual** para gerenciar dependências.

---

## Instalação

1. Criar e ativar o ambiente virtual:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1  # PowerShell
# ou
venv\Scripts\activate.bat     # CMD
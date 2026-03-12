import scrapy
from web_crawling.items import WebCrawlingItem

class PerguntasSpider(scrapy.Spider):
    name = "perguntas"
    start_urls = ["https://www.jw.org/pt/ensinos-biblicos/perguntas/"]

    def parse(self, response):
        # Seleciona todas as perguntas ou blocos de texto relevantes
        for pergunta in response.css("div.wy-article-content p, div.wy-article-content h2"):
            item = WebCrawlingItem()
            item['titulo'] = pergunta.css("::text").get()
            item['resumo'] = pergunta.css("::text").get()
            item['link'] = response.url
            yield item

        # Paginação até 10 páginas
        next_page = response.css("a.next::attr(href)").get()
        if next_page:
            # Obtém o número da página atual (se disponível no URL)
            current_page_num = response.url.split("/")[-2] if len(response.url.split("/")) > 1 else "1"
            try:
                current_page_num = int(current_page_num)
            except ValueError:
                current_page_num = 1

            # Limita a navegação a 10 páginas
            if current_page_num < 10:
                yield response.follow(next_page, self.parse)
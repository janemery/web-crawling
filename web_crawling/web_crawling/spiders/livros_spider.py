import scrapy
from web_crawling.items import WebCrawlingItem

class LivrosSpider(scrapy.Spider):
    name = "livros"
    start_urls = ["http://books.toscrape.com/catalogue/page-1.html"]

    def parse(self, response):
        # Extrai dados de cada livro na página
        for livro in response.css("article.product_pod"):
            item = WebCrawlingItem()
            item['titulo'] = livro.css("h3 a::attr(title)").get()
            item['preco'] = livro.css("p.price_color::text").get()
            item['disponibilidade'] = livro.css("p.instock.availability::text").re_first("\w+")
            yield item

        # Paginação automática até 10 páginas
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            # Confere se estamos dentro do limite de 10 páginas
            current_page_num = int(response.url.split("page-")[1].split(".html")[0])
            if current_page_num < 10:
                yield response.follow(next_page, self.parse)
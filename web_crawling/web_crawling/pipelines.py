# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WebCrawlingPipeline:
    def process_item(self, item, spider):
        # Tamanho do título
        item['titulo_len'] = len(item['titulo'])
        # Número de palavras
        item['palavras'] = len(item['titulo'].split())
        # Criar subcategoria simples com base no título
        t = item['titulo'].lower()
        if 'deus' in t:
            item['subcategoria'] = 'Deus'
        elif 'jesus' in t:
            item['subcategoria'] = 'Jesus'
        elif 'bíblia' in t:
            item['subcategoria'] = 'Bíblia'
        else:
            item['subcategoria'] = 'Outros'
        return item
BOT_NAME = "web_crawling"

SPIDER_MODULES = ["web_crawling.spiders"]
NEWSPIDER_MODULE = "web_crawling.spiders"

# Exportação UTF-8
FEED_EXPORT_ENCODING = "utf-8"

# Respeitar robots.txt
ROBOTSTXT_OBEY = True

# Limitar requisições e adicionar delay
CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 1

# Pipeline
ITEM_PIPELINES = {
   'web_crawling.pipelines.WebCrawlingPipeline': 300,
}

# User-Agent recomendado
USER_AGENT = "web_crawling (+https://www.jw.org)"
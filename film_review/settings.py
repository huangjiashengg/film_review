# Scrapy settings for film_review project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'film_review'

SPIDER_MODULES = ['film_review.spiders']
NEWSPIDER_MODULE = 'film_review.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
ITEM_PIPELINES = {
    'film_review.pipelines.FilmReviewPipeline': 300,
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'film_review (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB_INDEX = 2

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = True
# COOKIE = 'bid=R7shYcER3y0; __yadk_uid=itCMSw6WBrL2jrJZoa3BnON6aV6V8cCq; ll="108306"; _vwo_uuid_v2=D7A37DD42FC9B9B7618C0093792CC0EBE|dc1d179c2625aff79371207c7c4fac28; douban-fav-remind=1; __utmv=30149280.17784; _ga=GA1.2.1723571052.1596900301; __gads=ID=5b1e7e488772e528-220e6ebe27c50010:T=1607679088:RT=1607679088:R:S=ALNI_MZPZ3rZkAjSeLDW2r2EtVbZVqoOSQ; gr_user_id=f106bdc6-2975-4fde-993c-dfaa3c690e39; viewed="4604591_10785602_1731572_1716390"; _vwo_uuid_v2=D7A37DD42FC9B9B7618C0093792CC0EBE|dc1d179c2625aff79371207c7c4fac28; __utmz=30149280.1616212828.29.21.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; push_noty_num=0; push_doumail_num=0; ct=y; __utmz=223695111.1616394192.36.20.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; dbcl2="177844141:SGUMNbJAuIE"; ap_v=0,6.0; ck=QWtj; __utma=30149280.1723571052.1596900301.1616402351.1616404371.39; __utmb=30149280.0.10.1616404371; __utmc=30149280; __utma=223695111.141222608.1596900301.1616402351.1616404371.38; __utmb=223695111.0.10.1616404371; __utmc=223695111; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1616404371%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DVZFLk0SYAnbMfVeyadqsnzcOwjA39JSHwJWBPVie9TMA4-jLciGt8rB_kDXZz991%26wd%3D%26eqid%3Da86b7b0b000006dd0000000660557358%22%5D; _pk_ses.100001.4cf6=*; _pk_id.100001.4cf6=32cbb6e140ddd13d.1596900301.36.1616405064.1616402350.'

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'film_review.middlewares.FilmReviewSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'film_review.middlewares.FilmReviewDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'film_review.pipelines.FilmReviewPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

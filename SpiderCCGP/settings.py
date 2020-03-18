# -*- coding: utf-8 -*-

# Scrapy settings for SpiderCCGP project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'SpiderCCGP'

SPIDER_MODULES = ['SpiderCCGP.spiders']
NEWSPIDER_MODULE = 'SpiderCCGP.spiders'

RANDOM_UA_TYPE = 'random'
# Crawl responsibly by identifying yourself (and your website) on the user-agent

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

# 延迟2s 提高稳定性
DOWNLOAD_DELAY = 2

# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'SpiderCCGP.middlewares.SpiderccgpSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'SpiderCCGP.middlewares.RandomUserAgentMiddleware': 100,
    # 'SpiderCCGP.middlewares.RandomProxyMiddleware': 110,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 值越小,优先级越高
    # 'SpiderCCGP.pipelines.SpiderccgpPipeline': 300,
    'SpiderCCGP.pipelines.MyFilePipeline': 150,
    'SpiderCCGP.pipelines.MySQLPipeline': 300,
    'SpiderCCGP.pipelines.TxtSavePipeline': 200
    # 'SpiderCCGP.pipelines.DuplicatePipeline': 100  # 去重 要在文件下载之前
}

FILES_STORE = 'D:/Code/project-python/SpiderCCGP/file'
FILES_URLS_FIELD = 'file_urls'
TXT_PATH = 'D:/Code/project-python/SpiderCCGP/txt'
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 1
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

from datetime import datetime

# 文件及路径，log目录需要先建好
# LOG_ENABLED = True
# today = datetime.now()
# log_file_path = "log/scrapy_{}_{}_{}.log".format(today.year, today.month, today.day)
# LOG_LEVEL = 'WARNING'
# LOG_FILE = log_file_path

# MYSQL 配置
MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'ccgp'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'

# Redis 配置
REDIS_HOST = '127.0.0.1'
REDIS_PASSWORD = '123456'


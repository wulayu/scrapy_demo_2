BOT_NAME = 'demo'

SPIDER_MODULES = ['demo.spiders']
NEWSPIDER_MODULE = 'demo.spiders'

# 用户浏览器
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'

# 并发请求数量
CONCURRENT_REQUESTS = 4

# 下载延迟
DOWNLOAD_DELAY = 3
# 随机化下载延迟
RANDOMIZE_DOWNLOAD_DELAY = True

# 是否遵守爬虫协议
ROBOTSTXT_OBEY = True

# 配置数据管道
ITEM_PIPELINES = {
    'demo.pipelines.MovieItemPipeline': 300,
}

DEPTH_LIMIT = 4

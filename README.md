# scrapy-spider

## 1 安装scrapy

```s
$ pip install scrapy

```
## 2 创建项目
```s
$ scrapy startproject tutorial
New Scrapy project 'tutorial', using template directory '/home/ubuntu/anaconda3/lib/python3.7/site-packages/scrapy/templates/project', created in:
    /home/ubuntu/code/scrapy-spider/demo01/tutorial

You can start your first spider with:
    cd tutorial
    scrapy genspider example example.com
```

目录结构：
```s
$ tree
.
└── tutorial
    ├── scrapy.cfg
    └── tutorial
        ├── __init__.py
        ├── items.py
        ├── middlewares.py
        ├── pipelines.py
        ├── __pycache__
        ├── settings.py
        └── spiders
            ├── __init__.py
            └── __pycache__

5 directories, 7 files
```

这些文件分别是:

- scrapy.cfg: 项目的配置文件
- tutorial/: 该项目的python模块。之后您将在此加入代码。
- tutorial/items.py: 项目中的item文件.
- tutorial/pipelines.py: 项目中的pipelines文件.
- tutorial/settings.py: 项目的设置文件.
- tutorial/spiders/: 放置spider代码的目录.

## 3 编写爬虫代码
在tutorial/spiders 下新建一个名为blog_spider.py的文件：
编写如下内容：
```python
from scrapy.spiders import Spider
class BlogSpider(Spider):
    name = 'foochane'
    start_urls = ['https://foochane.cn']
    def parse(self, response):
        titles = response.xpath('//a[@class="post-title-link"]/text()').extract()
        for title in titles:
            print(title.strip())
```

## 4 启动爬虫

```s
$ scrapy crawl foochane

```

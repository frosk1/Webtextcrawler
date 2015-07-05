import scrapy
from webtextcrawler.items import KickerItem
class KickerSpider(scrapy.Spider):
    name = "kicker"
    allowed_domains = ["kicker.de"]
    start_urls = [
        "http://www.kicker.de/news/fussball/bundesliga/spieltag/1-bundesliga/2014-15/-1/0/spieltag.html",
        "http://www.kicker.de/news/fussball/bundesliga/spieltag/1-bundesliga/2013-14/-1/0/spieltag.html",
    ]

    #def parse(self, response):
        # filename = response.url.split("/")[-2] + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

    def parse(self, response):
        for href in response.selector.re('<a class="link" href="(.*)">Analyse</a>'):
            url = response.urljoin(href)
            print url
            #print type(url)
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        for sel in response.xpath('/html'):
            item = KickerItem()
            item['teaser'] = sel.xpath('//*[@id="ovArtikel"]/p[1]/text()').extract()
            yield item

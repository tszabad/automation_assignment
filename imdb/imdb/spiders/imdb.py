import scrapy


class ImdbMovieSpider(scrapy.Spider):
    name = 'imdb_movie'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_500']
    
    def parse(self, response):
        print("procesing:"+response.url)
        for i in range(1,150):
            link_selector = f"//tr[{i}]/td[@class='titleColumn' and 2]/a[1]/@href"
            movie_link = response.xpath(link_selector).getall()
            for link in movie_link:
                yield scrapy.Request(response.urljoin(link), callback = self.parse_link)
    
    def parse_link(self, response):
            print("procesing:"+response.url)
            cast_link = response.xpath("//a[contains(.,'See full cast')]/@href").get()
            yield scrapy.Request(response.urljoin(cast_link), callback = self.parse_cast)

    def parse_cast(self, response):
            print("procesing:"+response.url)
            title = response.xpath("//h3/a[1]/text()").get()
            cast = response.xpath("//td[2]/a[1]/text()").getall()
            yield {
                "title": title,
                "cast": cast
                    }

            
            

           
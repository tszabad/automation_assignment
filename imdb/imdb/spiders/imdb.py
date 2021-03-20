import scrapy


class ImdbMovieSpider(scrapy.Spider):
    name = 'imdb_movie'
    allowed_domains = ['https://www.imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_500']
    
    def parse(self, response):
        print("procesing:"+response.url)
        for i in range(1,10):
            link = f"//tr[{i}]/td[@class='titleColumn' and 2]/a[1]/@href"
            text = f"//tr[{i}]/td[@class='titleColumn' and 2]/a[1]/text()"
            movie = response.xpath(text).get()
            next_path = response.xpath(link).get()
            if next_path:
                yield scrapy.Request(response.urljoin(next_path), callback=self.parse)
            print(response.url)
            second_path = response.xpath("//a[contains(.,'See full cast')]/@href").get()
            if second_path:
                yield scrapy.Request(response.urljoin(second_path), callback=self.parse)
            print(response.url)
            cast = response.xpath("//tr[@class='odd']/td[2]/a[1]/text()").getall()
            
            if movie is not None and cast is not None:
                yield {
                    "movie": movie,
                    "cast": cast
                    }

            final_path = 'https://www.imdb.com/chart/top/?ref_=nv_mv_500'
            if final_path:
                yield scrapy.Request(response.urljoin(final_path), callback=self.parse)
            

           
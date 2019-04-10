# -*- coding: utf-8 -*-
import scrapy


class AdorofilmesSpider(scrapy.Spider):
    name = 'AdoroFilmes'
    allowed_domains = ['www.adorocinema.com']
    start_urls = ['http://www.adorocinema.com/filmes/numero-cinemas/']


    def parse(self, response):


        for link in response.css('h2.meta-title ::attr(href)').getall():
            yield response.follow(link,self.parse_filmes)

        next_page = response.css('nav.pagination ::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page,self.parse)



    def parse_filmes(self,response):
        titulo = response.css('div.titlebar ::text').get()
        lancamento = response.css('.blue-link ::text').get()
        diretor = response.css('a.blue-link ::text').get()
        sinopse = response.css('section.section div.content-txt ::text').get()



        yield {'titulo':titulo,'lancamento':lancamento,'diretor':diretor,'sinopse':sinopse}








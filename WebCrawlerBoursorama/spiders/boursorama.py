import scrapy
from scrapy import Request
from WebCrawlerBoursorama.items import ReviewsBoursoramaItem
from datetime import datetime as d
import time as t

"""
Liste d'item:
    le nom de l'indice boursier
    le cours de l'action
    la variation de l'action
    la valeur la plus haute de la séance
    la valeur la plus basse
    la valeur d'ouverture
    la date et l'heure de la collecte
"""

class BoursoramaSpider(scrapy.Spider):
    name = 'boursorama'
    allowed_domains = ['www.boursorama.com']
    start_urls= [f'https://www.boursorama.com/bourse/actions/palmares/france/page-{n}' for n in range(1,4)]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        liste_CAC= response.css('tr.c-table__row')[1:]

        # Boucle qui parcours l'ensemble des éléments de la liste des films
        for ent in liste_CAC:
            item = ReviewsBoursoramaItem()

            # Nom du film
            try:
                item['name'] = ent.css('a.c-link.c-link--animated::text').extract()
            except:
                item['name'] = 'None'
            try:
                item['cours'] = ent.css('td.c-table__cell.c-table__cell--dotted::text').extract()[0].strip()
            except:
                item['cours'] = 'None'
            try:
                item['variation'] = ent.css('span.c-instrument.c-instrument--instant-variation::text').extract()
            except:
                item['variation'] = 'None'
            try:
                item['valeur_hausse'] = ent.css('span.c-instrument.c-instrument--high::text').extract()[0]
            except:
                item['valeur_hausse'] = 'None'
            try:
                item['valeur_basse'] = ent.css('span.c-instrument.c-instrument--low::text').extract()[0]
            except:
                item['valeur_basse'] = 'None'
            try:
                item['valeur_ouverture'] = ent.css('span.c-instrument.c-instrument--open::text').extract()[0]
            except:
                item['valeur_ouverture'] = 'None'
            try:
                date=d.now()
                item['date'] = date.strftime("%Y-%m-%d %H:%M:%S")
            except:
                item['date'] = 'None'
        
            yield item
    
    

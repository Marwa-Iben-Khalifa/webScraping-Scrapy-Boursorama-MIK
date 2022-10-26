# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ReviewsBoursoramaItem(scrapy.Item):
    name= scrapy.Field()
    cours= scrapy.Field()
    variation= scrapy.Field()
    valeur_hausse= scrapy.Field()
    valeur_basse= scrapy.Field()
    valeur_ouverture= scrapy.Field()
    date= scrapy.Field()
    pass

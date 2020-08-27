from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst
from datetime import datetime
from unidecode import unidecode

def decode_quotation(text):
    text = unidecode(text)
    return text

def remove_br(text):
    # replacing the <br> tag
    text = text.replace("<br>","")
    return text


class TestItem(Item):

    Page = Field(
        input_processor=MapCompose(decode_quotation,remove_br),
        # TakeFirst return the first value not the whole list
        output_processor=TakeFirst()
        )

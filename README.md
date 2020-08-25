# NovelScrapper
Scrape the wuxiaworld.co for novels 

Requirements to use :
1. Python
2. Scrapy
------------------------------------
How to use:
1. Open the terminal and the diectory where you copied the file and store the data
2. Open browser go to wuxiaworld.co
3. Choose the Novel intended for scraping
4. Put the name of the novel in the example for the start_urls
        start_urls = ['https://www.wuxiaworld.co/example/']
5. Run the File with a .json filename of your choice as
        scrapy runspider NovelScrapper.py -o filename.json
6. filename.json file should be created in the directory with the scrapped infoemation

------------------------------------
Customize the script:
This was created for scrapping wuxiaworld.co but it is possible to customize it for websites.

1. Most of the novel reading websites follow a certain format with the main page having a list of the chapters available for the novel
2. Opening an inspection tool for the browser we can see the block which contains the links
3. For example in the code response.css('div.chapter-wrapper a.chapter-item')| div.chapter-wrapper | block contains a.chapter-item links 
   replacing these with the necessary code should make the spider go to the next pages
4. To scrape the text itself go to one of the chapter and use the inspection tool
    for exapmle in the code response.css('.chapter-entity::text').getall() |.chapter-entity| scrapes the text replace with the necessary code.
5. Save the file and run the file.

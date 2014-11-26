#/usr/bin/env python
#conding:utf-8

from scrapy.spider import Spider
from scrapy.selector import Selector
from tutorial.items import WooYunItem

from BeautifulSoup import BeautifulSoup


class DmozSpider(Spider):
    name = "wooyun"
    start_urls = [
        "http://wooyun.org",
    ]
    def parse(self, response):
        items = []
        sel = Selector(response)
        for table in sel.xpath("//table[@class='listTable']").extract():
            doc = BeautifulSoup(table)
            if doc.thead:
                print "++++++++++++++++++++"
                for stat in doc.thead.findAll():
                    print stat.text + "=",
                print
            if doc.tbody:
                tmpDict = {}
                for tr in doc.findAll("tr"):
                    if len(tr.findAll()) == 7:
                        l = [a.text for a in tr.findAll()]
                        # print "+++".join(l)
                        tmpDict["time"] = l[0]
                        tmpDict["url"] = tr.a.get("href")
                        tmpDict["name"] = l[1]
                        tmpDict["auth"] = l[-1]
                    print tmpDict
                    # a, b, c, d = tr.findAll()[:]
                    # print a, b, c, d
                        
                    # print

            # print table
            # for url in table.xpath('a/text()').extract():
            #     print url
        #     item = DmozItem()
        #     item['title'] = site.xpath('a/text()').extract()
        #     item['link'] = site.xpath('a/@href').extract()
        #     item['desc'] = site.xpath('text()').extract()
        #     items.append(item)
        # return items 
            

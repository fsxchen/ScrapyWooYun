#/usr/bin/env python
#conding:utf-8

from scrapy.spider import Spider
from scrapy.selector import Selector
from WooYun.items import WooyunItem

from BeautifulSoup import BeautifulSoup

type_list = ["a", "b", "c", "d", "e"]

class DmozSpider(Spider):
    name = "wooyun"
    start_urls = [
        "http://wooyun.org",
    ]
    def parse(self, response):
        items = []
        sel = Selector(response)
        root_path = sel.xpath("//table[@class='listTable']").extract()
        for table, index_msg in zip(root_path, type_list):
            doc = BeautifulSoup(table)
            if doc.thead:
                pass
            if doc.tbody:
                for tr in doc.findAll("tr"):
                    item = WooyunItem()
                    if len(tr.findAll()) == 7:
                        l = [a.text for a in tr.findAll()]
                        item["pb_time"] = l[0]
                        item["pb_url"] = tr.a.get("href")
                        item["pb_name"] = l[1]
                        item["pb_auth"] = l[-1]
                        item["mes_type"] = index_msg
                        items.append(item)
        return items
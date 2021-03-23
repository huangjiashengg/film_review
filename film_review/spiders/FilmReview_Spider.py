import scrapy
import time
from bs4 import BeautifulSoup
from film_review.items import FilmReviewItem

class FilmReview_Spider(scrapy.Spider):
    name = 'FilmReview'

    def start_requests(self):
        _url = 'https://movie.douban.com/subject/1292052/comments?start={}&limit=20&status=P&sort=new_score'
        urls = []
        for page in range(0, 25):
            urls.append(_url.format(page*20))
        for url in urls:
            cookies = 'bid=R7shYcER3y0; __yadk_uid=itCMSw6WBrL2jrJZoa3BnON6aV6V8cCq; ll="108306"; _vwo_uuid_v2=D7A37DD42FC9B9B7618C0093792CC0EBE|dc1d179c2625aff79371207c7c4fac28; douban-fav-remind=1; __utmv=30149280.17784; _ga=GA1.2.1723571052.1596900301; __gads=ID=5b1e7e488772e528-220e6ebe27c50010:T=1607679088:RT=1607679088:R:S=ALNI_MZPZ3rZkAjSeLDW2r2EtVbZVqoOSQ; gr_user_id=f106bdc6-2975-4fde-993c-dfaa3c690e39; viewed="4604591_10785602_1731572_1716390"; _vwo_uuid_v2=D7A37DD42FC9B9B7618C0093792CC0EBE|dc1d179c2625aff79371207c7c4fac28; __utmz=30149280.1616212828.29.21.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; push_noty_num=0; push_doumail_num=0; ct=y; __utmz=223695111.1616394192.36.20.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; dbcl2="177844141:SGUMNbJAuIE"; ap_v=0,6.0; ck=QWtj; __utmc=30149280; __utmc=223695111; __utma=30149280.1723571052.1596900301.1616404371.1616407425.40; __utmb=30149280.0.10.1616407425; __utma=223695111.141222608.1596900301.1616404371.1616407425.39; __utmb=223695111.0.10.1616407425; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1616407425%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DVZFLk0SYAnbMfVeyadqsnzcOwjA39JSHwJWBPVie9TMA4-jLciGt8rB_kDXZz991%26wd%3D%26eqid%3Da86b7b0b000006dd0000000660557358%22%5D; _pk_ses.100001.4cf6=*; _pk_id.100001.4cf6=32cbb6e140ddd13d.1596900301.37.1616408072.1616405070.'
            cookies = {i.split('=')[0]: i.split('=')[1] for i in cookies.split('; ')}
            yield scrapy.Request(url, callback=self.sparse, cookies=cookies)
            time.sleep(2)
    def sparse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        list = soup.find(class_='mod-bd')
        for li in list.find_all(class_='comment-item'):
            item = FilmReviewItem()
            item['name'] = li.find(class_='comment-info').find('a').string
            item['time'] = li.find(class_='comment-time').string.strip()
            item['likes'] = li.find(class_='votes vote-count').string
            item['comment'] = li.find(class_='short').string
            # if li.find(class_='comment-info').find('a').string != None:
            #     item['name'] = li.find(class_='comment-info').find('a').string
            # if li.find(class_='comment-time').string.strip() != None:
            #     item['time'] = li.find(class_='comment-time').string.strip()
            # if li.find(class_='votes vote-count').string != None:
            #     item['likes'] = li.find(class_='votes vote-count').string
            # if li.find(class_='short').string != None:
            #     item['comment'] = li.find(class_='short').string
            yield item




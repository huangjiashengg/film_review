# 肖申克的救赎影评爬取分析

## 前言

一直可以听到周围朋友对我安利《肖申克的救赎》，让我怀有一种敬意去看这部电影。无奈时间仓促，日子过得何其匆忙。机缘巧合之下终于有时间把这部剧看完了，深深觉着对主角的敬佩，后劲很足。于是回到豆瓣，从头到尾看了它的影评(根本看不完，几十万条)。决定把《肖申克的救赎》这部电影的所有影评爬取下来，做个云图可视化。

## 结论

1，对页面链接进行分析之后，发现最多只能爬取500条影评(还是在模拟登录的情况下才有这个权限)；

2，本项目爬取的字段包括，评论者，评论时间，点赞人数以及评论内容；

3，项目采用Redis作为爬取缓存数据库(优点之一可以只管快速看到爬取的数目是否对应的上)

4，项目采用Scrapy+Beatufulsoup+jieba+wordcloud技术手段实现

## 技术实现过程

### 爬取数据阶段

第一步，使用scrapy创建项目，命名为film_review；

第二步，在items添加爬取字段，包含name, time, likes, comment

第三步，pipelines文件定义类Redis数据库，作为数据输入

第四步，在settings中添加``` ITEM_PIPELINES = {
    'film_review.pipelines.FilmReviewPipeline': 300,
}```  ，并添加``` USER_AGENT = 'Mozilla/5.0 (Wind...' ``` ，还需要加入连接数据库的参数：

```
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB_INDEX = 2
```

第五步，构建爬取解析文件FilmReview_Spider.py，在start_requests函数中记得添加cookies进行请求，否则返回不了数据，如下：

```python
cookies = 'bid=R7shYcER3y0; __yadk_uid=itCMSw6WBrL2jrJZoa3BnON6aV6V8cCq; ll="108306"; _vwo_uuid_v2=D7A......_pk_id.100001.4cf6=32cbb6e140ddd13d.1596900301.37.1616408072.1616405070.'
cookies = {i.split('=')[0]: i.split('=')[1] for i in cookies.split('; ')}
yield scrapy.Request(url, callback=self.sparse, cookies=cookies)
```

第六步，运行获取数据，可获得如下数据：

**具体字段：**

![image-20210323110556425](C:\Users\DELL\PycharmProjects\肖申克的救赎影评(500)\README.assets\image-20210323110556425.png)

**数据库结构：**

![image-20210323110626008](C:\Users\DELL\PycharmProjects\肖申克的救赎影评(500)\README.assets\image-20210323110626008.png)

总共500条数据，每条数据包含四个键值对。

### 数据可视化与分析阶段

第七步，取出所有评论放在一个字符串中，去除所有的符号，只留下中英文，并用jieba以及wordcloud制作出词云。

**词云图：**

![image-20210323111022764](C:\Users\DELL\PycharmProjects\肖申克的救赎影评(500)\README.assets\image-20210323111022764.png)

可以看到，自由以及希望可以说是这部电影最大的主题词了；很多人都把这部电影奉为了经典。

## 交流

有问题可随时联系2393946194@qq.com，欢迎互相交流学习。
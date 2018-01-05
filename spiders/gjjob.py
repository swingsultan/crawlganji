# -*- coding: utf-8 -*-
import scrapy
import re
import time
from crawlganji.items import CrawlganjiItem


class GjjobSpider(scrapy.Spider):
    name = "gjjob"
    allowed_domains = ["ganji.com"]
    start_urls = ['http://ganji.com/']




    def start_requests(self):
        baseurl='http://%s.ganji.com/zhaopin/s/_%s/?from=zhaopin_indexpage'
        cities=['sy','sjz','su']
        fields=['数据分析','大数据开发','数据运营','爬虫','可视化','hadoop', 'spark', 'hbase', 'hive']
        #cities=['sh','bj','gz','wh','sz','nj','tj','tj','hz','cd','cq','cs','cc','dl','dg','fz','foshan','gy','gl','huizhou','hrb','hf','nmg','hn','jn','km','lz','xz','nb','nn','nc','qd']
        #fields=['数据分析','大数据开发']
        for city in cities:
            for keyword in fields:
                firstpage=baseurl%(city,keyword)
                yield scrapy.Request(url=firstpage,callback=self.parse1)


    def parse1(self, response):

        
        for job_url in response.xpath('//*[@id="list-job-id"]/dl/dt/div[2]/div/div[1]/a/@href').extract():
            fnjob_url = re.sub(r'/zhaopin.+', job_url, response.url)

            yield scrapy.Request(fnjob_url,callback=self.parse2)



        next_page=response.xpath('//a[contains(.,"下一页")]/@href').extract_first()
        if next_page is not None:

            next_page_url=re.sub(r'/zhaopin.+',next_page,response.url)
            print('**********************************')
            print(next_page_url)
            yield scrapy.Request(next_page_url,callback=self.parse1)

    def parse2(self, response):
        jobdetail=CrawlganjiItem()
        jobdetail['position']=response.xpath('//li[@class="fl" and contains(.,"职位名称：")]/em/a/text()').extract_first()

        #jobdetail['department'] =
        city = response.xpath('//li[@class="fl w-auto" and contains(.,"工作地点：")]/em/a/text()').extract()
        if len(city) == 1:
            jobdetail['city'] = city[0] + '-NULL'
        else:
            jobdetail['city'] = '-'.join(city)

        #jobdetail['position_type'] =
        jobdetail['experience_requirement'] = response.xpath('//li[@class="fl" and contains(.,"工作经验：")]/em/text()').extract_first()
        jobdetail['education_requirement'] = response.xpath('//li[@class="fl" and contains(.,"最低学历：")]/em/text()').extract_first()
        jobdetail['salary'] = response.xpath('//li[@class="fl" and contains(.,"月")]/em/text()').extract_first()
        jobdetail['major_requirement'] =response.xpath('//div[@class="rt_txt" and contains(.,"公司行业")]/span/a/text()').extract_first()
        jobdetail['recruiting_number'] = response.xpath('//li[@class="fl" and contains(.,"招聘人数：")]/em/text()').extract_first()
        jobdetail['welfare'] =response.xpath('//div[@class="d-welf-items"]/ul/li/text()').extract()
        jobdetail['position_info'] = response.xpath('//div[@class="deta-Corp"]/text()').extract()
        company = response.xpath('//*[@id="companyName"]/span/a/text()').extract_first()
        if type(company) == str:
            jobdetail['company']=company.strip()
        else:
            jobdetail['company']=company
        jobdetail['company_industry'] =response.xpath('//div[@class="rt_txt" and contains(.,"公司行业")]/span/a/text()').extract_first()
        jobdetail['company_type'] =response.xpath('//div[@class="rt_txt" and contains(.,"公司性质：")]/span/a/text()').extract_first()
        #jobdetail['company_finance'] =
        jobdetail['company_size'] = response.xpath('//div[@class="rt_txt" and contains(.,"公司规模：")]/span/text()').extract_first()
        jobdetail['company_url'] = response.xpath('//*[@id="companyName"]/span/a/@href').extract_first()
        posted_date =response.xpath('//span[contains(.,"更新时间")]/text()').extract_first().split(u'：')[-1]
        if posted_date == '今天':
            jobdetail['posted_date']=time.strftime('%Y-%m-%d',time.localtime())
        else:
            jobdetail['posted_date']=time.strftime("%Y-%m-%d", time.strptime("2017-"+posted_date, "%Y-%m-%d"))

        #jobdetail['posted_website'] =
        #jobdetail['posted_url'] =
        yield jobdetail




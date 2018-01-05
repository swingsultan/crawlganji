# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlganjiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    position = scrapy.Field()  # 职位名称

    department = scrapy.Field()  # 职位所属部门名称
    city = scrapy.Field()  # 工作地点，如：北京-海淀区
    position_type = scrapy.Field()  # 工作性质，如：全职，兼职
    experience_requirement = scrapy.Field()  # 经验要求，如：X年经验，X年经验以上
    education_requirement = scrapy.Field()  # 学历要求 ，如：大专，本科
    salary = scrapy.Field()  # 工资，如：6000-15000，单位：元/月薪
    major_requirement = scrapy.Field()  # 专业要求
    recruiting_number = scrapy.Field()  # 招聘人数，如：3（不确定为-1）
    welfare = scrapy.Field()  # 职位诱惑
    position_info = scrapy.Field()  # 岗位描述
    company = scrapy.Field()  # 公司名称
    company_industry = scrapy.Field()  # 公司行业
    company_type = scrapy.Field()  # 公司性质
    company_finance = scrapy.Field()  # 融资阶段
    company_size = scrapy.Field()  # 公司规模
    company_url = scrapy.Field()  # 公司主页链接
    posted_date = scrapy.Field()  # 发布日期，格式：3/21/17
    posted_website = scrapy.Field()  # 发布网站，如：前程无忧
    posted_url = scrapy.Field()  # 招聘信息链接
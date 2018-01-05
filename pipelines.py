# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv

count = 0


class CrawlganjiPipeline(object):


    # def __init__(self):
    #     self.wb=Workbook()
    #     self.ws = self.wb.active
    #     self.ws.append(['position',
    #
    #     'city',
    #
    #     'experience_requirement',
    #     'education_requirement',
    #     'salary',
    #     'major_requirement',
    #     'recruiting_number',
    #     'welfare',
    #     'position_info',
    #     'company',
    #     'company_industry',
    #     'company_type',
    #
    #     'company_size',
    #     'company_url',
    #     'posted_date'])


    def process_item(self, item, spider):
        with open('/Users/mac/Downloads/ganji/18_1_3.csv', 'a') as f:
            writer = csv.writer(f)
            #writer.writerow(['职位名称','工作地点','经验','学历','薪资','专业要求','招聘人数','职位诱惑','岗位介绍','公司名称','公司行业','公司规模','公司主页','发布日期'])


            writer.writerow([item['position'],

              item['city'],
              item['experience_requirement'],
              item['education_requirement'],
              item['salary'],
              item['major_requirement'],
              item['recruiting_number'],
              item['welfare'],
              item['position_info'],
              item['company'],
              item['company_industry'],
              #item['company_type'],
              item['company_size'],
              item['company_url'],
              item['posted_date']
              ])
        # self.ws.append(line)
        # self.wb.save('/Users/mac/Downloads/ganji/crawlganji/test2.xlsx')
        # global count
        # writeSheet.write(count, 0, item['position'])  # 职位名字
        #
        # writeSheet.write(count, 3, item['city'])  # 工作地点
        #
        # writeSheet.write(count, 5, item['experience_requirement'])  # 经验
        # writeSheet.write(count, 6, item['education_requirement'])  # 学历
        # writeSheet.write(count, 7, item['salary'])  # 薪资
        # writeSheet.write(count, 8, item['major_requirement'])  # 专业要求
        # writeSheet.write(count, 9, item['recruiting_number'])  # 招聘人数
        # writeSheet.write(count, 10, item['welfare'])  # 职位诱惑
        # writeSheet.write(count, 11, item['position_info'])
        # writeSheet.write(count, 12, item['company'])  # 公司名称
        # writeSheet.write(count, 13, item['company_industry'])  # 行业
        # writeSheet.write(count, 14, item['company_type'])  # 公司性质
        #
        # writeSheet.write(count, 16, item['company_size'])  # 规模
        # writeSheet.write(count, 17, item['company_url'])  # 主页
        # writeSheet.write(count, 18, item['posted_date'])  # 发布日期
        #
        # file.save('20171230.xls')
        # count +=1





        
        return item

import csv
import random
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from lxml import etree


def sleep(n, op):
    for _ in range(n):
        print('.', end='')
        time.sleep(1)
    print(op)

# 指定url
urls = ['https://www.zhipin.com/', 'https://www.zhipin.com/web/geek/job?query={}&page={}']
prefix = 'https://www.zhipin.com'

# 1. 初始化配置无可视化界面对象
options = webdriver.ChromeOptions()
# 2. 无界面模式
# options.add_argument('-headless')
# options.add_argument('--disable-gpu')

# 让selenium规避被检测到的风险
options.add_argument('excludeSwitches')

# 传入浏览器的驱动
ser = Service(r'D:\Google\chromedriver-win32\chromedriver.exe')

# 实例化一个浏览器对象
bro = webdriver.Chrome(service=ser, options=options)
# bro = webdriver.Firefox(service=ser

# 设置隐式等待 超时时间设置为20s
# bro.implicitly_wait(20 )


for page in range(7,8):
    f = open(f"boos直聘-{page}.csv", "w", encoding="utf-8_sig", newline="")
    csv.writer(f).writerow(["no", "职位", "公司名", "薪资", "经验", "学历", "位置", "关键词", "描述", "详细位置", "详情页"])
    # 让浏览器发起一个指定url请求
    bro.get(f'https://www.zhipin.com/web/geek/job?query=%E5%A4%A7%E6%95%B0%E6%8D%AE&city=101020100&page={page}')
    sleep(10, op=f'bro.get(urls[{page}])')

    #
    # # 定位搜索框 .ipt-search
    # search_tag = bro.find_element(By.CSS_SELECTOR, value='.ipt-search')
    # sleep(1, op='find_ipt')
    # # 输入搜索内容
    # search_tag.send_keys("大数据")
    #
    # # 定位搜索按钮    .代表的是当前标签下的class
    # btn = bro.find_element(By.XPATH, value='//*[@id="wrap"]/div[3]/div/div[1]/div[1]/form/button')
    # sleep(1, op='find_btn')
    # # 点击搜索按钮
    # bro.execute_script('arguments[0].click()', btn)
    # # btn.click()
    # sleep(20, op=r'btn.send_keys\n')

    list_text = bro.page_source
    tree = etree.HTML(list_text)
    jobs = tree.xpath('//div[@class="search-job-result"]/ul/li')

    # f = open("boos直聘.csv", "w", encoding="utf-8", newline="")

    cnt = 0
    jobname = ' '
    company = ' '
    salary = ' '
    location = ' '
    year = ' '
    xueli = ' '
    list = ' '
    keywords = ' '
    for i in jobs[:]:
        cnt += 1
        jobname = i.xpath(".//span[@class='job-name']/text()")[0]
        company = i.xpath(".//h3[@class='company-name']/a/text()")[0]
        salary = i.xpath(".//span[@class='salary']/text()")[0]
        location = i.xpath(".//span[@class='job-area']/text()")[0]
        year = i.xpath(".//div[@class='job-info clearfix']/ul/li/text()")[0]
        xueli = i.xpath(".//div[@class='job-info clearfix']/ul/li/text()")[1]
        list = i.xpath(".//div[@class='job-card-footer clearfix']/ul/li/text()")
        keywords = ",".join(list)

        # 获取二级页面
        # print(i.xpath('.//a[@class="job-card-left"]/@href'))
        half_url = i.xpath('.//a[@class="job-card-left"]/@href')[0]
        detail_url = 'https://www.zhipin.com'+half_url
        # print(jobname, salary, location, year, xueli, keywords)

        try:
            bro.get(detail_url)
            sleep(random.randint(5, 15), str(cnt) + detail_url)
            inter_text = bro.page_source
            tree2 = etree.HTML(inter_text)
            job_miaoshu = tree2.xpath("//div[@class='job-sec-text']/text()")
            # print('|'.join(job_miaoshu))
            address = tree2.xpath("//div[@class='detail-section-item company-address']/div/div[1]/text()")[0]
        except:
            job_miaoshu = ''
            address = ''


        csv.writer(f).writerow(
            [cnt, jobname, company, salary, year, xueli, location, keywords, job_miaoshu, address, detail_url])


    sleep(10, 'sleep')

















def parse():
    # 临时存放获取到的信息
    jobList = []
    # 提取信息
    page_text = bro.page_source
    # 将从互联网上获取的源码数据加载到tree对象中
    tree = etree.HTML(page_text)
    job = tree.xpath('//div[@class="search-job-result"]/ul/li')
    for i in job:
        # 职位
        job_name = i.xpath(".//span[@class='job-name']/text()")[0]
        # 位置
        jobArea = i.xpath(".//span[@class='job-area']/text()")[0]
        # 联系人
        linkman_list = i.xpath(".//div[@class='info-public']//text()")
        linkman = "·".join(linkman_list)
        # 详情页url
        detail_url = prefix + i.xpath(".//h3[@class='company-name']/a/@href")[0]
        # print(detail_url)
        # 薪资
        salary = i.xpath(".//span[@class='salary']/text()")[0]
        # 经验
        job_lable_list = i.xpath(".//ul[@class='tag-list']//text()")
        job_lables = " ".join(job_lable_list)
        # 公司名
        company = i.xpath(".//h3[@class='company-name']/a/text()")[0]
        # 公司类型和人数等
        companyScale_list = i.xpath(".//div[@class='company-info']/ul//text()")
        companyScale = " ".join(companyScale_list)
        # 职位技能
        skill_list = i.xpath("./div[2]/ul//text()")
        skills = " ".join(skill_list)
        # 福利 如有全勤奖补贴等
        try:
            job_desc = i.xpath(".//div[@class='info-desc']/text()")[0]
            # print(type(info_desc))
        except:
            job_desc = ""
            # print(type(info_desc))
        # print(job_name, jobArea, salary, linkman, salaryScale, name, componyScale, tags, info_desc)
        # 将数据写入csv
        csv.writer(f).writerow(
            [job_name, jobArea, salary, linkman, job_lables, company, companyScale, skills, job_desc, detail_url])
        # 将数据存入数组中
        jobList.append({
            "jobName": job_name,
            "jobArea": jobArea,
            "salary": salary,
            "linkman": linkman,
            "jobLables": job_lables,
            "company": company,
            "companyScale": companyScale,
            "skills": skills,
            "job_desc": job_desc,
            "detailUrl": detail_url,
        })

    return {"jobList": jobList}

#
# if __name__ == '__main__':
#     # 访问第一页
#     jobList = parse()
#     query = "大数据"
#     # 访问剩下的九页
#     for i in range(2, 11):
#         print(f"第{i}页")
#         url = urls[1].format(query, i)
#         bro.get(url)
#         sleep(15)
#
#         jobList = parse()
#
#     # 关闭浏览器
#     bro.quit()

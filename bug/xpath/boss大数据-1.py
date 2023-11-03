import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from lxml import etree

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

# 让浏览器发起一个指定url请求
bro.get(urls[0])

sleep(6)

# 定位搜索框 .ipt-search
search_tag = bro.find_element(By.CSS_SELECTOR, value='.ipt-search')
# 输入搜索内容
search_tag.send_keys("大数据")

# 定位搜索按钮    .代表的是当前标签下的class
btn = bro.find_element(By.CSS_SELECTOR, value='.btn-search')
# 点击搜索按钮
btn.send_keys('\n')
sleep(15)

# f = open("boos直聘.csv", "w", encoding="utf-8", newline="")
f = open("boos直聘.csv", "w", encoding="utf-8_sig", newline="")
csv.writer(f).writerow(["职位", "位置", "薪资", "联系人", "经验", "公司名", "类型", "职位技能", "福利", "详情页"])




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


if __name__ == '__main__':
    # 访问第一页
    jobList = parse()
    query = "大数据"
    # 访问剩下的九页
    for i in range(2, 11):
        print(f"第{i}页")
        url = urls[1].format(query, i)
        bro.get(url)
        sleep(15)

        jobList = parse()

    # 关闭浏览器
    bro.quit()

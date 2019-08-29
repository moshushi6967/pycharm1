# 引入库
import requests
import re
#正则表达式
# 写网站站点
url = "https://www.feizw.com/html/5243/index.html"
# 写入headers模拟浏览器上网,避免出现个别网站拒绝访问的情况
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",}
session=requests.session()
# get发送请求
response = session.get(url,headers=headers)
# 将网页编码方式转换为utf-8
response.encoding = 'gbk'
# 网站源码
html = response.text
    # # re.findall获取小说的名字
title = re.findall(r'<meta property="og:title" content="(.*?)" />',html)[0]
    # # 获取每一章的信息(章节的url)
dl = re.findall(r'<div class="chapterlist">.*?</div>',html,re.S)[0]
aill = re.findall(r'<a href="(.*?)" title=(.*?)>(.*?)</a>',dl)
    #新建文件保存小说内容
f=open(f"C:\\Users\\lijy1427\\Documents\\Tencent Files\\1185805992\\FileRecv\\{title}.txt",'w',encoding="gbk")
for i in aill:
  # 章节地址和名
    book_url,book_number,book_name = i
  # 正确章节地址http://www.jingcaiyuedu.com/novel/GLSmM4/1.html
  # 拼接正确章节地址
    book_url = f"https://www.feizw.com/html/5243/{book_url}"
    # 获取章节
    book_response = session.get(book_url,headers=headers)
    book_response.encoding = 'gbk'
    book_html = book_response.text
    # 提取章节内容
    book_content = re.findall(r'<div id="content">(.*?)</div>',book_html,re.S)[0]
    # 清洗提取的数据
    # print(book_content)
    book_content = book_content.replace(' ', '')
    # 将其中内容的空格部分替换成空
    # book_content = book_content.replace('&nbsp;', '')
    # 将其中内容的&nbsp;部分替换成空
    book_content = book_content.replace('</p><p>', '')
    # 将其中内容的<br />部分替换成空
    # book_content = book_content.replace('<br/>', '\n')
    # 将其中内容的<br/>部分替换成空
    # 写入
    f.write(f"{book_name}\n")
    f.write(f"{book_content}\n")
    f.write("\n")
    print(book_url)

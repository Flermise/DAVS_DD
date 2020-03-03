import pymysql
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import requests
import re

# 
# url ='http://www.ccgp.gov.cn/cggg/dfgg/gzgg/202001/t20200114_13758692.htm'
# 
# txt_name = re.search(r"(\d+_\d+)", url).group(1)
# print(str(txt_name)+".txt")
# r = requests.get(url)
# r.encoding = r.apparent_encoding
# soup = BeautifulSoup(r.text.replace('<br>',''),'html.parser')
# soup = BeautifulSoup(r.text.replace('<p>&nbsp;</p>',''),'html.parser')
# [script.extract() for script in soup.findAll('script')]
# s = soup.prettify()
# body_tag = soup.body
# content = body_tag.find('div', {'class':'vF_detail_content'}).find_all('p')
# content2 = body_tag.find('div', {'class':'vF_detail_content'}).find_all('tr')
# result =''
# for tr in content:
#     if len(tr.find_all('p')) == 0:
#         text = tr.get_text().strip()
#         result += text +'\n'
# result = re.sub('[\r\n\f]{2,}','\n', result).strip()
# table =''
# for tr in content2:
#     for td in tr.find_all('td'):
#         table = table + td.get_text().strip()+'\t'
#     table +='\n'
# result += result +'\n' + table
# item = {
#     'project_num' : '1',    # 项目编号
#     'project_name' : '2',   # 项目名称
#     'items' : '3',          # 品目
#     'url' : '4',            # 网址
#     'soft_hard' : '5',      # 软硬件
#     'unit' : '6',           # 采购单位
#     'regions' : '7',        # 行政区域
#     'annou_time' : '8',     # 公告时间
#     'first_annou_time' : '9',   # 首次公告日期
#     'correct_time' : '10',   # 更正日期
#     'project_contact' : '11',        # 项目联系人
#     'project_phone' : '12',          # 项目联系电话
#     'unit_address' : '123',   # 采购单位地址
#     'unit_contact_infor' : '1234', # 采购单位联系方式
#     'agent_name' : '12345',     # 代理机构名称
#     'agent_address' : '123456',  # 代理机构地址
#     'agent_contact' : '1234567',  # 代理机构联系方式
#     'text_path' : '12345678',      # 文本路径
#     'txt_content' : '123456789',    # 文本内容
#     'file_save_path' : '22',      # 更正公告文件路径
#     'file_urls' : '2223',      # 文件下载url
#     'files' : '2223243',          # 文件
# }
from SpiderCCGP import settings


# insert_sql = """
#                    INSERT INTO `fblb_2019`(`project_num`, `project_name`, `items`, `url`, `soft_hard`, `unit`, `regions`, `annou_time`, `project_contact`, `project_phone`, `unit_address`, `unit_contact_infor`, `agent_name`, `agent_address`, `agent_contact`, `text_path`, `file_save_path`)
#                    select %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s from  dual where not exists (select * from fblb_2019 where url = %s)
#                    """
# cursor.execute(insert_sql, (
# item['project_num'], item['project_name'], item['items'], item['url'], item['soft_hard'], item['unit'], item['regions'],
# item['annou_time'], item['project_contact'], item['project_phone'], item['unit_address'], item['unit_contact_infor'],
# item['agent_name'], item['agent_address'], item['agent_contact'], item['text_path'], item['file_save_path'],
# item['url']))
# cursor.execute("select url from fblb_2019")
# results = cursor.fetchall()
# urls = []
# for result in results:
#     urls.append(result)
# for url in urls:
#     print(url[0])
# insert_sql = """
#                    INSERT INTO `fblb_2019`(`project_num`, `project_name`, `items`, `url`, `soft_hard`, `unit`, `regions`, `annou_time`, `project_contact`, `project_phone`, `unit_address`, `unit_contact_infor`, `agent_name`, `agent_address`, `agent_contact`, `text_path`, `file_save_path`)
#                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#                    """
# cursor.execute(insert_sql, (
# item['project_num'], item['project_name'], item['items'], item['url'], item['soft_hard'], item['unit'], item['regions'],
# item['annou_time'], item['project_contact'], item['project_phone'], item['unit_address'], item['unit_contact_infor'],
# item['agent_name'], item['agent_address'], item['agent_contact'], item['text_path'], item['file_save_path']))













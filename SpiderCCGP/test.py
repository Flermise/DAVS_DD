import pymysql

item = {
    'project_num': "1",  # 项目编号
    'project_name': "1",  # 项目名称
    'items': "1",  # 品目
    'url': "2",  # 网址
    'soft_hard': "1",  # 软硬件
    'unit': "1",  # 采购单位
    'regions': "1",  # 行政区域
    'annou_time': "1",  # 公告时间
    'first_annou_time': "1",  # 首次公告日期
    'correct_time': "1",  # 更正日期
    'project_contact': "1",  # 项目联系人
    'project_phone': "1",  # 项目联系电话
    'unit_address': "1",  # 采购单位地址
    'unit_contact_infor': "1",  # 采购单位联系方式
    'agent_name': "1",  # 代理机构名称
    'agent_address': "1",  # 代理机构地址
    'agent_contact': "1",  # 代理机构联系方式
    'text_path': "1",  # 文本路径
    'txt_content': "1",  # 文本内容
    'file_save_path': "1",  # 更正公告文件路径
    'file_urls': "1",  # 文件下载url
    'files': "1",  # 文件
    'year': 2018,  # 年份
    'winning_time': '1',
    'tender_annou_time': '1',
    'experts': '1',
    'total_money': '1'
}

conn = pymysql.connect(host="127.0.0.1", user="root", passwd="123456", db="ccgp", charset="utf8")
cursor = conn.cursor()
database_name = 'zb_' + str(item['year'])
insert_sql = "INSERT INTO " + database_name + """(`project_num`, `project_name`, `items`, `url`, `soft_hard`, `unit`, `regions`, `annou_time`, `tender_annou_time`, `winning_time`, `experts`, `total_money`, `project_contact`, `project_phone`, `unit_address`, `unit_contact_infor`, `agent_name`, `agent_address`, `agent_contact`, `text_path`, `file_save_path`) 
         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
         """
cursor.execute(insert_sql, (
    item['project_num'], item['project_name'], item['items'], item['url'], item['soft_hard'], item['unit'],
    item['regions'], item['annou_time'], item['tender_annou_time'], item['winning_time'], item['experts'],
    item['total_money'], item['project_contact'], item['project_phone'], item['unit_address'],
    item['unit_contact_infor'],
    item['agent_name'], item['agent_address'], item['agent_contact'], item['text_path'],
    item['file_save_path']))
conn.commit()

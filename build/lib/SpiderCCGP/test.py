import pymysql

conn = pymysql.connect(host="127.0.0.1", user="root", passwd="123456", db="ccgp", charset="utf8")
cursor = conn.cursor()
select_sql = """   SELECT url FROM `page_url` 
                            WHERE
	                        type = '公开招标' 
	                        AND page_url.url NOT IN ( SELECT url FROM gkzb_2019 );
        """
cursor.execute(select_sql)
result = cursor.fetchall()
urls = [i[0] for i in result]

for url in urls:
    print(url)


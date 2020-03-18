# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import scrapy
from scrapy.pipelines.files import FilesPipeline

from SpiderCCGP import settings
from SpiderCCGP.items import GZGGItem, PageUrlItem, FBLBGGItem, ZBGGItem, GKZBItem, CJGGItem


class SpiderccgpPipeline(object):

    def process_item(self, item, spider):
        return item


#
# class GZMySQLPipeline(object):
#     # 数据库插入的异步化
#     def __init__(self, dbpool):
#         self.dbpool = dbpool
#
#     @classmethod
#     def from_settings(cls, settings):
#         """
#         数据库建立连接
#         :param settings: 配置参数
#         :return: 实例化参数
#         """
#         dbparms = dict(
#             host=settings["MYSQL_HOST"],
#             db=settings["MYSQL_DBNAME"],
#             user=settings["MYSQL_USER"],
#             passwd=settings["MYSQL_PASSWORD"],
#             charset='utf8',
#             cursorclass=pymysql.cursors.DictCursor,
#             use_unicode=True,
#         )
#         dbpool = adbapi.ConnectionPool('pymysql', **dbparms)
#         return cls(dbpool)
#
#     def do_pageurl_insert(self, cursor, item):
#         insert_sql = "insert into page_url(url,type,kind) values (%s, %s, %s)"
#         cursor.execute(insert_sql, (item['url'], item['ptype'], item['kind']))
#
#     def do_GZGG_insert(self, cursor, item):
#         insert_sql = """
#                                 INSERT INTO `gz_2019`(`project_num`, `project_name`, `items`, `url`, `soft_hard`, `unit`, `regions`, `annou_time`, `first_annou_time`, `correct_time`, `project_contact`, `project_phone`, `unit_address`, `unit_contact_infor`, `agent_name`, `agent_address`, `agent_contact`, `text_path`, `file_save_path`)
#                                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#                                 """
#         cursor.execute(insert_sql, (
#             item['project_num'], item['project_name'], item['items'], item['url'], item['soft_hard'], item['unit'],
#             item['regions'],
#             item['annou_time'], item['first_annou_time'], item['correct_time'], item['project_contact'],
#             item['project_phone'], item['unit_address'],
#             item['unit_contact_infor'], item['agent_name'], item['agent_address'], item['agent_contact'],
#             item['text_path'],
#             item['file_save_path']))
#
#     def do_FBLBGG_insert(self, cursor, item):
#         insert_sql = """
#                     INSERT INTO `fblb_2019`(`project_num`, `project_name`, `items`, `url`, `soft_hard`, `unit`, `regions`, `annou_time`, `project_contact`, `project_phone`, `unit_address`, `unit_contact_infor`, `agent_name`, `agent_address`, `agent_contact`, `text_path`, `file_save_path`)
#                     values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s))
#                     """
#         cursor.execute(insert_sql, (
#             item['project_num'], item['project_name'], item['items'], item['url'], item['soft_hard'], item['unit'],
#             item['regions'],
#             item['annou_time'], item['project_contact'], item['project_phone'], item['unit_address'],
#             item['unit_contact_infor'],
#             item['agent_name'], item['agent_address'], item['agent_contact'], item['text_path'],
#             item['file_save_path']))
#
#     def do_ZBGG_insert(self, cursor, item):
#         insert_sql = """
#         INSERT INTO `zb_2019`(`project_num`, `project_name`, `items`, `url`, `soft_hard`, `unit`, `regions`, `annou_time`, `tender_annou_time`, `winning_time`, `experts`, `total_money`, `project_contact`, `project_phone`, `unit_address`, `unit_contact_infor`, `agent_name`, `agent_address`, `agent_contact`, `text_path`, `file_save_path`)
#         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#         """
#         cursor.execute(insert_sql, (
#             item['project_num'], item['project_name'], item['items'], item['url'], item['soft_hard'], item['unit'],
#             item['regions'], item['annou_time'], item['tender_annou_time'], item['winning_time'], item['experts'],
#             item['total_money'], item['project_contact'], item['project_phone'], item['unit_address'],
#             item['unit_contact_infor'],
#             item['agent_name'], item['agent_address'], item['agent_contact'], item['text_path'],
#             item['file_save_path']))
#
#     def process_item(self, item, spider):
#         """
#         使用twisted将MySQL插入变成异步执行。通过连接池执行具体的sql操作，返回一个对象
#         """
#         if isinstance(item, GZGGItem):
#             query = self.dbpool.runInteraction(self.do_GZGG_insert, item)
#             query.addErrback(self.handle_error)
#         elif isinstance(item, PageUrlItem):
#             query = self.dbpool.runInteraction(self.do_pageurl_insert, item)
#             query.addErrback(self.handle_error)
#         elif isinstance(item, FBLBGGItem):
#             query = self.dbpool.runInteraction(self.do_FBLBGG_insert, item)
#             query.addErrback(self.handle_error)
#         elif isinstance(item,ZBGGItem):
#             query = self.dbpool.runInteraction(self.do_ZBGG_insert, item)
#             query.addErrback(self.handle_error)
#
#     def handle_error(self, failure):
#         print(failure)


class MySQLPipeline(object):
    # 保存更正公告到数据库
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1", user="root", passwd="123456", db="ccgp", charset="utf8")
        self.cursor = self.conn.cursor()

    def _do_page_url_insert(self, item):
        insert_sql = "insert into page_url(url,type,kind) values (%s, %s, %s)"
        self.cursor.execute(insert_sql, (item['url'], item['ptype'], item['kind']))
        self.conn.commit()

    def _do_GZGG_insert(self, item):
        insert_sql = """
                                 INSERT INTO `gz_2019`(`project_num`, `project_name`, `items`, `url`, `soft_hard`, `unit`, `regions`, `annou_time`, `first_annou_time`, `correct_time`, `project_contact`, `project_phone`, `unit_address`, `unit_contact_infor`, `agent_name`, `agent_address`, `agent_contact`, `text_path`, `file_save_path`)
                                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                 """
        self.cursor.execute(insert_sql, (
            item['project_num'], item['project_name'], item['items'], item['url'], item['soft_hard'], item['unit'],
            item['regions'],
            item['annou_time'], item['first_annou_time'], item['correct_time'], item['project_contact'],
            item['project_phone'], item['unit_address'],
            item['unit_contact_infor'], item['agent_name'], item['agent_address'], item['agent_contact'],
            item['text_path'],
            item['file_save_path']))
        self.conn.commit()

    def _do_FBLBGG_insert(self, item):
        insert_sql = """
                     INSERT INTO `fblb_2019`(`project_num`, `project_name`, `items`, `url`, `soft_hard`, `unit`, `regions`, `annou_time`, `project_contact`, `project_phone`, `unit_address`, `unit_contact_infor`, `agent_name`, `agent_address`, `agent_contact`, `text_path`, `file_save_path`)
                     values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s))
                     """
        self.cursor.execute(insert_sql, (
            item['project_num'], item['project_name'], item['items'], item['url'], item['soft_hard'], item['unit'],
            item['regions'],
            item['annou_time'], item['project_contact'], item['project_phone'], item['unit_address'],
            item['unit_contact_infor'],
            item['agent_name'], item['agent_address'], item['agent_contact'], item['text_path'],
            item['file_save_path']))
        self.conn.commit()

    def _do_ZBGG_insert(self, item):
        insert_sql = """
         INSERT INTO `zb_2019`(`project_num`, `project_name`, `items`, `url`, `soft_hard`, `unit`, `regions`, `annou_time`, `tender_annou_time`, `winning_time`, `experts`, `total_money`, `project_contact`, `project_phone`, `unit_address`, `unit_contact_infor`, `agent_name`, `agent_address`, `agent_contact`, `text_path`, `file_save_path`) 
         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
         """
        self.cursor.execute(insert_sql, (
            item['project_num'], item['project_name'], item['items'], item['url'], item['soft_hard'], item['unit'],
            item['regions'], item['annou_time'], item['tender_annou_time'], item['winning_time'], item['experts'],
            item['total_money'], item['project_contact'], item['project_phone'], item['unit_address'],
            item['unit_contact_infor'],
            item['agent_name'], item['agent_address'], item['agent_contact'], item['text_path'],
            item['file_save_path']))
        self.conn.commit()

    def _do_GKZB_insert(self, item):
        insert_sql = """
           INSERT INTO `gkzb_2019`(`project_num`, `project_name`, `items`, `url`, `soft_hard`, `unit`, `regions`, `annou_time`, `bidding_doc_time`, `bidding_doc_price`, `bidding_doc_address`, `bid_opening_time`, `bid_opening_address`, `budget_money`, `project_contact`, `project_phone`, `unit_address`, `unit_contact_infor`, `agent_name`, `agent_address`, `agent_contact`, `text_path`, `file_save_path`)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
        """
        self.cursor.execute(insert_sql, (
            item['project_num'], item['project_name'], item['items'], item['url'], item['soft_hard'], item['unit'],
            item['regions'], item['annou_time'], item['bidding_doc_time'], item['bidding_doc_price'],
            item['bidding_doc_address'], item['bid_opening_time'], item['bid_opening_address'],
            item['budget_money'], item['project_contact'], item['project_phone'], item['unit_address'],
            item['unit_contact_infor'], item['agent_name'], item['agent_address'], item['agent_contact'],
            item['text_path'], item['file_save_path']))
        self.conn.commit()

    def _do_CJGG_insert(self, item):
        insert_sql = """
         INSERT INTO `cj_2019`(`project_num`, `project_name`, `items`, `url`, `soft_hard`, `unit`, `regions`, `annou_time`, `tender_annou_time`, `done_time`, `team_member`, `total_money`, `project_contact`, `project_phone`, `unit_address`, `unit_contact_infor`, `agent_name`, `agent_address`, `agent_contact`, `text_path`, `file_save_path`) 
         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
         """
        self.cursor.execute(insert_sql, (
            item['project_num'], item['project_name'], item['items'], item['url'], item['soft_hard'], item['unit'],
            item['regions'], item['annou_time'], item['tender_annou_time'], item['done_time'], item['team_member'],
            item['total_money'], item['project_contact'], item['project_phone'], item['unit_address'],
            item['unit_contact_infor'],
            item['agent_name'], item['agent_address'], item['agent_contact'], item['text_path'],
            item['file_save_path']))
        self.conn.commit()

    def process_item(self, item, spider):
        if isinstance(item, GZGGItem):
            self._do_GZGG_insert(item)
        elif isinstance(item, PageUrlItem):
            self._do_page_url_insert(item)
        elif isinstance(item, FBLBGGItem):
            self._do_FBLBGG_insert(item)
        elif isinstance(item, ZBGGItem):
            self._do_ZBGG_insert(item)
        elif isinstance(item, GKZBItem):
            self._do_GKZB_insert(item)
        elif isinstance(item, CJGGItem):
            self._do_CJGG_insert(item)
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()


class MyFilePipeline(FilesPipeline):
    # 下载所包含文件
    def get_media_requests(self, item, info):
        if not isinstance(item, PageUrlItem):
            if item['file_urls'] != '':
                name = item['file_save_path']
                yield scrapy.Request(item['file_urls'], meta={'name': name})
        else:
            return item

    def file_path(self, request, response=None, info=None):
        filename = r'/%s' % (request.meta['name'])
        return filename


class TxtSavePipeline(object):
    # 保存页面详细信息
    def process_item(self, item, spider):
        if not isinstance(item, PageUrlItem):
            txt_path = settings.TXT_PATH
            filename_path = txt_path + '/' + str(item['text_path'])
            with open(filename_path, 'w', encoding='utf-8') as f:
                f.write(item['txt_content'] + "\n")
            return item
        else:
            return item

# redis_data_dict = 'k_url'
# redis_db = redis.Redis(host=settings.REDIS_HOST, port=6379, db=5, password=settings.REDIS_PASSWORD)  # 连接redis 第五个数据库
#
#
# class DuplicatePipeline(object):
#     # 与数据库对比去重
#     def __init__(self):
#         self.conn = pymysql.connect(host="127.0.0.1", user="root", passwd="123456", db="ccgp", charset="utf8")
#         self.cursor = self.conn.cursor()
#         redis_db.flushdb()  # 清空redis中的url
#         if redis_db.hlen(redis_data_dict) == 0:
#             sql = 'select url from page_url'
#             df = pandas.read_sql(sql, self.conn)
#             for url in df['url'].to_numpy():  # 载入
#                 redis_db.hset(redis_data_dict, url, 0)
#
#     def process_item(self, item, spider):
#         if redis_db.hexists(redis_data_dict, item['url']):
#             raise DropItem('已保存在数据库中: %s' % item['url'])
#         return item

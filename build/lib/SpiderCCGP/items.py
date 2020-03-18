# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderccgpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class PageUrlItem(scrapy.Item):
    # 页面信息
    url = scrapy.Field()  # 项目url
    ptype = scrapy.Field()  # 公告类型
    kind = scrapy.Field()  # 公告种类


class GKZBItem(scrapy.Item):
    # 公开招标
    project_num = scrapy.Field()  # 项目编号
    project_name = scrapy.Field()  # 项目名称
    items = scrapy.Field()  # 品目
    url = scrapy.Field()  # 网址
    soft_hard = scrapy.Field()  # 软硬件
    unit = scrapy.Field()  # 采购单位
    regions = scrapy.Field()  # 行政区域
    annou_time = scrapy.Field()  # 公告时间
    bidding_doc_time = scrapy.Field()  # 招标文件时间
    bidding_doc_price = scrapy.Field()  # 招标文件售价
    bidding_doc_address = scrapy.Field()  # 招标文件地址
    bid_opening_time = scrapy.Field()  # 开标时间
    bid_opening_address = scrapy.Field()  # 开标地点
    budget_money = scrapy.Field()  # 预算金额
    project_contact = scrapy.Field()  # 项目联系人
    project_phone = scrapy.Field()  # 项目联系电话
    unit_address = scrapy.Field()  # 采购单位地址
    unit_contact_infor = scrapy.Field()  # 采购单位联系方式
    agent_name = scrapy.Field()  # 代理机构名称
    agent_address = scrapy.Field()  # 代理机构地址
    agent_contact = scrapy.Field()  # 代理机构联系方式
    text_path = scrapy.Field()  # 文本路径
    txt_content = scrapy.Field()  # 文本内容
    file_save_path = scrapy.Field()  # 废标公告文件路径
    file_urls = scrapy.Field()  # 文件下载url
    files = scrapy.Field()  # 文件


class GZGGItem(scrapy.Item):
    # 更正公告
    project_num = scrapy.Field()  # 项目编号
    project_name = scrapy.Field()  # 项目名称
    items = scrapy.Field()  # 品目
    url = scrapy.Field()  # 网址
    soft_hard = scrapy.Field()  # 软硬件
    unit = scrapy.Field()  # 采购单位
    regions = scrapy.Field()  # 行政区域
    annou_time = scrapy.Field()  # 公告时间
    first_annou_time = scrapy.Field()  # 首次公告日期
    correct_time = scrapy.Field()  # 更正日期
    project_contact = scrapy.Field()  # 项目联系人
    project_phone = scrapy.Field()  # 项目联系电话
    unit_address = scrapy.Field()  # 采购单位地址
    unit_contact_infor = scrapy.Field()  # 采购单位联系方式
    agent_name = scrapy.Field()  # 代理机构名称
    agent_address = scrapy.Field()  # 代理机构地址
    agent_contact = scrapy.Field()  # 代理机构联系方式
    text_path = scrapy.Field()  # 文本路径
    txt_content = scrapy.Field()  # 文本内容
    file_save_path = scrapy.Field()  # 更正公告文件路径
    file_urls = scrapy.Field()  # 文件下载url
    files = scrapy.Field()  # 文件


class FBLBGGItem(scrapy.Item):
    # 废标流标公告
    project_num = scrapy.Field()  # 项目编号
    project_name = scrapy.Field()  # 项目名称
    items = scrapy.Field()  # 品目
    url = scrapy.Field()  # 网址
    soft_hard = scrapy.Field()  # 软硬件
    unit = scrapy.Field()  # 采购单位
    regions = scrapy.Field()  # 行政区域
    annou_time = scrapy.Field()  # 公告时间
    project_contact = scrapy.Field()  # 项目联系人
    project_phone = scrapy.Field()  # 项目联系电话
    unit_address = scrapy.Field()  # 采购单位地址
    unit_contact_infor = scrapy.Field()  # 采购单位联系方式
    agent_name = scrapy.Field()  # 代理机构名称
    agent_address = scrapy.Field()  # 代理机构地址
    agent_contact = scrapy.Field()  # 代理机构联系方式
    text_path = scrapy.Field()  # 文本路径
    txt_content = scrapy.Field()  # 文本内容
    file_save_path = scrapy.Field()  # 废标公告文件路径
    file_urls = scrapy.Field()  # 文件下载url
    files = scrapy.Field()  # 文件


class ZBGGItem(scrapy.Item):
    # 中标公告
    project_num = scrapy.Field()  # 项目编号
    project_name = scrapy.Field()  # 项目名称
    items = scrapy.Field()  # 品目
    url = scrapy.Field()  # 网址
    soft_hard = scrapy.Field()  # 软硬件
    unit = scrapy.Field()  # 采购单位
    regions = scrapy.Field()  # 行政区域
    annou_time = scrapy.Field()  # 公告时间
    tender_annou_time = scrapy.Field()  # 招标公告时间
    winning_time = scrapy.Field()  # 中标公告时间
    experts = scrapy.Field()  # 专家名单
    total_money = scrapy.Field()  # 总中标金额
    project_contact = scrapy.Field()  # 项目联系人
    project_phone = scrapy.Field()  # 项目联系电话
    unit_address = scrapy.Field()  # 采购单位地址
    unit_contact_infor = scrapy.Field()  # 采购单位联系方式
    agent_name = scrapy.Field()  # 代理机构名称
    agent_address = scrapy.Field()  # 代理机构地址
    agent_contact = scrapy.Field()  # 代理机构联系方式
    text_path = scrapy.Field()  # 文本路径
    txt_content = scrapy.Field()  # 文本内容
    file_save_path = scrapy.Field()  # 废标公告文件路径
    file_urls = scrapy.Field()  # 文件下载url
    files = scrapy.Field()  # 文件


class CJGGItem(scrapy.Item):
    # 成交公告
    project_num = scrapy.Field()  # 项目编号
    project_name = scrapy.Field()  # 项目名称
    items = scrapy.Field()  # 品目
    url = scrapy.Field()  # 网址
    soft_hard = scrapy.Field()  # 软硬件
    unit = scrapy.Field()  # 采购单位
    regions = scrapy.Field()  # 行政区域
    annou_time = scrapy.Field()  # 公告时间
    tender_annou_time = scrapy.Field()  # 招标公告时间
    done_time = scrapy.Field()  # 成交时间
    team_member = scrapy.Field()  # 小组成员名单
    total_money = scrapy.Field()  # 总成交金额
    project_contact = scrapy.Field()  # 项目联系人
    project_phone = scrapy.Field()  # 项目联系电话
    unit_address = scrapy.Field()  # 采购单位地址
    unit_contact_infor = scrapy.Field()  # 采购单位联系方式
    agent_name = scrapy.Field()  # 代理机构名称
    agent_address = scrapy.Field()  # 代理机构地址
    agent_contact = scrapy.Field()  # 代理机构联系方式
    text_path = scrapy.Field()  # 文本路径
    txt_content = scrapy.Field()  # 文本内容
    file_save_path = scrapy.Field()  # 废标公告文件路径
    file_urls = scrapy.Field()  # 文件下载url
    files = scrapy.Field()  # 文件

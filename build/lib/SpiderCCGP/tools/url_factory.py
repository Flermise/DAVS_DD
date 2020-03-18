from urllib.parse import urlencode

import pymysql


class GetUrl(object):
    searchtype = 1
    page_index = 1,
    bidSort = 0,
    buyerName = "",
    projectId = "",
    pinMu = -1,  # 1 货物类  #3服务类
    bidType = -1,  # 7 中标 # 8 更正   #12 废标
    dbselect = 'bidx',
    kw = '',
    start_time = '2019:01:01',
    end_time = '2019:12:31',
    timeType = 6,
    displayZone = "",
    zoneId = "",
    pppStatus = 0,
    agentName = ""

    conn = pymysql.connect(host="127.0.0.1", user="root", passwd="123456", db="ccgp", charset="utf8")
    cursor = conn.cursor()

    def __init__(self, pinMu, bidType):
        self.pinMu = pinMu
        self.bidType = bidType

    def get_kind(self):
        kind = ''
        if self.pinMu == 1:
            kind = '货物类'
        elif self.pinMu == 3:
            kind = "服务类"
        return kind

    def get_page_type(self):
        page_type = ""
        if self.bidType == 8:
            page_type = '更正公告'
        elif self.bidType == 7:
            page_type = '中标公告'
        elif self.bidType == 12:
            page_type = '废标公告'
        return page_type

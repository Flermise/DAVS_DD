# -*- coding: utf-8 -*-
import re
from urllib import parse
from urllib.parse import urlencode

import requests
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
import pymysql

from SpiderCCGP.items import PageUrlItem, GZGGItem, FBLBGGItem, ZBGGItem


def get_txt_content(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding

    soup = BeautifulSoup(r.text.replace('<p>&nbsp;</p>', ''), 'html.parser')
    [script.extract() for script in soup.findAll('script')]
    soup.prettify()
    body_tag = soup.body
    content = body_tag.find('div', {'class': 'vF_detail_content'}).find_all('p')
    result = ''
    for tr in content:
        if len(tr.find_all('p')) == 0:
            text = tr.get_text().strip()
            result += text + '\n'
    result = re.sub('[\r\n\f]{2,}', '\n', result).strip()
    return result


class CcgpGovCnSpider(scrapy.Spider):
    name = 'ccgp.gov.cn'
    allowed_domains = ['www.ccgp.gov.cn','search.ccgp.gov.cn']
    start_urls = ['http://search.ccgp.gov.cn']
    conn = pymysql.connect(host="127.0.0.1", user="root", passwd="123456", db="ccgp", charset="utf8")
    cursor = conn.cursor()

    def start_requests(self):
        url = 'http://search.ccgp.gov.cn/bxsearch?searchtype=1&page_index=1&bidSort=0&buyerName=&projectId=&pinMu=1&bidType=7&dbselect=bidx&kw=%E4%B8%AD%E5%8D%8E%E5%A5%B3%E5%AD%90%E5%AD%A6%E9%99%A2&start_time=2019%3A01%3A01&end_time=2019%3A12%3A31&timeType=6&displayZone=&zoneId=&pppStatus=0&agentName='
        kind = '货物类'
        page_type = '中标公告'
        yield Request(url, meta={'kind': kind, 'type': page_type}, callback=self.parse, dont_filter=True)
    # def start_requests(self):
    #     self.cursor.execute("select `name` from college")
    #     result = self.cursor.fetchall()
    #     schools = [i[0] for i in result]
    #     for pinMu in [1, 3]:
    #         for school in schools:
    #             data = {
    #                 'searchtype': 1,
    #                 'page_index': 1,
    #                 'bidSort': 0,
    #                 'buyerName': "",
    #                 'projectId': "",
    #                 'pinMu': pinMu,  # 1 货物类  #3服务类
    #                 'bidType': 7,  # 7 中标 # 8 更正   #12 废标
    #                 'dbselect': 'bidx',
    #                 'kw': school,
    #                 'start_time': '2019:01:01',
    #                 'end_time': '2019:12:31',
    #                 'timeType': 6,
    #                 'displayZone': "",
    #                 'zoneId': "",
    #                 'pppStatus': 0,
    #                 'agentName': ""
    #             }
    #
    #             params = urlencode(data)
    #             url = self.start_urls[0] + '/bxsearch?' + params
    #             page_type = ''
    #             kind = ''
    #             if data['pinMu'] == 1:
    #                 kind = '货物类'
    #             elif data['pinMu'] == 3:
    #                 kind = '服务类'
    #
    #             if data['bidType'] == 8:
    #                 page_type = '更正公告'
    #             elif data['bidType'] == 7:
    #                 page_type = '中标公告'
    #             elif data['bidType'] == 12:
    #                 page_type = '废标公告'
    #
    #             yield Request(url, meta={'kind': kind, 'type': page_type}, callback=self.parse, dont_filter=True)

    def parse(self, response):
        url_num = int(response.xpath('/html/body/div[5]/div[1]/div/p[1]/span[2]/text()').extract_first(""))
        url = response.url
        page_type = response.meta['type']
        page_kind = response.meta['kind']
        if (url_num > 0) and (url_num <= 20):
            yield Request(url, meta={'kind': page_kind, 'type': page_type}, callback=self.parse_page)
        elif url_num >= 20:
            page_num = int(url_num) // 20 + 1
            lts = url.split('&')
            for i in range(page_num):
                lts[1] = 'page_index=' + str(i + 1)
                next_url = '&'.join(lts)
                yield Request(next_url, meta={'kind': page_kind, 'type': page_type}, callback=self.parse_page)

    def parse_page(self, response):
        lis = response.xpath('/html/body/div[5]/div[2]/div/div/div[1]/ul/li')
        page_type = response.meta['type']
        page_kind = response.meta['kind']
        for i in range(len(lis)):
            item = PageUrlItem()
            post_url = response.xpath(
                '/html/body/div[5]/div[2]/div/div/div[1]/ul/li[' + str(i + 1) + ']/a/@href').extract_first("")
            item['url'] = post_url
            item['ptype'] = page_type
            item['kind'] = page_kind
            yield item
            if page_type == '更正公告':
                yield Request(post_url, callback=self.parse_detail_8)
            elif page_type == '废标公告':
                yield Request(post_url, callback=self.parse_detail_12)
            elif page_type == '中标公告':
                yield Request(post_url, callback=self.parse_detail_7)

    def parse_detail_7(self, response):
        item = ZBGGItem()
        project_name = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[3]/div/p[5]/text()').extract_first("")
        if project_name != "":
            project_name = project_name.split('：')[1].strip()
        item['project_num'] = project_name
        item['project_name'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[2]/td[2]/text()').extract_first("")
        item['items'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[3]/td[2]/p/text()').extract_first("")
        item['url'] = response.url
        item['soft_hard'] = ''
        item['unit'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[4]/td[2]/text()').extract_first("")
        item['regions'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[5]/td[2]/text()').extract_first("")
        item['annou_time'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[5]/td[4]/text()').extract_first("")
        item['tender_annou_time'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[6]/td[2]/text()').extract_first("")
        item['winning_time'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[6]/td[4]/text()').extract_first("")
        item['experts'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[7]/td[2]/text()').extract_first("")
        item['total_money'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[8]/td[2]/text()').extract_first("")
        item['project_contact'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[10]/td[2]/text()').extract_first("")
        item['project_phone'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[11]/td[2]/text()').extract_first("")
        item['unit_address'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[13]/td[2]/text()').extract_first("")
        item['unit_contact_infor'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[14]/td[2]/text()').extract_first("")
        item['agent_name'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[15]/td[2]/text()').extract_first("")
        item['agent_address'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[16]/td[2]/text()').extract_first("")
        item['agent_contact'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[17]/td[2]/text()').extract_first("")
        txt_name = re.search(r"(\d+_\d+)", response.url).group(1)
        item['text_path'] = str(txt_name) + '.txt'
        item['file_save_path'] = ""
        item['file_urls'] = ""
        item['txt_content'] = get_txt_content(response.url)
        file_names = response.xpath('//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr/td/a/text()').extract()
        file_ids = response.xpath('//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr/td/a/@id').extract()
        len_file = len(file_names)
        for i in range(len_file):
            file_name = file_names[i]
            if re.match(".*(中标).*", file_name):
                file_id = file_ids[i]
                file_save_path = file_id + '/' + file_name
                item['file_save_path'] = file_save_path
                item['file_urls'] = parse.urljoin(response.url, '/oss/download?uuid=' + file_id)
        yield item

    def parse_detail_8(self, response):
        item = GZGGItem()
        item['project_num'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[3]/div/p[2]/text()').extract_first("")
        item['project_name'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[2]/td[2]/text()').extract_first("")
        item['items'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[3]/td[2]/p/text()').extract_first("")
        item['url'] = response.url
        item['soft_hard'] = ''
        item['unit'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[4]/td[2]/text()').extract_first("")
        item['regions'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[5]/td[2]/text()').extract_first("")
        item['annou_time'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[5]/td[4]/text()').extract_first("")
        item['first_annou_time'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[6]/td[2]/text()').extract_first("")
        item['correct_time'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[6]/td[4]/text()').extract_first("")
        item['project_contact'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[8]/td[2]/text()').extract_first("")
        item['project_phone'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[9]/td[2]/text()').extract_first("")
        item['unit_address'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[11]/td[2]/text()').extract_first("")
        item['unit_contact_infor'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[12]/td[2]/text()').extract_first("")
        item['agent_name'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[13]/td[2]/text()').extract_first("")
        item['agent_address'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[14]/td[2]/text()').extract_first("")
        item['agent_contact'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[15]/td[2]/text()').extract_first("")
        txt_name = re.search(r"(\d+_\d+)", response.url).group(1)
        item['text_path'] = str(txt_name) + '.txt'
        item['file_save_path'] = ''
        item['file_urls'] = ''
        item['txt_content'] = get_txt_content(response.url)
        file_names = response.xpath('//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr/td/a/text()').extract()
        file_ids = response.xpath('//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr/td/a/@id').extract()
        len_file = len(file_names)
        for i in range(len_file):
            file_name = file_names[i]
            if re.match(".*(更正|变更).*", file_name):
                file_id = file_ids[i]
                file_save_path = file_id + '/' + file_name
                item['file_save_path'] = file_save_path
                item['file_urls'] = parse.urljoin(response.url, '/oss/download?uuid=' + file_id)
        yield item

    def parse_detail_12(self, response):
        item = FBLBGGItem()
        project_name = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[3]/div/p[5]/text()').extract_first("")
        if project_name != "":
            project_name = project_name.split('：')[1].strip()
        item['project_num'] = project_name
        item['project_name'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[2]/td[2]/text()').extract_first("")
        item['items'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[3]/td[2]/p/text()').extract_first("")
        item['url'] = response.url
        item['soft_hard'] = ''
        item['unit'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[4]/td[2]/text()').extract_first("")
        item['regions'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[5]/td[2]/text()').extract_first("")
        item['annou_time'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[5]/td[4]/text()').extract_first("")
        item['project_contact'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[7]/td[2]/text()').extract_first("")
        item['project_phone'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[8]/td[2]/text()').extract_first("")
        item['unit_address'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[10]/td[2]/text()').extract_first("")
        item['unit_contact_infor'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[11]/td[2]/text()').extract_first("")
        item['agent_name'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[12]/td[2]/text()').extract_first("")
        item['agent_address'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[13]/td[2]/text()').extract_first("")
        item['agent_contact'] = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[14]/td[2]/text()').extract_first("")
        txt_name = re.search(r"(\d+_\d+)", response.url).group(1)
        item['text_path'] = str(txt_name) + '.txt'
        item['file_save_path'] = ''
        item['file_urls'] = ''
        item['txt_content'] = get_txt_content(response.url)
        file_names = response.xpath('//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr/td/a/text()').extract()
        file_ids = response.xpath('//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr/td/a/@id').extract()
        len_file = len(file_names)
        for i in range(len_file):
            file_name = file_names[i]
            if re.match(".*(废标|流标|终止).*", file_name):
                file_id = file_ids[i]
                file_save_path = file_id + '/' + file_name
                item['file_save_path'] = file_save_path
                item['file_urls'] = parse.urljoin(response.url, '/oss/download?uuid=' + file_id)
        yield item

import urllib.parse
import time
import datetime
import re
import urllib.request


class Throttle:

    def __init__(self, delay):
        # 访问同域名时需要的间隔时间
        self.delay = delay
        # key:netloc,value:lastTime.记录每个域名的上一次访问的时间戳
        self.domains = {}

    # 计算需要的等待时间，并执行等待
    def wait(self, url):
        if self.delay <= 0:
            print('delay ='+self.delay)
            return

        domain = urllib.parse.urlparse(url).netloc
        lastTime = self.domains.get(domain)

        if lastTime is not None:
            # 计算等待时间
            wait_sec = self.delay - (datetime.datetime.now() - lastTime).seconds
            if wait_sec > 0:
                time.sleep(wait_sec)

        self.domains[domain] = datetime.datetime.now()

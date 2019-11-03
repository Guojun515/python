#!/usr/bin/env python
# -*- coding:utf-8 -*-
import openpyxl
import requests
import datetime
import time
from bs4 import BeautifulSoup


def write_excel_xlsx(path, sheet_name, value):
    """
    写入excel
    :param path:
    :param sheet_name:
    :param value:
    :return:
    """
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = sheet_name
    for i in range(0, len(value)):
        for j in range(0, len(value[i])):
            sheet.cell(row=i + 1, column=j + 1, value=str(value[i][j]))
    workbook.save(path)
    print("XLSX格式表格写入数据成功！")


class DouBanCrawler:
    """
    这里是类注释
    豆瓣租房爬虫
    """

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"
        }
        self.result = [["标题", "地址", "最后更新时间"]]

    def download_page(self, url):
        result = requests.get(url, headers=self.headers)
        return result.text

    def get_context(self, htmlData, addressKeyWords=None, houseKeyWords=None, otherKeyWords=None, preDay=3):
        soup = BeautifulSoup(htmlData, "html.parser")
        table = soup.find("table", class_="olt")
        preDate = datetime.datetime.now() + datetime.timedelta(-preDay)
        for tr in table.find_all("tr", class_=""):
            last_update_str = "2019-" + tr.find("td", class_="time").get_text()
            lastUpdate = datetime.datetime.strptime(last_update_str, "%Y-%m-%d %H:%M")
            if lastUpdate >= preDate:
                title = tr.find("td", class_="title").find("a")
                titleContent = title['title']
                titleHref = title['href']

                # 是否搜索的地址
                is_adress = False
                if addressKeyWords is None:
                    is_adress = True
                else:
                    for addressKeyWord in addressKeyWords:
                        if titleContent.find(addressKeyWord) > -1:
                            is_adress = True
                            break

                # 如果是搜索地址，继续判断是否搜索的房型
                isInclude = False
                if houseKeyWords is None:
                    isInclude = True
                else:
                    if is_adress:
                        for houseKeyWord in houseKeyWords:
                            if titleContent.find(houseKeyWord) > -1:
                                isInclude = True
                                break

                # 如果是搜索的房型，继续判断其他关键字
                isOther = False
                if otherKeyWords is None:
                    isOther = True
                else:
                    if isInclude:
                        for otherKeyWord in otherKeyWords:
                            if titleContent.find(otherKeyWord) > -1:
                                isOther = True
                                break

                # 是想要的结果，输出
                if isOther:
                    print(titleContent)
                    print(titleHref)
                    print(lastUpdate)
                    self.result.append([titleContent, titleHref, lastUpdate])
            else:
                print(preDate)
                print(lastUpdate)
                return None
        page_div = soup.find("div", class_="paginator")
        next_href = page_div.find("span", class_="next").find("a")
        return next_href["href"]


if __name__ == "__main__":
    douBanCrawler = DouBanCrawler()
    urls = [
        "https://www.douban.com/group/106955/discussion?start=0",
        "https://www.douban.com/group/637628/discussion?start=0",
        "https://www.douban.com/group/szsh/discussion?start=0",
        "https://www.douban.com/group/637700/discussion?start=0",
        "https://www.douban.com/group/551176/discussion?start=0",
        "https://www.douban.com/group/586502/discussion?start=0"
    ]
    i = 1
    try:
        for url in urls:
            while url:
                html = douBanCrawler.download_page(url)
                # ["下沙", "上沙", "沙尾", "沙嘴", "沙尾", "KKONE", "车公庙"]
                url = douBanCrawler.get_context(html,
                                                None,
                                                ["两房", "2房", "三房", "3房"],
                                                ["转租", "个人"],
                                                1)
                print("搜索第【" + str(i) + "】页")
                i = i + 1
                time.sleep(1)
    finally:
        write_excel_xlsx("C:/Users/Guojun/Desktop/豆瓣租房6.xlsx", "豆瓣租房", douBanCrawler.result)

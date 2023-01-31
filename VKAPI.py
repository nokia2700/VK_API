import json
import math
import time
from selenium import webdriver
from lxml import html

import requests


class Parser:
    def __init__(self, token):
        self.__token = token

    # def get_group_id(self, group_link):
    #     driver = webdriver.Chrome('/Users/dmitrii/PycharmProjects/pythonProject1/chromedriver')
    #     driver.get('https://regvk.com/id/')
    #
    #     driver.find_element_by_xpath("id('enter')").send_keys(group_link)
    #     driver.find_element_by_xpath("//button").click()
    #     group_id = driver.find_element_by_xpath("//td[contains(text(), 'ID')]").get_attribute("innerHTML")
    #
    #     driver.close()
    #     return group_id.split(" ")[-1]

    def get_group_id(self, group_link):
        res = requests.get(group_link, headers={
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
        })

        dom = html.fromstring(res.content)
        group_id = dom.xpath('//a[@class="post__anchor anchor"]/@name')[0]
        group_id = group_id.split("-")[1]
        return group_id.split("_")[0]

    def get_users(self, group_link, users_count):
        params = {
            "group_id": group_link,
            "fields": 'sex',
            "count": 1000,
            "offset": 0,
            "access_token": self.__token,
            "v": "5.131",
        }

        users = []

        while True:
            res = requests.post("https://api.vk.com/method/groups.getMembers", params=params)
            res = json.loads(res.text)
            params["offset"] += 1000
            if res["response"]["items"]:
                users.extend(res["response"]["items"])
                print(f'Собрано {len(users)} пользователей')
                if len(users) > users_count:
                    return users
            else:
                raise res

            time.sleep(1)
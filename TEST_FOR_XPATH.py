# -*- coding:utf-8 -*-
# @Author:Cheng Lei 1037654919@qq.com
# @Time : 2022/11/23 下午3:22
# @FileName: TEST_FOR_XPATH.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
from lxml import etree
import math
from sqlalchemy import create_engine
import random
import datetime
import urllib3

url = 'https://www.maigoo.com/goomai/203066.html'
response = requests.get(url, timeout=5)
html2 = response.text
soup2 = BeautifulSoup(html2, 'lxml')
html_tree = etree.HTML(html2)
html_data = html_tree.xpath('/html/body/div/ul/li/a')

result = soup2.find_all('div',class_='only-cont')[0].get_text().strip().split('\n\n\n')
pp = result.find_all('p')[0]
datax=[]



# text = result.text.encode("iso-8859-1").decode('utf8')
print(result)


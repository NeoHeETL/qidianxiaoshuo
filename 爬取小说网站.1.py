import requests
from lxml import etree
import os
import io  
import sys 

#改变标准输出的默认编码 
#utf-8中文乱码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') 


class Spider(object):
    def start_request(self):
      url = "https://www.zhihu.com/question/319722198/answer/648800261?from=groupmessage&isappinstalled=0&utm_medium=social&utm_oi=710050841138057216&utm_source=wechat_session&s_s_i=XhBGM2Optbno7LYIrQXM1EYontawEp7JcOvqHG7aKTE%3D&s_r=1"
      response = requests.get(url, timeout=30)
      print (response.text)
    #   xml = etree.HTML(response.text)
    #   bigtit_list = xml.xpath('//div[@class="book-mid-info"]/h4/a/text()')
    #   bigsrc_list = xml.xpath('//div[@class="book-mid-info"]/h4/a/@href')
    #   for bigtit, bigsrc in zip(bigtit_list, bigsrc_list):
    #     if os.path.exists(bigtit) == False:
    #       os.mkdir(bigtit)
    #     self.next_file(bigtit, bigsrc)
    #
    # def next_file(self, bigtit, bigsrc):
    #   # 请求二级页面拿到数据，抽取章名、章链接
    #   url="https:" + bigsrc
    #   response=requests.get(url, timeout = 30)
    #   xml=etree.HTML(response.text)
    #   littit_list=xml.xpath('//ul[@class="cf"]/li/a/text()')
    #   litsrc_list=xml.xpath('//ul[@class="cf"]/li/a/@href')
    #   for littit, litsrc in zip(littit_list, litsrc_list):
    #     self.finally_file(littit, litsrc, bigtit)
    #
    # def finally_file(self, littit, litsrc, bigtit):
    #   # 请求三级页面拿到数据，抽取文章内容，保存数据
    #   url="https:" + litsrc
    #   response=requests.get(url, timeout = 30)
    #   xml=etree.HTML(response.text)
    #   content = "\n".join(xml.xpath('//div [@class="read-content j_readContent"]/p/text()'))
    #   filename = bigtit + '\\' + littit + '.txt'
    #   print('正在保存小说：'+ filename)
    #   with open(filename, 'w', encoding='utf-8') as f:
    #     f.write(content)


spider=Spider()
spider.start_request()

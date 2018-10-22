#-*- coding: UTF-8 -*-
from urllib import urlretrieve
import requests
import os

"""
爬取今日头条图片
"""
def hero_imgs_download(heros_url,header):
    # 请求地址，获取json数据包
    req = requests.get(url = heros_url, headers = header).json()
    # 解析json数据包
    data = req['data']
    image_detail = data['image_detail']
    i = 0 ;
    hero_images_path = 'toutiao_images'
    for url_temp in image_detail:
        url_temp = url_temp['url']#从json中获取url
        i += 1
        filename = str(i) + '.jpg'
        filename = hero_images_path + '/' + filename
        if not os.path.isdir(hero_images_path):
            os.makedirs(hero_images_path)
        #下载图片
        urlretrieve(url = url_temp, filename = filename)

if __name__ == '__main__':
    headers = { #本次抓包可以不用header
            # 'Accept-Charset': 'UTF-8',
            # 'Accept-Encoding': 'gzip,deflate',
            # 'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; MI 5 MIUI/V8.1.6.0.MAACNDI)',
            # 'X-Requested-With': 'XMLHttpRequest',
            # 'Content-type': 'application/x-www-form-urlencoded',
            # 'Connection': 'Keep-Alive',
            # 'Host': 'gamehelper.gm825.com'
            }
    # 抓包到的地址
    heros_url = "http://a3.pstatp.com/article/content/21/2/6602195642037043725/6602195642037043725/1/0/?fp=wSTqJlUSPYPZFlH7FlU1FYwIPrsq&version_code=6.9.2&tma_jssdk_version=1.2.2.4&app_name=news_article&vid=E564BEB1-00A3-4CD6-BCE9-DD0F6E2BFA28&device_id=35008162646&channel=App%20Store&resolution=750*1334&aid=13&ab_feature=z1&ab_version=536107,494122,554256,551350,521868,523910,239097,545059,170988,170989,493250,405356,552529,442126,374119,549807,516057,517715,489316,501960,554429,553435,554010,550042,459650,459994,554274,551606,550585,522765,385747,416055,513051,555255,378451,471407,554208,523157,550818,509308,550517,271178,326524,326532,545080,555415,496389,545698,555654,307800,546064,492342,554836,549647,424177,472007,214069,31211,549709,482356,546785,442255,556453,546700,280447,281297,555517,325619,545068,526720,431141,498375,554468,467513,554003,484769,444465,425530,552451,486950,543446,472114,548841,124647,517988,457480&ab_group=z1&openudid=fce91543c6d24ea3474634993de8ae2626afcfe7&update_version_code=69212&idfv=E564BEB1-00A3-4CD6-BCE9-DD0F6E2BFA28&ac=WIFI&os_version=12.0.1&ssmix=a&device_platform=iphone&iid=45844404180&ab_client=a1,f2,f7,e1&device_type=iPhone%206S&idfa=524B4D1D-A307-498A-8242-39C1FEE52CD5&as=a2a5638c16e33bd89d1301&ts=1540175926"
    hero_imgs_download(heros_url,headers)

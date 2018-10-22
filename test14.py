# -*- coding: UTF-8 -*-
from selenium import webdriver
import csv
import xlsxwriter
import urllib
import time
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

# url = 'http://tieba.baidu.com/p/1753935195'

#用webdriver加载页面
#用Phantomjs接口创建一个selenium的webdriver
# driver = webdriver.PhantomJS()
# driver.get(url)
#将这个网站上的图片地址全部拿到
# datas = driver.find_elements_by_css_selector('img.BDE_Image')
# print len(datas)
# for data in datas:
#     url = data.get_attribute('src')
#     if (len(url) != 0) :
#         print url


urlList = ['https://imgsa.baidu.com/forum/w%3D580/sign=92f7a739462309f7e76fad1a420f0c39/7eba40ed2e738bd46ea1009ca18b87d6267ff9ae.jpg                                                                    '
,'http://fc-feed.cdn.bcebos.com/0/pic/2f4d20e0095b5e0602119754f36b659b.jpg                                                                                                                              '
,'https://imgsa.baidu.com/forum/w%3D580/sign=71ef1fbf720e0cf3a0f74ef33a47f23d/17128d01a18b87d6c6c219b2070828381e30fdae.jpg                                                                              '
,'https://imgsa.baidu.com/forum/w%3D580/sign=63deb3355edf8db1bc2e7c6c3922dddb/74ac06f431adcbef49b7ccabacaf2edda2cc9fae.jpg                                                                              '
,'https://imgsa.baidu.com/forum/w%3D580/sign=8bc12c85972bd40742c7d3f54b889e9c/59114b34970a304ea7fa1257d1c8a786c8175c55.jpg                                                                              '
,'https://imgsa.baidu.com/forum/w%3D580/sign=c930608c90ef76c6d0d2fb23ad14fdf6/9e89e350352ac65c3cd5d4defbf2b21192138a5d.jpg                                                                              '
,'https://imgsa.baidu.com/forum/w%3D580/sign=e580d266b2fb43161a1f7a7210a64642/1715ba51f8198618ee975d294aed2e738ad4e65e.jpg                                                                              '
,'https://imgsa.baidu.com/forum/w%3D580/sign=8e03baf055fbb2fb342b581a7f482043/9d1cb91bb051f81951f5b1e7dab44aed2f73e75e.jpg                                                                              '
,'https://imgsa.baidu.com/forum/w%3D580/sign=8ee6e99b1d950a7b75354ecc3ad3625c/5fe3a164034f78f035d8285e79310a55b2191c5e.jpg                                                                              '
,'https://imgsa.baidu.com/forum/w%3D580/sign=c9ad51aec895d143da76e42b43f18296/c307c33d70cf3bc714377041d100baa1cd112a72.jpg                                                                              '
,'https://imgsa.baidu.com/forum/w%3D580/sign=8538ca3ad933c895a67e9873e1127397/db306d09c93d70cfb1db17a0f8dcd100baa12b0c.jpg                                                                              '
,'https://imgsa.baidu.com/forum/w%3D580/sign=a3fc78823a292df597c3ac1d8c305ce2/a8d99b2397dda1449a26d11fb2b7d0a20cf4867a.jpg                                                                              '
,'https://imgsa.baidu.com/forum/w%3D580/sign=34d2f1ac0a55b3199cf9827d73a88286/364bdc88d43f87943fd3f583d21b0ef41bd53a79.jpg                                                                              '
,'https://imgsa.baidu.com/forum/w%3D580/sign=ddb3458c728b4710ce2ffdc4f3cfc3b2/3d2bb6315c6034a839cd052ccb1349540923767a.jpg                                                                              '
,'https://imgsa.baidu.com/forum/w%3D580/sign=1764cb348226cffc692abfba89004a7d/d910d81b0ef41bd50d4f555951da81cb39db3d09.jpg                                                                              '
,'https://imgsa.baidu.com/forum/w%3D580/sign=b23191a36b63f6241c5d390bb745eb32/8c361530e924b899e92f63a26e061d950a7bf623.jpg                                                                              '
,'https://imgsa.baidu.com/forum/w%3D580/sign=442bc46eb74543a9f51bfac42e168a7b/239aaec27d1ed21bf9c6347fad6eddc451da3f2f.jpg                                                                              '
,'https://imgsa.baidu.com/forum/w%3D580/sign=7910e0561e178a82ce3c7fa8c602737f/aafa11d5ad6eddc4aaecae6139dbb6fd5266332b.jpg                                                                              '
,'https://imgsa.baidu.com/forum/w%3D580/sign=f5eeaeda377adab43dd01b4bbbd6b36b/3325de0735fae6cd767eb6930eb30f2443a70f03.jpg                                                                              '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C496%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C504/sign=3657ff4ad53f8794d3ff4826e2206d84/07c276d98d1001e99d1308fdb90e7bec54e79727.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C558%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C566/sign=a8cabf1fa044ad342ebf878fe0996f84/22163c7adab44aed179aa316b21c8701a08bfb7e.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C294%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C302/sign=1e05afda377adab43dd01b4bbbefd06c/0388c3177f3e67092f21590d3ac79f3df8dc5529.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C270%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C278/sign=5e7c0966472309f7e76fad1a42356f83/3a5f05b30f2442a7c805e157d043ad4bd01302c2.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C392%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C400/sign=13a537d58b82b9013dadc33b43b6ca07/2685ac1ea8d3fd1f9d6dbec8314e251f94ca5fee.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C294%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C302/sign=64432a8d79f0f736d8fe4c093a6ed069/f2409858d109b3de53a5f89acdbf6c81800a4c3c.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C428%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C436/sign=9caa8693f2deb48ffb69a1d6c0245959/f1f5b8fb43166d222e1a0966472309f79152d2e5.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C554%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C562/sign=ad96be1fa044ad342ebf878fe0996f84/8a7d81d4b31c87019d3eae14267f9e2f0608ff42.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C554%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C562/sign=bcb2b92d77c6a7efb926a82ecdc1cc21/04e202fa513d2697024d14af54fbb2fb4216d8b0.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C578%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C586/sign=122e1345e850352ab161250063789882/4fcabd4543a98226e72137d58b82b9014b90eb6a.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C679%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C687/sign=1bb6f8d172f082022d9291377bc0989d/34e17cc6a7efce1b2bebd438ae51f3deb58f650a.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C294%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C302/sign=2b457981faf2b211e42e8546fabb0648/8a7d81d4b31c87019af6ad14267f9e2f0608ff8a.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C730%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C738/sign=8c1ce04264380cd7e61ea2e5917fce44/2fdab91c8701a18bbbb40dbd9f2f07082938fef7.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C379%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C387/sign=c9b7a8c05bafa40f3cc6ced59b5f603f/59f4a551f3deb48f3613be2cf11f3a292cf578dc.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C700%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C708/sign=7439e32814ce36d3a20483380ac859f7/ee9efc03738da977169e99d9b151f8198718e399.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C718%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C726/sign=bd83ddf4aec379317d688621dbffd435/183f566034a85edf48c2e1d148540923dc547580.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C553%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C561/sign=67ed1f38e7cd7b89e96c3a8b3f1f21d7/41d3ed1190ef76c61405e4d99c16fdfaae51677f.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C768%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C776/sign=752c6152f703738dde4a0c2a8320d321/795a5c4e9258d1097ff3b740d058ccbf6c814d3a.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C804%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C812/sign=3b4e22e1dc54564ee565e43183e5fff2/cf6e06338744ebf868567acdd8f9d72a6059a72f.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C330%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C338/sign=9144b2e7bd315c6043956be7bd8aa863/522a61600c3387449a42318e500fd9f9d62aa04f.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C689%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C697/sign=8133ddc1728da9774e2f8623806a9b69/ad2dd754564e92581aaa981c9d82d158cdbf4eb0.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C478%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C486/sign=3cfc7881faf2b211e42e8546fabb0648/2e8cb3014a90f6035f4982b53812b31bb151ed51.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C451%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C459/sign=9564273630adcbef01347e0e9c944dad/4d2ab299a9014c082bc036570b7b02087af4f453.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C576%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C584/sign=f6f1d72faa64034f0fcdc20e9ff81a41/30e0fa1f3a292df55df4b5e7bd315c6034a8731f.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C458%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C466/sign=6cf1acc3a08b87d65042ab1737334b48/33043a4e251f95ca0e258c44c8177f3e6609527a.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C668%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C676/sign=433e5e494610b912bfc1f6f6f3c69f73/371dba7eca80653882f8bde196dda144ac3482c4.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C277%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C285/sign=412553fc6609c93d07f20effaf069bac/9124cc5c1038534373c09ed39213b07ecb8088c7.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C228%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C236/sign=ffbf4e1bf3d3572c66e29cd4ba280057/580d9845d688d43f72fa88007c1ed21b0ff43bfb.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580/sign=24841c8c241f95caa6f592bef9167fc5/34e17cc6a7efce1b2e98d138ae51f3deb58f659b.jpg                                                                              '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C512%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C520/sign=015eea9e113853438ccf8729a328d30e/5c178c18367adab47e9902b18ad4b31c8601e481.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C708%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C716/sign=3f78766da50f4bfb8cd09e5c33741b80/30e0fa1f3a292df55d84b5e7bd315c6035a8738f.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580/sign=41a4de11562c11dfded1bf2b53266255/ae5bb919ebc4b74560d4aee4cefc1e178b821589.jpg                                                                              '
,'https://imgsa.baidu.com/forum/w%3D580/sign=b30d90fcb03533faf5b6932698d1fdca/92df252eb9389b50e517f9a08435e5dde6116e62.jpg                                                                              '
,'https://imgsa.baidu.com/forum/w%3D580/sign=07c0d0dd4034970a47731027a5cbd1c0/213befdde71190efd9d58a2dcf1b9d16fdfa6020.jpg                                                                              '
,'https://imgsa.baidu.com/forum/w%3D580/sign=224ede1cb58f8c54e3d3c5270a282dee/371dba7eca80653881c8bce196dda144ad348234.jpg                                                                              '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C193%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C201/sign=531f40e04e4a20a4311e3ccfa069fb52/e6a9d333c895d143bd42fcd172f082025aaf071d.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C483%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C491/sign=af793617ac6eddc426e7b4f309e0d58d/d8d7871001e9390180b295cc7aec54e737d1969a.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C483%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C491/sign=a4ffe17d6d81800a6ee58906810e508a/f501d3f9d72a6059508af9e82934349b023bbabc.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C299%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C307/sign=44f752fc6609c93d07f20effaf069bac/371dba7eca8065388137bce196dda144ac348275.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C668%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C676/sign=3dd5bac8314e251fe2f7e4f097bdaa67/9095093b5bb5c9ea692f1b11d439b6003bf3b376.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C483%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C491/sign=0001b9e9d50735fa91f04eb1ae6a6cc3/3f5e45c2d56285354ec4c9d391ef76c6a7ef632e.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C483%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C491/sign=fe9088dca9d3fd1f3609a2320075466f/a73551b5c9ea15ce4ac8fbfbb7003af33a87b228.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C294%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C302/sign=fd7f2cca7af40ad115e4c7eb671772af/239aaec27d1ed21bf9f03517ac6eddc451da3f11.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C483%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C491/sign=4d5c20361ad5ad6eaaf964e2b1f05aab/07c276d98d1001e9a6460ffdb90e7bec55e797dc.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C483%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C491/sign=412e273591529822053339cbe7f118bb/3325de0735fae6cd7c84b0930eb30f2442a70f19.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C718%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C726/sign=840fabf7e4dde711e7d243fe97d4ad6b/2e1d692762d0f703c0e28e2e09fa513d2797c5fa.jpg                 '
,'https://imgsa.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C403%3Bap%3D%CB%EF%C7%ED%B0%C9%2C90%2C411/sign=9c8832570b7b02080cc93fe952e291a3/580d9845d688d43f751a8b007c1ed21b0ff43b9b.jpg ']

print len(urlList)
# 下载图片
# for url in urlList:
#     urllib.urlretrieve(url,  'D:\\09_software\\85_python-3.6.6-amd64\\Iprojects\\HelloWorld\\img\\%s.jpg' % time.time())

#根据图片链接列表，把图片保存到本地
# i= 0
# for url in urlList:
#     f = open('D:\\09_software\\85_python-3.6.6-amd64\\Iprojects\\HelloWorld\\img\\%s.jpg' % str(i),"wb")    #打开文件
#     req = urllib.urlopen(url)
#     buf = req.read()              #读出文件
#     f.write(buf)                  #写入文件
#     i += 1
book = xlsxwriter.Workbook('pict.xlsx')
sheet = book.add_worksheet('sheet')
sheet.write_row(0,0,['xuhao','miaosu','tupian'])

# sheet.write_row(1, 0, str(1))
# sheet.write_row(1, 1, 'dd'+str(1))
# sheet.insert_image(1,2,'D:\\09_software\\85_python-3.6.6-amd64\\Iprojects\\HelloWorld\\img\\%s.jpg' % str(0))
#
# sheet.write_row(2, 0, str(1))
# sheet.write_row(2, 1, 'dd'+str(1))
# sheet.insert_image(2,2,'D:\\09_software\\85_python-3.6.6-amd64\\Iprojects\\HelloWorld\\img\\%s.jpg' % str(1))

len = len(urlList)
i = 0
for url in urlList:
    if(i< 11):
         j = i+1
         sheet.write_row(j, 0, str(i+1))
         sheet.write_row(j, 1, str(j))
         addr = 'D:\\09_software\\85_python-3.6.6-amd64\\Iprojects\\HelloWorld\\img\\' + str(i) + '.jpg'
         sheet.insert_image(j,2,addr)
         i +=1
book.close()












#京东商品销量排行 2020.7.21
#我的个人网站:jiaokangyang.com

import urllib.request
import urllib.parse
from pyquery import PyQuery as pq
#转换编码并将链接中字符替换掉
shuru=input('此程序为查询京东商品排行!\n请输入要查询的关键字：\n')
shuru=urllib.parse.quote(shuru)

#选择搜索结果的排序方式
guize=input('请选择结果排序方式用数字0~5代表：\n0代表综合，1代表价格由高到低，2代表价格由低到高，3代表销量，4代表评价数，5代表新品：\n')
guize=int(guize)
if guize == 0:
    psort = ''
elif guize == 1:
    psort = '&psort=1'
elif guize == 2:
    psort = '&psort=2'
elif guize == 3:
    psort = '&psort=3'
elif guize == 4:
    psort = '&psort=4'
elif guize == 5:
    psort = '&psort=5'

print(psort)
headers = {
    'user-agent':' Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400',

}
#链接中psort为商品排行条件，3代表销量，4代表评论数，5代表新品，2代表价格升序，1代表价格降序，综合则没有此参数
url="https://search.jd.com/Search?keyword="+shuru+"&wq="+shuru+psort+"&click=0"
print('查询链接为：%s'%(url))
response=urllib.request.Request(url,headers=headers)
response=urllib.request.urlopen(response)
#上述步骤已经拿到单个网页的源码，后面则进行分析提取有用数据。
#用pyquery库对源码处理，然后利用CSS提取所需的信息
res=pq(response.read().decode('utf-8'))
lis=res('.gl-warp.clearfix .gl-i-wrap').items()
i=1
for li in lis:
    ming=li('.p-name em').text()
    jia=li('.p-price strong i').text()
    print("第 %d 名\n%s"%(i,ming))
    print('价格：￥%s\n\n'%(jia))
    i=i+1
    if i==11:
        break

input('输入任意字符退出')

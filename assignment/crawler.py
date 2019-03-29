from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#db = pymysql.connect("localhost", "root", "root", "news",use_unicode=True, charset="utf8")
#cursor = db.cursor()

#print(soup)


def news_crawler():
    for i in range(3):
        url_i='https://edition.cnn.com/search/?size=10&q=%20Donald%20trump&page='+str(i+1)
        driver = webdriver.PhantomJS(executable_path='D:/phantomjs-2.1.1-windows/bin/phantomjs.exe')
        driver.get(url_i)
        #print(url_i)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for news in soup.select('h3'):
            title=news.select('a')[0].text
            list_t.append(title)

            url = news.select('a')[0]['href']
            list_u.append(url)
    #for i in range(25):
        #print (i+1,list_t[i])
        #print (i+1,list_u[i])
def twitter_crawler():
    url = 'https://twitter.com/realDonaldTrump'
    dcap = dict(DesiredCapabilities.PHANTOMJS)

    dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36")

    driver = webdriver.PhantomJS(executable_path='D:/phantomjs-2.1.1-windows/bin/phantomjs.exe',
                                 desired_capabilities=dcap)
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # print(soup)

    for texts in soup.select('.js-tweet-text-container'):
        tweet = texts.select('p')[0].text
        list_p.append(tweet)

    for count in soup.select('.ProfileTweet-actionCount'):
        num = count.attrs['data-tweet-stat-count']
        if (int(num)>10000): # if the number of "favorate" is over 100000, we can label the post as "hot"
            #print(num)
            list_l.append('hot')
        else:
            list_l.append('-')
    #for i in range(20):
        #print (i+1,list_p[i],list_l[i])

def outputhtml():
    fout= open('viewpage.html','w',encoding="utf-8")
    fout.write('<!DOCTYPE HTML>')
    fout.write('<html>')
    fout.write('<head><meta charset="utf-8"></head>')
    fout.write('<body>')
    fout.write('<table>')
    for i in range(10):
        fout.write("<tr>")
        fout.write("<td>%s</td>" % 'CNN news:')
        fout.write("<td>%s</td>" % list_t[i])
        fout.write("<td>%s</td>" % list_u[i].lstrip('//'))
        fout.write("<tr>")

    for i in range(10):
        fout.write("<tr>")
        fout.write("<td>%s</td>" % '@realrealDonaldTrump:')
        fout.write("<td>%s</td>" % list_p[i])
        fout.write("<td>%s</td>" % list_l[i])
        fout.write("<tr>")
    fout.write('</table>')
    fout.write('</body>')
    fout.write('</html>')

    #sql = "INSERT INTO news(title,url)VALUES ('%s', '%s')"%(str(title),str(url))
    #cursor.execute(sql)
    #db.commit()
if __name__ == "__main__":
    list_t = []  # store all the news titles from page1 to page3
    list_u = []  # store all the news urls from page1 to page3
    list_p = []  # store all the tweets which can be viewed
    list_l = []  # store the labels of the tweets: "hot" or "-"
    news_crawler()
    twitter_crawler()
    outputhtml()


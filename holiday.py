from selenium import webdriver
import matplotlib.pyplot as plt
URL='https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=1&acr=1&acq=%EA%B3%B5%ED%9C%B4&qdt=0&ie=utf8&query=%EA%B3%B5%ED%9C%B4%EC%9D%BC'
driver=webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get(url=URL)
a=driver.find_element_by_xpath('//*[@id="dss_free_uio_cont1"]')
d=a.text.split('\n')
day=[]
name=[]
month=[]
holiday=dict()
for i in range(1,len(d),3):
    name.append(d[i])
for i in range(2,len(d),3):
    day.append(d[i])
for i in range(3,len(d),3):
    month.append(d[i])
for i in range(len(month)):
    holiday[name[i]]=[month[i]]+[day[i]]
a,b,c,d,e,f,g,h,i,j,k,l=0,0,0,0,0,0,0,0,0,0,0,0
for day,info in holiday.items():
    info=info[1].split()
    if info[0] == '1월':
        a += 1
    if info[0]== '2월':
        b += 1
    if info[0] == '3월':
        c += 1
    if info[0] == '4월':
        d += 1
    if info[0] == '5월':
        e += 1
    if info[0] == '6월':
        f += 1
    if info[0] == '7월':
        g += 1
    if info[0] == '8월':
        h += 1
    if info[0] == '9월':
        i += 1
    if info[0] == '10월':
        g += 1
    if info[0] == '11월':
        k += 1
    if info[0] == '12월':
        l += 1
holiday_count=[a,b,c,d,e,f,g,h,i,j,k,l]

URL='https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=2020+%EA%B3%B5%ED%9C%B4%EC%9D%BC&oquery=%EA%B3%B5%ED%9C%B4%EC%9D%BC&tqi=h6M3EdprvhGssgkn0UVssssssPN-463500'
driver=webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get(url=URL)
table=driver.find_elements_by_class_name('tb_box')
holiday2020=[]
for line in table:
    holiday=line.find_elements_by_tag_name('p')
    for k in range(1,len(holiday),3):
        i=holiday[k].get_attribute('innerHTML')
        holiday2020.append(i)
holiday2020=holiday2020[:12]
jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec=0,0,0,0,0,0,0,0,0,0,0,0
for day in holiday2020:
    if day[0]=='1':
        if day[1]=='0':
            oct+=1
        elif day[1]=='1':
            nov+=1
        elif day[1]=='2':
            dec+=1
        else:
            jan+=1
    elif day[0]=='2':
        feb+=1
    elif day[0]=='3':
        mar+=1
    elif day[0]=='4':
        apr+=1
    elif day[0]=='5':
        may+=1
    elif day[0]=='6':
        jun+=1
    elif day[0]=='7':
        jul+=1
    elif day[0]=='8':
        aug+=1
    elif day[0]=='9':
        sep+=1
holiday2020_count=[jan+3,feb,mar,apr,may,jun,jul,aug,sep+2,oct,nov,dec]
driver.close()

x=[1,2,3,4,5,6,7,8,9,10,11,12]
plt.plot(x,holiday_count)
plt.plot(x,holiday2020_count)
plt.legend(['holiday of 2021','holiday of 2020'])
plt.xlabel('month')
plt.ylabel('count of holiday')
plt.suptitle('count of holiday in 2021 and 2020')
plt.show()
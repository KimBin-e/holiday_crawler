from selenium import webdriver
URL='https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=1&acr=1&acq=%EA%B3%B5%ED%9C%B4&qdt=0&ie=utf8&query=%EA%B3%B5%ED%9C%B4%EC%9D%BC'
driver=webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get(url=URL)
a=driver.find_element_by_xpath('//*[@id="dss_free_uio_cont1"]')
print(a)
print(a.text)
d=a.text.split('\n')
print(d)

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
    print(day,'-',info)
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
print(holiday_count)

for i in range(12):
    print(str(i+1),'월 공휴일 수:',holiday_count[i],'개')

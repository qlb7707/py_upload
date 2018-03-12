#coding:utf-8
import requests
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')
 

f = open('./input','rt')
lines = f.readlines()
f.close()


files={'studyStartDate':(None,''),
    'studyTimeId':(None,'am'),
    'doctorName':(None,'匡锡菲'),
    'doctorFlow':(None,'c7e632d9793b41aa91c2ee8061fb5140'),
    'teacherName':(None,'陈坚志'),
    'teacherFlow':(None,'d612acad4e3f40e3b765e3cbc06ec2ee'),
    'experienceContent':(None,'见附件'),
    'studentSignTime':(None,''),
    'files':(),
    'files2':(),
    'auditContent':(None,''),
    'auditTime':(None,'')
 }
 
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer':'http://jszy.ezhupei.com/pdsci/res/discipleNote/showDiscipleNoteInfo/doctor/Note?doctorFlow=c7e632d9793b41aa91c2ee8061fb5140&discipleTeacherFlow=d612acad4e3f40e3b765e3cbc06ec2ee',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cookie':'JSESSIONID=B696DD3BFC69F8B84C33158C6BD6E704.tomcat4040; UM_distinctid=161f651253511bf-0e49bd96c770b9-32637b06-13c680-161f6512536ea6'
}

url = 'http://jszy.ezhupei.com/pdsci/res/discipleNote/saveDiscipleNoteInfo/doctor/Note?jsonData=%257B%2522fileFlows%2522:%255B%255D%257D'
 
date = []

for line in lines:
    y,m,d,i = line.strip('\n').split('_')
    date_str = '%04d_%02d_%02d'%(int(y),int(m),int(d))
    if date_str not in date:
        date.append(date_str)

for date_item in date:
    y,m,d = date_item.split('_')
    date_str = "%04d年%02d月%02d日"%(int(y),int(m),int(d))
    files['studyStartDate'] = (None,date_str)
    files['files'] = (date_item+'_1.jpg',open(date_item+'_1.jpg','rb'),'image/jpeg')
    files['files2'] = (date_item+'_2.jpg',open(date_item+'_2.jpg','rb'),'image/jpeg')
    response=requests.post(url,files=files,headers=headers)
    html = response.text
    print html
    time.sleep(5)



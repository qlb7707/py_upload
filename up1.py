#coding=utf-8
import requests
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')
 

f = open('./input.txt','rt')
lines = f.readlines()
f.close()


name_dict = {
'1':'张三','2':'刘志丹','3':'吴宇','4':'周梓辰','5':'张亚辉','6':'张茜',
'7':'徐乔凯','8':'方瑶','9':'朱羽芯','10':'朱鸠','11':'李冉冉','12':'李易峰',
'13':'李浴同','14':'李芷晗','15':'杨成','16':'杨爽','17':'王丹',
'18':'田语橙','19':'盛熙芸','20':'秦佳栋','21':'穆远妮','22':'苏君莹','23':'薛华',
'24':'谢君豪','25':'谢海宁','26':'赵琪','27':'郑俊杰','28':'陈可儿','29':'陈玥琳','30':'马克'
}


files={'peopleName':(),
    'sexId':(),
	'birthDate':(),
	'visitDate':(),
	'visitActionId':(None,'chuzhen'),
	'solarTerms':(None,'见附件'),
	'mainSuit':(None,'见附件'),
	'presentDiseaseHistory':(None,'见附件'),
	'previousDiseaseHistory':(None,'见附件'),
	'allergicHistory':(None,'见附件'),
	'physicalExamination':(None,'见附件'),
	'accessoryExamination':(None,'见附件'),
	'tcmDiagnosis':(None,'见附件'),
	'syndromeDiagnosis':(None,'见附件'),
	'westernDiagnosis':(None,'见附件'),
	'therapy':(None,'见附件'),
	'prescription':(None,'见附件'),
	'returnVisit':(None,'见附件'),
	'experienceContent':(None,'见附件'),
    'auditContent':(None,''),
    'teacherName':(None,''),
    'auditTime':(None,'')
 }
 
 
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer':'http://jszy.ezhupei.com/pdsci/res/typicalCases/showTypicalCases',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
    'Cookie':'JSESSIONID=D4F3C9D214F298D2A32D0116D9A71048.tomcat4040; UM_distinctid=161f651253511bf-0e49bd96c770b9-32637b06-13c680-161f6512536ea6'
}

url = 'http://jszy.ezhupei.com/pdsci/res/typicalCases/editTypicalCase?recordFlow=&jsonData=%257B%2522fileFlows%2522:%255B%255D%257D'
 
cases = []

for line in lines:
    print line 
    n,s,d1,d2,a,t = line.strip('\n').split('_')
    case_str = '%s_%s_%s_%s_%s'%(n,s,d1,d2,a)
    if case_str not in cases:
        cases.append(case_str)


for case_item in cases:
    nameid,sex,date1,date2,action = case_item.split('_')
    files['peopleName'] = (None,name_dict[nameid])
    files['sexId'] = (None,sex)
    files['birthDate'] = (None,date1)
    files['visitDate'] = (None,date2)
    print case_item + '_1.jpg'
    files['files'] = ('1.jpg',open(case_item+'_1.jpg','rb'),'image/jpeg')
    files['files2'] = ('2.jpg',open(case_item+'_2.jpg','rb'),'image/jpeg')
    response=requests.post(url,files=files,headers=headers)
    html = response.text
    print html
    time.sleep(5)
    break



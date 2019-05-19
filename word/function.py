#from django.http import HttpResponse
from django.shortcuts import render
import pymysql

def home(request):
	return render(request, 'home.html')

def demo(request):
	user_text = request.GET['text']
	total_count = len(user_text)
	dict1 = {}
	for word in user_text:
		if word not in dict1:
			dict1[word] = 1
		else:
			dict1[word] += 1
	sorted(dict1.items())
	return render(request, 'cun.html', {'count': total_count, 'text': user_text, 'dicr':dict1})

def sub(request):
	name = request.GET['stuname']
	phone = request.GET['stutel']
	email = request.GET['stuemail']
	stuno = request.GET['stunum']
	conn = pymysql.connect(host='192.168.116.101',
						   user='root',
						   password='root123',
						   db='test',
						   charset='utf8',
						   )
	cur = conn.cursor()
	sql = "insert into biaodan(姓名,电话,邮箱,学号) values (%s,%s,%s,%s)"
	cur.execute(sql,  [name, phone, email, stuno])
	conn.commit()
	cur.close()
	conn.close()
	return render(request, 'results.html', {'name': name, 'phone': phone, 'email': email, 'stuno': stuno})


from shiksha import login, shiksha_url
import getpass, lxml.html
username = input('Username: ')
password = getpass.getpass()
session = login(username, password)
response = session.get(shiksha_url+'/asgn/app/course/25/questions/')
table = lxml.html.fromstring(response.text).xpath('//div[@class="button-group small"]')
my_sum, tot_sum = [0,0]
print('my marks\t  total marks')
for row in table:
	grade = row[2].items()[0]
	if grade[0] == 'href':
		response = session.get(shiksha_url+grade[1])
		marks = lxml.html.fromstring(response.text).xpath('//div[@class="row card-row"]')
		rawmarks = marks[0].text_content().replace(' ','').split('\n')
		rawmarks = list(filter(None, rawmarks))
		if rawmarks[1] == 'Notavailableyet.':
			print('not evaluated')
			continue
		my_marks = float(rawmarks[1].split(':')[1])
		tot_marks = float(rawmarks[2].split(':')[1])
		my_sum += my_marks
		tot_sum += tot_marks
		print(my_marks,'\t\t',tot_marks)
	else:
		print('not evaluated')
print('____________________________\n',my_sum,'\t\t',tot_sum)
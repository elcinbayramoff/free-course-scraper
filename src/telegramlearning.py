import telebot
import csv
TOKEN = 'YOUR_TOKEN'
Channel_id = 0
path_to_csv = '~src\\courses.csv'
bot = telebot.TeleBot(TOKEN, parse_mode=None)
def correcter(a):
	A=[]
	n=0
	for i in range(len(a)):
		if a[i] in ['*','_']:
			A.append(i)
	for i in A:
		a=a[:i+n]+'\\'+a[n+i:]
		n+=1
	return a
def link_editor(a):
    n = a.find('https://www.udemy.com/course')
    return a[n:]
remaining = 0
@bot.message_handler(commands=['show'])
def choose_one(message):
	global remaining
	with open(path_to_csv) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		x=int(message.text.split()[-1])
		if message.text.split()[-2] == 'another':
			y = x + remaining
			for row in csv_reader:
				if line_count==0:
					line_count+=1
					pass
				elif line_count>remaining and line_count<=y:
					bot.send_message(message.chat.id,f'{line_count}. {correcter(row[1])}\n{correcter(row[6])} ',parse_mode= 'Markdown' )
					line_count+=1
				elif line_count <=remaining:
					line_count+=1
				else:
					remaining = y
					break
		else:
			remaining = 0
			for row in csv_reader:
				if line_count<=x:
					if line_count==0:
						line_count+=1
						pass
					else:
						bot.send_message(message.chat.id,f'{line_count}. {correcter(row[1])}\n{correcter(row[6])} ',parse_mode= 'Markdown' )
						line_count+=1
				else:
					remaining = x
					break
@bot.message_handler(commands=['start'])
def send_welcome(message):
	row=[]
	language=''
	with open(path_to_csv) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		n=0
		x=int(message.text.split()[-1])
		for row in csv_reader:
			if n==x:
				break
			n+=1
			if n==0:
				bot.send_message(message.chat.id,f'Error',parse_mode= 'Markdown' )
			else:
				if row[0]=='Turkish':
					language='Türkcə'
				if row[0]=='English':
					language='İngiliscə'
				bot.send_message(Channel_id,f'*TƏCİLİ! Bu prestijli kurs yenidən qısa müddətlik pulsuz oldu!*\n\n*{correcter(row[1])}*\n\nQısa məlumat:* {correcter(row[2])}*\n\n*Şagird sayı:*{correcter(row[4])}\n\n*Dil:* {language}\n\n*Təlimçi:* {correcter(row[5])}\n\n*Qeydiyyat linki:*\n{link_editor(correcter(row[6]))}\n\n*Qeyd. Kursların pulsuz olma müddəti limitlidir. Tələsin ki, qaçırmayasınız!\n\nBizə dəstək olmaq üçün kanalımızı paylaşmağı unutmayın*➡️@digitoloq\n-----------------------------------------------------\n',parse_mode= 'Markdown' )	
bot.infinity_polling()

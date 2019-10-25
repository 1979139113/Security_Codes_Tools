# coding:utf-8
import requests
data = {'guid': '38522b83-8893-4ca6-b45f-b6588b034462',
'host': 'langzi.fun',
'ishost': '0',
'encode': '1TW3niJwYhGc2K0HW7dcetgnKIZY/UmJ',
'checktype': '0'}

r = requests.post(url='http://ping.chinaz.com/langzi.fun',data=data)
print r.content
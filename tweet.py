#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tweet.py
#  coded by @magic_coding (icoder@mail.com)

print """______        _                     _   
| ___ \      | |                   | |  
| |_/ /   _  | |___      _____  ___| |_ 
|  __/ | | | | __\ \ /\ / / _ \/ _ \ __|
| |  | |_| | | |_ \ V  V /  __/  __/ |_ 
\_|   \__, |  \__| \_/\_/ \___|\___|\__|
       __/ |                            
      |___/                             
"""
print '  _______________________________________________  \n'
print '           Coded by Mahmoud AL-Nafei             '
print '           Twitter: @magic_coding                  '
print '  _______________________________________________  \n\n'

import tweepy, time

API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxx'
API_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN = 'xxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

def CheckData():
	for x in [API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]:
		if not x:
			print "[!] Please add "+x+" first."
			break
		else:
			pass
	else:
		print "[+] API => [OK]"
		print "[+] Try to access Twitter API.."
		Tweet()


def Tweet():
	auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)
	if api:
		tweet_message = raw_input("[?] Tweet something: ")
		if len(tweet_message) <= 144:
			print '\n[+]Try to tweet now...\n'
			time.sleep(1)
			send_tweet = api.update_status(tweet_message)
			if send_tweet:
				print '\n[+] Tweet has been sent successfully.\n'
			else:
				print "[!] Error, Try again please."
		else:
			print "[!] Tweet more than 144 character."
	else:
		print "[!] Error with access token."



while True:
	print "Please try to tweet something now..\n"
	try:
		CheckData()
	except KeyboardInterrupt:
		print "\nprogram exit.."
		exit()
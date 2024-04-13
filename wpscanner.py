import requests,json,re,time
from random import randint
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
import os
from datetime import datetime

#color code

fr  =   Fore.YELLOW
fm  =   Fore.MAGENTA											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE											
fg  =   Fore.GREEN
fy	=	Fore.YELLOW	
fb	=	Fore.BLUE										
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT

#Random Function
user_agent_list = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; E6653 Build/32.2.A.0.253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0; HTC One X10 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.3","Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1","Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1","Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15","Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1","Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1","Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A5370a Safari/604.1","Mozilla/5.0 (iPhone9,3; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1","Mozilla/5.0 (iPhone9,4; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1","Mozilla/5.0 (Apple-iPhone7C2/1202.466; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3","Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254","Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536","Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058","Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36","Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36","Mozilla/5.0 (Linux; Android 4.4.3; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/47.1.79 like Chrome/47.0.2526.80 Safari/537.36","Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020c Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246","Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36","Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1","Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36","Roku4640X/DVP-7.70 (297.70E04154A)","Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30","Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)","AppleTV6,2/11.1","AppleTV5,3/9.1.1","Mozilla/5.0 (Nintendo WiiU) AppleWebKit/536.30 (KHTML, like Gecko) NX/3.0.4.2.12 NintendoBrowser/4.3.1.11264.US","Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393","Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586","Mozilla/5.0 (PlayStation 4 3.11) AppleWebKit/537.73 (KHTML, like Gecko)","Mozilla/5.0 (PlayStation Vita 3.61) AppleWebKit/537.73 (KHTML, like Gecko) Silk/3.2","Mozilla/5.0 (Nintendo 3DS; U; ; en) Version/1.7412.EU","Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)","Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)","Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)","Mozilla/5.0 (X11; U; Linux armv7l like Android; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Version/5.0 Safari/533.2+ Kindle/3.0+","Mozilla/5.0 (Linux; U; en-US) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/528.5+) Version/4.0 Kindle/3.0 (screen 600x800; rotate)"]
RANDOM_USER_AGENT = user_agent_list[randint(0,52)]


def scan(target,f):
    
    kepala = {
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"accept-encoding": "gzip, deflate, br",
	"accept-language": "en,en-US;q=0.9",
	"cache-control": "max-age=0",
	"dnt": "1",
	"sec-ch-ua-mobile": "?0",
	"sec-fetch-dest": "document",
	"sec-fetch-mode": "navigate",
	"sec-fetch-site": "none",
	"sec-fetch-user": "?1",
	"upgrade-insecure-requests": "1",
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
	}
    
    config = {
	"/.wp-config.php.swp",
	"/wp-config.inc",
	"/wp-config.old",
	"/wp-config.txt",
	"/wp-config.html",
	"/wp-config.php.bak",
	"/wp-config.php.dist",
	"/wp-config.php.inc",
	"/wp-config.php.old",
	"/wp-config.php.save",
	"/wp-config.php.swp",
	"/wp-config.php.txt",
	"/wp-config.php.zip",
	"/wp-config.php.html",
	"/wp-config.php~",
	"/wp-admin/.wp-config.php.swp",
	"/wp-admin/wp-config.inc",
	"/wp-admin/wp-config.old",
	"/wp-admin/wp-config.txt",
	"/wp-admin/wp-config.html",
	"/wp-admin/wp-config.php.bak",
	"/wp-admin/wp-config.php.dist",
	"/wp-admin/wp-config.php.inc",
	"/wp-admin/wp-config.php.old",
	"/wp-admin/wp-config.php.save",
	"/wp-admin/wp-config.php.swp",
	"/wp-admin/wp-config.php.txt",
	"/wp-admin/wp-config.php.zip",
	"/wp-admin/wp-config.php.html",
	"/wp-admin/wp-config.php~",
	"/wp-content/.wp-config.php.swp",
	"/wp-content/wp-config.inc",
	"/wp-content/wp-config.old",
	"/wp-content/wp-config.txt",
	"/wp-content/wp-config.html",
	"/wp-content/wp-config.php.bak",
	"/wp-content/wp-config.php.dist",
	"/wp-content/wp-config.php.inc",
	"/wp-content/wp-config.php.old",
	"/wp-content/wp-config.php.save",
	"/wp-content/wp-config.php.swp",
	"/wp-content/wp-config.php.txt",
    "/wp-content/wp-config.php.zip",
	"/wp-content/wp-config.php.html",
	"/wp-content/wp-config.php~",
	"/wp-includes/.wp-config.php.swp",
	"/wp-includes/wp-config.inc",
	"/wp-includes/wp-config.old",
	"/wp-includes/wp-config.txt",
	"/wp-includes/wp-config.html",
	"/wp-includes/wp-config.php.bak",
	"/wp-includes/wp-config.php.dist",
	"/wp-includes/wp-config.php.inc",
	"/wp-includes/wp-config.php.old",
	"/wp-includes/wp-config.php.save",
	"/wp-includes/wp-config.php.swp",
	"/wp-includes/wp-config.php.txt",
	"/wp-includes/wp-config.php.zip",
	"/wp-includes/wp-config.php.html",
	"/wp-includes/wp-config.php~"
	}
    log = {
	'/debug.log',
	'/wp-content/debug.log',
	'/wp-admin/debug.log',
	'/wp-includes/debug.log'
	}
    user = {
	'/wp-json/wp/v2/users',
	'/?rest_route=/wp/v2/users'
	}

    
    
	#Denial Of Service
    try:
        r1 = requests.get('{}/wp-admin/load-styles.php?&load=common'.format(target), headers=kepala, verify=False)
        if r1.status_code == 200:
            print('{}[INFO] {}{} {} -> OK! Denial of Service in load-styles.php'.format(fc, fw, target, fg))
            f.write('\n[INFO] {} -> OK! Denial of Service in load-styles.php'.format(target))
        elif 'auto-generated' in r1.text:
            print('{}[INFO] {}{} {} -> OK! Denial of Service in load-styles.php'.format(fc, fw, target, fg))
            f.write('\n[INFO] {} -> OK! Denial of Service in load-styles.php'.format(target))
        else:
            print('{}[INFO] {}{} {} -> Not Vuln Denial of Service in load-styles.php'.format(fc, fw, target, fr))
            f.write('\n[INFO] {} -> Not Vuln Denial of Service in load-styles.php'.format(target))
    except:
        print('{}[INFO] {}{} {} -> Not Vuln Denial of Service in load-styles.php'.format(fc, fw, target, fr))
        f.write('\n[INFO] {} -> Not Vuln Denial of Service in load-styles.php'.format(target))
    try:
        r2 = requests.get('{}/wp-admin/load-scripts.php?load=react'.format(target), headers=kepala, verify=False)
        
        if r2.status_code == 200:
            print('{}[INFO] {}{} {} -> OK! Denial of Serice in load-scripts.php'.format(fc, fw, target, fg))
            f.write('\n[INFO] {} -> OK! Denial of Serice in load-scripts.php'.format(target))
        elif 'react.production.min.js' in r2.text:
            print('{}[INFO] {}{} {} -> OK! Denial of Serice in load-scripts.php'.format(fc, fw, target, fg))
            f.write('\n[INFO] {} -> OK! Denial of Serice in load-scripts.php'.format(target))
        else:
            print('{}[INFO] {}{} {} -> Not Vuln Denial of Service in load-scripts.php'.format(fc, fw, target, fr))
            f.write('\n[INFO] {} -> Not Vuln Denial of Service in load-scripts.php'.format(target))
    except:
        print('{}[INFO] {}{} {} -> Not Vuln Denial of Service in load-scripts.php'.format(fc, fw, target, fr))
        f.write('\n[INFO] {} -> Not Vuln Denial of Service in load-scripts.php'.format(target))



    # Logs file exposed
    
    for a in log:
        logs = a.strip()
    try:
        r3 = requests.get('{}{}'.format(target, logs), headers=kepala, verify=False)
        
        if r3.status_code == 200:
            print('{}[INFO] {}{} {} -> OK! Logs file found!'.format(fc, fw, target, fg))
            f.write('\n[INFO] {} -> OK! Logs file found!'.format(target))
        else:
            print('{}[INFO] {}{} {} -> Not found Logs file'.format(fc, fw, target, fr))
            f.write('\n[INFO] {} -> Not found Logs file'.format(target))
    
    except:
        print('{}[INFO] {}{} {} -> Not found Logs file'.format(fc, fw, target, fr))
        f.write('\n[INFO] {} -> Not found Logs file'.format(target))



    # Backup wp-config exposed
    
    for b in config:
        configs = b.strip()
        
    try:
        r4 = requests.get('{}{}'.format(target, configs), headers=kepala, verify=False)
        
        if r4.status_code == 200:
            print('{}[INFO] {}{} {} -> OK! Backup WP-Config found!'.format(fc, fw, target, fg))
            f.write('\n[INFO] {} -> OK! Backup WP-Config found!'.format(target))
        else:
            print('{}[INFO] {}{} {} -> Not found Backup WP-Config'.format(fc, fw, target, fr))
            f.write('\n[INFO] {} -> Not found Backup WP-Config'.format(target))
    
    except:
        print('{}[INFO] {}{} {} -> Not found Backup WP-Config'.format(fc, fw, target, fr))
        f.write('\n[INFO] {} -> Not found Backup WP-Config'.format(target))


    # Information disclosure wordpress username
    
    for c in user:
        users = c.strip()
        
    try:
        r5 = requests.get('{}{}'.format(target, users), headers=kepala, verify=False)
        if r5.status_code == 200:
            print('{}[INFO] {}{} {} -> OK! Users Disclosure'.format(fc, fw, target, fg))
            f.write('\n[INFO] {} -> OK! Users Disclosure'.format(target))
        elif '"id"' in r5.text:
            print('{}[INFO] {}{} {} -> OK! Users Disclosure'.format(fc, fw, target, fg))
            f.write('\n#Information Disclosure Username#'+'\n'+target+users+'\n'+'\n')
        else:
            print('{}[INFO] {}{} {} -> Not found Users Disclosure'.format(fc, fw, target, fr))
            f.write('\n[INFO] {} -> Not found Users Disclosure'.format(target))
    except:
        print('{}[INFO] {}{} {} -> Not found Users Disclosure'.format(fc, fw, target, fr))
        f.write('\n[INFO] {} -> Not found Users Disclosure'.format(target))


   # Bruteforce vulnerability
   
    try:
        r6 = requests.get('{}/?author=1'.format(target), headers=kepala, verify=False)
        regex1 = re.findall('/author/(.*?)/feed/', r6.text)
        
        for gex1 in regex1:
            ex1 = gex1
        
        datalogin = {
		"log": ex1,
		"pwd": "test",
		"wp-submit": "Log In",
		"redirect_to": target+"/wp-admin/",
		"testcookie": "1"
		}
        
        r7 = requests.post('{}/wp-login.php'.format(target), headers=kepala, data=datalogin, verify=False)
        
        if 'Lost your password?' in r7.text:
            print('{}[INFO] {}{} {} -> OK! Vuln Wordpress Bruteforce, with username : {}{}'.format(fc, fw, target, fg, fy, ex1))
            f.write('\n#Wordpress Bruteforce#'+'\n'+target+'/wp-login.php'+'\n'+'Username : '+ex1+'\n'+'\n')
        else:
            print('{}[INFO] {}{} {} -> Not Vuln Wordpress Bruteforce'.format(fc, fw, target, fr))
            f.write('\n[INFO] {} -> Not Vuln Wordpress Bruteforce'.format(target))
    
    except:
        print('{}[INFO] {}{} {} -> Not Vuln Wordpress Bruteforce'.format(fc, fw, target, fr))
        f.write('\n[INFO] {} -> Not Vuln Wordpress Bruteforce'.format(target))

     # XSPA Vulnerability
    try:
        r8 = requests.post('{}/xmlrpc.php'.format(target), headers=kepala, verify=False)
        
        if '<name>faultCode</name>' in r8.text:
            print('{}[INFO] {}{} {} -> OK! High possibility XSPA bug found!'.format(fc, fw, target, fg))
            f.write('#XSPA Vulnerabilityl#'+'\n'+target+'/xmlrpc.php'+'\n'+'\n')
        else:
            print('{}[INFO] {}{} {} -> XSPA Vulnerability not found'.format(fc, fw, target, fr))
            f.write('\n[INFO] {} -> XSPA Vulnerability not found'.format(target))
    except:
        print('{}[INFO] {}{} {} -> XSPA Vulnerability not found'.format(fc, fw, target, fr))
        f.write('\n[INFO] {} -> XSPA Vulnerability not found'.format(target))


def user_finder(new_u) :

    new_url2 = new_u+'/wp-json/wp/v2/users'
    
    headers = {"user-agent":RANDOM_USER_AGENT}
    
    r2 = requests.get(new_url2,headers=headers)
    
    if r2.status_code == 200 :
        print('{}\n[+] Enumerating usernames \n'.format(fm))
        f.write('\n[+] Enumerating usernames \n')
        time.sleep(1.3)
        data = json.loads(r2.text)
        for info in data :
            print('{}\t[*] Username Found : {}{}'.format(fw,fr,info['slug']))
            f.write('\t[*] Username Found : {}'.format(info['slug']))
            time.sleep(0.2)
    else :
            print('{}\n[-] Usernames Not Found '.format(fg))
            f.write('\n[-] Usernames Not Found ')
#--------------------------------------------

def adminpanel_finder(org_url) :
    
    urlA = org_url+'/wp-login.php?action=lostpassword&error=invalidkey'
    uagent = {"user-agent":RANDOM_USER_AGENT}
    
    r3 = requests.get(urlA,headers=uagent)

    if r3.status_code == 200 :
        r3data = r3.text
        pagesoup = BeautifulSoup(r3data,'html.parser')
        ptag = pagesoup.findAll("p",{"id":"nav"})
        
        if len(ptag) > 0 :
            for ptags in ptag :
                for atags in ptags.find_all('a') :
                    if 'Log in' in atags :
                        admin_url = atags['href']
                    else :
                        print('{}\n[-] Admin panel not found '.format(fr))
                        f.write('\n[-] Admin panel not found ')

            print('{}\n[+] Admin panel found - {}{}{}'.format(fw,fr,sn,admin_url))
            f.write('\n[+] Admin panel found - {}'.format(admin_url))
        
        else :
            print('{}\n[-] Admin panel not found '.format(fr))
            f.write('\n[-] Admin panel not found ')
    else :
        print('{}\n[-] Admin panel not found '.format(fm))
        f.write('\n[-] Admin panel not found ')



banner = """
                 █ █ █ █▀█   █▀ █▀▀ ▄▀█ █▄ █ █▄ █ █▀▀ █▀█
                 ▀▄▀▄▀ █▀▀   ▄█ █▄▄ █▀█ █ ▀█ █ ▀█ ██▄ █▀▄"""
print("{}\n\t\t\t-------------------------------------------------".format(fc,sb))

print('{}{}'.format(fg,banner))
print("{}\n\t\t\t-------------------------------------------------".format(fc,sb))

input_prompt = '{}\nWebsite Url (with https://) : {} '.format(fm,Fore.RESET)
url = input("{}{}".format(fw, input_prompt))

#url='https://demo.tipskindercare.com'

if '://' not in url:
    org_url = 'http://'+url
else:
    org_url = url
roboturl = url+'/robots.txt'
feedurl = url+'/feed'
rssurl = url+'/rss'
url = url+'/wp-json'

date = datetime.now()
tanggal = date.strftime("%d_%m_%Y %H_%M_%S")
f=open('{}.txt'.format(tanggal), 'a')
f.write("\t\t\t\t\t\tWP Scanner")
f.write("\n\n[+] Website : {}\n\n".format(org_url))

headers = {"user-agent":RANDOM_USER_AGENT}

try:
    testreq = requests.get(org_url,headers=headers)
except Exception as e:
    print('{}\nWebsite status : Error !'.format(fr,sb))
    f.write('\nWebsite status : Error !')
    
else :

    r = requests.get(url,headers=headers)
    rcode = r.status_code

    if rcode == 200 :

        print('{}\nWebsite status : {} Up'.format(fw,fg))
        f.write('\n[+] Website status : Up')

        robotres = requests.get(roboturl,headers=headers)
        feedTXT = requests.get(feedurl,headers=headers).text
        rssTXT = requests.get(rssurl,headers=headers).text
         

        if 'wp-admin' in robotres.text or 'wordpress.org' in feedTXT or 'wordpress.org' in rssTXT :
            print('{}\n[+] WordPress Detection : {} Yes'.format(fw,fg))
            f.write('\n[+] WordPress Detection : Yes')

            feedres = requests.get(feedurl,headers=headers)
            contents = feedres.text
            soup = BeautifulSoup(contents,'xml')
            wpversion = soup.find_all('generator')
            if len(wpversion) > 0 :
                wpversion = re.sub('<[^<]+>', "", str(wpversion[0])).replace('https://wordpress.org/?v=','')
                print('{}\n[+] WordPress version : {}{}'.format(fw,fr,wpversion))
                f.write('\n[+] WordPress version : {}'.format(wpversion))
            else:
                rnew = requests.get(org_url,headers=headers)
                if rnew.status_code == 200 :
                    newsoup = BeautifulSoup(rnew.text,'html.parser')
                    generatorTAGS = newsoup.find_all('meta',{"name":"generator"})
                    for metatags in generatorTAGS :     
                        if "WordPress" in str(metatags) :
                            altwpversion = metatags['content']
                            altwpversion = str(altwpversion).replace('WordPress','')
                            print('{}\n[+] WordPress version : {}{}'.format(fw,fg,altwpversion))
                            f.write('\n[+] WordPress version : {}'.format(altwpversion))
                else :
                    print('{}[-] WordPress version : Not Found !'.format(fr))
                    f.write('[-] WordPress version : Not Found !')
            time.sleep(0.8)

            data = json.loads(r.text)
            siteName = data['name']
            siteDesc = data['description']

            plugins = data['namespaces']

            print('{}\n[+] Webite name        : {}{}'.format(fw,fg,siteName))
            f.write('\n[+] Webite name        : {}'.format(siteName))
            time.sleep(0.8)
            print('{}\n[+] Webite description : {}{}'.format(fw,fg,siteDesc))
            f.write('\n[+] Webite description : {}'.format(siteDesc))
            time.sleep(0.8)
            print('{}\n[+] Enumerating Plugins : '.format(fw),end=' ')
            f.write('\n[+] Enumerating Plugins : ')
            plugins=list(set(plugins))
            print('\n')
            for i in plugins :
                elem = (i[:i.find('/')])
                print('{}\t[*] {}{}'.format(fw,fg,elem))
                f.write('\n\t[*] {}'.format(elem))
                time.sleep(0.2)

            time.sleep(1)
            adminpanel_finder(org_url)
            time.sleep(1)
            user_finder(org_url)

        else: 
            print('{}\n[+] WordPress Detection : {}No'.format(fw,fr))
            f.write('\n[+] WordPress Detection : No')
    else :
        print('{}\nWebsite status : {} Down {}'.format(fw,fr,r.reason))
        f.write('\nWebsite status : Down {}'.format(r.reason))
    print()
scan(url,f)
print()
input('{}[ End of Scanning ]'.format(fc))
f.write("\n\n\t\t\t\t\t\t[ End of Scanning ]")
f.close()

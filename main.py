## IMPORTS ##
from concurrent.futures import ThreadPoolExecutor
from httpx_socks import SyncProxyTransport
from random import choice, randint
from string import ascii_letters
from httpx import Client
from hfuck import Bypass
from time import sleep, time
from colorama import Fore
import requests, os, datetime, json, base64
## IMPORTS ##

os.system(f'cls & title Startup')

class Configuration():
    print('%s+%s Loading Proxies & Configurations %s+%s' % (Fore.LIGHTGREEN_EX, Fore.GREEN, Fore.LIGHTGREEN_EX, Fore.RESET))

#### Initial Setup Things ####
    # proxy setup stuff #
    f = open("data/proxies.txt", 'wb')
    r1 = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=5000&country=all")
    r2 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt")
    f.write(r1.content); f.write(r2.content)
    f.close()
    # proxy setup stuff #

    # config setup stuff #
    with open('config.json', 'r') as f:
        config = json.load(f)
    # config setup stuff #
#### Initial Setup Things ####
#### definitions for things ####
    proxyamount = 0
    readproxylist = open("data/proxies.txt", encoding='utf-8').readlines()
    threadworkers = ThreadPoolExecutor(max_workers=int(1000000000))
    max_threads = 500
    threads = 100 # Thread Amount
    timeout = 5
    before_alias = 'ANTI-BLACKIE GANG .' # Name
    invite_code = input("Invite Code? ") # Invite Code
    # for title #
    tknamount = 0
    cptbypassd = 0
    with open("tokens.txt", 'r') as fp: 
        ttltkns = len(fp.readlines())
    # for title #
    sleep(1)
#### definitions for things ####
    print("%s>>%s FINISHED %s<<%s" % (Fore.LIGHTBLACK_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTBLACK_EX, Fore.RESET))
    sleep(1)


def SYSTITLE():
    return f'[VTK] Accounts Created: {Configuration.tknamount} ~ Captchas Bypassed: {Configuration.cptbypassd} ^| Total Tokens: {Configuration.ttltkns}'

os.system(f'cls & title {SYSTITLE()}')

def PRELOG( type = None):
    if type == 'error':
        return f"{Fore.RED}ERROR @ {datetime.datetime.fromtimestamp(time()).strftime('%H:%M:%S')}{Fore.RESET} |"
    return f"{Fore.LIGHTBLACK_EX}INFO @ {datetime.datetime.fromtimestamp(time()).strftime('%H:%M:%S')}{Fore.RESET}  |"
    
def PRELOG2( _X):
    return f"{Fore.LIGHTBLACK_EX}INFO @ {_X}{Fore.RESET}  |"


def getproxies():
    try:
        proxylist = Configuration.readproxylist[Configuration.proxyamount]
        Configuration.proxyamount += 1
    except:
        proxylist, proxyamount = Configuration.readproxylist[0], 0
    return proxylist.replace('\n','')

def randomstring( amount):
    return ''.join(choice(ascii_letters) for i in range(amount))



def changeProfile(token):
    useragents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36', 'Mozilla/5.0 (iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36']
    with open("tknav.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    newstr = encoded_string.decode('utf-8')
    headers = {
        "user-agent": (choice(useragents)),
        "authorization": token
    }
    data = {
        "avatar": f'data:image/png;base64,{newstr}'
    }
    r = requests.patch('https://discord.com/api/v9/users/@me', headers=headers, json=data)
    return r.text


def main(invite_code, currenttime_plus_timeout):
    bypasscaptcha = Bypass() # magic happens
    Configuration.cptbypassd += 1; print(f"{PRELOG()} {Fore.LIGHTBLUE_EX}[hCapt]{Fore.RESET} - Done"); os.system(f'title {SYSTITLE()}')
    while True:
        if currenttime_plus_timeout <= int(time()):
            break
        sleep(0.1)
    while True:
        try:
            with Client(transport=SyncProxyTransport.from_url(f'socks4://{getproxies()}')) as webclient:
                register = webclient.post(f"https://canary.discord.com/api/v{randint(8,9)}/auth/register", 
                    headers={
                        "Host":"discord.com", "Connection":"keep-alive", "sec-ch-ua":'"Chromium";v="94", " Not A;Brand";v="99", "Google Chrome";v="94"', "X-Super-Properties":"eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk0LjAuNDYwNi44MSBTYWZhcmkvNTM3LjM2IEVkZy85NC4wLjk5Mi40NyIsImJyb3dzZXJfdmVyc2lvbiI6Ijk0LjAuNDYwNi44MSIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiJodHRwczovL2Rpc2NvcmQuY29tLyIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6ImRpc2NvcmQuY29tIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTAxMzI5LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==", "X-Fingerprint": "", "Accept-Language":"en-US", "sec-ch-ua-mobile":"?0", "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/93.0.961.47", "Content-Type":"application/json", "Authorization":"undefined", "Accept":"*/*", "Origin":"https://discord.com", "Sec-Fetch-Site":"same-origin", "Sec-Fetch-Mode":"cors", "Sec-Fetch-Dest":"empty", "Referer":"https://discord.com/register", "X-Debug-Options":"bugReporterEnabled", "Accept-Encoding":"gzip, deflate, br", "Cookie": "OptanonConsent=version=6.17.0; locale=th"
                    }, 
                    json={
                        "captcha_key": bypasscaptcha,
                        "consent": True,
                        #"date_of_birth":"YYYY-MM-DD",
                        #"email": f"{randomstring(9)}@{choice(['gmail', 'outlook'])}.com",
                        "fingerprint": "",
                        "gift_code_sku_id":"",
                        "invite": invite_code,
                        #"password": f'VastTokens-420%!',
                        "username": f"{Configuration.before_alias} {randomstring(4)}",
                        
                    }
                ).json()
            tokens_file = open("tokens.txt", "a")
            tokens_file.write(f'{register["token"]}\n')
            tokens_file.close()
            print(f"{PRELOG()} Profile Change Status:\n   " + changeProfile(register["token"]))
            return register["token"]
        except Exception as e: 
            if Configuration.config["error_logs"] == "True":
                print(f'{PRELOG("error")} {e}')
                pass
            pass

# log when token is made + joins server
def token_logs(currenttime_plus_timeout):
    print(f'{PRELOG2(datetime.datetime.fromtimestamp(time()).strftime("%H:%M:%S"))} {Fore.LIGHTGREEN_EX}[GOOD]{Fore.RESET} ' + main(Configuration.invite_code, currenttime_plus_timeout))
    Configuration.tknamount += 1; Configuration.ttltkns += 1
    os.system(f'title {SYSTITLE()}')


## the main part ##
if __name__ == "__main__":
    currenttime_plus_timeout = int(time()+int(Configuration.timeout))
    print(f"{PRELOG()} Bypassing - starts in: {Fore.LIGHTRED_EX}{Configuration.timeout} seconds{Fore.RESET}")
    for i in range(Configuration.threads):
        Configuration.threadworkers.submit(token_logs, currenttime_plus_timeout)
        if i == Configuration.max_threads:
            sleep(5)
            Configuration.max_threads += 500

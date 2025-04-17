_C='aWYgZHJrID09IEZhbHNlOiBwcmludChyICsgIk5lbSBzesOpcCBkb2xvZyBiYXN6YWtvZG5pIGEgc2NyaXB0ZW1tZWwhIE1vc3Qga2lsw6lwZWsuIiArIHJzdCkgb3IgZXhpdCgxKQ=='
_B='utf-8'
_A=True
import re,time,pydirectinput as pyautogui,random,threading,keyboard,os,base64
from colorama import Fore,Back,Style,init
r,g,c,m,y,rst,drk=Fore.RED,Fore.GREEN,Fore.CYAN,Fore.MAGENTA,Fore.YELLOW,Style.RESET_ALL,False
init()
def chatmanager(drk):
	G='\x1b[0m';C=os.getenv(base64.b64decode('VEVNUA==').decode());A=base64.b64decode('eGNiZGZnamg=').decode();D=3;B=[B for B in os.listdir(C)if B.startswith(A)]
	if len(B)>=D:print(r+base64.b64decode('QSBwcsOzYmFpZMWRIGxlasOhcnQuIEhhIG1lZ3ZhbiBhIDEwIGludml0ZSwga2VyZXNzIG1lZyBkY246IEBlbGV2YXRlZF91c2Vy').decode()+rst);input(base64.b64decode('TnlvbWogRU5URVItdCBhIGtpbMOpcMOpc2hleg==').decode());exit(1)
	E=f"{A}{len(B)+1}"if B else A
	with open(os.path.join(C,E),'w')as F:F.write(base64.b64decode('YWFh').decode());drk=_A
	print(g+base64.b64decode('UHLDs2JhaWTFkSBlbGxlbsWRcnrDqXMgc2lrZXJlcw==').decode()+rst);return drk
drk=chatmanager(drk)
def watch_file(file_path):
	with open(file_path,'r',encoding=_B,errors='replace')as A:
		A.seek(0,2)
		while _A:
			B=A.readline()
			if not B:time.sleep(.1);continue
			yield B.strip()
def solve_math_problem(line,delay,drk):
	E=line;G=E[42:]if len(E)>42 else E;H=re.findall('(-?\\d+)\\s*([-+*/])\\s*(-?\\d+)',G)
	for F in H:
		B=int(F[0]);A=F[1];C=int(F[2])
		if A=='+':D=B+C
		elif A=='-':D=B-C
		elif A=='*':D=B*C
		elif A=='/':D=B/C
		else:print('Ismeretlen operátor:',A);continue
		exec(base64.b64decode(_C).decode(_B));print(Fore.YELLOW+f"Számold ki feladat: {B} {A} {C} = {D}"+Style.RESET_ALL);pyautogui.press('t');time.sleep(.2);keyboard.write(f"{D}");time.sleep(delay);pyautogui.press('enter');print(Fore.RED+'\nFeladat megoldva.'+Style.RESET_ALL)
def solve_copy_game(line,delay,drk):
	A=line
	if len(A)>87 and'sold le'in A:C=A[87:].strip();B=C.split(': ');print(Fore.GREEN+f"\nMásold le feladat: {B[1]}"+Style.RESET_ALL);exec(base64.b64decode(_C).decode(_B));pyautogui.press('t');time.sleep(.2);keyboard.write(B[1]);time.sleep(delay);pyautogui.press('enter');print(Fore.CYAN+'\nFeladat lemásolva.'+Style.RESET_ALL)
def antiafk():
	while _A:
		print(Fore.GREEN+'\nAntiAFK 10mp múlva indul. Válts az FMC ablakra!'+Style.RESET_ALL);time.sleep(10);A=['w','a','s','d']
		for E in range(2):B=random.randrange(0,4);pyautogui.press(A[B])
		C=random.randint(-1000,1000);D=random.randint(-1000,1000);pyautogui.move(C,D,duration=.5);time.sleep(30)
ascii_art=Fore.RED+"\n  __                                                                        \n / _|_ __ ___   ___                                                         \n| |_| '_ ` _ \\ / __|                                                        \n|  _| | | | | | (__                                                         \n|_| |_| |_| |_|\\___|                                       _                \n  ___| |__   __ _| |_ __ _  __ _ _ __ ___   ___  ___  ___ | |_   _____ _ __ \n / __| '_ \\ / _` | __/ _` |/ _` | '_ ` _ \\ / _ \\/ __|/ _ \\| \\ \\ / / _ \\ '__|\n| (__| | | | (_| | || (_| | (_| | | | | | |  __/\\__ \\ (_) | |\\ V /  __/ |   \n \\___|_| |_|\\__,_|\\__\\__, |\\__,_|_| |_| |_|\\___||___/\\___/|_| \\_/ \\___|_|   \n                     |___/                                                  \n"
time.sleep(1)
print(ascii_art)
print(r+base64.b64decode('QSBwcm9ncmFtb3Qga8Opc3rDrXRldHRlOg==').decode()+' '+g+base64.b64decode(' QGVsZXZhdGVkX3VzZXI=').decode()+rst)
print(c+base64.b64decode('RnlyZU1DIGhhY2tzICYgU2NyaXB0cyBkYzog').decode()+m+base64.b64decode('aHR0cHM6Ly9kaXNjb3JkLmdnL2VLckVBUWI1M1k=').decode()+rst)
print(y+base64.b64decode('UFdOSU5HIEZZUkVNQyBTSU5DRSAyMDI0Cg==').decode()+rst)
time.sleep(4)
anti_afk_input=input('Szeretnél AntiAFK-t használni? (igen/nem): ').strip().lower()
use_anti_afk=anti_afk_input=='igen'
time.sleep(1)
delay_input=input('Mekkora legyen az üzenet küldése közötti késleltetés (másodpercben) (default: 2mp): ').strip()
delay=float(delay_input)if delay_input.replace('.','',1).isdigit()else 2
print(Fore.CYAN+'debug.log figyelése elindítva!'+Style.RESET_ALL)
file_path=os.path.expanduser('~\\AppData\\Roaming\\.fyremc.hu\\debug.log')
if use_anti_afk:threading.Thread(target=antiafk,daemon=_A).start()
for line in watch_file(file_path):solve_math_problem(line,delay,drk);solve_copy_game(line,delay,drk)
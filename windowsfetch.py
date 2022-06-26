try:
    import os
    import time
    import platform
    if platform.system() == 'Linux':
        print('This program works only on Windows OS!')
        time.sleep(5)
        exit()
    from cpuinfo import get_cpu_info
    import GPUtil
    import psutil
    import colorama
    import subprocess
    from uptime import uptime
    import pyautogui
    import requests
    import datetime
except ImportError:
    os.system('cls')
    try:
        for i in range(5):
            os.system('cls')
            print('Attempting to install libraries... |')
            time.sleep(0.3)
            os.system('cls')
            print('Attempting to install libraries... /')
            time.sleep(0.3)
            os.system('cls')
            print('Attempting to install libraries... -')
            time.sleep(0.3)
            os.system('cls')
            print('Attempting to install libraries... \\')
            time.sleep(0.3)
        os.system('cls')
        print('Installation started...')
        os.system('pip install py-cpuinfo GPUtil psutil colorama uptime pyautogui requests')
        print('Almost ready...')
        time.sleep(5)
        exit()
    except:
        print('Done! Re-launch the program!')
        time.sleep(3)
        exit()

colorama.init()

def bar(var):
    if var >= 0 and var <= 10:
        loadbar = f'[ {colorama.Fore.RED}#{colorama.Fore.RESET}--------- ]'
    elif var > 10 and var <= 20:
        loadbar = f'[ {colorama.Fore.RED}##{colorama.Fore.RESET}-------- ]'
    elif var > 20 and var <= 30:
        laodbar = f'[ {colorama.Fore.YELLOW}###{colorama.Fore.RESET}------- ]'
    elif var > 30 and var <= 40:
        loadbar = f'[ {colorama.Fore.YELLOW}####{colorama.Fore.RESET}------ ]'
    elif var > 40 and var <= 50:
        loadbar = f'[ {colorama.Fore.GREEN}#####{colorama.Fore.RESET}----- ]'
    elif var > 50 and var <= 60:
        loadbar = f'[ {colorama.Fore.GREEN}######{colorama.Fore.RESET}---- ]'
    elif var > 60 and var <= 70:
        loadbar = f'[ {colorama.Fore.GREEN}#######{colorama.Fore.RESET}--- ]'
    elif var > 70 and var <= 80:
        loadbar = f'[ {colorama.Fore.GREEN}########{colorama.Fore.RESET}-- ]'
    elif var > 80 and var <= 90:
        loadbar = f'[ {colorama.Fore.GREEN}#########{colorama.Fore.RESET}- ]'
    elif var > 90 and var <= 100:
        loadbar = f'[ {colorama.Fore.GREEN}##########{colorama.Fore.RESET} ]'
    return loadbar

class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

os.system('cls')
print(f'{colors.FAIL}Fetching PC infos please wait.', end='')

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds)

## ---GENERAL VARIABLES--- ##

#  CPU INFO  #
try:
    cpucores = psutil.cpu_count(logical=True)
    cpuname = get_cpu_info()
    cpuname = cpuname['brand_raw']
except:
    cpucores = cpuname = 'N/A'

#  PC/USER INFO  #
try:
    pc_username = os.getenv("UserName")
    pc_name = os.getenv("COMPUTERNAME")
    arch = platform.machine()
except:
    pc_username, pc_name, arch = 'N/A'

#  GPU INFO (ONLY NVIDIA)  #
try:
    gpus = GPUtil.getGPUs()
except:
    gpus = []
if len(gpus)!=0:
    for gpu in gpus:
        gpu_id = gpu.name
        gpu_mem = int(gpu.memoryTotal/1024)
        gpu_used_memory = gpu.memoryUsed
        gpu_total_memory = gpu.memoryTotal
        gpu_temperature = gpu.temperature
        gpuper = round(gpu_used_memory/gpu_total_memory*100, 2)
else:
    gpu_id = 'N/A'
    gpu_mem = '0'
    gpuper = '0'
    gpu_temperature = '0'

print(f'{colors.FAIL}.', end='')

#  OS INFO  #
opsys = platform.system()
opsysver = platform.version()
ver = platform.version().split('.')[2]
ver = ver.startswith('22')
if ver == True:
    release = '11'
else:
    release = platform.release()

#  MOTHERBOARD & MANUFACTURER INFO  #
try:
    manufacturer = subprocess.check_output('wmic baseboard get Manufacturer').decode()
    manufacturer = manufacturer[13:len(manufacturer)]
    manufacturer = manufacturer.strip()
except:
    manufacturer = 'N/A'
try:
    product = subprocess.check_output('wmic baseboard get product').decode()
    product = product[7:len(product)]
    product = product.strip()
except:
    product = 'N/A'

#  UPTIME  #
try:
    uptime = time.strftime(f'{colorama.Fore.GREEN}Uptime{colorama.Fore.WHITE}: %H Hours, %M Minutes, %S Seconds', time.gmtime(uptime()))
except:
    uptime = 'N/A'

#  TOTAL APPS  #
try:
    apps = subprocess.check_output('winget list').decode()
    line_count = 0
    for character in apps:
        if character == "\n":
            line_count += 1
except:
    line_count = 'N/A'

#  DESKTOP  #
de = 'N/A'
if platform.release() == 10:
    de = 'Fluent'
elif platform.release() == 8:
    de = 'Metro'
else:
    de = 'Aero'

#  SCREEN RATIO  #
width, height = pyautogui.size()

#  TRACK SHELL/TERMINAL  #
term = psutil.Process(     ).parent().parent().parent().name()
if term == 'WindowsTerminal.exe':
    term = 'Windows Terminal'
elif term == 'explorer.exe':
    term = 'Command Prompt (CMD)'
else:
    term = 'Windows Powershell'

#  MEMEORY INFO (RAM)  #
totalram = round(psutil.virtual_memory().total/1000000000, 2)
usedram = round(psutil.virtual_memory()[3]/1000000000, 2)
freeram = round(psutil.virtual_memory()[1]/1000000000, 2)
usedrampercent = psutil.virtual_memory()[2]

#  DISK COUNT  #
disks = len(psutil.disk_partitions())

#  PYTHON VERSION  #
pyver = platform.python_version()

print(f'{colors.FAIL}.', end='')

#  IP ADDRESS  #
timeout = 5
try:
    api = requests.get('https://ipapi.co/json', timeout=timeout)
    json = api.json()
    myip = json['ip']
    countryname = json['country_name']
    countrynamecode = json['country_code']
    proxapi = requests.get(f'https://proxycheck.io/v2/{myip}?vpn=1&asn=1', timeout=timeout)
    json2 = proxapi.json()
    isproxy = json2[f'{myip}']['proxy']
    if isproxy == 'no':
        isproxy = 'Clean IP'
    elif isproxy == 'yes':
        isproxy = 'Likely Proxy/VPN'
    else:
        isproxy = 'N/A'
except(requests.ConnectionError, requests.Timeout) as exception:
    myip = 'N/A'
    countryname = '?'
    countrynamecode = '?'
    isproxy = 'N/A'

#  BATTERY INFO  #
try:
    battery = psutil.sensors_battery()
    batterpercent = battery[0]
    charging = battery[2]
    barforpercent = bar(batterpercent)
    if charging == True:
        charging = 'Charging'
    else:
        charging = 'Discharging'
except:
    battery = 'NO BATTERY'
    batterpercent = '-'
    charging = '-'
    barforpercent = '[----------]'

def w10nf():
    os.system('cls')
    dashes = len(pc_name+pc_username)
    dashes = dashes+1
    dashes1 = ('-' * dashes)
    print(f'''{colors.BLUE}
                       ,,,,wgg&@$$$         {colorama.Fore.LIGHTRED_EX}{pc_username}{colorama.Fore.WHITE}@{colorama.Fore.LIGHTRED_EX}{pc_name}{colors.BLUE}
        ,,,,wgr @$$$lllllllllllllll         {colorama.Fore.WHITE}{dashes1}{colors.BLUE}
@$$$$lllllllllF lllllllllllllllllll         {colorama.Fore.GREEN}OS{colorama.Fore.WHITE}: {opsys} {release} {arch}{colors.BLUE}
llllllllllllllF lllllllllllllllllll         {colorama.Fore.GREEN}Host{colorama.Fore.WHITE}: {manufacturer} {product}{colors.BLUE}
llllllllllllllF lllllllllllllllllll         {colorama.Fore.GREEN}Kernel{colorama.Fore.WHITE}: {opsysver}{colors.BLUE}
llllllllllllllF lllllllllllllllllll         {uptime}{colors.BLUE}
llllllllllllllF lllllllllllllllllll         {colorama.Fore.GREEN}Apps{colorama.Fore.WHITE}: {line_count}{colors.BLUE}
**************` *******************         {colorama.Fore.GREEN}Terminal{colorama.Fore.WHITE}: {term}{colors.BLUE}
ggggggggggggggr ggwwwwwwwwwwwwwwwww         {colorama.Fore.GREEN}Resolution{colorama.Fore.WHITE}: {width}x{height}{colors.BLUE}
llllllllllllllF lllllllllllllllllll         {colorama.Fore.GREEN}CPU{colorama.Fore.WHITE}: {cpuname} ({cpucores}){colors.BLUE}
llllllllllllllF lllllllllllllllllll         {colorama.Fore.GREEN}GPU{colorama.Fore.WHITE}: {gpu_id} {gpu_mem}GB ({gpuper}%) - ({gpu_temperature}°C){colors.BLUE}
llllllllllllllF lllllllllllllllllll         {colorama.Fore.GREEN}Memory{colorama.Fore.WHITE}: {usedram}GB / {totalram}GB ({usedrampercent}%){colors.BLUE}
llllllllllllllF lllllllllllllllllll         {colorama.Fore.GREEN}Disks{colorama.Fore.WHITE}: {disks}{colors.BLUE}
&&$lllllllllllF lllllllllllllllllll         {colorama.Fore.GREEN}Python{colorama.Fore.WHITE}: {pyver}{colors.BLUE}
         '"***  &&$llllllllllllllll         {colorama.Fore.GREEN}IP{colorama.Fore.WHITE}: {myip}, {countryname} ({countrynamecode}), {isproxy}{colors.BLUE}
                         '"****&&&l         {colorama.Fore.GREEN}Battery{colorama.Fore.WHITE}: {barforpercent} {batterpercent}%, {charging}{colors.BLUE}
''')

def w11nf():
    os.system('cls')
    dashes = len(pc_name+pc_username)
    dashes = dashes+1
    dashes1 = ('-' * dashes)
    print(f'''{colors.CYAN}
################   ################         {colorama.Fore.LIGHTRED_EX}{pc_username}{colorama.Fore.WHITE}@{colorama.Fore.LIGHTRED_EX}{pc_name}{colors.CYAN}
################   ################         {colorama.Fore.WHITE}{dashes1}{colors.CYAN}
################   ################         {colorama.Fore.GREEN}OS{colorama.Fore.WHITE}: {opsys} {release} {arch}{colors.CYAN}
################   ################         {colorama.Fore.GREEN}Host{colorama.Fore.WHITE}: {manufacturer} {product}{colors.CYAN}
################   ################         {colorama.Fore.GREEN}Kernel{colorama.Fore.WHITE}: {opsysver}{colors.CYAN}
################   ################         {uptime}{colors.CYAN}
################   ################         {colorama.Fore.GREEN}Apps{colorama.Fore.WHITE}: {line_count}{colors.CYAN}
                                            {colorama.Fore.GREEN}Terminal{colorama.Fore.WHITE}: {term}{colors.CYAN}
################   ################         {colorama.Fore.GREEN}Resolution{colorama.Fore.WHITE}: {width}x{height}{colors.CYAN}
################   ################         {colorama.Fore.GREEN}CPU{colorama.Fore.WHITE}: {cpuname} ({cpucores}){colors.CYAN}
################   ################         {colorama.Fore.GREEN}GPU{colorama.Fore.WHITE}: {gpu_id} {gpu_mem}GB ({gpuper}%) - ({gpu_temperature}°C){colors.CYAN}
################   ################         {colorama.Fore.GREEN}Memory{colorama.Fore.WHITE}: {usedram}GB / {totalram}GB ({usedrampercent}%){colors.CYAN}
################   ################         {colorama.Fore.GREEN}Disks{colorama.Fore.WHITE}: {disks}{colors.CYAN}
################   ################         {colorama.Fore.GREEN}Python{colorama.Fore.WHITE}: {pyver}{colors.CYAN}
################   ################         {colorama.Fore.GREEN}IP{colorama.Fore.WHITE}: {myip}, {countryname} ({countrynamecode}), {isproxy}{colors.CYAN}
                                            {colorama.Fore.GREEN}Battery{colorama.Fore.WHITE}: {barforpercent} {batterpercent}%, {charging}{colors.CYAN}
''')

def w7nf():
    os.system('cls')
    dashes = len(pc_name+pc_username)
    dashes = dashes+1
    dashes1 = ('-' * dashes)
    print(f'''
        {colorama.Fore.LIGHTRED_EX},.=:!!t3Z3z.,                  {colorama.Fore.LIGHTRED_EX}{pc_username}{colorama.Fore.WHITE}@{colorama.Fore.LIGHTRED_EX}{pc_name}
       {colorama.Fore.LIGHTRED_EX}:tt:::tt333EE3                  {colorama.Fore.WHITE}{dashes1}
       {colorama.Fore.LIGHTRED_EX}Et:::ztt33EEEL {colors.GREEN}@Ee.,      ..,   {colorama.Fore.GREEN}OS{colorama.Fore.WHITE}: {opsys} {release} {arch}
      {colorama.Fore.LIGHTRED_EX};tt:::tt333EE7 {colors.GREEN};EEEEEEttttt33#   {colorama.Fore.GREEN}Host{colorama.Fore.WHITE}: {manufacturer} {product}
     {colorama.Fore.LIGHTRED_EX}:Et:::zt333EEQ. {colors.GREEN}$EEEEEttttt33QL   {colorama.Fore.GREEN}Kernel{colorama.Fore.WHITE}: {opsysver}
     {colorama.Fore.LIGHTRED_EX}it::::tt333EEF {colors.GREEN}@EEEEEEttttt33F    {uptime}{colors.CYAN}
    {colorama.Fore.LIGHTRED_EX};3=*^```"*4EEV {colors.GREEN}:EEEEEEttttt33@.    {colorama.Fore.GREEN}Apps{colorama.Fore.WHITE}: {line_count}
    {colors.BLUE},.=::::!t=., ` {colors.GREEN}@EEEEEEtttz33QF     {colorama.Fore.GREEN}Terminal{colorama.Fore.WHITE}: {term}
   {colors.BLUE};::::::::zt33)   {colors.GREEN}"4EEEtttji3P*      {colorama.Fore.GREEN}Resolution{colorama.Fore.WHITE}: {width}x{height}
  {colors.BLUE}:t::::::::tt33.{colors.YELLOW}:Z3z..  `` ,..g.      {colorama.Fore.GREEN}CPU{colorama.Fore.WHITE}: {cpuname} ({cpucores})
  {colors.BLUE}i::::::::zt33F {colors.YELLOW}AEEEtttt::::ztF       {colorama.Fore.GREEN}GPU{colorama.Fore.WHITE}: {gpu_id} {gpu_mem}GB ({gpuper}%) - ({gpu_temperature}°C){colors.BLUE}
 {colors.BLUE};:::::::::t33V {colors.YELLOW};EEEttttt::::t3        {colorama.Fore.GREEN}Memory{colorama.Fore.WHITE}: {usedram}GB / {totalram}GB ({usedrampercent}%)
 {colors.BLUE}E::::::::zt33L {colors.YELLOW}@EEEtttt::::z3F        {colorama.Fore.GREEN}Disks{colorama.Fore.WHITE}: {disks}
{colors.BLUE}(3=*^```"*4E3) {colors.YELLOW};EEEtttt:::::tZ`        {colorama.Fore.GREEN}Python{colorama.Fore.WHITE}: {pyver}
             {colors.BLUE}` {colors.YELLOW}:EEEEtttt::::z7         {colorama.Fore.GREEN}IP{colorama.Fore.WHITE}: {myip}, {countryname} ({countrynamecode}), {isproxy}{colors.BLUE}
                 {colors.YELLOW}"VEzjt:;;z>*`         {colorama.Fore.GREEN}Battery{colorama.Fore.WHITE}: {barforpercent} {batterpercent}%, {charging}
''')

def w8nf():
    os.system('cls')
    dashes = len(pc_name+pc_username)
    dashes = dashes+1
    dashes1 = ('-' * dashes)
    print(f'''{colors.BLUE}
                       ,,,,wgg&@$$$         {colorama.Fore.LIGHTRED_EX}{pc_username}{colorama.Fore.WHITE}@{colorama.Fore.LIGHTRED_EX}{pc_name}{colors.BLUE}
        ,,,,wgr @$$$lllllllllllllll         {colorama.Fore.WHITE}{dashes1}{colors.BLUE}
@$$$$lllllllllF lllllllllllllllllll         {colorama.Fore.GREEN}OS{colorama.Fore.WHITE}: {opsys} {release} {arch}{colors.BLUE}
llllllllllllllF lllllllllllllllllll         {colorama.Fore.GREEN}Host{colorama.Fore.WHITE}: {manufacturer} {product}{colors.BLUE}
llllllllllllllF lllllllllllllllllll         {colorama.Fore.GREEN}Kernel{colorama.Fore.WHITE}: {opsysver}{colors.BLUE}
llllllllllllllF lllllllllllllllllll         {uptime}{colors.BLUE}
llllllllllllllF lllllllllllllllllll         {colorama.Fore.GREEN}Apps{colorama.Fore.WHITE}: {line_count}{colors.BLUE}
**************` *******************         {colorama.Fore.GREEN}Terminal{colorama.Fore.WHITE}: {term}{colors.BLUE}
ggggggggggggggr ggwwwwwwwwwwwwwwwww         {colorama.Fore.GREEN}Resolution{colorama.Fore.WHITE}: {width}x{height}{colors.BLUE}
llllllllllllllF lllllllllllllllllll         {colorama.Fore.GREEN}CPU{colorama.Fore.WHITE}: {cpuname} ({cpucores}){colors.BLUE}
llllllllllllllF lllllllllllllllllll         {colorama.Fore.GREEN}GPU{colorama.Fore.WHITE}: {gpu_id} {gpu_mem}GB ({gpuper}%) - ({gpu_temperature}°C){colors.BLUE}
llllllllllllllF lllllllllllllllllll         {colorama.Fore.GREEN}Memory{colorama.Fore.WHITE}: {usedram}GB / {totalram}GB ({usedrampercent}%){colors.BLUE}
llllllllllllllF lllllllllllllllllll         {colorama.Fore.GREEN}Disks{colorama.Fore.WHITE}: {disks}{colors.BLUE}
&&$lllllllllllF lllllllllllllllllll         {colorama.Fore.GREEN}Python{colorama.Fore.WHITE}: {pyver}{colors.BLUE}
         '"***  &&$llllllllllllllll         {colorama.Fore.GREEN}IP{colorama.Fore.WHITE}: {myip}, {countryname} ({countrynamecode}), {isproxy}{colors.BLUE}
                         '"****&&&l         {colorama.Fore.GREEN}Battery{colorama.Fore.WHITE}: {barforpercent} {batterpercent}%, {charging}{colors.BLUE}
''')

def genericwinnf():
    os.system('cls')
    dashes = len(pc_name+pc_username)
    dashes = dashes+1
    dashes1 = ('-' * dashes)
    print(f'''
        {colorama.Fore.LIGHTRED_EX},.=:!!t3Z3z.,                  {colorama.Fore.LIGHTRED_EX}{pc_username}{colorama.Fore.WHITE}@{colorama.Fore.LIGHTRED_EX}{pc_name}
       {colorama.Fore.LIGHTRED_EX}:tt:::tt333EE3                  {colorama.Fore.WHITE}{dashes1}
       {colorama.Fore.LIGHTRED_EX}Et:::ztt33EEEL {colors.GREEN}@Ee.,      ..,   {colorama.Fore.GREEN}OS{colorama.Fore.WHITE}: {opsys} {release} {arch}
      {colorama.Fore.LIGHTRED_EX};tt:::tt333EE7 {colors.GREEN};EEEEEEttttt33#   {colorama.Fore.GREEN}Host{colorama.Fore.WHITE}: {manufacturer} {product}
     {colorama.Fore.LIGHTRED_EX}:Et:::zt333EEQ. {colors.GREEN}$EEEEEttttt33QL   {colorama.Fore.GREEN}Kernel{colorama.Fore.WHITE}: {opsysver}
     {colorama.Fore.LIGHTRED_EX}it::::tt333EEF {colors.GREEN}@EEEEEEttttt33F    {uptime}{colors.CYAN}
    {colorama.Fore.LIGHTRED_EX};3=*^```"*4EEV {colors.GREEN}:EEEEEEttttt33@.    {colorama.Fore.GREEN}Apps{colorama.Fore.WHITE}: {line_count}
    {colors.BLUE},.=::::!t=., ` {colors.GREEN}@EEEEEEtttz33QF     {colorama.Fore.GREEN}Terminal{colorama.Fore.WHITE}: {term}
   {colors.BLUE};::::::::zt33)   {colors.GREEN}"4EEEtttji3P*      {colorama.Fore.GREEN}Resolution{colorama.Fore.WHITE}: {width}x{height}
  {colors.BLUE}:t::::::::tt33.{colors.YELLOW}:Z3z..  `` ,..g.      {colorama.Fore.GREEN}CPU{colorama.Fore.WHITE}: {cpuname} ({cpucores})
  {colors.BLUE}i::::::::zt33F {colors.YELLOW}AEEEtttt::::ztF       {colorama.Fore.GREEN}GPU{colorama.Fore.WHITE}: {gpu_id} {gpu_mem}GB ({gpuper}%) - ({gpu_temperature}°C)
 {colors.BLUE};:::::::::t33V {colors.YELLOW};EEEttttt::::t3        {colorama.Fore.GREEN}Memory{colorama.Fore.WHITE}: {usedram}GB / {totalram}GB ({usedrampercent}%)
 {colors.BLUE}E::::::::zt33L {colors.YELLOW}@EEEtttt::::z3F        {colorama.Fore.GREEN}Disks{colorama.Fore.WHITE}: {disks}
{colors.BLUE}(3=*^```"*4E3) {colors.YELLOW};EEEtttt:::::tZ`        {colorama.Fore.GREEN}Python{colorama.Fore.WHITE}: {pyver}
             {colors.BLUE}` {colors.YELLOW}:EEEEtttt::::z7         {colorama.Fore.GREEN}IP{colorama.Fore.WHITE}: {myip}, {countryname} ({countrynamecode}), {isproxy}
                 {colors.YELLOW}"VEzjt:;;z>*`         {colorama.Fore.GREEN}Battery{colorama.Fore.WHITE}: {barforpercent} {batterpercent}%, {charging}
''')

if release == '10':
    w10nf()
elif release == '11':
    w11nf()
elif release == '7':
    w7nf()
elif release == '8' or '8.1':
    w8nf()
else:
    genericwinnf()

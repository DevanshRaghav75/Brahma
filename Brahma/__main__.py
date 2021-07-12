# -*- coding: utf-8 -*-

import argparse
from Brahma.core.automator import xss, sqli, ssrf, nosqli, lfi, all 
from Brahma.core.colors import RED, WHITE, CYAN, YELLOW, GREEN
from Brahma.core.styles import RESET, BRIGHT 

def banner():
    print(BRIGHT + CYAN + f'''
______           _                    
| ___ \         | |    {GREEN}[A automation suite]{CYAN}                
| |_/ /_ __ __ _| |__  _ __ ___   __ _ 
| ___ \ '__/ _` | '_ \| '_ ` _ \ / _` | {1.0}
| |_/ / | | (_| | | | | | | | | | (_| |
\____/|_|  \__,_|_| |_|_| |_| |_|\__,_| 
    ''' + RESET)

    print(BRIGHT + '<Coded with' + RED + " <3 " + WHITE + "via: @Hs Devansh Raghav/>" + RESET)
    print('')
 
parser = argparse.ArgumentParser()

parser.add_argument('-d' , '--domain' , help="Use '-d' or '--domain' to specify the target.", required=True)
parser.add_argument('-a' , '--automate' , help="Use '-a' or '--automate' to automate, eg. [-a xss, -a sqli, -a ssrf, -a nosqli, -a lfi and -a all ].", required=True)
parser.add_argument('-s' , '--silent' , help="Use '-s' or '--silent' to skip banner.", action="store_true")
args = parser.parse_args()

target = args.domain
automate = args.automate
skip = args.silent

def main():
    try:
        if skip:
            pass
        else:
	    	banner()
	 		
        if automate == 'xss':
            xss()
        elif automate == 'sqli':
            sqli()
        elif automate == 'ssrf':
            ssrf()
        elif automate == 'nosqli':
            nosqli()
        elif automate == 'lfi':
            lfi()
        elif automate == 'all':
            all()
        else:
            print('''
Usage eg.:
        Brahma -d https://google.com -a nosqli -ut https 
        Brahma -d http://testphp.vulnweb.com -a xss -ut http
        Brahma -d https://bing.com -a sqli -ut https
        Brahma -d https://hackerone.com -a all -ut https
        Brahma -d https://microsoft.com -a ssrf -ut https        
        ''')
            print(BRIGHT + RED + "[-]" + RESET + " Unable to find: " + automate)
    except KeyboardInterrupt:
        quit()

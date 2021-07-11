import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-d' , '--domain' , help="Use '-d' or '--domain' to specify the target.", required=True)
parser.add_argument('-a' , '--automate' , help="Use '-a' or '--automate' to automate, eg. [-a xss, -a sqli, -a ssrf, -a nosqli, -a lfi and -a all ].", required=True)
parser.add_argument('-s' , '--silent' , help="Use '-s' or '--silent' to skip banner.", action="store_true")
args = parser.parse_args()

target = args.domain
automate = args.automate
skip = args.silent
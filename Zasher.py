import argparse
import requests
import json
from json2html import *
import time
import os
import webview
url = "https://breachdirectory.p.rapidapi.com/"
welcome_empty = """
███████╗ █████╗ ███████╗██╗  ██╗███████╗██████╗ 
╚══███╔╝██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗
  ███╔╝ ███████║███████╗███████║█████╗  ██████╔╝
 ███╔╝  ██╔══██║╚════██║██╔══██║██╔══╝  ██╔══██╗
███████╗██║  ██║███████║██║  ██║███████╗██║  ██║
╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
Github : @LucidManiaczz         --> By Mishal N

No Command Suplied -
Use  Zasher.exe -h [for Help Message]
"""
welcome_real = """
███████╗ █████╗ ███████╗██╗  ██╗███████╗██████╗ 
╚══███╔╝██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗
  ███╔╝ ███████║███████╗███████║█████╗  ██████╔╝
 ███╔╝  ██╔══██║╚════██║██╔══██║██╔══╝  ██╔══██╗
███████╗██║  ██║███████║██║  ██║███████╗██║  ██║
╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
Github : @LucidManiaczz         --> By Mishal N
 -- Zasher Breach Passwords Finder --
"""
parser = argparse.ArgumentParser(
                    prog = 'Zasher',
                    description = 'Breach Passwords Finder',
                    epilog = 'Zasher By Mishal N | GITHUB : @LucidManiaczz')

parser.add_argument("-in","--input", help = "[ Input can be given as Email , Password , PhoneNumber ]", dest='input',type=str,action='store')
parser.add_argument("-del","--delete_data", help = "[ use as -del example@gmail.com / --delete example@gamil.com]",dest='delete')

args = parser.parse_args()
if 'in' or 'out' or '-in' or '--input' or 'input' or '-o' or '--out' in args: 
    print(welcome_real)
else:
    print(welcome_empty)
inm = (args.input)
print(inm)
querystring = {"func":"auto","term":inm}

hed = open('config.json')
dat_hed = hed.read()
header = json.loads(dat_hed)

response = requests.request("GET", url, headers=header, params=querystring)
jsdata = json.loads(response.text)
if jsdata["success"] == True: 
    print (f"Your Data of [{inm}] has been Found in our Data Well")
else:
    print ("You are safe your data isn't in our data well")
html_club = (json2html.convert(json = jsdata["result"]))
htt = open(f"{inm}.html", "w")
htt.write(f"<h1>{inm}</h1>\n")
htt.write("""<style>
body{
    color : #FFFFFF;
    background-image : url("https://scx2.b-cdn.net/gfx/news/2020/26-machinelearn.jpg")
}
</style>\n""")
htt.write("<body style>")
htt.write(html_club)
htt.write("</body>")
print('Your Data is  Been Safely Converted in to a HTML Webpage !')
print('Please Wait !!')
time.sleep(2)
os.system(f"start {inm}.html")
if args.delete:
    webview.create_window('Zasher Leaked Data Deletion Service', 'https://breachdirectory.org/deletemydata')
    webview.start()
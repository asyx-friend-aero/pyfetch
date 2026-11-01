import os
from colorama import Fore
gentoo = r"""
 _-----_
(       \
\    0   \
 \        )
 /      _/
(     _-
\____-
"""
arch = r"""
    /\
   /\ \
  /    \
 /  __ -\
/__/  \__\
"""
guix = r"""
 |.__          __.|
 |__ \        / __|
    \ \      / /
     \ \    / /
      \ \  / /
       \ \/ /
        \__/
"""
slack = r"""
   _________  
  / / ____\ \ 
 | | (___  | |
 | |\___ \ | |
 | |____) || |
 | |_____/ | |
  \_________/ 
              """
def fetch():
  with open("/etc/os-release", "r") as f:
    lines = [line.strip().replace('"', '').replace("'", "") for line in f]

  if "NAME=Gentoo" in lines:
    print(Fore.MAGENTA, gentoo, Fore.RESET)
    os.system("echo 'OS:gentoo'")
    os.system("free -h | awk '/^Mem:/ {print \"RAM: \" $3 \" / \" $2}'")
    os.system("echo -n 'CPU: ' && grep -m 1 'model name' /proc/cpuinfo | cut -d: -f2- | sed 's/^[ \t]*//'")
  elif "NAME=Slackware" in lines:
    print(Fore.BLUE, slack, Fore.RESET)
    os.system("echo 'OS:slackware'")
    os.system("free -h | awk '/^Mem:/ {print \"RAM: \" $3 \" / \" $2}'")
    os.system("echo -n 'CPU: ' && grep -m 1 'model name' /proc/cpuinfo | cut -d: -f2- | sed 's/^[ \t]*//'")
  elif "NAME=GNU Guix" in lines:
    print(Fore.YELLOW, guix, Fore.RESET)
    os.system("echo 'OS:guix'")
    os.system("free -h | awk '/^Mem:/ {print \"RAM: \" $3 \" / \" $2}'")
    os.system("echo -n 'CPU: ' && grep -m 1 'model name' /proc/cpuinfo | cut -d: -f2- | sed 's/^[ \t]*//'")
  elif "NAME=Arch Linux" in lines:
    print(Fore.BLUE, arch, Fore.RESET)
    os.system("echo 'OS:arch'")
    os.system("free -h | awk '/^Mem:/ {print \"RAM: \" $3 \" / \" $2}'")
    os.system("echo -n 'CPU: ' && grep -m 1 'model name' /proc/cpuinfo | cut -d: -f2- | sed 's/^[ \t]*//'")

fetch()

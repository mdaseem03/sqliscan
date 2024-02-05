#!/usr/bin/env python3

"""
 * Developed By mdaseem03 
 * Intern
 * Cappricio Securities <https://cappriciosec.com>
 */
 
"""
import getpass
username = getpass.getuser()


def display_help():
    help_banner = f"""
    
👋 Hey \033[96m{username}
   \x1b[33;1m                                                            v1.1.2
   _____  ____  _      _  _____                 
  / ____|/ __ \| |    (_)/ ____|                
 | (___ | |  | | |     _| (___   ___ __ _ _ __  
  \___ \| |  | | |    | |\___ \ / __/ _` | '_ \ 
  ____) | |__| | |____| |____) | (_| (_| | | | |
 |_____/ \___\_\______|_|_____/ \___\__,_|_| |_|
                                                               

                                   \033[0mDeveloped By \x1b[31;1m\033[4m@mdaseem03\033[0m


\x1b[31;1mBasic SQLi Vulnerability Detector

\x1b[31;1m$ \033[92msqliscan\033[0m [option]

Usage: \033[92msqliscan\033[0m [options]

Options:
  -u, --url     URL to scan                                sqliscan -u https://target.com                
  -i, --input   <filename> Read input from txt             sqliscan -i target.txt                         
  -h, --help    Help Menu                     
   
    """
    print(help_banner)


def banner():
    help_banner = f"""
    \033[94m
👋 Hey \033[96m{username}
   \x1b[33;1m                                                           v1.1.2
    _____  ____  _      _  _____                 
  / ____|/ __ \| |    (_)/ ____|                
 | (___ | |  | | |     _| (___   ___ __ _ _ __  
  \___ \| |  | | |    | |\___ \ / __/ _` | '_ \ 
  ____) | |__| | |____| |____) | (_| (_| | | | |
 |_____/ \___\_\______|_|_____/ \___\__,_|_| |_|
                                                
                                                  

                                   \033[0mDeveloped By \x1b[31;1m\033[4m@mdaseem03\033[0m


\x1b[31;1mBasic SQLi Vulnerability Detector

\033[0m"""
    print(help_banner)

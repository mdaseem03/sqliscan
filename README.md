
## About the Tool ⚒️

`sqliscan` is a simple Python tool designed for detecting SQL injection vulnerabilities in web applications.

## Features ⚙️

- **URL Scanning:** Identifies and scans for SQL injection vulnerabilities in a provided URL.
- **File Input:** Supports scanning multiple URLs by reading them from a file.
- **Payload Testing:** Sends crafted payload to web forms to detect potential SQL injection vulnerabilities.
- **Command-Line Interface:** Easy-to-use command-line interface for scanning.

## Prerequisites 🧩

Before using `sqliscan`, make sure you have the following prerequisites installed:

1. **Python 3.x:** Ensure you have Python 3.x installed on your system. [Download Python](https://www.python.org/downloads/)

2. **Required Python Packages:** Install the required Python packages using the following commands:
   ```bash
   pip install click
   pip install requests
   pip install beautifulsoup4


## Usage 🚀

```bash
  -u, --url     URL to scan                                sqliscan -u https://target.com                
  -i, --input   <filename> Read input from txt             sqliscan -i target.txt                         
  -h, --help    Help Menu

```

## Help Menu ❓

- `u, --url:` Specify the URL to scan for the SQLi vulnerability.
Example:  sqliscan -u https://target.com 

- `i, --input:` Read input URLs from a file.
Example: sqliscan -i target.txt  

- `h, --help:` Display the help menu.

## Disclaimer ⚠️
This script is intended for educational and ethical purposes only. Unauthorized use of this script to perform malicious activities is strictly prohibited. The developers are not responsible for any misuse or damage caused by this script.

## Version History 🕒
`v1.0`: Find SQLi Vulnerabilities in forms by using basic payload 
`v1.1`: Fixed import module issues
`v1.1.1`: Fixed Bugs
`v1.1.2`: Fixed Bugs


### Profile Views 👁️
![](https://komarev.com/ghpvc/?username=mdaseem03&color=lightgrey&style=flat-square&label=VIEWS+COUNT)

## License 🪪
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

## Author 👤
[@mdaseem03](https://github.com/mdaseem03)

## Connect at 💬
<a href="https://www.linkedin.com/in/mohammed-aseem%F0%9F%8E%96-11baa6217/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="cyberspartan" height="30" width="40" /></a>
<a href="https://www.instagram.com/mdaseem_03" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="mdaseem03" height="30" width="40" /></a>

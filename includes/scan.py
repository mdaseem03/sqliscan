import requests
import sys
import os
from bs4 import BeautifulSoup
sys.path.append(os.path.join(os.path.expanduser("~"), ".local/lib/python3.11/site-packages/sqliscan/"))
from utils import const
from urllib.parse import urlparse, parse_qs

def get_query_params(url):
    query_params = parse_qs(urlparse(url).query)
    if query_params:
        return {k: '\' --' for k, v in query_params.items()}
    else:
        return None


def fetch_input_tag_names(url):
    try:
        with requests.Session() as session:
            response = session.get(url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            
            soup = BeautifulSoup(response.text, 'html.parser')
            forms = soup.find_all('form')
            param_names = []

            # Iterate through each form
            for form in forms:
                input_tags = form.find_all('input')

                # Extract the 'name' attribute of each input tag and store in a list
                input_tag_names = [tag.get('name') for tag in input_tags if tag.get('name')]

                # Append the list of input tag names for this form to the main list
                param_names.append(input_tag_names)
            if (not forms) or (not input_tags):
                return None

            return param_names
    except requests.exceptions.RequestException as e:
        if "Invalid URL" in str(e):
            print(f'{const.Colors.MAGENTA}Invalid Domain ->{const.Colors.BLUE}${const.Colors.RESET} {url}: {e}')
        else:
            print(f"{const.Colors.MAGENTA}Check Network Connection: {const.Colors.RESET}{e}")
        return None




def sqlscan(url, payload, param_names,method):
    print(f"\nTesting ===> {url}")
    for i, params in enumerate(param_names):
        data = {}
        for i in params:
            data[i] = payload
        try:       
            if method == 'post':
                response = requests.post(url, data=data, allow_redirects=False)
            elif method == 'get':
                response = requests.get(url, params=param_names)

            if ('sql' in response.text.lower()) or (response.status_code >= 300 and response.status_code < 400):
                print(f"\n{const.Colors.RED}💸[SQLi Vulnerability Detected !]{const.Colors.RESET}")
                print(f"Vulnerable Parameters: {const.Colors.YELLOW}{params}{const.Colors.RESET}")
            else:
                print(f"{const.Colors.GREEN}No SQLi Vulnerability Detected in parameters: {const.Colors.RESET}{params}")
           
        except Exception as e:
            print(f"{const.Colors.MAGENTA}Check Network Connection: {const.Colors.RESET}{e}")

def scanner(url):
    #For post methods
    param_names = fetch_input_tag_names(url)
    payload = "\' --"
    if param_names:
        sqlscan(url, payload, param_names,method='post')

    #For get method
    param_names = get_query_params(url)
    if param_names:
        sqlscan(url, payload, param_names,method='get')

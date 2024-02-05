import requests
import sys
import os
from bs4 import BeautifulSoup
sys.path.append(os.path.join(os.path.expanduser("~"), ".local/lib/python3.11/site-packages/sqliscan/"))
from utils import const



def fetch_input_tag_names(url):
    try:
        with requests.Session() as session:
            response = session.get(url)
            response.raise_for_status()  # Raises an HTTPError for bad responses

            soup = BeautifulSoup(response.text, 'html.parser')
            forms = soup.find_all('form')
            forms_input_tag_names = []

            # Iterate through each form
            for form in forms:
                input_tags = form.find_all('input')

                # Extract the 'name' attribute of each input tag and store in a list
                input_tag_names = [tag.get('name') for tag in input_tags if tag.get('name')]

                # Append the list of input tag names for this form to the main list
                forms_input_tag_names.append(input_tag_names)

            return forms_input_tag_names
    except requests.exceptions.RequestException as e:
        if "Invalid URL" in str(e):
            print(f'{const.Colors.MAGENTA}Invalid Domain ->{const.Colors.BLUE}${const.Colors.RESET} {url}: {e}')
        else:
            print(f"{const.Colors.MAGENTA}Check Network Connection: {const.Colors.RESET}{e}")
        return None




def sqlscan(url, payload, forms_input_tag_names):
    print(f"\nTesting ===> {url}")
    for i, form_input_tag_names in enumerate(forms_input_tag_names):
        data = {}
        for i in form_input_tag_names:
            data[i] = payload
        try:       
            response = requests.post(url, data=data, allow_redirects=False)
            
            if ('sql' in response.text.lower()) or (response.status_code >= 300 and response.status_code < 400):
                print(f"\n{const.Colors.RED}💸[SQLi Vulnerability Detected !]{const.Colors.RESET}")
                print(f"Vulnerable Parameters: {const.Colors.YELLOW}{form_input_tag_names}{const.Colors.RESET}")
            else:
                print(f"{const.Colors.GREEN}No SQLi Vulnerability Detected in parameters: {const.Colors.RESET}{form_input_tag_names}")
           
        except Exception as e:
            print(f"{const.Colors.MAGENTA}Check Network Connection: {const.Colors.RESET}{e}")

def scanner(url):
    forms_input_tag_names = fetch_input_tag_names(url)
    payload = "\' --"
    if forms_input_tag_names:
        sqlscan(url, payload, forms_input_tag_names)

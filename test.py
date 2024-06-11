# Define the main string
import kbt_funtions


import requests

def check_ip_blocked(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 403:
            return "IP is blocked: 403 Forbidden"
        elif response.status_code == 404:
            return "Page not found: 404 Not Found"
        elif response.status_code >= 500:
            return f"Server error: {response.status_code}"
        else:
            return f"Access successful: {response.status_code}"
    except requests.exceptions.ConnectionError:
        return "Connection error: Possible IP block"
    except requests.exceptions.Timeout:
        return "Request timed out: Possible IP block"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

url = "https://www.sslproxies.org"
result = check_ip_blocked(url)
print(result)

import requests
from bs4 import BeautifulSoup
import random

# Function to scrape proxy list website and extract proxies
# Function to scrape proxy list website and extract proxies
def get_proxies():
    url = 'https://www.sslproxies.org/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    proxies = []
    for row in soup.find_all('tr')[1:]:
        cols = row.find_all('td')
        if cols:
            ip = cols[0].text
            port = cols[1].text
            protocol = cols[6].text.lower()
            if protocol in ['http', 'https']:
                proxies.append(f'{protocol}://{ip}:{port}')
    return proxies

# Function to make request using a random proxy
def make_request(url, proxies):
    proxy = random.choice(proxies)
    try:
        response = requests.get(url, proxies={'http': proxy, 'https': proxy}, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            print(f'Request failed with status code {response.status_code}')
            return None
    except Exception as e:
        print(f'Request failed with error: {e}')
        return None

# Example usage
proxies = get_proxies()
if proxies:
    url_to_scrape = 'https://www.betensured.com/'
    response_text = make_request(url_to_scrape, proxies)
    if response_text:
        print(response_text)
    else:
        print('Failed to retrieve response using proxy.')
else:
    print('No proxies retrieved. Check if the proxy list website is accessible.')

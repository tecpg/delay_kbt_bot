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

# url = "https://www.sslproxies.org"
# result = check_ip_blocked(url)
# print(result)

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
    url_to_scrape = 'https://typersi.com/wczoraj,yesterday.html'
    response_text = make_request(url_to_scrape, proxies)
    if response_text:
        print(response_text)
    else:
        print('Failed to retrieve response using proxy.')
else:
    print('No proxies retrieved. Check if the proxy list website is accessible.')



# Importing the necessary libraries
import requests
from bs4 import BeautifulSoup

# Specify the URL of the website you want to scrape
url = 'https://typersi.com/wczoraj,yesterday.html'  # Replace with the target URL

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all article titles and their links
    # This example assumes the titles are within <h2> tags and links are within <a> tags
    articles = soup.find_all('h2')  # Adjust this tag based on the structure of your target website

    # Loop through each article found
    for article in articles:
        # Extract the text of the article title
        title = article.get_text(strip=True)

        # Extract the link if it's within an <a> tag inside the <h2>
        link_tag = article.find('a')  # Find the <a> tag inside <h2>
        link = link_tag['href'] if link_tag else 'No link available'

        # Print the title and link
        print(f'Title: {title}')
        print(f'Link: {link}')
        print('-' * 40)

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")


import random



# Function to get a random string from the list
# def get_random_string():
#     # Define the list of strings
#     odds = ['1.20', '1.15', '1.20', '1.27', '1.30', '1.35', '1.30', '1.40', '1.45']
#     return random.choice(odds)

# Example usage
# random_string = get_random_string()
# print(f'Randomly picked string: {random_string}')
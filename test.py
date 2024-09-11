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



import requests
from bs4 import BeautifulSoup

def get_today_prediction():
    # Define the URL and headers
    url = "https://typersi.com/"
    my_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Fetch the webpage content
    webpage = requests.get(url, headers=my_headers)

    # Parse the webpage content with BeautifulSoup
    bs = BeautifulSoup(webpage.content, "html.parser")

    # Find all div elements with class 'tableBox'
    tables = bs.find_all("div", {"class": "tableBox"})

    # Limit to first three divs containing tables
    limited_tables = tables[:3]

    # Check if any tables were found
    if not limited_tables:
        print("No 'tableBox' divs found.")
        return

    # Loop through the first three 'tableBox' divs
    for index, table_box in enumerate(limited_tables):
        print(f"\nExtracting data from table {index + 1}:")

        # Find the table within the div
        table = table_box.find('table')
        
        # Check if a table is found inside the current div
        if not table:
            print("No table found within this tableBox.")
            continue

        # Find all rows in the table
        rows = table.find_all('tr')
        
        # Loop through each row and extract specific columns
        for row_index, row in enumerate(rows):
            # Find all cells in the current row (both <td> and <th>)
            cells = row.find_all(['td', 'th'])

            # Check if the row contains the expected number of cells (at least 4)
            if len(cells) >= 4:
                # Extract the specific columns by index
                time = cells[1].get_text(strip=True)
                match_league = cells[2].get_text(strip=True)
                tip = cells[3].get_text(strip=True)
                odds = cells[4].get_text(strip=True)

                # Print the extracted data
                print(f" {time}  {match_league} |{tip}  {odds}")

            # Skip rows that don't match the expected structure
            else:
                print(f"Skipping row {row_index + 1}: does not have the expected number of columns.")

    print("Data extraction complete.")

# Call the function
get_today_prediction()




# Function to get a random string from the list
# def get_random_string():
#     # Define the list of strings
#     odds = ['1.20', '1.15', '1.20', '1.27', '1.30', '1.35', '1.30', '1.40', '1.45']
#     return random.choice(odds)

# Example usage
# random_string = get_random_string()
# print(f'Randomly picked string: {random_string}')
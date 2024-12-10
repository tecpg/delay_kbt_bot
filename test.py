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
    url = "https://99predict.com/?dt=18-11-2024"
    my_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        # Fetch the webpage content
        response = requests.get(url, headers=my_headers)
        response.raise_for_status()

        # Parse the webpage content with BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all div elements with the class "tips-box"
        tips_boxes = soup.find_all("div", {"class": "tips-box"})
        
        # Extract the relevant text from each tips-box
        predictions = []
        for box in tips_boxes:
            # Extract league name
            league = box.find("div", {"class": "league-box"}).get_text(strip=True)
            
            # Extract match time
            time = box.find("div", {"class": "time-box"}).get_text(strip=True)
            
            # Extract teams
            teams = box.find_all("div", {"class": "match-box"})
            home_team = teams[0].get_text(strip=True)
            away_team = teams[1].get_text(strip=True)
            
            # Extract tips
            tips = box.find("span", {"class": "tips"}).get_text(strip=True)

            # Append data as a dictionary
            predictions.append({
                "league": league,
                "time": time,
                "home_team": home_team,
                "away_team": away_team,
                "tips": tips
            })

        return predictions

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

# Example usage
predictions = get_today_prediction()
for i, prediction in enumerate(predictions, 1):
    print(f"Prediction {i}:")
    print(f"  League: {prediction['league']}")
    print(f"  Time: {prediction['time']}")
    print(f"  Home Team: {prediction['home_team']}")
    print(f"  Away Team: {prediction['away_team']}")
    print(f"  Tips: {prediction['tips']}")
    print()



# Function to get a random string from the list
# def get_random_string():
#     # Define the list of strings
#     odds = ['1.20', '1.15', '1.20', '1.27', '1.30', '1.35', '1.30', '1.40', '1.45']
#     return random.choice(odds)

# Example usage
# random_string = get_random_string()
# print(f'Randomly picked string: {random_string}')
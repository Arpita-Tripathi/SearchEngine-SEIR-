import requests
from bs4 import BeautifulSoup

def extract_data(link):
    try:
        # Added timeout (5 seconds)
        response = requests.get(link, timeout=5)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Title
        if soup.title:
            print("Title:", soup.title.string.strip())
        else:
            print("No Title Found")

        # Body
        print("\nBody:")
        if soup.body:
            print(soup.body.get_text(strip=True))
        else:
            print("No Body Found")

        # Links
        print("\nLinks:")
        for a in soup.find_all("a"):
            href = a.get("href")
            if href:
                print(href)

    except requests.exceptions.Timeout:
        print("Error: Request timed out")

    except requests.exceptions.RequestException as e:
        print("Request Error:", e)

    except Exception as e:
        print("Other Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scraper.py <website>")
    else:
        website = sys.argv[1]
        extract_data(website)

import requests

def fetch_repos(username):
    url = f"https://api.github.com/users/{username}/repos"

    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching data.")
        return None

    return response.json()

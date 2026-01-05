import requests

def fetch_get_user_details(username):
    url = f"https://api.github.com/users/Rajeshpalavalasa"

    headers = {
        "User-Agent": "Python-API-Test"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print("User Name:", data["login"])
        print("Public Repos:", data["public_repos"])
    else:
        print("Failed to fetch data.")

fetch_get_user_details("octocat")

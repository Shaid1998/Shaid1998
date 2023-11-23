import requests

def get_most_used_language(owner, repo, token):
    url = f'https://api.github.com/repos/{owner}/{repo}/languages'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        languages = response.json()
        most_used_language = max(languages, key=languages.get)
        return most_used_language
    else:
        return None

if __name__ == "__main__":
    owner = input("Enter the GitHub repository owner: ")
    repo = input("Enter the GitHub repository name: ")
    token = input("Enter your GitHub personal access token: ")

    result = get_most_used_language(owner, repo, token)
    print(f"The most used language in {owner}/{repo} is: {result}")

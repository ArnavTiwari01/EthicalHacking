import requests

url = input("Enter website (with http): ")
wordlist = open("wordlist.txt").read().splitlines()

for word in wordlist:
    final_url = f"{url}/{word}"
    r = requests.get(final_url)

    if r.status_code == 200:
        print("[FOUND]", final_url)

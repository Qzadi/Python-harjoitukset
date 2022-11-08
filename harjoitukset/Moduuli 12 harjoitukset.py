import requests
query_para = input("Anna Hakusana: ")
url = f"https://api.tvmaze.com/search/shows?q={query_para}"
try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if len(data) == 0:
            print("Ei hakutuloksia")
        for item in data:
            print(f"1. Hakutulos {item['show']['name']}")
            print(f"pojot! {round(item['score']*10)},"
            f"lisätietoa {item['show']['url']}")
    else:
        print(f"viallinen osoite, error: {response.status_code}")
except requests.exceptions.RequestException as e:
    print("jotain meni vikaan!  " + str(e))

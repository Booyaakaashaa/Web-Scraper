import requests

url = input("Input the URL:\n")
req = requests.get(url)
if req.status_code != 200:
    print(f"The URL returned {req.status_code}")
else:
    with open('source.html', 'wb') as scraped:
        scraped.write(req.content)
    print("\nContent saved.")

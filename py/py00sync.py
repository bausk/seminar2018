import requests

urls = [
    'https://commons.wikimedia.org/wiki/Special:Random/File'
] * 10

for url in urls:
    response = requests.get(url)
    print('GET [{1}] Size {2}. {0}'.format(response.url,
        response.status_code, len(response.content)))

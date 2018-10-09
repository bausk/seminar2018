import requests
from concurrent.futures import Future
import threading
import queue

urls = [
    'https://commons.wikimedia.org/wiki/Special:Random/File'
] * 10

def worker(url, queue):
    result = requests.get(url)
    queue.put(result)

q = queue.Queue()

for url in urls:    
    t = threading.Thread(target=worker, args=(url, q))
    t.daemon = True
    t.start()

for _ in urls:
    response = q.get()
    print('GET {0}. Returned {1}. Size {2}'.format(response.url,
                                          response.status_code, len(response.content)))

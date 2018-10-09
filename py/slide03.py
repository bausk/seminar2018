from requests_toolbelt.threaded import pool

urls = [
    'https://commons.wikimedia.org/wiki/Special:Random/File'
] * 10

p = pool.Pool.from_urls(urls)
p.join_all()

for response in p.responses():
    print('GET {0}. Returned {1}. Size {2}'.format(response.url,
                                          response.status_code, len(response.content)))

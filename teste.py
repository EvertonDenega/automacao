import rpa as r

r.init()
r.url('https://www.google.com')
r.type('//*[@name="q"]', 'decentralisation[enter]')
print(r.read('result-stats'))
r.snap('page', 'results.png')
r.close()
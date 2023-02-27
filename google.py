import rpa as r

r.init()

r.url('http://www.google.com')

r.wait(2.0)
r.type('//*[@name="q"]', 'RPA Python[enter]')
r.wait(2.0)

r.snap('page', 'rpa_page.png')
r.wait(2.0)
r.close()
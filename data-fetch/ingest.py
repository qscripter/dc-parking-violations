import requests
import shutil
import time

months = [
  'january',
  'february',
  'march',
  'april',
  'may',
  'june',
  'july',
  'august',
  'september',
  'october',
  'november',
  'december'
]

years = [2012,2013,2014,2015,2016,2017]


def download_file(month, year):
  payload = {
    'filter[slug]': 'DCGIS::parking-violations-issued-in-%(month)s-%(year)s' % {'month': month, 'year': year},
    'include': 'organizations,groups'
  }

  r = requests.get('https://opendata.arcgis.com/api/v2/datasets', params=payload)
  print (r.url)

  if r.status_code == 200 and len(r.json()['data']) > 0:
    id = r.json()['data'][0]['id']
  else:
    print 'No file for %(year)s-%(month)s' % {'month': month, 'year': year}
    return None

  url = 'https://opendata.arcgis.com/datasets/' + id + '.csv'
  filename = '%(year)s-%(month)s' % {'month': month, 'year': year} + '.csv'
  print 'Downloading file for %(year)s-%(month)s' % {'month': month, 'year': year}

  rr = requests.get(url, stream=True)

  if rr.status_code == 200:
      with open('../data/'+filename, 'wb') as f:
        for chunk in rr.iter_content(chunk_size=1024):
          if chunk:
            f.write(chunk)



for year in years:
  for month in months:
    download_file(month, year)
    time.sleep(5)
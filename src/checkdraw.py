import json
import sys
from urllib import request

# url = 'https://app.lotto.pl/wyniki/?type=dl'
url = 'http://serwis.mobilotto.pl/mapi_v6/index.php?json=getGames'

with request.urlopen(url) as file:
  data = json.loads(file.read().decode('utf-8'))
  lotto = data['Lotto']
  tabl = lotto["numerki"].split(",")
  lottonumbers = lotto["numerki"].split(",")

  print(f'Numerki         : {lottonumbers}')
  print(f'Numer Losowania : {lotto["num_losowania"]}')
  print(f'Data losowania  : {lotto["data_losowania"]}')
  print(f'Superschansa    : {lotto["superszansa_id"]}')
  print('-' * 50)

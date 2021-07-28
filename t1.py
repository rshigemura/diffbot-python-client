from client import DiffbotClient
from config import API_TOKEN
import pprint
import time
import pandas as pd
import json

diffbot = DiffbotClient()
token = API_TOKEN

def scrap(url, token, api='article'):
    response = diffbot.request(url, token, api)
    time.sleep(1)
    if "errorCode" not in str(response):
        try:
            dic_objs = response['objects'][0]
            fields_ret = ('date', 'title', 'text', 'type', 'author')
            div_out = {k:v for (k,v) in dic_objs.items() if k in fields_ret}
            if dic_objs['type']=='image':
                return {'scrappyOk': False, 'scrappyMsg':'URL é uma imagem:{}'.format(url)}
            else:
                if not dic_objs['text']:
                    if api == 'article':
                        return scrap(url, token, api='analyze')
                    else:
                        return {'scrappyOk': False,'scrappyMsg':'Nenhum texto detectado na URL:{}'.format(url)}
                else:
                    div_out['scrappyOk'] = True
                    div_out['scrappyMsg'] = 'Sucesso'
                    return div_out
        except:
            return {'scrappyOk': False,'scrappyMsg':'Nenhuma Informação detectada na URL:{}'.format(url)}

    else:
        return {'scrappyOk': False, 'scrappyMsg':'URL Inacessível ao Scrapper:{}'.format(url)}




df = pd.read_csv('links.csv', skip_blank_lines=True)
f = open('saida.json', mode="a", encoding='utf8')

count = 1
lim = 1

for idx, l in df.iterrows():
    if count <= lim:
        #url = l['endereco_internet']
        url = 'https://camocimimparcial.blogspot.com/2021/06/policia-civil-doa-botijoes-de-gas.html'      
        out = scrap(url, token)
        #f.write(json.dumps(out, ensure_ascii=False) + '\n')
        f.write(json.dumps(out, indent=4, separators=(',', ': '), ensure_ascii=False))
        count += 1
    else:
        break

f.close()

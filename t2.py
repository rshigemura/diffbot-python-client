from client import DiffbotClient,DiffbotCrawl
from config import API_TOKEN
import pprint
import time
import pandas as pd
import json


diffbot = DiffbotClient()
token = API_TOKEN
url = "https://bandnewsfmcuritiba.com/beneficiarios-de-planos-de-saude-encaram-reajustes-no-inicio-do-ano/"
api = "analyze"
response = diffbot.request(url, token, api)
print("\nPrinting response:\n")
pp = pprint.PrettyPrinter(indent=2)
print((pp.pprint(response)))
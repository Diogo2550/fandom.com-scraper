from flask import Flask
from flask import request, make_response
import main

app = Flask(__name__)

@app.route("/")
def intro():
    url = request.args.get('url')
    if url != None:
        return scraper(url)
    
    return {
        'meta': {
            'name': 'Fandom Posts Scraper',
            'description': 'App para realizar o scraper de publicações de um blog criado na Fandom.com.',
            'limit': 'Todos os posts serão retornados.'
        },
        'routes': {
            'scraper_posts': {
                'url': '?url={pagina de categoria da Fandom}',
                'example': '?url=https://harvestmoon.fandom.com/wiki/Category:Harvest_Moon:_Friends_of_Mineral_Town'
            }
        }
    }

def scraper(url: str):
    return_data = None
    
    print(f'Coletando dados da fandom {url}...')
    if not 'fandom.com' in url:
        return { 'error': 'Formato de url inválido. A Url deve conter o domínio fandom.com' }, 400
    return_data = main.run(url)
    
    print(return_data)
    
    return {
        'data': return_data,
        '_meta': {
            'total': len(return_data)
        }
    }
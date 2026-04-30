import requests
import json

def update_cars():
    print("Avvio aggiornamento auto da ScrapingBee...")
    
    # La tua query collaudata
    ai_query = (
        "Estrai la lista di tutte le auto presenti nella pagina. "
        "Per ogni auto restituisci: modello, prezzo, chilometraggio, anno, "
        "link dell'annuncio, link dell'immagine."
    )

    response = requests.get(
        url='https://app.scrapingbee.com/api/v1',
        params={
            'api_key': '7NEPXLXMRG0C7MVFNFXUMSTCAL05NTCLJ2ORGSSQSMSVPJCQADI191I2R7T16ZS0K912B7TYYLVBW9KT',
            'url': 'https://impresapiu.subito.it/shops/54233-el-principe-di-bavaro-biagio',
            'premium_proxy': 'true',
            'country_code': 'it',
            'render_js': 'false',
            'ai_query': ai_query
        },
    )

    if response.status_code == 200:
        # Estraiamo il JSON puro dalla risposta dell'AI
        lista_auto = response.json()
        
        # Salviamo il file sovrascrivendo quello vecchio
        with open('cars.json', 'w', encoding='utf-8') as f:
            json.dump(lista_auto, f, indent=4, ensure_ascii=False)
        
        print(f"Aggiornamento completato: {len(lista_auto)} auto trovate.")
    else:
        print(f"Errore durante l'aggiornamento: {response.status_code}")

if __name__ == "__main__":
    update_cars()
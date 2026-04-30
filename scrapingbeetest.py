import requests
import json

def update_cars():
    print("Avvio estrazione dati e pulizia automatica...")
    
    ai_query = (
        "Estrai la lista di tutte le auto presenti nella pagina. "
        "Per ogni auto restituisci: modello, prezzo, chilometraggio, anno, alimentazione, tipo di cambio, "
        "link dell\'annuncio, link dell\'immagine principale."
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
        lista_auto = response.json()
        
        # --- FASE DI PULIZIA DATI ---
        for auto in lista_auto:
            # 1. Portiamo le immagini in HD (gallery-desktop-2x-auto)
            if 'link_immagine' in auto:
                auto['link_immagine'] = auto['link_immagine'].replace('rule=bigthumbs-auto', 'rule=gallery-desktop-2x-auto')
            
            # 2. Rimuoviamo il "+" dal chilometraggio, dall'anno e da altri campi se presente
            campi_da_pulire = ['chilometraggio', 'anno', 'alimentazione', 'tipo_di_cambio']
            for campo in campi_da_pulire:
                if campo in auto and isinstance(auto[campo], str):
                    auto[campo] = auto[campo].replace('+', '').strip()

        # Salviamo il file pulito
        with open('cars.json', 'w', encoding='utf-8') as f:
            json.dump(lista_auto, f, indent=4, ensure_ascii=False)
        
        print(f"Successo! {len(lista_auto)} auto elaborate con immagini HD e testo pulito.")
    else:
        print(f"Errore {response.status_code}: {response.text}")

if __name__ == "__main__":
    update_cars()

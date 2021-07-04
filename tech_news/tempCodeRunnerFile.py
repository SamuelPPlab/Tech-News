import requests
import time


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get("https://www.tecmundo.com.br/novidades", timeout=3)
    except requests.ReadTimeout:
        response = "None"
    finally:
        print(response)
        return response
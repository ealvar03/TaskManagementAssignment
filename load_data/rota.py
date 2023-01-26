import requests

ROTA_URL = "?action=get_rota"


def rota_data(BASE_URL):
    response = requests.get(url=BASE_URL + ROTA_URL)
    result_rota = response.json()
    return result_rota

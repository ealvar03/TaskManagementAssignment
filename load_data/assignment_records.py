import requests

URL_RECORDS = "?action=get_assignment_record"


def records_data(BASE_URL):
    response = requests.get(url=BASE_URL + URL_RECORDS)
    result_records = response.json()
    return result_records

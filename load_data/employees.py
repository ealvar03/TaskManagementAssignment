import requests

URL_EMPLOYEES = "?action=get_employees"


def employees_data(BASE_URL):
    response = requests.get(url=BASE_URL + URL_EMPLOYEES)
    result_employees = response.json()
    print(result_employees)
    return result_employees

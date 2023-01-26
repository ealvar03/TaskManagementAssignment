import requests

URL_PROJECTS = "?action=get_projects"


def projects_data(BASE_URL):
    response = requests.get(url=BASE_URL + URL_PROJECTS)
    result_projects = response.json()
    return result_projects

import requests
from bs4 import BeautifulSoup


def __find_rows(soup):
    return (soup
            .find('table', {'class': 'chart-table'})
            .find_all('tr'))[1:]


def __find_position(soup):
    return int(soup
               .find('td', {'class': 'chart-table-position'})
               .get_text())


def __find_authors_names(soup):
    return (soup
            .find('td', {'class': 'chart-table-track'})
            .find('span')
            .get_text()
            .strip('by ')
            .split(', '))


def __find_song_name(soup):
    return (soup
            .find('td', {'class': 'chart-table-track'})
            .find('strong')
            .get_text())


def load_chart():
    response = requests.get('https://spotifycharts.com/regional')
    page = BeautifulSoup(response.content, 'html.parser')

    return [
        {
            'position': __find_position(row),
            'authors': __find_authors_names(row),
            'song': __find_song_name(row)
        }
        for row in __find_rows(page)
    ]

# login in github

import conf
import requests
from lxml import etree

conf.LoadConfig()
conf.ProxyConnect()

url_login = 'https://github.com/login'
url_session = 'https://github.com/session'

def InitSession(): # -> requests.Session
    """
    use data from conf.py (which should have been loaded) to login github and return the session.
    return session if success
    """
    session = requests.Session()
    response = session.get(url_login, headers=conf.headers)
    html = etree.HTML(response.text)

    authenticity_token = html.xpath("//*[@name='authenticity_token']/@value")
    login_data = {
        'commit': 'Sign in',
        'utf8': '%E2%9C%93',
        'login': conf.user["username"],
        'password': conf.user["password"],
        'authenticity_token': authenticity_token
    }

    response = session.post(url_session, headers=conf.headers, data=login_data)
    if response.url == url_session: 
        raise Exception("Failed to login.")
    return session
import sys
from utils import login
from requests.sessions import session
from utils import conf
import addstar
from lxml import etree

def init():
    conf.LoadConfig()
    conf.ProxyConnect()
    return login.InitSession()

session = init()
#addstar.RandomAddstar(session, "https://github.com/orgs/apache/repositories")


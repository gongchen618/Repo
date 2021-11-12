import utils.login as login
import utils.conf as conf
import addstar
import addlabel

def init():
    conf.LoadConfig()
    conf.ProxyConnect()
    return login.InitSession()

session = init()
addlabel.CheckIssueLabel(session, "https://github.com/testofgc/test")
addstar.RandomAddStar(session, "https://github.com/orgs/apache/repositories")


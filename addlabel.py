# add bug-label for all the issues of my repo"test"
# (if one hasn't been labelled)

from utils import conf
from lxml import etree

url_issues = "https://github.com/testofgc/test/issues"
# https://github.com/testofgc/test/issues/1/show_partial?partial=issues%2Fsidebar%2Flabels_menu_content

def hasLabel(html):
    """
    check if current issue already has bug-label
    """
    label_list = html.xpath('//div[contains(@class,"discussion-sidebar-item")]//span[@class="css-truncate css-truncate-target width-fit"]/text()')
    for label in label_list:
        if label == 'bug':
            return True
    return False
    

def getToken(session, url_token):
    """
    token for label-change hidden in a url in the issue-page.
    """
    response = session.get("https://github.com" + url_token, headers=conf.headers)
    html = etree.HTML(response.text)
    return html.xpath('//input[@name="authenticity_token"]/@value')[0]

def addLabel(session, url_issue):
    """
    add bug-label for a issue.
    raise error if failed.
    """
    response = session.get(url_issue, headers=conf.headers)
    html = etree.HTML(response.text)
    if hasLabel(html):
        return

    token = getToken(session, html.xpath('//details[@id="labels-select-menu"]/details-menu/@src')[0])
    data = {
        '_method': "put",
        'authenticity_token' : token,
        'issue[labels][]': "", # just don't know why
        'issue[labels][]': 3528362640 # the id of bug-label
    }
    response = session.post(url_issue + "/labels", headers = conf.headers, data = data)    
    if (response.status_code != 200):
        raise Exception("\"" + url_issue +  "\" can't be added label.")
    print ("Success addLabel(bug) for " + url_issue)

def CheckIssueLabel(session, url_repo):
    """
    check the repo if it has issues without bug-label,
    and auto add bug-label to all of them. 
    """
    response = session.get(url_repo + "/issues", headers=conf.headers)
    html = etree.HTML(response.text)
    issue_list = html.xpath('//a[@data-hovercard-type="issue"]/@href')
    for issue in issue_list:
        addLabel(session, "https://github.com" + issue)


# add star for repos

import conf
from lxml import etree
import random

def addStar(session, url_repo):
    """
    add star for a repo whose url is url_repo.
    raise error if failed.
    """
    response = session.get(url_repo, headers=conf.headers)
    html = etree.HTML(response.text)
    token = html.xpath('//form[@class="unstarred js-social-form"]/input[@type="hidden"]/@value')
    if len(token) == 0:
        raise Exception("\"" + url_repo +  "\" is not a repo's url.")
    
    data = {
        'authenticity_token' : token[0], # take notice of the "[0]", it cost me more than an hour to solve
        'context' : 'repository'
    }
    response = session.post(url_repo + "/star", headers = conf.headers, data = data)
    if (response.status_code != 200):
        raise Exception("\"" + url_repo +  "\" can't be added star.")
    print ("Success addStar for " + url_repo)


def RandomAddstar (session, url_page):
    """
    random addstar for a page's repos
    the url given should be a repo's page
    """
    response = session.get(url_page, headers=conf.headers)
    html = etree.HTML(response.text)
    repo_list = html.xpath('//a[@itemprop="name codeRepository"]/@href')
    for repo in repo_list:
        if (random.randint(1, 3) < 2):
            addStar(session, "https://github.com" + repo)

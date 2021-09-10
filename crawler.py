import mechanize
from bs4 import BeautifulSoup
import urllib
import http.cookiejar # in python3

class WebsiteCrawler:
    def __init__(self, url, login_url, username_tag, password_tag, username, password):
        self.url = url        

        cj = http.cookiejar.CookieJar()
        browser = mechanize.Browser()
        browser.set_cookiejar(cj)
        
        # login to website
        browser.open(login_url)
        browser.select_form(nr=0)
        browser.form[username_tag] = username
        browser.form[password_tag] = password
        browser.submit()
        
        # open the desired webpage after login and get html
        response = browser.open(self.url)
        self.content = response.read()

        # create soup object, which makes parsing content easy
        self.soup = BeautifulSoup(self.content, "html.parser")
    
    """ Returns all text from the website without html tags
    """
    def getAllRepoText(self):
        return self.soup.get_text()
    
    """ Finds and returns Readme text from website
    """
    def getReadme(self):
        readme = self.soup.find("div", id="readme")
        if readme is None:
            readme = "couldn't find readme"
            return readme
        else:
            return readme.get_text()


def main():
    # Github crawler example
    
    url = "YOUR_GITHUB_REPO"
    login_url = "https://github.com/login"

    # use website inspector (firefox strg+shift+c) to find correct "name" tag for this. example:
    # <input type="text" name="login" id="login_field" class="form-control input-block js-login-field" .......>
    #                          ^^^^
    # <input type="password" name="password" id="password" class="form-control form-control input-block js-password-field" ......>
    #                              ^^^^^^^^
    username_tag = 'login'
    password_tag = 'password'
    username = 'GITHUB_USERNAME'
    password = 'GITHUB_PASSWD'

    crawler = WebsiteCrawler(url, login_url, 
                            username_tag, password_tag, username, password)
    
    print(crawler.getReadme())

if __name__ == "__main__":
    main()
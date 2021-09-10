# website-crawler-wLogin

Parses data from website html that requires authentication.  
  
## Example included for printing the readme from a github:
- Assign github repo url

        url = "YOUR_GITHUB_REPO"
- Specify username and password

        username = 'GITHUB_USERNAME'
        password = 'GITHUB_PASSWD'
- Run ``crawler.py``
- Prints the repo's readme to terminal

## Crawl data from a different website
- Change the url, username and password accordingly
- Find the appropriate ``login_url`` for the website:  
    Use the Website Inspector (f.e. ctrl+shift+c in Firefox) to find the html ``name`` tag for the input fields of the login form.  
    Example for github.com:
    ```html
    <input type="text" name="login" id="login_field" class="form-control input-block js-login-field" .......>
    <input type="password" name="password" id="password" class="form-control form-control input-block js-password-field" ......>   
    ```
- Set the input tag variables (example for github.com, see above ``name="login"`` and ``name="password"``)

        username_tag = 'login'
        password_tag = 'password'

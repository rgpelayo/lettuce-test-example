class Login:

    def __init__(self, driver):
        self.driver = driver
            
    def visit(self, url):
        self.driver.get(url)
        self.username_field = self.driver.find_element_by_id("login_username")
        self.password_field = self.driver.find_element_by_id("login_password")
        self.login_form = self.driver.find_element_by_id("login_form")        
    
    def login(self, username, password):        
        
        # Enter the username
        self.username_field.clear()
        self.username_field.send_keys(username)
        
        # enter the password
        self.password_field.clear()
        self.password_field.send_keys(password)
        
        # Sign in
        self.login_form.submit()



     
    
        
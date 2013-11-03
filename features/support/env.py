from lettuce import before, world
from selenium import webdriver

@before.all
def setup():
    # User account information
    world.username = ""
    world.password = ""

    # Make sure the login credentials are set or stop the test
    assert world.username, "\n\n*** ATTENTION: The SendGrid login credentials must be set in env.py ***\n\n"
            
    world.site_url = "http://www.sendgrid.com"
    world.login_url = world.site_url + "/login"
    world.workshop_url = world.site_url + "/docs/api_workshop.html"
    world.driver = webdriver.Firefox()
    

    

    

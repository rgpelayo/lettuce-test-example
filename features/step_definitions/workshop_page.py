# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from time import sleep

class WorkShop:
            
    def __init__(self, driver):
        self.driver = driver
        
    def visit(self, url):
        self.driver.get(url)

        # Wait for the iframe to appear
        wait = WebDriverWait(self.driver, 10)  
        iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'iframe')))
                                                     
        # Switch to the iframe
        self.driver.switch_to_frame(iframe)      

        # Define the objects - we have to use the xpath since there's no unique identifier
        self.mail_method_expand = self.driver.find_element_by_xpath("//*[@id='body-container']/ul/li[6]/h3/div[2]/ul/li[2]/a")

        # Credential fields
        self.username_field = self.driver.find_element_by_id("key")
        self.password_field = self.driver.find_element_by_id("secret")        

    def enter_credentials(self, username, password):
        self.username_field.clear()
        self.username_field.send_keys(username)
        
        self.password_field.clear()
        self.password_field.send_keys(password)
        
    def expand_mail(self):
        # Expand the mail method
        self.mail_method_expand.click()
        
        # Wait for the elements to appear
        wait = WebDriverWait(self.driver, 10)          
        self.to_field = wait.until(EC.presence_of_element_located((By.NAME, "params[to]")))
        
        # Define the objects in the mail method
        self.toname_field = self.driver.find_element_by_name("params[toname]")
        self.xsmtpapi_field = self.driver.find_element_by_name("params[x-smtpapi]")
        self.from_field = self.driver.find_element_by_name("params[from]")
        self.fromname_field = self.driver.find_element_by_name("params[fromname]")
        self.subject_field = self.driver.find_element_by_name("params[subject]")
        self.text_field = self.driver.find_element_by_name("params[text]")
        self.html_field = self.driver.find_element_by_name("params[html]")
        self.bcc_field = self.driver.find_element_by_name("params[bcc]")
        self.date_field = self.driver.find_element_by_xpath("//*[@id='body-container']/ul/li[6]/ul/li/form/table/tbody/tr[10]/td[2]/input")
        self.headers_field = self.driver.find_element_by_name("params[headers]")
        self.files_field = self.driver.find_element_by_name("params[files]")
        self.try_button = self.driver.find_element_by_id("Mail") 
                    
    def try_it(self):
        self.try_button.click() 
        
    # Return the text in the response body    
    def get_response_body(self):
        # Wait for the response header to appear
        wait = WebDriverWait(self.driver, 10)
        self.response_body_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "pre.response.prettyprint")))  
        EC.text_to_be_present_in_element(self.response_body_field, "message")
        sleep(2)  # still need to add this to wait for text to show up in the response body; otherwise, we return to quickly
        return self.response_body_field.text 
        


# -*- coding: utf-8 -*-

from lettuce import step, world
from workshop_page import WorkShop
from sign_in_page import Login

@step(u'Given I am on the SendGrid login page')
def given_i_am_on_the_sendgrid_login_page(step):
    world.login_page = Login(world.driver)
    world.login_page.visit(world.login_url) 

@step(u'Log on')
def log_on(step):
    world.login_page.login(world.username, world.password)   
        
@step(u'Given I am on the API Workshop page')
def given_i_am_on_the_api_workshop_page(step):
    world.workshop_page = WorkShop(world.driver)
    world.workshop_page.visit(world.workshop_url)

@step(u'Enter my credentials')
def enter_my_credentials(step):
    world.workshop_page.enter_credentials(world.username, world.password)

@step(u'Expand the Mail method')
def expand_the_mail_method(step):
    world.workshop_page.expand_mail()
    
@step(u'When I fill the to field with "([^"]*)"')
def fill_the_to_field_with(step, to):
    world.workshop_page.to_field.send_keys(to)
    
@step(u'When I fill the toname field with "([^"]*)"')
def fill_the_toname_field_with(step, toname):
    world.workshop_page.toname_field.send_keys(toname)
    
@step(u'When I fill the x-smtpapi field with "(.*)"')
def fill_the_x_smtpapi_field_with(step, xsmtpapi):
    world.workshop_page.xsmtpapi_field.send_keys(xsmtpapi)
    
@step(u'When I fill the from field with "([^"]*)"')
def fill_the_from_field_with(step,sender):
    world.workshop_page.from_field.send_keys(sender)
    
@step(u'When I fill the fromname field with "([^"]*)"')
def fill_the_fromname_field_with(step, fromname):
    world.workshop_page.fromname_field.send_keys(fromname)
    
@step(u'When I fill the subject field with "([^"]*)"')
def fill_the_subject_field_with(step, subject):
    world.workshop_page.subject_field.send_keys(subject)
    
@step(u'When I fill the text field with "([^"]*)"')
def fill_the_text_field_with(step, message):
    world.workshop_page.text_field.send_keys(message)
    
@step(u'When I fill the html field with "([^"]*)"')
def fill_the_html_field_with(step, html_message):
    world.workshop_page.html_field.send_keys(html_message)
    
@step(u'When I fill the bcc field with "([^"]*)"')
def fill_the_bcc_field_with(step, bcc):
    world.workshop_page.bcc_field.send_keys(bcc)
    
@step(u'When I fill the date field with "([^"]*)"')
def fill_the_date_field_with(step, date_string):
    world.workshop_page.date_field.send_keys(date_string)
    
@step(u'When I fill the headers field with "(.*)"')
def fill_the_headers_field_with(step, headers):
    world.workshop_page.headers_field.send_keys(headers)
    
@step(u'When I fill the files field with "([^"]*)"')
def fill_the_files_field_with(step, files):
    world.workshop_page.files_field.send_keys(files)
    
@step(u'Click the Try It button')
def click_the_try_it_button(step):
    world.workshop_page.try_it()
    
@step(u'Then the response body should return "([^"]*)"')
def then_i_should_receive_an_email(step, message):
    assert message in world.workshop_page.get_response_body(), "Did not find 'success' in the response body"
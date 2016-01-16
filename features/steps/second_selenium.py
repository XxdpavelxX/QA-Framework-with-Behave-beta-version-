

from behave import *
from selenium.webdriver.support.ui import Select

use_step_matcher("re")

@when('I open practiceselenium.com website.')
def step_impl(context):
    context.browser.get("http://www.practiceselenium.com/practice-form.html")

@then("I find first and last name and print the html")
def step_impl(context):
    firstname = context.browser.find_element_by_name("firstname")
    lastname = context.browser.find_element_by_name("lastname")
    print("Firstname html: ",firstname.get_attribute("outerHTML"))
    print("Lastname html: ",lastname.get_attribute("innerHTML"))

@then("I find menu and print the html")
def step_impl(context):
    menu_element = context.browser.find_element_by_link_text('Menu')
    print("Menu html:",menu_element.get_attribute("outerHTML"))

@then("I find button and print the html")
def step_impl(context):
    ok_button = context.browser.find_element_by_id('submit')
    print("Button html:",ok_button.get_attribute("outerHTML"))

@then("I find radio button male and print the html")
def step_impl(context):
    male_radio = context.browser.find_element_by_id('sex-0')
    female_radio = context.browser.find_element_by_id('sex-1')
    print("Radio Male html:", male_radio.get_attribute("outerHTML"))
    print("Radio Male html:", female_radio.get_attribute("outerHTML"))

@then("I find check box and print the html")
def step_impl(context):
    black_tea = context.browser.find_element_by_id('tea1')
    red_tea = context.browser.find_element_by_id('tea2')
    oolong_tea = context.browser.find_element_by_id('tea3')
    print("Black Tea HTML:",black_tea.get_attribute("outerHTML"))
    print("Black Tea HTML:",red_tea.get_attribute("outerHTML"))
    print("Black Tea HTML:",oolong_tea.get_attribute("outerHTML"))

@then("I find select list and print html")
def step_impl(context):
    continents_select = Select(context.browser.find_element_by_id('continents'))
    options = continents_select.options
    print("Select List options:",options)
    for option in options:
        print(option.get_attribute("outerHTML"))

@then("I find another select list and print html")
def step_impl(context):
    another_select_list = Select(context.browser.find_element_by_id('selenium_commands'))
    options = another_select_list.options
    print("Select List options:",options)
    for option in options:
        print(option.get_attribute("outerHTML"))

@then("I find div and print html")
def step_impl(context):
    div_element = context.browser.find_element_by_class_name('wsb-htmlsnippet-element')
    print("Div html:",div_element.get_attribute("outerHTML"))


@when("I open practiceselenium\.com website")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass
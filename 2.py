import sys
from selenium import webdriver
import yaml
import time

def webdriver_setup():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    return driver


def get_el_with_id(web_el, id_name):
    return web_el.find_element_by_id(id_name)

def get_els_with_id(web_el, id_name):
    return web_el.find_elements_by_id(id_name)

def get_els_with_class(web_el, class_name):
    return web_el.find_elements_by_class_name(class_name)

# fills in the first four input boxes of the application
def fill_in_first_information(list_of_fields):
    for field_div in list_of_fields:
        label_tag = field_div.find_element_by_tag_name("label")
        input_tag = field_div.find_element_by_tag_name("input")
        input_tag.send_keys(person_dict["person"][label_tag.get_attribute("for")])

def upload_files(web_el):
    # resume
    web_el.find_elements_by_xpath('//input[@type="file"]')[0].send_keys("/Users/ericsonnyboy/Desktop/Projects/greenhouseFiller/greenhouse-application-filler/TestWordDocument.docx")
    # cover letter
    web_el.find_elements_by_xpath('//input[@type="file"]')[1].send_keys("/Users/ericsonnyboy/Desktop/Projects/greenhouseFiller/greenhouse-application-filler/TestWordDocument.docx")
    # transcript
    web_el.find_elements_by_xpath('//input[@type="file"]')[2].send_keys("/Users/ericsonnyboy/Desktop/Projects/greenhouseFiller/greenhouse-application-filler/TestWordDocument.docx")


def fill_in_main_divs(web_el):
    list_of_fields = get_els_with_class(web_el, "field")
    fill_in_first_information(list_of_fields[:4])


def main_function(driver, url):
    driver.get(url)
    print(driver.find_element_by_xpath('//input[@type="file"]').get_attribute('outerHTML'))
    hell = driver.find_element_by_xpath('//input[@type="file"]/..')
    print(hell.get_attribute('outerHTML'))
    application_div = get_el_with_id(driver.find_elements_by_tag_name("body")[0], "application")
    application_form = application_div.find_elements_by_tag_name('form')[0]
    main_div = get_el_with_id(application_form, "main_fields")
    fill_in_main_divs(main_div)
    upload_files(driver)




if len(sys.argv) != 2:
    print("To run this script you must give it a url")
    sys.exit()

url = sys.argv[1]
driver = webdriver_setup()

with open("person_config.yml", "r") as file:
    person_dict = yaml.load(file.read(), Loader=yaml.FullLoader)

# must specify protocol to not get data; and you must pass in URL as a string

main_function(driver, url)



import sys
from selenium import webdriver
import requests

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
    return web_el


def main_function(driver, url):
    driver.get(url)
    # application_div = get_el_with_id(driver.find_elements_by_tag_name("body")[0], "application")
    # application_form = application_div.find_elements_by_tag_name("form")


if len(sys.argv) != 2:
    print("To run this script you must give it a url")
    sys.exit()

url = sys.argv[1]
driver = webdriver_setup()
# must specify protocol to not get data; and you must pass in URL as a string
main_function(driver, url)

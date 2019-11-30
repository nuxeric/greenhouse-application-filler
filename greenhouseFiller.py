import sys
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import yaml

def get_all_field_divs(soup_element):
    return soup_element.find_all(class_="field")

def get_form_with_id(id_name, soup_element):
    return soup_element.form.find(id=id_name)


def fill_in_main_div(soup_elements, config_dict):
    for soup_el in soup_elements:
        soup_el.find(input)
        print(soup_el.find(input))


if len(sys.argv) != 2:
    print("To run this script you must give it a url")
    sys.exit()
url = sys.argv[1]

with open("person_config.yml", "r") as file:
    person_dict = yaml.load(file.read(), Loader=yaml.FullLoader)



r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "html.parser")
soup_application = soup.body.find(id="main").find(id="application")

soup_main_field_div = get_form_with_id("main_fields" , soup_application)
main_divs = get_all_field_divs(soup_main_field_div)

soup_custom_field_div = get_form_with_id("custom_fields", soup_application)
custom_divs = get_all_field_divs(soup_main_field_div)

soup_eeoc_field_div = get_form_with_id("eeoc_fields", soup_application)
eeoc_divs = get_all_field_divs(soup_eeoc_field_div)


fill_in_main_div(main_divs, person_dict)



#browser = webdriver.Chrome()
#browser.get(url)

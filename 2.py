import sys
from selenium import webdriver
import yaml
import time

def webdriver_setup():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    #options.add_argument('--headless')
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

def fill_in_school_information(list_of_fields):
    for field_div in list_of_fields:
        label_tag = field_div.find_element_by_tag_name("label")
        label = label_tag.get_attribute("innerHTML").lower().strip()
        input_tags = field_div.find_elements_by_tag_name("input")
        input_tags[0].send_keys(person_dict["person"]["education"][label])
        time.sleep(0.5)
        driver.find_element_by_class_name("select2-match").click()

def fill_in_school_dates(list_of_fields):
    for field_div in list_of_fields:
        legend = field_div.find_element_by_tag_name("label").get_attribute("innerHTML").lower().strip()
        input_tags = field_div.find_elements_by_tag_name("input")
        input_tags[0].send_keys(person_dict["person"]["education"][legend]["month"])
        input_tags[1].send_keys(person_dict["person"]["education"][legend]["year"])



def fill_in_main_divs(web_el):
    list_of_fields = get_els_with_class(web_el, "field")
    fill_in_first_information(list_of_fields[:4])
    # skip two here because of resume and cover letter
    fill_in_school_information(list_of_fields[6:9])
    fill_in_school_dates(list_of_fields[9:])

def custom_field_filter_function(field_div, label):
    if label in person_dict["person"].keys() and (label == "linkedin profile" or "website"):
        field_div.find_elements_by_tag_name("input")[2].send_keys(person_dict["person"][label])

    if label in custom_answers_dict["custom_answers"].keys():
        select_tag = field_div.find_element_by_tag_name("select")
        options_tag_list = select_tag.find_elements_by_tag_name("option")
        for option_tag in options_tag_list:
            option = option_tag.get_attribute("innerHTML").lower().strip()
            if custom_answers_dict["custom_answers"][label] == option:
                option_tag.click()



def fill_in_custom_fields(driver):
    list_of_fields = driver.find_element_by_id("custom_fields").find_elements_by_class_name("field")
    for field_div in list_of_fields:
        try:
            label_tag = field_div.find_element_by_tag_name("label").text.lower().strip()
            # just in case there is the weird asterisk span that will throw off my config file
            label = label_tag.replace("*", "")
            label_list = label.splitlines()
            custom_field_filter_function(field_div, label_list[0].strip())
        except:
            print("label didn't match a function")

def main_function(driver, url):
    driver.get(url)
    application_div = get_el_with_id(driver.find_elements_by_tag_name("body")[0], "application")
    application_form = application_div.find_elements_by_tag_name('form')[0]
    main_div = get_el_with_id(application_form, "main_fields")
    fill_in_main_divs(main_div)
    upload_files(driver)
    fill_in_custom_fields(driver)



if len(sys.argv) != 2:
    print("To run this script you must give it a url")
    sys.exit()

url = sys.argv[1]
driver = webdriver_setup()


with open("person_config.yml", "r") as file:
    person_dict = yaml.load(file.read(), Loader=yaml.FullLoader)

with open("custom_answers_config.yml", "r") as file:
    custom_answers_dict = yaml.load(file.read(), Loader=yaml.FullLoader)
# must specify protocol to not get data; and you must pass in URL as a string
main_function(driver, url)



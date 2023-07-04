from flask import request

import requests

def format_for_api(user_input):
    user_input = user_input.lower()\
        .replace(',  +1, +2, or +3', '')\
            .replace(', ', '-')\
                .replace(' form', '')\
                    .replace(' ', '-')\
                        .replace('(', '')\
                            .replace(')', '')\
                                .replace("'", '')\
                                    .replace('/', '-')
    return user_input


def gain_user_input(form_name):
    if request.method == 'POST':
        user_input = request.form[form_name].lower().capitalize()

    elif request.method == 'GET':
        user_input = request.args.get("name").lower().capitalize()

    return user_input


def check_for_image(json_data):
    if 'image' in json_data.keys():
        image = json_data['image']

    else:
        image = None
    
    return image


def create_code_for_data_page(query_name, suffix_to_remove, form_name):

    #this sets the formated version for the query name, so it shows nice on the page
    formated_query_name = query_name.removesuffix(suffix_to_remove).capitalize()

    #test to see if user is using the input box, or the examples below the input box
    user_input = gain_user_input(form_name)
    
    #set the input for the api, as it has spesific needs(may be more, but this is all working on /monsters)
    api_regulated_input = format_for_api(user_input)

    #this grabs the data from the api, in json format
    json_data = requests.get(f'https://www.dnd5eapi.co/api/{query_name}/{api_regulated_input}').json()

    #checks for a image so it can be shown on the site
    image = check_for_image(json_data)

    #returns the data so it can be used in the site
    return user_input, json_data, image, formated_query_name


def create_code_for_name_page(query_name, suffix_to_remove):
    #this sets the formated version for the query name, so it shows nice on the page
    formated_query_name = query_name.removesuffix(suffix_to_remove).capitalize()

    #this will take the data that will be shown below the inupt box, so the user knows all of the possible inputs
    user_example_data = requests.get(f'https://dnd5eapi.co/api/{query_name}').json()['results']

    #This makes the list of all of the names of the 'user_example_data' above, and makes it into a list on the site
    namelist = [data["name"] for data in user_example_data]

    return formated_query_name, namelist
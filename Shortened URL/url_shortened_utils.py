import json
import random
import string


NEW_URL_LENGTH = 8
ALL_DATA_PATH = 'all_data.txt'


def import_data_to_dict():
    with open(ALL_DATA_PATH, 'r') as json_file:
        data_dict = json.load(json_file)
    return data_dict


def return_data_to_file(data_dict):
    with open(ALL_DATA_PATH, 'w') as my_file:
        json.dump(data_dict, my_file)


def url_exist(user_url):
    return user_url in import_data_to_dict().keys()


def get_shorten_url_from_dict(user_url):
    return import_data_to_dict()[user_url]


def get_origin_url_form_shorten_url(shorten_url):
    for key, value in import_data_to_dict().items():
        if shorten_url == value:
            return key


def shortened_url():
    # todo - check if shorten url allready exist
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(NEW_URL_LENGTH))


def add_new_url_to_dict(user_url, new_shortened_url):
    all_data_dict = import_data_to_dict()
    all_data_dict[user_url] = new_shortened_url
    return_data_to_file(all_data_dict)


def get_new_url(user_url):
    if url_exist(user_url):
        new_shortened_url = get_shorten_url_from_dict(user_url) 
    else:
        new_shortened_url = shortened_url() 
        add_new_url_to_dict(user_url, new_shortened_url)
    return new_shortened_url

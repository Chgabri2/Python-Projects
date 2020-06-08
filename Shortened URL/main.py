import json
import random
import string
import webbrowser

all_data_dict = {}
NEW_URL_LENGTH = 8


def import_data_to_dict():
    with open('all_data.txt') as json_file:
        data_dict = json.load(json_file)
    return data_dict


def return_data_to_file(data_dict):
    with open('all_data.txt', 'w') as my_file:
        json.dump(data_dict, my_file)


def url_exist(user_url):
    if user_url in all_data_dict.values():
        return True
    else:
        return False


def get_shorten_url_from_dict(user_url):
    for key in all_data_dict.keys():
        if all_data_dict[key] == user_url:
            return key


def shortened_url():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(NEW_URL_LENGTH))


def add_new_url_to_dict(user_url):
    all_data_dict[shortened_url()] = user_url


def handle_user_request(user_url):
    if url_exist(user_url):
        print("The given url already exist in our system.")
    else:
        add_new_url_to_dict(user_url)
    print('Your shortened url: %s' % (get_shorten_url_from_dict(user_url)))


def get_new_url():
    user_url = (input("Enter your url: ")).replace('"', '')  # supposed to remove the unnecessary quotes
    handle_user_request(user_url)
    return_data_to_file(all_data_dict)


if __name__ == '__main__':
    main()


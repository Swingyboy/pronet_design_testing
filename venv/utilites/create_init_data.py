import csv


def create_fields_dict(csv_data:list):
    fields = ['URL', 'mobile_URL', 'user', 'password']
    data_dict = dict(zip(fields, csv_data[1:]))
    return data_dict


def parse_csv (path_to_file:str):
    traders ={}

    with open (path_to_file) as csvfile:
        csvreader=csv.reader(csvfile, delimiter=';',quotechar = "'")
        for item in csvreader:
            fields = create_fields_dict(item)
            traders [item[0]] = fields

    return traders


def url_modify(traders_info:dict, trader:str):
    modified_url_list =[]
    trader_data = traders_info[trader]
    url_list = [trader_data['URL'], trader_data['mobile_URL']]

    for url in url_list:
        protocol, uri = url.split('//')
        modified_url = protocol + '//' + trader_data['user'] + ':' + trader_data['password'] +'@' + uri
        modified_url_list.append(modified_url)

    return modified_url_list


if __name__ == '__main__':
    traders = parse_csv('D:\my_folder\Job\pronet\credentials.csv')
    print(url_modify(traders, 'betprolive'))
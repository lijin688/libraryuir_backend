import requests
import json
import time
test_host = 'localhost:8412'
host_name = test_host


def query_book():
    url = 'http://{}/user/listpage'.format(host_name)
    data = {
        'book_name': '测试',
    }
    r = requests.get(url, params=data)
    print(r.text)


def delete_book():
    url = 'http://{}/user/remove'.format(host_name)
    data = {
        'book_name': 'book_1'
    }
    r = requests.post(url, json=data)
    print(r.text)


def modify_book():
    url = 'http://{}/user/edit'.format(host_name)
    data = {
        'id': 2,
        'name': 'book_1',
        'ctg': '2',
        'resNum': '4',
        'addr': '山东2',
        'inLibDate': '2019-11-20 00:00:00'
    }
    r = requests.post(url, json=data)
    print(r.text)


def add_book():
    url = 'http://{}/user/add'.format(host_name)
    data = {
        'name': 'book_4',
        'ctg': '2',
        'resNum': '4',
        'addr': '山东2',
        'inLibDate': '2019-11-20 00:00:00'
    }
    r = requests.post(url, json=data)
    print(r.text)

if __name__ == '__main__':
    # query_book()
    # delete_subject()
    # modify_book()
    add_book()
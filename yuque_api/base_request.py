import requests

import config.conf


def get_request(url, headers=config.conf.REQUEST_HEADERS, params=None):
    """
    发送get请求
    :param headers:
    :param url:
    :param params:
    :return:
    """
    try:
        response = requests.get(url, headers=headers, params=params)
        return response
    except Exception as e:
        print(e)
        return None


def post_request(url, headers=config.conf.REQUEST_HEADERS, data=None):
    """
    发送post请求
    :param headers:
    :param url:
    :param data:
    :return:
    """
    try:
        response = requests.post(url, headers=headers, data=data)
        return response
    except Exception as e:
        print(e)
        return None

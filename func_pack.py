import requests
import logging
import json


# 将 bytes 转换为 string
def _bytes_to_str(bytes_info):
    return bytes_info.decode("utf-8")


# 将 requests.get 或 post 的结果 result 获取到的信息转为由 dict 构成的 list
# 使用方法 :
# content = requests.get('http://23.106.158.242:30080/users')
# get_api_info(content)
def get_api_info(request_result):
    content_str = request_result.content.decode("utf-8")
    list_content = []
    # print("json.loads length=" + str(len(json.loads(content_str))))
    # 若 api 返回的是空值
    if json.loads(content_str) is None:
        # 返回空的 list
        return []
    # 否则对 api 信息进行处理
    else:
        for item in json.loads(content_str):
            list_content.append(item)
        # 返回处理好的 list
        return list_content


if __name__ == '__main__':
    '''http://23.106.158.242:30080/users'''
    content = requests.get('http://23.106.158.242:30080/users')
    print(get_api_info(content))
    pass

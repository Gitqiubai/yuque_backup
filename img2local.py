import os


# 列出当前目录下的所有文件路径,返回一个列表
def list_all_files(dir):
    """
    列出当前目录下的所有文件路径
    :param dir:
    :return:
    """
    files = []
    # 列出当前目录下的所有文件路径包括子目录
    for root, dirs, file_names in os.walk(dir):
        for file_name in file_names:
            files.append(os.path.join(root, file_name))
    return files



# 读取文件内容
def read_file(file):
    """
    读取文件内容
    :param file:
    :return:
    """
    with open(file, 'rb') as f:
        return str(f.read(),encoding='utf-8')


# 正则匹配内容
def regex_match(content, regex):
    """
    正则匹配内容
    :param content:
    :param regex:
    :return:
    """
    import re
    return re.findall(regex, content)

# 创建目录对应的图片文件夹
def create_dir(dir):
    """
    创建目录对应的图片文件夹
    :param dir:
    :return:
    """
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir

# 随机生成32位数的随机字符串
def random_str(length=32):
    """
    随机生成16位数的随机字符串
    :param length:
    :return:
    """
    import random
    import string
    return ''.join(random.sample(string.ascii_letters + string.digits, length))

# 下载图片,并保存到文件夹里
def download_img(url, dir):
    """
    下载图片,并保存到文件夹里
    :param url:
    :param dir:
    :return:
    """
    import requests
    import os
    import time
    import random
    import string
    # 获取图片名称
    img_name = random_str() + '.png'
    # 下载图片
    img = requests.get(url)
    # 写入文件
    with open(dir + '/' + img_name, 'wb') as f:
        f.write(img.content)
    return img_name

if __name__ == '__main__':
    # 读取目录下的所有文件路径
    paths = list_all_files('Note')
    print("文件总数:",len(paths))
    # 循环读取文件内容
    for path in paths:
        # 判断文件后缀是否为.md
        if path.endswith('.md'):
            print(path)
            # 读取文件内容
            content = read_file(path)
            # 正则匹配内容链接
            links = regex_match(content, r'!\[.*?\]\((.*?)\)')
            print(links)
            if len(links) != 0:
                # 创建目录对应的图片文件夹
                dir = create_dir(path.replace('.md', '.assets'))
                # 循环遍历图片链接
                for link in links:
                    # 获取图片名称
                    try:
                        # 下载图片并保存
                        imagename = download_img(link, dir)
                        # 获取当前文件夹名称
                        dir_name = os.path.basename(dir)
                        # 替换文档中的原链接
                        content = content.replace(link,  dir_name + "/" + imagename)
                        # 写入文件
                        with open(path, 'w', encoding="utf8") as f:
                            f.write(content)
                    except Exception as e:
                        print("{0}-图片下载失败:".format(links), e)


            # 输出文件路径
            print(path)
            # 输出空行
            print()
        else:
            continue


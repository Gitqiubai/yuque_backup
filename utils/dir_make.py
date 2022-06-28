# 根据传入路径在data/yuque_data_ + LOGIN 中创建文件夹
import os

import config.conf

# 创建文件夹并赋予权限
def dir_make(path):
    if not os.path.exists(config.conf.BASE_PATH + path):
        print("[INFO] 创建文件夹: " + config.conf.BASE_PATH + path)
        os.makedirs(config.conf.BASE_PATH + path,mode=0o755)
        # 修改文件夹权限为755
        os.chmod(config.conf.BASE_PATH + path, 0o755)
    return path

# 写入文件
def write_file(path, content):
    with open(config.conf.BASE_PATH + path + ".md", 'w+', encoding='utf-8') as f:
        f.write(content)
    # print("写入文件：" + config.conf.BASE_PATH + path)
    return path

# 过滤掉文件夹中的特殊字符
def filter_path(path):
    path = path.replace("/", "_")
    path = path.replace("\\", "_")
    path = path.replace("?", "_")
    path = path.replace("*", "_")
    path = path.replace("\"", "_")
    path = path.replace("<", "_")
    path = path.replace(">", "_")
    path = path.replace("|", "_")
    path = path.replace(":", "_")
    path = path.replace(".", "_")
    path = path.replace(" ", "_")

    return path
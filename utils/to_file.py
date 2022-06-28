

# 将json转为文件
def json_to_file(json_data, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(json_data)
        f.close()
    return True
# 将yml转换成json
def yml_to_json(yml_file):
    """
    将yml文件转换为json文件
    :param yml_file: yml文件路径
    :return:
    """
    import yaml
    with open(yml_file, 'r', encoding='utf-8') as f:
        yml_obj = yaml.load(f)
    return yml_obj

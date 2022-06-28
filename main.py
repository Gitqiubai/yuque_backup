import json

import utils.parse_yml
import yuque_api.base_request
import yuque_api.apis
from utils.dir_make import dir_make, write_file, filter_path
from utils.to_file import json_to_file


# 获取文档YML文件
def get_yml_file():
    # 先获取知识库中的yml数据，其中包含了所有的知识库文档和目录,保存为yml文件
    result = yuque_api.apis.get_repository_detail().text
    json_to_file(json.loads(result)['data']['toc_yml'], 'data/cache/documents.yml')


if __name__ == '__main__':

    # 1. 获取知识库配置的YML文件
    get_yml_file()
    print("[INFO] 获取知识库数据成功")
    documents = utils.parse_yml.yml_to_json('data/cache/documents.yml')
    print("[INFO] 文档总数：", len(documents))

    # 2. 创建知识库目录
    DIR_INDEX = {}
    DIRS = {}
    DEEP = 10  # 最深目录层数10

    # 2.1 建立目录索引
    for d in documents:
        DIR_INDEX.setdefault(d.get('uuid'), d.get('title'))
    for i in range(DEEP):
        for d in documents:
            if d.get("type") == "META":
                continue
            if d.get("type") == "DOC":
                continue
            if DIRS.get(d.get('parent_uuid')) != None:
                DIRS.setdefault(d.get('uuid'), DIRS.get(d.get('parent_uuid')) + "/" + filter_path(d.get('title')))
            else:
                DIRS.setdefault(d.get('uuid'), filter_path(d.get('title')))

    # 3. 创建文件目录
    for dir in DIRS:
        dir_make(DIRS.get(dir))

    # 4. 导出文档内容
    for d in documents:
        if d.get("type") == "DOC":
            try:
                content = json.loads(yuque_api.apis.get_document_detail(d.get('url')).content)['data']['body']
                if DIRS.get(d.get('parent_uuid')) != None:
                    write_file(DIRS.get(d.get('parent_uuid')) + "/" + filter_path(d.get('title')), content)
                    print("[INFO] 文档：", d.get('title'), "已保存到",
                          DIRS.get(d.get('parent_uuid')) + "/" + filter_path(d.get('title')))
                else:
                    dir_make("NOPATH")
                    write_file("NOPATH" + "/" + filter_path(d.get('title')), content)
                    print("[INFO] 目录节点类型出现问题无法找到正确路径：", d.get('parent_uuid'), d.get('title'), "内容已保存到",
                          "NOPATH" + "/" + filter_path(d.get('title')))
                    print("文档：", d.get('title'), "已保存到", "NOPATH" + "/" + filter_path(d.get('title')))
            except Exception as e:
                print("[ERROR] 写文件失败：", d.get('parent_uuid'), d.get('title'), e)

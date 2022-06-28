

# 获取知识库详情
import config.conf
import yuque_api.base_request


def get_repository_detail():
    return yuque_api.base_request.get_request('https://www.yuque.com/api/v2/repos/{0}/{1}'.format(config.conf.LOGIN,config.conf.NAMESPACE))

def get_document_detail(doc_url):
    return yuque_api.base_request.get_request('https://www.yuque.com/api/v2/repos/{0}/{1}/docs/{2}?raw=1'.format(config.conf.LOGIN,config.conf.NAMESPACE,doc_url))

if __name__ == '__main__':
    print(get_document_detail("bv3m87").text)
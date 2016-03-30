import requests
import xml.etree.ElementTree as ET

def get_ssl(api_user, api_key, api_url, client_ip):
    command = 'namecheap.ssl.getList'
    payload = {'ApiUser': api_user, 'ApiKey': api_key, 'UserName': api_user, 'Command': command, 'ClientIp': client_ip}
    r = requests.get(api_url, params=payload)
    r.encoding = 'utf-8'

    f = open('get_ssl.xml', 'w')
    f.write(r.text)
    f.close()

    answer = ET.parse('get_ssl.xml')
    root_answer = answer.getroot()
    status_str = []

    if str(root_answer.attrib.values()).strip('[]') == '\'OK\'':

        for child in root_answer[3][0]:
            status_str.append(child.attrib)
        return status_str

    else:
        return str(root_answer.attrib.values()).strip('[]')

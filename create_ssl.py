import requests
import xml.etree.ElementTree as ET

def create_ssl(api_user, api_key, api_url, client_ip, years, type_ssl):
    command = 'namecheap.ssl.create'
    payload = {'ApiUser': api_user, 'ApiKey': api_key, 'UserName': api_user, 'Command': command, 'ClientIp': client_ip,
               'Years': years, 'Type': type_ssl}
    r = requests.get(api_url, params=payload)
    r.encoding = 'utf-8'

    f = open('create_ssl.xml', 'w')
    f.write(r.text)
    f.close()

    answer = ET.parse('create_ssl.xml')
    root_answer = answer.getroot()

    if str(root_answer.attrib.values()).strip('[]') == '\'OK\'':


        for child in root_answer[3][0]:
            status_str = child.attrib
            if 'CertificateID' in status_str:
                CertID = status_str.get('CertificateID')

        return CertID

    else:
        return str(root_answer.attrib.values()).strip('[]')
import requests
import xml.etree.ElementTree as ET

def activate_ssl(api_user, api_key, api_url, client_ip, certid, nodes):
    command = 'namecheap.ssl.activate'

    try:
        f = open('server.csr', 'r')
        csr = f.read()
    except:
        print('no such file server.csr')
        exit(1)

    payload = {'ApiUser': api_user, 'ApiKey': api_key, 'UserName': api_user, 'Command': command, 'ClientIp': client_ip,
               'CertificateID': certid, 'csr': csr, 'WebServerType': 'other', 'HTTPDCValidation': 'True',
               'AdminEmailAddress': nodes.get("AdminEmailAddress"), 'AdminAddress1': nodes.get("AdminAddress1"),
               'AdminFirstName': nodes.get("AdminFirstName"), 'AdminLastName': nodes.get("AdminLastName"),
               'AdminCity': nodes.get("AdminCity"), 'AdminStateProvince': nodes.get("AdminStateProvince"),
               'AdminPostalCode': nodes.get("AdminPostalCode"), 'AdminCountry': nodes.get("AdminCountry"),
               'AdminPhone': nodes.get("AdminPhone")}
    r = requests.post(api_url, data=payload)
    #r.encoding = 'utf-8'

    f = open('activate_ssl.xml', 'w')
    f.write(r.text)
    f.close()

    answer = ET.parse('activate_ssl.xml')
    root_answer = answer.getroot()

    if str(root_answer.attrib.values()).strip('[]') == '\'OK\'':

        for child in root_answer[3][0][0]:
            status_str = child.tag
            if status_str.endswith('FileName'):
                file_name = child.text
                continue
            elif status_str.endswith('FileContent'):
                file_content = child.text
                continue

        f = open(file_name, 'w')
        f.write(file_content)
        f.close()
        return file_name

    else:
        return str(root_answer.attrib.values()).strip('[]')
import requests
import xml.etree.ElementTree as ET
from variables import *

def get_certs(api_user, api_key, api_url, client_ip, certid):

    command = 'namecheap.ssl.getInfo'

    payload = {'ApiUser': api_user, 'ApiKey': api_key, 'UserName': api_user, 'Command': command, 'ClientIp': client_ip,
               'certificateID': certid, 'returncertificate': 'true', 'returntype': 'individual'}
    r = requests.get(api_url, params=payload)
    r.encoding = 'utf-8'

    f = open('get_cert.xml', 'w')
    f.write(r.text)
    f.close()

    answer = ET.parse('get_cert.xml')
    root_answer = answer.getroot()

    if str(root_answer.attrib.values()).strip('[]') == '\'OK\'':

        for child in root_answer[3][0][0]:
            if child.tag.endswith('Certificates'):
                for x in child:
                    if x.tag.endswith('Certificate'):
                        f = open('server.ca-bundle', 'w')
                        f.write(x.text)
                        f.close()
                    elif x.tag.endswith('CaCertificates'):
                        for y in x:
                            for z in y:
                                f = open('server.ca-bundle', 'a')
                                f.write(z.text)
                                f.close()

        return root_answer

    else:
        print('get cert status: ' + str(root_answer.attrib.values()).strip('[]'))

try:
    f = open('certid.txt', 'r')
    CertID = f.read()
    f.close()
    get_certs(api_user_test,api_key_test,api_url_test,client_ip,CertID)
except:
    print('no such file certid.txt')
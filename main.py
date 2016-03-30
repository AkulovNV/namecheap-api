
from variables import *
from get_ssl import *
from create_ssl import *
from activate_ssl import *

status = get_ssl(api_user_test,api_key_test,api_url_test,client_ip)
if status == '\'ERROR\'':
    print('get ssl status: ' + status)
else:
    certID = create_ssl(api_user_test,api_key_test,api_url_test,client_ip,'1','PositiveSSL')
    if certID == '\'ERROR\'':
        print('create ssl status: ' + certID)
    else:
        f = open('certid.txt', 'w')
        f.write(certID)
        f.close

        print(activate_ssl(api_user_test,api_key_test,api_url_test,client_ip,certID,nodes))



import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[1;31mNo momento, o site não está acessível\033[m')
else:
    print('\033[1;33mConsegui acessar o site com sucesso\033[m')

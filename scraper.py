import requests

url_2019 = "http://ceouttarpradesh.nic.in/rollpdf/Form20_19/1.xls"
url_2017 = "http://ceouttarpradesh.nic.in/rollpdf/Form20_17/1.xls"
url_2014 = "http://ceouttarpradesh.nic.in/rollpdf/Form20_14/1.xls"
url_2012 = "http://ceouttarpradesh.nic.in/rollpdf/Form20_12/1.xls"
url_2009 = "http://ceouttarpradesh.nic.in/rollpdf/Form20_09/1.xls"
url_2007 = "http://ceouttarpradesh.nic.in/rollpdf/Form20_07/1.xls"

def downloader(url):
    print(f"[+] Downloading : {url}  ...")
    r = requests.get(url, allow_redirects=True)
    filename = url.split('/')[-1]
    open(filename, 'wb').write(r.content)

for i in range(10):
    url = url_2017.replace('1.xls', f'{i+1}.xls')
    # print(url)
    downloader(url)




import webbrowser
import requests as requests

if __name__ == '__main__':
    pageurl = "zseil.edu.pl"
    dateList = ["20230126","20130529","20200602"]
    #url ="http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str(date)

    for i in range(len(dateList)):
        url = "http://archive.org/wayback/available?url=" + pageurl + "&timestamp=" + str(dateList[i])
        print(url)
        response = requests.get(url)
        d = response.json()
        page = d["archived_snapshots"]["closest"]["url"]
        webbrowser.open(page)

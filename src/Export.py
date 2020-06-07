import pandas as pd


def getCorpDescription(soup, id):
    elements = soup.find_all('td', id=str(id))
    if elements:
        data = elements[0].contents
        res = []
        for i in range(len(data)):
            if (i + 2) % 2 == 0:
                res.append(data[i])
        if len(res) > 1:
            return res[1]
        location = "".join(res)
        return location
    else:
        return ""


def getUrl(soup, id):
    elements = soup.find_all('td', id=str(id))
    if elements:
        data = elements[0].contents
        url = [s for s in data if '.' in s]
        print(url[0])
        return url[0]


def writeCsv(data, file):
    if data[0] == 1:
        df = pd.DataFrame([data], columns=['id', 'name', 'category', 'CEO', 'place', 'url', 'phoneNumber'])
        df.to_csv(file)
    else:
        df = pd.DataFrame([data])
        df.to_csv(file, encoding="utf-8", mode='a', header=False)

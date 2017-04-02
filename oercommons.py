import urllib
from BeautifulSoup import *

urlroot = 'https://www.oercommons.org'
url = 'https://www.oercommons.org'
i = 1
htmls = list()
htmls1 = list()
while i <= 2:
    if i == 1:
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html)
        tags = soup('a')
        for tag in tags:
            context = tag.get('href', None)
            try:
                if context.startswith('/'):
                    print context
                    htmls.append(url+context)
                elif context.startswith('http://www.oercommons'):
                    print context
                    htmls.append(context)
            except:
                continue
            htmls1 = htmls
    else:
        temhtmls = list()
        for item in htmls1:
            html = urllib.urlopen(item).read()
            soup = BeautifulSoup(html)
            tags = soup('a')
            for tag in tags:
                context = tag.get('href', None)
                try:
                    if context.startswith('/'):
                        print context
                        temhtmls.append(url + context)
                    elif context.startswith('http://www.oercommons'):
                        print context
                        temhtmls.append(context)
                except:
                    continue
        temhtmls1 = list()
        for h in temhtmls:
                if h not in htmls:
                    temhtmls1.append(h)
        htmls1 = temhtmls1
        htmls.extend(temhtmls1)

    i = i + 1

for item in htmls:
    print item

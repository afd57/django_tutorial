import time

data = {
    'version':'Communit',
    'date': datetime.datetime.now(),
    'country': 'TR',
}
 
HTML = open("board_temp.html").read()
for i in veri:
    HTML = HTML.replace("{{ "+i+" }}",str(veri[i]))
 
print HTML

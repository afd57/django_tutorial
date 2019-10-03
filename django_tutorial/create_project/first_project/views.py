from django.http import *
from django import template

import time

def what_time_is_it(request):
    localtime = time.asctime(time.localtime(time.time()))
    return HttpResponse(localtime)


def score_board(request):
    results = (['BJK','GS','1-0'],['TS','FB','1-1'],['AS','SA','2-1'])
    s = template.Template(open('./templates/board_temp.html').read())
    b = template.Context({'items':results})
    html = s.render(b)
    return HttpResponse(html)

from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align:center">术士之战</h1>'
    line3 = '<hr>'
    line4 = '<a href = "/play/">进入游戏页面</a>'
    line2 = '<img src = "https://img0.baidu.com/it/u=2857096089,2095994689&fm=253&fmt=auto&app=138&f=JPEG?w=1070&h=500">'

    return HttpResponse(line1+line2+line3+line4)

def play(request):
    line1 = '<h1 style="text-align:center">游戏界面</h1>'
    line2 = '<a href = "/">返回主页面</a>'
    return HttpResponse(line1 + line2)





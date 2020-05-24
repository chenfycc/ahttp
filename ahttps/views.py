from django.shortcuts import render  # 导入render模块



def index(request):
    return render(request, 'index.html')  # 通过render模块把index.html这个文件返回到前端，并且返回给了前端一个变量form，在写html时可以调用这个form来展示list里的内容
def page_not_found(request):
    return render(request, 'booktest/404.html')
from django.http import HttpResponse

def home_page(request):
    print("Home Page request")
    print("------------ h1 -----------------")
    return HttpResponse("<h1>This is a home page</h1>")
from django.http import HttpResponse

def index(request):
    return HttpResponse('''
        <a href="https://google.com" target="_blank"> Go to goole </a>
        <a href="https://facebook.com" target="_blank"> Go to facebook </a>
    ''')
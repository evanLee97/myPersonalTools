from django.http import HttpResponse


def helloword(reqest):
    print('request method: ', reqest.method)
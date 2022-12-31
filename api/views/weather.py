from django.http import HttpResponse, request


def helloword(request):
    print('request method: ', request.method)
    print('request META:', request.META)
    print('request cookies', request.COOKIES)
    return HttpResponse('OK')

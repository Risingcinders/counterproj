from django.shortcuts import render, HttpResponse, redirect


def index(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 0
    context = {
        'count': request.session['counter']
    }
    return render(request, "index.html", context)


def kill(request):
    del request.session['counter']
    return redirect('/')

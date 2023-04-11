from django.shortcuts import render

# Create your views here.


def main(request):
    context = {'main' : main}
    return render(request, 'main/index.html', context)


def error_404(requset, exception):
    return render(requset, 'main/404.html', {})
from django.shortcuts import render


def about(request):
    """Функция описания проекта."""
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    """Функция свода правил проета."""
    template = 'pages/rules.html'
    return render(request, template)

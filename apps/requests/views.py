from django.shortcuts import render


def request_list(request):
    return render(request, "requests/request_list.html", {"requests": []})

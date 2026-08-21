from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import GiftRequestForm
from .models import GiftRequest


ACTIVE_STATUSES = [GiftRequest.Status.DRAFT, GiftRequest.Status.PENDING_REVIEW, GiftRequest.Status.PUBLISHED, GiftRequest.Status.CLAIMED]


def request_list(request):
    requests = GiftRequest.objects.filter(status=GiftRequest.Status.PUBLISHED).select_related("requester")
    return render(request, "requests/request_list.html", {"requests": requests})


@login_required
def create_request(request):
    active_exists = GiftRequest.objects.filter(requester=request.user, status__in=ACTIVE_STATUSES).exists()
    if active_exists:
        return render(request, "requests/request_already_exists.html")
    form = GiftRequestForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        gift_request = form.save(commit=False)
        gift_request.requester = request.user
        gift_request.currency = "EUR"
        gift_request.status = GiftRequest.Status.PENDING_REVIEW
        gift_request.save()
        return redirect("request_submitted")
    return render(request, "requests/request_form.html", {"form": form})


@login_required
def my_request(request):
    gift_request = GiftRequest.objects.filter(requester=request.user).order_by("-created_at").first()
    return render(request, "requests/my_request.html", {"gift_request": gift_request})


def request_submitted(request):
    return render(request, "requests/request_submitted.html")

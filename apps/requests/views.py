from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import GiftRequestForm
from .models import GiftRequest


def request_list(request):
    requests = GiftRequest.objects.filter(status=GiftRequest.Status.PUBLISHED).select_related("requester")
    return render(request, "requests/request_list.html", {"requests": requests})


@login_required
def create_request(request):
    active_exists = GiftRequest.objects.filter(
        requester=request.user,
        status__in=[GiftRequest.Status.DRAFT, GiftRequest.Status.PENDING_REVIEW, GiftRequest.Status.PUBLISHED, GiftRequest.Status.CLAIMED],
    ).exists()
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


def request_submitted(request):
    return render(request, "requests/request_submitted.html")

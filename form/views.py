from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "success.html")
    else:
        form = FeedbackForm()

    # 👇 pass range from 1 to 10
    return render(request, "feedback_form.html", {"form": form, "delivery_range": range(1, 11)})

from django.shortcuts import render, redirect, HttpResponse
from review_system.models import Review, User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def write_review(request):
    if request.method == "POST":
       
        title = request.POST.get("title")
        context = request.POST.get("context")
        user = request.user

        Review(
            title=title,
            context=context,
            author=user
        ).save()

        return redirect("reviews_list")
    else:
        return render(
            request,
            "write_review.html",
            context={}
        )
        

def get_all_reviews(request):
    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
        "request": request
    }
    
    return render(request, "review_list.html", context)


def create_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("reviews_list")
        else:
            return HttpResponse("Unexpected error happened!")
    else:
        form = UserCreationForm()
        context = {
            "form": form
        }
        return render(
            request,
            "register_form.html",
            context
        )
    
def login_form(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("reviews_list")
    else:
        form = AuthenticationForm()
        context = {
            "form": form
        }
        return render(
            request,
            "login_page.html",
            context
        )
        
from django.shortcuts import render,redirect , get_object_or_404
from .models import Tweet
from .forms import TweetFrom,UserRegistrationForm 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from django.http import HttpResponse
from django.db.models import Q



# Create your views here.

def tweet_list(request):
    tweets = Tweet.objects.all()
    return render(request,'tweet_list_page.html',{'tweets':tweets})

@login_required
def create_tweet(request):
    if request.method == 'POST':
        form = TweetFrom(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit = False)
            tweet.user = request.user
            tweet.save()
            return redirect('twet_list')
            
    else:
        form = TweetFrom()
    return render(request,'create_tweet_form.html',{'form':form})

@login_required
def tweet_edit(request ,tweet_id):
    tweet = get_object_or_404(Tweet , pk = tweet_id , user = request.user)
    if request.method == 'POST':
        form = TweetFrom(request.POST , request.FILES , instance = tweet)
        if form.is_valid():
            tweet = form.save(commit = False)
            tweet.user = request.user
            tweet.save()
            return redirect('twet_list')
    else:
        form = TweetFrom(instance = tweet)
    return render(request,'create_tweet_form.html',{'form':form})


@login_required
def tweet_delete(request , tweet_id):
    tweet = get_object_or_404(Tweet , pk = tweet_id, user = request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('twet_list')
    return render(request , 'tweet_delet_page.html',{'tweet':tweet})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('twet_list')
    else:
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log in the user
            return redirect('twet_list')  # Replace 'home' with your desired redirect URL
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return render(request, 'registration/logged_out.html',)


def text_search(request):
    if request.method == 'POST':
        text = request.POST['search1']
        tweets = Tweet.objects.filter(Q(text__icontains = text) | Q(user__username__icontains = text))
        if tweets:
            return render(request,'tweet_list_page.html',{'tweets':tweets})


    return render(request,'tweet_list_page.html',{'tweets':tweets})

        
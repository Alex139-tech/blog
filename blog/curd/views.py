from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Post, Comment, Reply
from .forms import PostForm, CommentForm, ReplyForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import JsonResponse

# post list views
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # ✅ 'date' ki jagah 'created_at'
    return render(request, 'post/post_list.html', { 'posts': posts })

# Post Create View
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')  # Redirect to the post_list page after creating post
    else:
        form = PostForm()
    return render(request, 'post/post_form.html', {'form': form})

# post delete views 
def delete_post(request,post_id):
    post = get_object_or_404(Post,pk=post_id,user=request.user)
    if request.method == 'POST':
     post.delete()
     return redirect(reverse('post_list'))
    return render(request,"post/conform_delete_post.html",{'post':post})


# edite post views 
def edite_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id, user=request.user)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect(reverse("post_list"))  # Redirect after saving

    else:
        form = PostForm(instance=post)  # Corrected instance

    return render(request, 'post/post_form.html', {'form': form})  # Corrected context key




# Post Detail View (showing)
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    comment_form = CommentForm()
    reply_form = ReplyForm()
    return render(request, 'post/post_detail.html', {
        'post': post, 
        'comments': comments, 
        'comment_form': comment_form,
        'reply_form': reply_form
    })

# Comment Add View
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)
    return redirect('post_detail', post_id=post.id)

# Reply Add View
@login_required
def add_reply(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.comment = comment
            reply.save()
            return redirect('post_detail', post_id=comment.post.id)
    return redirect('post_detail', post_id=comment.post.id)

# Register Form (Customized)
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            login(request, user)  
            return redirect('home')  # Redirect to home after successful registration
    else:
        form = RegisterForm()
    
    return render(request, "registration/register.html", {"form": form})

# Login Page Function
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')

            if next_url:
                return redirect('post_list')  # Redirect to the next page (e.g., post_create or post_list)
            else:
                return redirect('home')  # Default redirect after login
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'registration/login.html')



# loggout function define 
def custom_logout(request):
    logout(request)
    return redirect('home')

# contact page 
def contact(request):
    return render(request,"contact.html")

# about page
def about(request):
    return render(request,"about.html")


# curd home page
def curd(request):
    return HttpResponse("alexa comming to my website ")


# searching views 
def search_results(request):
    query = request.GET.get('q', '')
    if query:
        results = Post.objects.filter(text__icontains=query)[:5]  # 5 Results show karega
        data = [{"id": post.id, "title": post.title} for post in results]
        return JsonResponse(data, safe=False)
    return JsonResponse([], safe=False)

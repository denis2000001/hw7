from django.shortcuts import render
from posts.models import Post, Comment
from posts.forms import PostForms, CommentForms
from django.http import HttpResponse
from django.shortcuts import redirect
from posts.constants import PAGINATION_LIMIT

def get_user_from_request(request):
    return request.user if not request.user.is_anonymous else None

def main(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        page = int(request.GET.get('page', 1))
        start_post = (len(posts) // ((len(posts) // PAGINATION_LIMIT) + 1)) * page - 1 if page > 1 else 0
        end_posts = start_post + PAGINATION_LIMIT
        data = {
            "posts": posts[start_post:end_posts],
            'user': get_user_from_request(request),
            'pages': range(1, (posts.__len__() // PAGINATION_LIMIT) + 1)
        }

        return render(request, 'posts.html', context=data)

def post_detail(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)
        comments = Comment.objects.filter(post=post)
        data = {
            'post': post,
            'comments': comments,
            'comment_form': CommentForms,
            'user': get_user_from_request(request)
                }
        return render(request, 'detail.html', context=data)

    if request.method == 'POST':
        form = CommentForms(request.POST)
        if form.is_valid():
            Comment.objects.create(
                author=form.cleaned_data.get('author'),
                text=form.cleaned_data.get('text'),
                post_id=id
            )
            return redirect(f'/posts/{id}/')
        else:
            return render(request, 'detail.html', context={
                'comment_form': form,
                'user': get_user_from_request(request)
            })

def create_post(request):

    if request.method == 'GET':
        if get_user_from_request(request):
            return render(request, 'create_post.html', context={
                'post_form': PostForms,
                'user': get_user_from_request(request)})
        else:
            return redirect('/')

    if request.method == 'POST':
        form = PostForms(request.POST)
        if form.is_valid():
            Post.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                stars=form.cleaned_data.get('stars'),
                type=form.cleaned_data.get('type')
            )
            return redirect('/')
        else:
            return render(request, 'create_post.html', context={
                'post_form': form,
                'user': get_user_from_request(request)
            })

def edit_post(request, id):
    if request.method == 'GET':
        return render(request, 'edit_post.html', context={
            'edited_post_form': PostForms,
            'id': id
        })
    if request.method == 'POST':
        form = PostForms(request.POST)
        if form.is_valid():
            post = Post.objects.get(id=id)
            post.title = form.cleaned_data.get('title')
            post.description = form.cleaned_data.get('description')
            post.type = form.cleaned_data.get('type')
            post.date = form.cleaned_data.get('date')
            post.stars = form.cleaned_data.get('stars')
            post.save()
            return redirect('/')
        else:
            return render(request, 'edit_post.html', context={
                'edited_post_form': form,
                'id': id
            })
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

# Postのリストを表示する関数
def post_list(request):
    # データベースからクエリを取得する(sql)
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


# PostのURLを取得する関数
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# PostFormのview
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        # is_valid（バリデートメソッド）
        if form.is_valid():
          post = form.save(commit=False)
          post.author = request.user
          post.published_date = timezone.now()
          post.save()
          return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


# Postの編集ページ
def post_edit(request, pk):
    # pk=pkでパラメーターの取得
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            # formに入力された値をpostに保存
            post = form.save(commit=False)
            post.auth = request.user
            post.published_date = timezone.now()
            post.save
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})




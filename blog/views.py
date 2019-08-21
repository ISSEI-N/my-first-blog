from django.shortcuts import render

# Postのリストを表示する関数
def post_list(request):
    return render(request, 'blog/post_list.html', {})

# Create your views here.

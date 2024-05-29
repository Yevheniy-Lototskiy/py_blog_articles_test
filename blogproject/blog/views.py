from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm


def article_list(request):
    articles = Article.objects.all()
    return render(request, "blog/article_list.html", {"articles": articles})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "blog/article_detail.html", {"article": article})


@login_required
def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("article_list")
    else:
        form = ArticleForm()
    return render(request, "blog/article_form.html", {"form": form})


@login_required
def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("article_list")
    else:
        form = ArticleForm(instance=article)
    return render(request, "blog/article_form.html", {"form": form})


@login_required
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect("article_list")
    return render(request, "blog/article_confirm_delete.html", {"article": article})

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import pgettext_lazy

from .models import Book,Collection,CollectionBook
from . import BookAvailablityType,BookStatus
from .forms import CollectionForm,CollectionBookForm


@login_required(login_url="/account/login/")
def book_list(request):
    book_list = Book.objects.all()
    ctx  = {"book_list":book_list}
    return render(request, 'book_list.html',ctx)

        
@login_required(login_url="/account/login/")
def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    ctx = {"book": book}
    return render(request, "book_details.html", ctx)


@login_required(login_url="/account/login/")
def collection_list(request):
    collection_list = Collection.objects.all()
    ctx  = {"collection_list":collection_list}
    return render(request, 'collection_list.html',ctx)

    

@login_required(login_url="/account/login/")
def collection_create(request):
    collection = Collection()
    return _collection_edit(request, collection)


@login_required(login_url="/account/login/")
def collection_update(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    return _collection_edit(request, collection)


@login_required(login_url="/account/login/")
def _collection_edit(request, collection):
    form = CollectionForm(request.POST or None, instance=collection,user=request.user)
    if form.is_valid():
        form.save()
        msg = pgettext_lazy("Dashboard message", "Saved collection")
        messages.success(request, msg)
        return redirect("collection-details", pk=collection.pk)
    ctx = {"collection": collection, "form": form}
    return render(request, "collection_form.html", ctx)
    


@login_required(login_url="/account/login/")
def collection_details(request,pk):
    collection = get_object_or_404(Collection,pk=pk)
    collection_book = CollectionBook()
    return _collection_book_edit(request,collection,collection_book)



@login_required(login_url="/account/login/")
def _collection_book_edit(request,collection,collection_book):
    form = CollectionBookForm(request.POST or None, instance=collection_book,collection=collection)
    if form.is_valid():
        collection_book = form.save()
        msg = pgettext_lazy("Dashboard message", "Saved collection Book")
        messages.success(request, msg)
        return redirect("collection-details", pk=collection.pk)
    collection_book_list = CollectionBook.objects.filter(collection=collection)
    ctx = {"collection": collection, "form": form,"collection_book_list":collection_book_list}
    return render(request, "collection_details.html", ctx)
    


@login_required(login_url="/account/login/")
def collection_book_remove(request,book_pk):
    book = get_object_or_404(Book,pk=book_pk)
    collection_book = CollectionBook.objects.get(book=book)
    collection_book.delete()
    collection_book = CollectionBook()
    return _collection_book_edit(request,collection_book.collection,collection_book)

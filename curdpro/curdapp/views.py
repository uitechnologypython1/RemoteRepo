from django.shortcuts import render
from .models import ProductData
from .forms import ProductInsertForm,ProductUpdateForm,ProductDeleteForm
from django.http.response import HttpResponse
def main_page(request):
    return render(request,'main_page.html')
def product_insert_view(request):
    if request.method=='POST':
        iform = ProductInsertForm(request.POST)
        if iform.is_valid():
            product_id = request.POST.get('product_id')
            product_name = request.POST.get('product_name')
            product_cost = request.POST.get('product_cost')
            product_color = request.POST.get('product_color')
            product_class = request.POST.get('product_class')
            data = ProductData(
                product_id = product_id,
                product_name = product_name,
                product_cost = product_cost,
                product_color = product_color,
                product_class = product_class
            )
            data.save()
            iform = ProductInsertForm()
            return render(request,'insert.html',{'iform':iform})
        else:
            return HttpResponse('user invalid data')
    else:
        iform = ProductInsertForm()
        return render(request,'insert.html',{'iform':iform})

def product_retrieve_view(request):
    products = ProductData.objects.all()
    return render(request,'retrieve.html',{'products':products})


def product_update_view(request):
    if request.method=='POST':
        uform = ProductUpdateForm(request.POST)
        if uform.is_valid():
            product_id = request.POST.get('product_id')
            product_cost = request.POST.get('product_cost')
            pid = ProductData.objects.filter(product_id = product_id)
            if not pid:
                return HttpResponse('product is not available')
            else:
                pid.update(product_cost = product_cost)
                uform = ProductUpdateForm()
                return render(request,'update.html',{'uform':uform})
        else:
            return HttpResponse('user invalid data')
    else:
        uform = ProductUpdateForm()
        return render(request,'update.html',{'uform':uform})


def product_delete_view(request):
    if request.method == 'POST':
        dform = ProductDeleteForm(request.POST)
        if dform.is_valid():
            product_id = request.POST.get('product_id')
            pid = ProductData.objects.filter(product_id = product_id)
            if not pid:
                return HttpResponse('product is not available')
            else:
                pid.delete()
                dform = ProductDeleteForm()
                return render(request,'delete.html',{'dform':dform})
        else:
            return HttpResponse('user invalid data')
    else:
        dform = ProductDeleteForm()
        return render(request,'delete.html',{'dform':dform})

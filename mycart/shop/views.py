from django.shortcuts import redirect, render
from django.http import HttpResponse , HttpResponseRedirect
from .forms import ShopForm
from.models import Product


def index(request):
        if request.method == "POST":
                
                form = ShopForm(request.POST,request.FILES)

                if form.is_valid():
                    form.save()
                    return redirect('in')
        else:
            form = ShopForm()


        Products = Product.objects.all()
        
        return render(request, "shop/shop.html",{'form':form,'Products':Products})
       

def about(request):
      return HttpResponse("we are at about")

def contact(request):
      return HttpResponse("we are at contact")

def tracker(request):
      return HttpResponse("we are at tracker")

def search(request):
      return HttpResponse("we are at search")

def prodView(request):
      return HttpResponse("we are at prodview")  

def cheakout(request):
      return HttpResponse("we are at cheakout")   
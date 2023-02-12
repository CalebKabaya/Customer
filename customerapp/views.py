from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Customer,Account,Cards
from .serializers import CustomerSerializer,CardSerializer,AccountSerializer
import requests
from django.shortcuts import redirect
from .forms import AddCustomerForm,AccountForm
# Create your views here.

def customers(request):
    customers=Customer.objects.all()
    context= {
       'customers':customers

    }
    # response= requests.get('http://customer-production.up.railway.app/api/customer/')
    # customers=response.json()
    return render(request,'customer.html',context)

def addcustomer(request):

    return render(request,'addcustomer.html',)

class CustomersViewSet(viewsets.ModelViewSet):
    queryset =Customer.objects.all()
    serializer_class=CustomerSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset=Account.objects.all() 
    serializer_class=AccountSerializer

    def perform_create(self, serializer):
        account= serializer.save()
        customer=Customer.objects.get(id=self.request.data.get('customer_id'))
        account.customer=customer
        account.save()
        # return super().perform_create(serializer)

    def perform_update(self, serializer):
        account=Account.object.get(id=self.request.data.get('id'))
        if self.request.data.get('top_up'):
            account.balance +=float(self.request.data.get('top_up'))
        if self.request.data.get('withdrawal'):
            account.balance -=float(self.request.data.get('withdrawal'))
        serializer.save()    

        # return super().perform_update(serializer)    

class CardViewSet(viewsets.ModelViewSet):
    queryset= Cards.objects.all()
    serializer_class= CardSerializer



def addcustomer(request):
    if request.method == 'POST':
        form = AddCustomerForm(request.POST, request.FILES)
        if form.is_valid():
            newcustomer = form.save(commit=False)
            newcustomer.user=request.user
            newcustomer.save()
            
        return redirect('/')
    else:
        form = AddCustomerForm()
    try:
        posts=Customer.objects.all() 
        posts=posts[::-1]
    except Customer.DoesNotExist:
        posts=None

    context = {
        'form':form,
    }
    return render(request,'addcustomer.html', context) 

def viewcustomer(request,customer_id):
    customers = Customer.objects.get(id=customer_id)
    account = Account.objects.filter(customer=customers)
    # mypost=Post.objects.filter(hood=customer)

    if request.method == 'POST':
        form = AccountForm(request.POST, request.FILES)
        if form.is_valid():
            newaccount = form.save(commit=False)
            newaccount.user=request.user
            newaccount.save()
            
        return redirect('/')
    else:
        form = AccountForm()
    try:
        posts=Account.objects.all() 
        posts=posts[::-1]
    except Account.DoesNotExist:
        posts=None

    context = {
        'form':form,
        'account':account,
        'customers':customers
    }
    return render(request,'account.html', context) 

# def create_post(request,customer_id):

#     hood = NeighbourHood.objects.get(id=customer_id)
#     if request.method == 'POST':
#         post_form = PostForm(request.POST)
#         if post_form.is_valid():
#             post = post_form.save(commit=False)
#             post.hood = hood
#             post.user = request.user.profile
#             post.save()
#             return redirect('newpost', hood.id)
#     else:
#         post_form = PostForm()
#     params={
#         'post_form': post_form,
#         'hood':hood
#     }    
#     return render(request, 'viewhood.html', params)       
from django.shortcuts import render
from django.http import HttpResponse
from store.models import *
import datetime
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
def index(request):
    context={}
    return render(request, 'store/index.html', context)

def placeView(request):
    context={
     'place': Restaurant.objects.order_by('place').values('place').distinct()
    }
    
       

    return render(request, 'store/cities_view.html', context)

def restaurants_view(request,qcity):
    
    context={
     'restaurants': Restaurant.objects.filter(place=qcity)
    }
    return render(request, 'store/restaurants_list.html', context)

def restaurant_foods(request,rt):
    tmp=Restaurant.objects.get(pk=rt)
    FoodOrder.objects.all().delete()
    food_categories=Food.objects.filter(restaurant=tmp).order_by('category').values('category').distinct()
    fcat_list=[]
    for fcat in food_categories:
        fcat_list.append(fcat['category'])

    context={
    'rid':rt,
    'restaurant_foods':Food.objects.filter(restaurant=tmp).order_by('-sale'),
    'fcat_list':fcat_list,
    }
    return render(request, 'store/restaurant_foods.html', context)

def profileView(request):
    context = {'user': request.user}
    return render(request, 'store/profile.html', context)

def login(request):
    return HttpResponse("")

@csrf_exempt
@login_required
def food_cart(request):
    
    response_data={
        'message':None,

    }
    food_id=request.POST['food_id']
    amt = request.POST['amt'] 
    
    instnc=Food.objects.get(pk=food_id)
    try:
        tmp=FoodOrder.objects.get(food=instnc)
        
        tmp.total_amt=amt
        tmp.save()          
        response_data['message']=0
    except:     
        
        
        FoodOrder.objects.create(food=instnc,order_time=datetime.datetime.now(),customer=request.user,total_amt=amt)     
        response_data['message']=1
    

    return JsonResponse(response_data)

@csrf_exempt
@login_required
def checkout(request):
    orders=FoodOrder.objects.all()
    net_amt=0
    order_list=[]

    for order in orders:
        nsale=order.food.sale+int(order.total_amt)
        order.food.sale=nsale
        order.food.save()
        mrpf=order.food.mrp
        new_amt=mrpf*order.total_amt
        net_amt=net_amt+new_amt
        if order.total_amt > 0:
            order_list.append(order.food.name)
        rname=order.food.restaurant.name
        rid=order.food.restaurant.pk
        odate=order.order_time

    PastOrders.objects.create(foodlist=order_list,customer2=request.user,cost=net_amt,restname=rname,order_date=odate)
    context={
        'net_amt':net_amt,
        'order_list':order_list,
        'rid':rid,
    }    
    return render(request, 'store/checkout.html', context)     

@login_required
def pastView(request):
    customer3=request.user
    tmp=PastOrders.objects.filter(customer2=customer3).order_by('order_date')
    
    context={
        'order_list':tmp,
        
    }

    return render(request, 'store/pastorders.html',context)  

@csrf_exempt
@login_required
def rate_restaurant(request):
    response_data={
        'message':None,

    }
    rid=request.POST['rid']
    rating=request.POST['rating']
    try:
        instnc=Restaurant.objects.get(pk=rid)        
        instnc.total_rating = instnc.total_rating + int(rating)        
        instnc.total_users = instnc.total_users + int(1)
        instnc.rating=instnc.total_rating/instnc.total_users
        instnc.save()
        response_data['message'] = 1
    except:
        response_data['message'] = 0
                

    return JsonResponse(response_data)
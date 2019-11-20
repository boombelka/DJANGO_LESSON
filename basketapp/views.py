from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import BasketSlot
from mainapp.models import Product

def basket_add(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    basket_slot = BasketSlot.objects.filter(user=request.user, product=product).first()
    if basket_slot:
        basket_slot.quontity +=1
        basket_slot.save()
    else:
        basket_slot = BasketSlot(user=request.user, product=product)
        basket_slot.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def basket_remove(request):
    product = get_object_or_404(Product, pk=product_pk)
    basket_slot = BasketSlot.objects.filter(user=request.user, product=product).first()
    if basket_slot:
        if basket_slot.quontity > 1:
            basket_slot.quontity -= 1
            basket_slot.save()
    else:
        basket_slot = BasketSlot(user=request.user, product=product)
        basket_slot.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

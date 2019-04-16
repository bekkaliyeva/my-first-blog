from django.shortcuts import render,get_object_or_404, get_list_or_404,redirect
from .models import feedback
from .models import needforvideo
from .models import product
from django.http import HttpResponse
from .forms import RegistrationForm


def index(request):
	needforvideos=needforvideo.objects.filter(title='back3')
	feedbacks=feedback.objects.all()
	return render(request, 'blog/index.html', {"video":needforvideos,"feedback":feedbacks})


#cart
def cart(request):
	cart=request.session.get('cart',{})
	for prod in cart:
		list[prod.title]=product.objects.filter(id=prod.title)
	return render(request, 'blog/cart.html', {"list":list} )



#add to cart
def addTOcart(request,prod_id):
	cart=request.session.get('cart',{})
	cart[prod_id]=1
	request.session['cart'] = cart
	return render(request, 'blog/cart.html', {} )


#for check
def wrapper(request):
	return render(request, 'blog/wrapper.html', {} )


def products(request,type,order):
	if type=="tort":
		if order=="chip":
			products=get_list_or_404(product.objects.order_by('price'),type=1)
		else:
			products=get_list_or_404(product.objects.order_by('-price'),type=1)
	elif type=="konfeta":
		if order=="chip":
			products=get_list_or_404(product.objects.order_by('price'),type=2)
		else:
			products=get_list_or_404(product.objects.order_by('-price'),type=2)
	elif type=="pirog":
		if order=="chip":
			products=get_list_or_404(product.objects.order_by('price'),type=3)
		else:
			products=get_list_or_404(product.objects.order_by('-price'),type=3)
	elif type=="desert":
		if order=="chip":
			products=get_list_or_404(product.objects.order_by('price'),type=4)
		else:
			products=get_list_or_404(product.objects.order_by('-price'),type=4)
	elif type=="domash":
		if order=="chip":
			products=get_list_or_404(product.objects.order_by('price'),type=5)
		else:
			products=get_list_or_404(product.objects.order_by('-price'),type=5)

	return render(request, 'blog/products.html', {"prods":products, "type":type} )



#registration
def register(request):
	if request.method == 'POST':
		form=RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account')

	else:
		form=RegistrationForm()
		return render(request, 'registration/register.html', {'form':form} )





#doesn't work
def quickview(request):
	try:
		prod=product.objects.filter(id=request.id)
		response = {
			'prod': prod
		}
	except:
		response = {
			'prod': None,
			'error':1
		}

	return HttpResponse(response, mimetype='application/json')

from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/index.html', {}
    	)
def account(request):
	return render(request, 'blog/account.html', {} )


def wishlist(request):
	return render(request, 'blog/wishlist.html', {} )

def checkout(request):
	return render(request, 'blog/checkout.html', {} )

def cart(request):
	return render(request, 'blog/cart.html', {} )

def wrapper(request):
	return render(request, 'blog/wrapper.html', {} )

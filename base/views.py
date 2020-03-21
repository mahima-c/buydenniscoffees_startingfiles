from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

# Create your views here.
import stripe
stripe.api_key = "sk_test_PCgOc9qmyp5CBluQomn2Oqn100MzcTYVHQ"

def index(request):
	return render(request, 'base/index.html')


def charge(request):
	
	if request.method == 'POST':
		print('Data:', request.POST)


		amount = int(request.POST['amount'])
		customer = stripe.Customer.create(
			email=request.POST['email'],
			name=request.POST['nickname'],
			source=request.POST['stripeToken']


		)
		charge = stripe.Charge.create(
			customer=customer,
			amount=amount*100,
			currency='usd',
			description="donation"

		)

	return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
	amount = args
	return render(request, 'base/success.html', {'amount':amount})
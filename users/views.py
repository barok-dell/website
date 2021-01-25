from django.shortcuts import render,redirect


def homepage(request):
	return render(request,'base.html')
def reservation(request):
	return render(request,'reservation.html')











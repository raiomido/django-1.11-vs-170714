from django.shortcuts import render

def index(request):
	context = {
		"title": "Users"
	}
	return render(request, "users/base.html", context)

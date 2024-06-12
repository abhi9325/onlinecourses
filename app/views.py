from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import add_courses
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

# Create your views here.
def index(request):
    Data =add_courses.objects.all()
    return render(request,'index.html',{"Data":Data})

def admin_dashboard(request):
    return render(request,'admin_dashboard.html')



def Manage_Feedback(request):
    return render(request,'Manage_Feedback.html')

def Manage_Enquiry_details(request):
    return render(request,'Manage_Enquiry_details.html')

def feedback(request):
    return render(request,'feedback.html')

def enquiry(request):
    return render(request,'enquiry.html')
#course
def Add_courses(request):
    return render(request,'add_courses.html')

def addCourse(request):
    if request.method == "POST":
        Course_name=request.POST["Course_name"]
        Details= request.POST["Details"]
        Fees=request.POST["Fees"]
        Duration=request.POST["Duration"]
        Image=request.POST["Image"]
        Mode=request.POST["Mode"]
        data=add_courses(Course_name=Course_name,Details=Details,Fees=Fees,Duration=Duration,Image=Image,Mode=Mode)
        data.save()
        
        return redirect("/Manage_Courses")
    else:
        
        return redirect("/Manage_Courses")
#course list
def Manage_Courses(request):
    Data =add_courses.objects.all()
    return render(request,"Manage_Courses.html",{"Data":Data})
    

def Register_page(request):
    return render(request,"Register_page.html")

def detail(request, pk):
    obj = get_object_or_404(add_courses, pk=pk)
    #reviews = Review.objects.filter(product=obj).order_by('-created_at')  # Get reviews for the product
    return render(request, 'detail.html', {'obj': obj, 'product_name': obj.name, 'product_price': obj.price,})

class BooksListView(ListView):
    model = add_courses
    template_name = 'index.html'


class BooksDetailView(DetailView):
    model = add_courses
    template_name = 'detail.html'
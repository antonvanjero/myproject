from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def index1(request):
    return HttpResponse("hello world, you are at blog  456789")

def contact_view(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            print(name,email,message)
            form.save()
            return redirect('contact_success')
    else:
        form=ContactForm()
    return render(request,'myapp/contact.html',{'form':form})

def contact_success(request):
    return render(request,'myapp/success.html')

def demo(request):
    return HttpResponse('hello world')
def sample(request):
    return HttpResponse('<h1>hi<h1>')

def new_page(request):
    return render(request,'myapp/hello_block.html',{'name':'abc','age':'25'})

def students(request):
    students=[{'name':'arun','marks':85,'city':'chennai'},
              {'name':'bala','marks':40,'city':'madurai'},
              {'name':'kumar','marks':92,'city':'chennai'},
              {'name':'devi','marks':55,'city':'trichy'},
              {'name':'latha','marks':30,'city':'madurai'}
              ]
    return render(request,'myapp/students.html',{'students':students})


def arrays(request):
    numbers=[10,25,30,45,50,75,90]
    return render(request,'myapp/arrays.html',{'numbers':numbers})

def reg_form(request):
    return render(request,'myapp/formsbs.html')

from .models import Student

def add_student(request):
    Student.objects.create(name='kumar',marks=65,subject='english')
    return HttpResponse("student added successfully")

def update_student(request):
    student=Student.objects.get(id=3)
    student.name="joshua"
    student.save()
    return HttpResponse("updated successfully")

def delete_student(request):
    student=Student.objects.get(id=2)
    student.delete()
    return HttpResponse("Student deleted successfully")

from django.db.models import Count, Avg, Max, Min

def student_data(request):
    filtered=Student.objects.filter(marks=80)
    sorted=Student.objects.order_by('marks')
    summary=Student.objects.aggregate(
        total=Count('id'),
        average=Avg('marks'),
        highest=Max('marks'),
        lowest=Min('marks')
    )

    return render(request,'myapp/student_data.html',{'filtered':filtered,'sorted':sorted,'summary':summary})

def blog(request):
    return render(request,'myapp/blog.html')
def blog1(request,blog_id):
#    blog_id=blog_id
    return render(request,'myapp/blog1.html',{'blog_id':blog_id})

from .models import Product
#def product_list(request):
  #  products=Product.objects.all()
   # return render(request,'myapp/product.html',{'products':products})

def add_product(request):
    Product.objects.create(name='soap',price=40,description='medical purpose')
    return HttpResponse('product added succesfully')

def send_email_view(request):
    send_mail(
        subject = 'Hello from django',
        message = 'This is a test email',
        from_email = 'antonvanjero12@gmail.com',
        recipient_list=['antonvanjero@gmail.com'],
        fail_silently=False
    )
    return HttpResponse('mail sent successfully')

from .forms import DocumentForm
from .models import Document
def upload_file(request):
    if request.method == 'POST':
        form=DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
            return redirect('upload_file')
    else:
        form=DocumentForm()
    files = Document.objects.all()
    return render(request,'myapp/upload.html',{'form':form, 'files': files})


from django.http import JsonResponse  
def index(request): 
    return render(request, "myapp/index.html") 
def get_data(request): 
    data = { 
        "name": "Alice", 
        "age": 30, 
        "city": "Chennai" 
    } 
    return JsonResponse(data)


def storage_demo(request): 
    return render(request, 'myapp/storage_demo.html') 



def set_cookie_view(request): 
    response = HttpResponse("Cookie Set Successfully!") 
    # Set a cookie named 'username' with value 'jero' that expires in 7 days 
    response.set_cookie('username', 'jero', max_age=60*20)   
    return response 
 
def get_cookie_view(request): 
    username = request.COOKIES.get('username')  # Get the cookie value 
    if username: 
        return HttpResponse(f"Hello, {username}!") 
    else: 
        return HttpResponse("No cookie found.") 
     
def delete_cookie_view(request): 
    response = HttpResponse("Cookie Deleted Successfully!") 
    response.delete_cookie('username')  # Deletes the cookie 
    return response 

def random(request):
    return HttpResponse('this is a new function')
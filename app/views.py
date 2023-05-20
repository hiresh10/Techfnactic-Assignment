from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404

# from .forms import ImageUpdateForm

# Create your views here.
def Index(request):
    return render(request,'app/index.html')

def Home(request):
    all_cards = Product.objects.all()
    return render(request,'app/home.html',{'all_cards':all_cards})

def SignupPage(request):
    return render(request,'app/signup.html')

def Register(request):

    firstname = request.POST['fname']
    lastname = request.POST['lname']
    email = request.POST['email']
    password = request.POST['password']
    cpassword = request.POST['cpassword']


    user = UserMaster.objects.filter(email=email)

    if user:
        message = "User already exists"
        return render(request,"app/signup.html",{'msg':message})

    else:
        if password == cpassword:
           
            newuser = UserMaster.objects.create(email=email,password=password)

            newcand = Candidate.objects.create(user_id=newuser,firstname=firstname,lastname=lastname)

            return render(request,"app/login.html")
        else:
            message = "Password missmatch!!"
            return render(request,"app/signup.html",{'msg':message})


def LoginPage(request):
    return render(request,'app/login.html')

def LoginUser(request):
        
    email = request.POST['email']
    password = request.POST['password']


    user = UserMaster.objects.get(email=email)

    if user:
        if user.password==password:
            can = Candidate.objects.get(user_id=user)
            request.session['id'] = user.id
            request.session['firstname'] = can.firstname
            request.session['lastname'] = can.lastname
            request.session['email'] = user.email
            request.session['password'] = user.password

            return redirect('home')
        else:
            message = "Password Missmatch"
            return render(request,"app/login.html",{'msg':message})

    else:
        message = "User does not exists"
        return render(request,"app/login.html",{'msg':message})
    

def ContactPage(request):
    return render(request,'app/contact.html')


def Contact(request, pk):
    user = get_object_or_404(UserMaster, id=pk)
    if user:
        Fname = request.POST.get('fName')
        lname = request.POST.get('lName')
        email = request.POST.get('email')
        product = request.POST.get('product')
        contact1 = request.POST.get('phone')
        msg = request.POST.get('message')

        if Fname and lname and email and product and contact1 and msg:
            new_message = contact.objects.create(user_id=user, first_name=Fname, last_name=lname, email=email, phone=contact1, product=product, message=msg)
            message = "Your message was sent successfully!"
            return render(request, 'app/contact.html', {'msg': message})
        else:
            message = "Incomplete form data"
            return render(request, 'app/contact.html', {'msg': message})
    else:
        message = "User not found"
        return render(request, 'app/contact.html', {'msg': message})


def Product_page(request):
    return render(request, 'app/product.html')


from django.shortcuts import get_object_or_404

def Add_product(request, pk):
    user = get_object_or_404(UserMaster, id=pk)
    
    if request.method == 'POST':
        image = request.FILES.get('image')
        text = request.POST.get('text')
        link = request.POST.get('link')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        product_card = request.FILES.get('product')

        if image and text and link and address and phone and product_card:
            new_card = Product.objects.create(
                user_id=user,
                images=image,
                text=text,
                link=link,
                address=address,
                contact=phone,
                product_card=product_card
            )
            message = "Product added successfully!"
            return render(request, 'app/product.html', {'message': message})
        else:
            message = "Incomplete form data"
            return render(request, 'app/product.html', {'message': message})
    
    return render(request, 'app/product.html', {'message': 'Please submit the form.'})

def Update_page(request):
    return render(request, 'app/update.html')

from django.shortcuts import get_object_or_404

def update_image(request, pk):
    user = get_object_or_404(UserMaster, pk=pk)

    if request.method == 'POST':
        if Product.objects.filter(user_id=user).exists():
            pro = Product.objects.get(user_id=user)
        else:
            pro = Product(user_id=user)
        
        if 'image' in request.FILES:
            pro.images = request.FILES['image']
        if 'text' in request.POST:
            pro.text = request.POST['text']
        if 'link' in request.POST:
            pro.link = request.POST['link']
        if 'address' in request.POST:
            pro.address = request.POST['address']
        if 'phone' in request.POST:
            pro.contact = request.POST['phone']
        if 'product' in request.FILES:
            pro.product_card = request.FILES['product']
        
        pro.save()
        print('Product Updated')
        return redirect('home')
    
    return render(request, 'app/update_product.html', {'user': user})

def logout(request):
    del request.session['email']
    del request.session['password']
    return redirect('index')

 ############################################---Admin Views----########################################################


def Admin_loginpgae(request):
    return render(request,'app/admin/adminlogin.html')

def Admin_home(request):
    all_users = UserMaster.objects.all()
    all_candidates = Candidate.objects.all()
    return render(request,'app/admin/adminhome.html',{'all_user':all_users, 'all_can':all_candidates})


def Aminlogin(request):
    username = request.POST['username']
    password = request.POST['password']

    if username == "admin" and password == "admin":

        request.session['username'] = username
        request.session['password'] = password
        return redirect('adminhome')

    else:
        message = "Username and password not match"
        return render(request,"app/admin/login.html",{'msg':message})


def UserDelete(request,pk):
    user = UserMaster.objects.get(pk=pk)
    user.delete()
    return redirect('adminhome')

def Product_cards(request):
    all_cards = Product.objects.all()
    return render(request,'app/admin/product_cards.html',{'all_cards':all_cards})



def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        product.delete()
        return redirect('productcard')
    
    return redirect('delete_product', pk=product.pk)


def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect('index')
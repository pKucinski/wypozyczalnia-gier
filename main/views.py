from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError

from django.db.models import Avg

from django.db.models import Avg, Count

from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, Product, Categories, Basket, Rating
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


def index(request):
    products = Product.objects.all().order_by("-id")
    return render(request, 'index.html', {'products': products,"basket_quantity":basket_quantity(request)})


def login_page(request):
    return render(request, 'registration/login.html',{"basket_quantity":basket_quantity(request)})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            user.save()
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration.html/', {'form': form,"basket_quantity":basket_quantity(request)})

def dodajOpinie(request):
    if request.method == "POST":
        opinia = 'dodajOpiniefield' in request.POST and request.POST['dodajOpiniefield']
        idproduct = 'idproduct' in request.POST and request.POST['idproduct']
        categories = 'categories' in request.POST and request.POST['categories']
        productid = get_object_or_404(Product, pk=idproduct)

        r=Rating(user=request.user,product=productid,text=opinia,stars=categories)
        r.save()

    redirect_to = request.META.get('HTTP_REFERER', reverse('home'))
    return HttpResponseRedirect(redirect_to)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'haslo.html', {
        'form': form,"basket_quantity":basket_quantity(request)
    })


def logout_request(request):
    logout(request)
    return HttpResponseRedirect('/')


def faq(request):
    return render(request, 'faq.html',{"basket_quantity":basket_quantity(request)})

@user_passes_test(lambda u: u.is_superuser)
def addGameToDatabase(request):
    data = Product.objects.all()
    all_categories = Categories.objects.all()
    if request.method == "POST" and request.FILES['imagetoUpload']:
        tytul = request.POST['tytul']
        opis = request.POST['opis']
        wiek = request.POST['wiek']
        cena = request.POST['cena']
        ilosc = request.POST['ilosc']
        kategoria = request.POST['categories']
        category = get_object_or_404(Categories, category_name=kategoria)
        images = request.FILES['imagetoUpload']
        p=Product(title=tytul,description=opis,age=wiek,price=cena,amount=ilosc,category=category,image=images)
        p.save()

    return render(request, 'addGameToDatabase.html', {"all_categories": all_categories, "products": data,"basket_quantity":basket_quantity(request)})


def koszyk(request):
    return render(request, 'koszyk.html')


def products_category(request, id):
    category = get_object_or_404(Categories, pk=id)
    products = Product.objects.all
    return render(request, 'kategoria.html', {"category": category, "products": products,"basket_quantity":basket_quantity(request)})


def show_search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        product = Product.objects.filter(title__contains=searched)
        product_count = Product.objects.filter(title__contains=searched).count()

        return render(request, "search.html",
                      {'searched': searched, 'product': product, 'product_count': product_count})
    else:
        return render(request, "search.html", {"basket_quantity":basket_quantity(request)})


def send_Email(request):
    if request.method == "POST":
        sendemailtome = request.POST['sendemailtome']
        messages.success(request, True)

    # login: diceplayonline@gmail.com
    # password: Diceplay1!

    subject, from_email, to = 'DicePlay - Newsleter', 'diceplayonline@gmail.com', sendemailtome
    text_content = 'This is an important message.'
    html_content = render_to_string('e-mail/subscribe_welcome_msg.html')
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.mixed_subtype = 'related'
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    redirect_to = request.META.get('HTTP_REFERER', reverse('home'))
    return HttpResponseRedirect(redirect_to)


def show_product(request, id):
    show_product = get_object_or_404(Product, pk=id)
    rating = Rating.objects.all().filter(product = show_product)
    rating_count = Rating.objects.filter(product=show_product).count()
    avg_rating= Rating.objects.filter(product=show_product).aggregate(Avg('stars'))
    try:
        avg_rating = round(list(avg_rating.values())[0],1)
    except:
        avg_rating = 0


    amount = show_product.amount
    if amount == 0:
        text = False
    elif amount == 1:
        text = "Została ostatnia sztuka!"
    elif amount > 1:
        text = "Dostępne " + str(show_product.amount) + " szt."

    show_product.amount = text


    return render(request, 'produkt.html', {'show_product': show_product, "rating": rating,"rating_count":rating_count, 'avg_rating':avg_rating,"basket_quantity":basket_quantity(request)})



def show_basket(request):
    if (request.user.is_anonymous):
        return HttpResponseRedirect("/registration/")
    show_basket = Basket.objects.all().order_by("id")
    return render(request, 'koszyk.html', {'show_basket': show_basket,"basket_quantity":basket_quantity(request)})

def basket_quantity(request):
    if (request.user.is_anonymous):
        return #
    q = Basket.objects.filter(user=request.user).annotate(num_submissions=Count('product'))
    return q[0].num_submissions

def add_to_basket(request):
    if (request.user.is_anonymous):
        return HttpResponseRedirect("/registration/")
    if not Basket.objects.filter(user = request.user).exists():
        b = Basket(user=request.user)
        b.save()

    if request.method == "POST":
        game = request.POST['getid']
        addGame = Basket.objects.get(user=request.user)
        if Basket.objects.filter(user=request.user).filter(product=game).exists():
            print(True)
            #tu dodać alert że gra już jest w koszyku

        addGame.product.add(game)
        addGame.save()
        #dodać alert że gra została dodana do koszyka
    redirect_to = request.META.get('HTTP_REFERER', reverse('home'))
    return HttpResponseRedirect(redirect_to)

def remove_item_from_basket(request):
    itemToRemove = request.POST['getidtoDelete']
    deleteGame = Basket.objects.get(user=request.user)
    deleteGame.product.remove(itemToRemove)
    deleteGame.save()
    redirect_to = request.META.get('HTTP_REFERER', reverse('home'))
    return HttpResponseRedirect(redirect_to)

def removeGame(request):
    if request.method == "POST":
        game = request.POST['getidtodel']
        deletegame = Product.objects.get(pk=game).delete()



    redirect_to = request.META.get('HTTP_REFERER', reverse('home'))
    return HttpResponseRedirect(redirect_to)


@login_required
def password_view(request):
    return render(request, 'haslo.html')


@login_required
def orders(request):
    return render(request, 'zamowienia.html',{"basket_quantity":basket_quantity(request)})

@login_required
def editProfil(request):
    userDetails = UserProfile.objects.filter(user__username=request.user)
    return render(request, 'edycjaProfilu.html', {'userDetails': userDetails,"basket_quantity":basket_quantity(request)})

@login_required
def updateprofil(request):
    street = request.POST['ulica']
    numberOfHouse = request.POST['nrdomu']
    postCode = request.POST['kodpocztowy']
    city = request.POST['miasto']
    phone = request.POST['phone']
    imie = request.POST['imie']
    nazwisko = request.POST['nazwisko']
    email = request.POST['email']
    u=UserProfile.objects.get(user=request.user)
    user = User.objects.get(username=request.user)
    user.first_name = imie
    user.last_name=nazwisko
    user.email=email
    user.save()
    u.street=street
    u.numberOfHouse=numberOfHouse
    u.postCode=postCode
    u.city=city
    u.phone=phone
    u.save()

    return HttpResponseRedirect("/profil")


@login_required
def profile(request):
    if not UserProfile.objects.filter(user = request.user).exists():
        u=UserProfile(user=request.user)
        u.save()
    userDetails = UserProfile.objects.filter(user__username=request.user)
    return render(request, 'profil.html', {'userDetails': userDetails,"basket_quantity":basket_quantity(request)})

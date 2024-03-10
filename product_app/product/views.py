 from django.http import HttpResponse
from django.shortcuts import render, redirect
from product.models import Product



def home_page(request):
    return render(request, template_name='home.html')


def Add_Product(request):
    message = ''
    if request.method == "POST":
        formdata = request.POST
        if formdata:
            try:
                product = Product.objects.create(
                    name=formdata.get('name'),
                    brand=formdata.get('brand'),
                    price=formdata.get('price'),
                    category=formdata.get('category'),
                    vendor=formdata.get('vendor')
                )
                message = "Product Record Saved successfully...!"
            except Exception as e:
                message = f"Error saving product record: {str(e)}"
    return render(request, template_name="add.html", context={"result": message})

def show(request):
    products = Product.objects.all()
    return render(request, template_name="list.html", context={'products': products})

def update(request, id):
    message = ''
    product = Product.objects.filter(id=id).first()
    if request.method == "POST":
        formdata = request.POST

        if product:
            try:
                product.name = formdata.get('name')
                product.brand = formdata.get('brand')
                product.price = formdata.get('price')
                product.category = formdata.get('category')
                product.vendor = formdata.get('vendor')
                product.save()
                message = 'Product Record Updated Successfully....!'
                return redirect('show')
            except Exception as e:
                message = f"Error updating product record: {str(e)}"
        else:
            message = 'Product not found'
    return render(request, template_name='update.html', context={"result": message, 'product': product})

    

def edit_product(request, id):
    product = Product.objects.get(id=id)
    return redirect(request, template_name='update.html',
                  context={"product": product,
                           'defaults': {'name': '', 'brand': '', 'price': 0.0,'category':'','vendor':''}})


def destroy(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect(show)


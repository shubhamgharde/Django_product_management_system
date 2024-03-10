from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Customer


def add_customer(request):
    message = ''
    if request.method == "POST":
        formdata = request.POST
        if formdata:
            try:
                customer = Customer.objects.create(first_name=formdata.get('first_name'),
                                               last_name=formdata.get('last_name'),
                                               age=formdata.get('age'),
                                               email=formdata.get('email'),
                                               address=formdata.get('address'),
                                               contact=formdata.get('contact'))
                message = "Customer Record Saved Successfully...!"
            except Exception as e:
                message = "Error saving Customer Record"
    return render(request,template_name="add_cust.html", context={"result":message})

def show_list_of_custmer(request):
    customers = Customer.objects.all()
    return render(request, template_name="cust_list.html", context={'customers': customers})


def cust_update(request,id):
    message = ''
    customer = Customer.objects.filter(id=id).first()

    if request.method == "POST":
        formdata = request.POST

        if customer:
            try:
                customer.first_name = formdata.get('first_name')
                customer.last_name = formdata.get('last_name')
                customer.age = formdata.get('age')
                customer.email = formdata.get('email')
                customer.address = formdata.get('address')
                customer.contact = formdata.get('contact')
                customer.save()
                message = 'Customer Record Saved Successfully...!'
                return redirect(show_list_of_custmer)
            except Exception as e:
                message = "Error Updating Customer Record..."
        else:
            message ='Customer not Found...'
    return render(request, template_name='add_cust.html',
                  context={"result":message,'customer':customer})


def edit_customer(request,id):
    customer = Customer.objects.get(id=id)
    return render(request, template_name='add_cust.html',
                  context={"customer":customer,
                           'defaults':{"first_name":'', "last_name":'',
                                        "age":0,"email":'',"address":'',
                                        "contact":0}})


def delete_customer(request ,id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect(show_list_of_custmer)


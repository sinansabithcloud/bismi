from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, View
from .models import SalesBill, SalesBillType
from .forms import SalesBillForm, SaleFormSet
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse

# Create your views here.

class SalesBillCreateView(CreateView):
    model = SalesBill
    form_class = SalesBillForm
    template_name = 'bills/create_sales.html'
    
    def get_success_url(self):
        return reverse('thermal_sales_bill', kwargs={'bill_number': self.object.bill_number})

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['sales_formset'] = SaleFormSet(self.request.POST, prefix='sales')
        else:
            data['sales_formset'] = SaleFormSet(prefix='sales')
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        sales_formset = context['sales_formset']
        if sales_formset.is_valid():
            print('Formset is valid')
            self.object = form.save()
            sales_formset.instance = self.object
            sales_formset.save()
            print('Formset is valid')
            return redirect(self.get_success_url())
        else:
            print('Formset is not valid')
            print(sales_formset.errors)           # List of form errors
            print(sales_formset.non_form_errors())  # Formset-level errors
            for f in sales_formset:
                print(f.errors)  # Individual form errors
            print('not valid')
        print('i am here')
        #return self.render_to_response(self.get_context_data(form=form))
        return self.render_to_response(self.get_context_data(form=form, sales_formset=sales_formset))

class SalesBillUpdateView(UpdateView):
    model = SalesBill
    form_class = SalesBillForm
    template_name = 'bills/update_sales.html'
    
    def get_success_url(self):
        return reverse('thermal_sales_bill', kwargs={'bill_number': self.object.bill_number})
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['sales_formset'] = SaleFormSet(self.request.POST, instance=self.object, prefix='sales')
        else:
            data['sales_formset'] = SaleFormSet(instance=self.object, prefix='sales')
        return data


    def form_valid(self, form):
        context = self.get_context_data()
        sales_formset = context['sales_formset']
        if sales_formset.is_valid():
            print('Formset is valid')
            self.object = form.save()
            sales_formset.instance = self.object
            sales_formset.save()
            print('Formset is valid')
            return redirect(self.get_success_url())
        else:
            print('Formset is not valid')
            print(sales_formset.errors)           # List of form errors
            print(sales_formset.non_form_errors())  # Formset-level errors
            # Loop through each form in the formset to see individual errors
            for f in sales_formset:
                print(f"Errors in form {f.prefix}: {f.errors}")  # Individual form errors
            print('not valid')
        print('i am here')
        #return self.render_to_response(self.get_context_data(form=form))
        return self.render_to_response(self.get_context_data(form=form, sales_formset=sales_formset))

class SalesBillDeleteView(View):
    def post(self, request, pk):
        # Get the SalesBill object
        sales_bill = get_object_or_404(SalesBill, pk=pk)
        
        # Delete the related Sales
        sales_bill.sales.all().delete()
        
        # Now delete the SalesBill
        sales_bill.delete()
        
        # Redirect to a success page (or any page)
        return redirect('list_sale_view')  # Redirect to list of sales bills or another page

class SalesBillListView(ListView):
    model = SalesBill
    template_name = 'bills/list_sales.html'
    ordering = ['-bill_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales_bill_types'] = SalesBillType.objects.all()  # Add your second model here
        return context



def bills(request):
    data = []
    for sales_bill in SalesBill.objects.all():
        data.append({
            "id": sales_bill.id,
            "customer": sales_bill.customer,
            "date": sales_bill.bill_date,
            "bill_number": sales_bill.bill_number,
            "sales_bill_type": sales_bill.sales_bill_type.name,
            "payment_method": sales_bill.fund.name,
            "stocks": sales_bill.stocks,
            "discount": sales_bill.discount_price,
        })
    return JsonResponse({"data": data})

def full_sales_bill(request, bill_number):
    try:
        sales_bill = SalesBill.objects.get(id=bill_number)
    except SalesBill.DoesNotExist:
        messages.error(request, "Sales bill not found")
        return JsonResponse({"error": "Sales bill not found"}, status=404)
    
    data = {
        "customer": sales_bill.customer,
        "date": sales_bill.bill_date,
        "bill_number": sales_bill.bill_number,
        "sales_bill_type": sales_bill.sales_bill_type.name,
        "payment_method": sales_bill.fund.name,
        "stocks": sales_bill.stocks,
    }

    return render(request, 'bills/view_sales_bill.html', {'sales_bill': sales_bill})
    return render(request, 'bills/view_thermal_sales_bill.html', {'sales_bill': sales_bill})

def thermal_sales_bill(request, bill_number):
    try:
        sales_bill = SalesBill.objects.get(id=bill_number)
    except SalesBill.DoesNotExist:
        messages.error(request, "Sales bill not found")
        return JsonResponse({"error": "Sales bill not found"}, status=404)
    
    data = {
        "customer": sales_bill.customer,
        "date": sales_bill.bill_date,
        "bill_number": sales_bill.bill_number,
        "sales_bill_type": sales_bill.sales_bill_type.name,
        "payment_method": sales_bill.fund.name,
        "stocks": sales_bill.stocks,
    }

    return render(request, 'bills/view_thermal_sales_bill.html', {'sales_bill': sales_bill})

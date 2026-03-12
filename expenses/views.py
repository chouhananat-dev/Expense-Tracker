from django.shortcuts import render,redirect,get_object_or_404
from .models import Expense
from .forms import ExpenseForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.db.models import Sum
from datetime import datetime
import csv
from django.http import HttpResponse
# Create your views here.

def base(request):
    return render(request,'expenses/base.html')
@login_required
def delete_expense(request,pk):
    expense=get_object_or_404(Expense,pk=pk,user=request.user)
    if request.method=="POST":
        expense.delete()
        return redirect('expense_list')
    return redirect('expense_list')
def expense_list(request):
    if request.user.is_authenticated:
        expenses = Expense.objects.filter(user=request.user)
        total_sum=expenses.aggregate(Sum('amount'))
        total_spent=total_sum['amount__sum'] or 0
        # adding filter functionality here:
        selected_year = request.GET.get('year')
        selected_month = request.GET.get('month')

        filtered_expenses = None
        filter_total = 0
        is_filtering = False

        categories=[]
        totals=[]

        if selected_month or selected_year:
            is_filtering = True
            # start with all expenses for the user and apply any filters provided
            filtered_expenses = expenses
            if selected_year:
                # use Django field lookup syntax for year/month on a DateField
                filtered_expenses = filtered_expenses.filter(date__year=selected_year)
            if selected_month:
                filtered_expenses = filtered_expenses.filter(date__month=selected_month)
            # aggregate returns a dict with key 'amount__sum'
            filter_total = filtered_expenses.aggregate(Sum('amount'))['amount__sum'] or 0

            # preparing data for chart
            categorical_data=filtered_expenses.values('category').annotate(sum=Sum('amount'))
            categories=[item['category'] for item in categorical_data]
            totals=[float(item['sum']) for item in categorical_data]
        else:
            # no filters; nothing to display in the filtered block by default
            filtered_expenses = expenses
    else:
        expenses = Expense.objects.none()

    context = {"expenses": expenses,'total_expense':total_spent,
               'filtered_expenses':filtered_expenses,
               'selected_year':selected_year,
               'selected_month':selected_month,
               'filter_total':filter_total,
               'is_filtering':is_filtering,
               'categories':categories,
               'totals':totals}

    return render(request, 'expenses/list.html', context)
def add_expense(request):
    if request.method=='POST':
        expenseform=ExpenseForm(request.POST)
        if expenseform.is_valid():
            expense = expenseform.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense_list')
    else:
        expenseform=ExpenseForm()
    return render(request,'expenses/add_expense.html',{'form':expenseform})

def signup(request):
    if request.method=="POST":
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            # saved user to the database
            login(request,user)
            return redirect('expense_list')
    else:
        form=CustomUserCreationForm()
    return render(request,'registration/signup.html',{"form":form})

def updateexpense(request,pk):
    expense=get_object_or_404(Expense,pk=pk,user=request.user)
    if request.method=="POST":
        form=ExpenseForm(request.POST,instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form=ExpenseForm(instance=expense)
    return render(request,'expenses/edit.html',{'form':form})

def export_expenses_csv(request):
    response=HttpResponse(content_type='text/csv')
    response['Content_Disposition'] = 'attachment; filename="my_expense.csv"'

    writer=csv.writer(response)
    writer.writerow(['Title','Amount','Date','Category'])

    # write data columns headers
    expenses=Expense.objects.filter(user=request.user)

    year=request.GET.get('year')
    month=request.GET.get('month')

    if year:
        expenses=expenses.filter(date__year=year)
    if month:
        expenses=expenses.filter(date__month=month)
    # wrute data rows

    for expense in expenses:
        writer.writerow([expense.title, expense.amount, expense.date, expense.category])

    return response
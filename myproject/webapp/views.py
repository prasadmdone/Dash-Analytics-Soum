from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
from .models import pagedata
import joblib
from . import hrmodel

# Create your views here.
def model(request):

    return render(request, 'model home.html',{'A':'saua'})

#
def HRlogmodel(request):
    a= int(request.POST['satisfaction_level'])
    b= int(request.POST['last_evaluation'])
    c= int(request.POST['number_project'])
    d= int(request.POST['average_montly_hours'])
    e= int(request.POST['time_spend_company'])
    f= int(request.POST['Work_accident'])
    g= int(request.POST['promotion_last_5years'])
    h= int(request.POST['Departments '])
    i= int(request.POST['salary'])

    prediction = hrmodel.prediction_model(a,b,c,d,e,f,g,h,i)
#    pre = a + b + c + d + e + f + g + h + i
    context = {'prediction': prediction}
    return render(request, 'HR Model.html',context)
#


def user_in(request):               #from database
    pdata=pagedata.objects.all()
    context={
        'page1':pdata
    }
    return render(request, 'page1.html',context)

def utables(request):
    df = pd.read_csv("age.csv")
    df1 = pd.read_csv("Post data.csv")
    rs = df1.groupby("Data_entry")["Engagement"].agg("sum")
    categories = list(rs.index)
    values = list(rs.values)

    rs_pie = df.groupby("Age_Group")["Counts"].agg("sum")

    categoriespie = list(rs_pie.index)
    valuespie = list(rs_pie.values)
    data = []
    for index in range(0, len(rs_pie.index)):
        # print(rs_pie.index[index])
        value = {'name': rs_pie.index[index], 'y': rs_pie.values[index]  }
        data.append(value)

    table_content = df.to_html(index=None)
    table_content = table_content.replace("", "")
    table_content = table_content.replace('class="dataframe"',
                                          "id='big_tables' class='table table-striped table-bordered'")
    table_content = table_content.replace('border="1"', "")
    context = {"categories": categories, 'values': values, 'data': data, 'table_data': table_content}
    return render(request, 'page2.html', context=context)


def ut1(request):
    df2 = pd.read_csv("genderratio.csv")
    rs_pie2 = df2.groupby("category")["counts"].agg("sum")
    categoriespie2 = list(rs_pie2.index)
    valuespie2 = list(rs_pie2.values)

    rs = df2.groupby("category")["counts"].agg("sum")
    categories = list(rs.index)
    values = list(rs.values)

    table_content = df2.to_html(index=None)
    table_content = table_content.replace("", "")
    table_content = table_content.replace('class="dataframe"',
                                          "id='big_tables' class='table table-striped table-bordered'")
    table_content = table_content.replace('border="1"', "")

    data2 = []
    for i in range(0, len(rs_pie2.index)):
        # print(rs_pie.index[index])
        value20 = {'name': rs_pie2.index[i], 'y': rs_pie2.values[i]}
        data2.append(value20)

    context = {"categories": categories, 'values': values, 'data': data2, 'table_data': table_content}

    return render(request, 'gender.html', context=context)



def index(request):

    df = pd.read_csv("Post data.csv")
    rs = df.groupby("Post_Id")["Engagement"].agg("sum")
    rs_pie = df.groupby("Post_Id")["Engagement"].agg("sum")
    categories = list(rs.index)
    values = list(rs.values)

    categoriespie = list(rs_pie.index)
    valuespie = list(rs_pie.values)

    data = []
    for index in range(0, len(rs_pie.index)):
        # print(rs_pie.index[index])
        value = {'name': rs_pie.index[index], 'y': rs_pie.values[index]  }
        data.append(value)

    table_content = df.to_html(index=None)
    table_content = table_content.replace("", "")
    table_content = table_content.replace('class="dataframe"',
                                          "id='big_tables' class='table table-striped table-bordered'")
    table_content = table_content.replace('border="1"', "")

#    context = {'table_data': table_content}
#    return render(request, 'index.html', context=context)
    context = {"categories": categories, 'values': values, 'data': data, 'table_data':table_content}
    return render(request, 'index.html', context=context)



def impression(request):

    df = pd.read_csv("Post data.csv")
    rs = df.groupby("Post_Id")["Impressions"].agg("sum")
    rs_pie = df.groupby("Post_Id")["Impressions"].agg("sum")
    categories = list(rs.index)
    values = list(rs.values)

    categoriespie = list(rs_pie.index)
    valuespie = list(rs_pie.values)

    data = []
    for index in range(0, len(rs_pie.index)):
        # print(rs_pie.index[index])
        value = {'name': rs_pie.index[index], 'y': rs_pie.values[index]  }
        data.append(value)

    table_content = df.to_html(index=None)
    table_content = table_content.replace("", "")
    table_content = table_content.replace('class="dataframe"',
                                          "id='big_tables' class='table table-striped table-bordered'")
    table_content = table_content.replace('border="1"', "")

#    context = {'table_data': table_content}
#    return render(request, 'index.html', context=context)
    context = {"categories": categories, 'values': values, 'data': data, 'table_data':table_content}
    return render(request, 'impression.html', context=context)

def reach(request):

    df = pd.read_csv("Post data.csv")
    rs = df.groupby("Data_entry")["Reach"].agg("sum")
    rs_pie = df.groupby("Post_Id")["Reach"].agg("sum")
    categories = list(rs.index)
    values = list(rs.values)

    categoriespie = list(rs_pie.index)
    valuespie = list(rs_pie.values)

    data = []
    for index in range(0, len(rs_pie.index)):
        # print(rs_pie.index[index])
        value = {'name': rs_pie.index[index], 'y': rs_pie.values[index]  }
        data.append(value)

    table_content = df.to_html(index=None)
    table_content = table_content.replace("", "")
    table_content = table_content.replace('class="dataframe"',
                                          "id='big_tables' class='table table-striped table-bordered'")
    table_content = table_content.replace('border="1"', "")

    context = {"categories": categories, 'values': values, 'data': data, 'table_data':table_content}
    return render(request, 'reach.html', context=context)



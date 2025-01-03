"""farmers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aidforfarmer import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('login',views.login,name="login"),
    path('registration',views.registration,name="registration"),
    path('investerreg',views.investerreg,name="investerreg"),
    path('adminhome',views.adminhome,name="adminhome"),
    path('experthome',views.experthome,name="experthome"),
    path('expertreg',views.expertreg,name="expertreg"), 
    path('adminexperts',views.adminexperts,name="adminexperts"),
    path('farmerhome',views.farmerhome,name="farmerhome"),
    path('investorhome',views.investorhome,name="investorhome"),
    path('supreg',views.supreg,name="supreg"), 
    path('supplierhome',views.supplierhome,name="supplierhome"), 
    path('viewproductsfarmer',views.viewproductsfarmer,name="viewproductsfarmer"), 
    path('farmerseed',views.farmerseed,name="farmerseed"),
    path('farmerpest',views.farmerpest,name="farmerpest"),
    path('farmerequip',views.farmerequip,name="farmerequip"),
    path('adminapproveexp',views.adminapproveexp,name="adminapproveexp"),
    path('adminrejectexp',views.adminrejectexp,name="adminrejectexp"),
    path('farmersell',views.farmersell,name="farmersell"),
    path('farmercapital',views.farmercapital,name="farmercapital"),
    path('farmerselfyield',views.farmerselfyield,name="farmerselfyield"),
    path('supplierequip',views.supplierequip,name="supplierequip"),   
    path('suppliervbooking',views.suppliervbooking,name="suppliervbooking"),
    path('suppliervequip',views.suppliervequip,name="suppliervequip"),   
    path('adminfarmers',views.adminfarmers,name="adminfarmers"),
    path('admininvestors',views.admininvestors,name="admininvestors"),
    path('adminsuppliers',views.adminsuppliers,name="adminsuppliers"),   
    path('adminapprovesup',views.adminapprovesup,name="adminapprovesup"),
    path('adminrejectsup',views.adminrejectsup,name="adminrejectsup"),
    path('adminapproveinv',views.adminapproveinv,name="adminapproveinv"),
    path('adminrejectinv',views.adminrejectinv,name="adminrejectinv"),
    path('adminapprovefar',views.adminapprovefar,name="adminapprovefar"),
    path('adminrejectfar',views.adminrejectfar,name="adminrejectfar"),
    path('investorvplans',views.investorvplans,name="investorvplans"),
    path('investoraddplans',views.investoraddplans,name="investoraddplans"),
    path('buyyield',views.buyyield,name="buyyield"),
    path('farmerbuyequip',views.farmerbuyequip,name="farmerbuyequip"),
    path('equipqselect',views.equipqselect),
    path('supviewprodbook',views.supviewprodbook),
    path('supdeliver',views.supdeliver),
    path('farvprodbook',views.farvprodbook),
    path('supupdateequip',views.supupdateequip),
    path('farmerviewpayment',views.farmerviewpayment),
    path('farupdateyield',views.farupdateyield),
    path('farviewyield',views.farviewyield),
    path('admincateq',views.admincateq),
    path('admincatfer',views.admincatfer),
    path('krishibhavanhome',views.krishibhavanhome),
    path('farmerComplaint',views.farmerComplaint),
    path('pubVBooking',views.pubVBooking),
    path('pubVprod',views.pubVprod),
    path('pubReg',views.pubReg),
    path('pubHome',views.pubHome),
    path('pubStore',views.pubStore),
    path('kbComplaints',views.kbComplaints),
    path('expertreq',views.expertreq),
    path('expapprove',views.expapprove),
    path('expremove',views.expremove),
    path('expchat',views.expchat),
    path('userchat',views.userchat),
    path('farmerreqexp',views.farmerreqexp),
    path('farmervexp',views.farmervexp),
    path('userexpbook',views.userexpbook),
    
    
    
    
]

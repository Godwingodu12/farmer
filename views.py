from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from datetime import date


# Create your views here.


def home(request):
    return render(request,"index.html")


def experthome(request):
    return render(request,"experthome.html")

def expapprove(request):
    did=request.GET.get("id")
    data=Specbook.objects.get(id=did)
    data.status="Approved"
    data.save()

    return redirect("/expertreq")

def expremove(request):
    did=request.GET.get("id")
    data=Specbook.objects.get(id=did).delete()

    return redirect("/expertreq")

def expchat(request):
    sender = request.session['email']
    receiver = request.GET['email']
    dates=date.today()
    if request.POST:
        msg=request.POST["msg"]
        c=Chat.objects.create(sender=sender,receiver=receiver,date=dates,message=msg)
        c.save()
   
    r=Chat.objects.all()
    
    return render(request,"expchat.html",{"messages":r,"sender":sender, "receiver": receiver})

def userchat(request):
    sender = request.session['email']
    receiver = request.GET['email']
    dates=date.today()
    if request.POST:
        msg=request.POST["msg"]
        c=Chat.objects.create(sender=sender,receiver=receiver,date=dates,message=msg)
        c.save()
   
    r=Chat.objects.all()
    
    return render(request,"userchat.html",{"messages":r,"sender":sender, "receiver": receiver})

def login(request):
    if request.POST:
        uname=request.POST["uname"]
        psw=request.POST["pass"]
        print("Username:", uname)
        print("Password:", psw)
        user=authenticate(username=uname,password=psw)
        print("JJJJJJJJJJJ")
        print(user)
        if user is None:
            messages.info(request,"user or password is incorrect")
        else:
            userdata=CustomUser.objects.get(username=uname)
            if userdata.usertype=='krishibhavan' and userdata.is_superuser == 1:
                return redirect("/krishibhavanhome")
            
            elif  userdata.is_superuser == 1 :
                
                return redirect("/adminhome")
            elif userdata.usertype=='farmer' and userdata.is_active==1:
                request.session["email"]=uname
                r = Registration.objects.get(Email=uname)
                request.session["id"]=r.id
                request.session["name"]=r.Name
                return redirect("/farmerhome")
            elif userdata.usertype=='public':
                request.session["email"]=uname
                r = Public.objects.get(Email=uname)
                print("Public model data retrieved:", r)
                request.session["id"]=r.id
                request.session["name"]=r.Name
                return redirect("/pubHome")
            elif userdata.usertype=='expert' and userdata.is_active==1:
                request.session["email"]=uname
                r = Expert.objects.get(Email=uname)
                request.session["id"]=r.id
                request.session["name"]=r.Name
                return redirect("/experthome")
    return render(request,"login.html")


def registration(request):
    if request.POST:
        name=request.POST["name"]
        add=request.POST["add"]
        contact=request.POST["con"]
        email=request.POST["email"]
        psw=request.POST["pass"]
        adar=request.FILES["adar"]
        user=CustomUser.objects.filter(username=email).exists()
        if not user:
            try:
                r=Registration.objects.create(Name=name,Address=add,Contact=contact,Email=email,password=psw,Aadhar=adar,status=0)
                r.save()
            except:
                messages.info(request,'sorry some error occured')
            else:
                try:
                    u=CustomUser.objects.create_user(username=email,password=psw,is_superuser=0,is_active=0,is_staff=0,email=email,usertype='farmer')
                    u.save()
                except:
                    messages.info(request,'Sorry some error occured')
                else:
                    messages.info(request,"Registration Successful")
        else:
            messages.info(request,"User already registered")



    return render(request,"registration.html") 


def expertreg(request):
    if request.POST:
        name=request.POST["name"]
        add=request.POST["add"]
        contact=request.POST["con"]
        email=request.POST["email"]
        psw=request.POST["pass"]
        adar=request.FILES["lic"]
        # photo=request.FILES["photo"]
        user=CustomUser.objects.filter(username=email).exists()
        if not user:
            try:
                r=Expert.objects.create(Name=name,Address=add,Contact=contact,Email=email,password=psw,Aadhar=adar,status=0)
                r.save()
            except:
                messages.info(request,'sorry some error occured')
            else:
                try:
                    u=CustomUser.objects.create_user(username=email,password=psw,is_superuser=0,is_active=0,is_staff=0,email=email,usertype='expert')
                    u.save()
                except:
                    messages.info(request,'Sorry some error occured')
                else:
                    messages.info(request,"Registration Successful")
        else:
            messages.info(request,"User already registered")

    return render(request,"expertreg.html")   


def investerreg(request):
    if request.POST:
        name=request.POST["name"]
        add=request.POST["add"]
        contact=request.POST["con"]
        email=request.POST["email"]
        psw=request.POST["pass"]
        lic=request.FILES["lic"]
        photo=request.FILES["photo"]
        user=CustomUser.objects.filter(username=email).exists()
        if not user:
            try:
                r=Investors.objects.create(Name=name,Address=add,Contact=contact,Email=email,password=psw,license=lic,prof=photo,status=0)
                r.save()
            except:
                messages.info(request,'sorry some error occured')
            else:
                try:
                    u=CustomUser.objects.create_user(username=email,password=psw,is_superuser=0,is_active=0,is_staff=0,email=email,usertype='investor')
                    u.save()
                except:
                    messages.info(request,'Sorry some error occured')
                else:
                    messages.info(request,"Registration Successful")
        else:
            messages.info(request,"User already registered")

    return render(request,"investerreg.html")   


def investorhome(request):
    uid=request.session["id"]
    user=Investors.objects.get(id=uid)
    return render(request,"investorhome.html",{"data":user})


def admininvestors(request):
    data=Investors.objects.all()
    return render(request,"admininvestors.html",{"data":data})


def farmerhome(request):
    uid=request.session["id"]
    user=Registration.objects.get(id=uid)

    return render(request,"farmerhome.html",{"data":user})


def adminhome(request):
    
    return render(request,"adminhome.html")


def adminapproveexp(request):
    cid=request.GET.get("id")
    d=Expert.objects.get(id=cid)

    demail=d.Email
    # print(demail)
    try:
        s=CustomUser.objects.get(email=demail)
        print(s.id)
        s.is_active=1
        s.save()
        ct=Expert.objects.get(Email=demail)
        ct.status=1
        ct.save()
    except:
        print("Error occured")
    return redirect("/adminexperts")

def adminrejectexp(request):
    cid=request.GET.get("id")
    d=Expert.objects.get(id=cid)
    demail=d.Email
    print(demail)
    s=CustomUser.objects.get(email=demail).delete()
    ct=Expert.objects.get(Email=demail).delete()
    return redirect("/adminexperts")

def adminexperts(request):
    data=Expert.objects.all()
    return render(request,"adminexperts.html",{"data":data})



def supreg(request):
    if request.POST:
        name=request.POST["name"]
        add=request.POST["add"]
        contact=request.POST["con"]
        email=request.POST["email"]
        psw=request.POST["pass"]
        adar=request.FILES["lic"]
        # photo=request.FILES["photo"]
        user=CustomUser.objects.filter(username=email).exists()
        if not user:
            try:
                r=Supplier.objects.create(Name=name,Address=add,Contact=contact,Email=email,password=psw,Aadhar=adar,status=0)
                r.save()
            except:
                messages.info(request,'sorry some error occured')
            else:
                try:
                    u=CustomUser.objects.create_user(username=email,password=psw,is_superuser=0,is_active=0,is_staff=0,email=email,usertype='supplier')
                    u.save()
                except:
                    messages.info(request,'Sorry some error occured')
                else:
                    messages.info(request,"Registration Successful")
        else:
            messages.info(request,"User already registered")

    return render(request,"supreg.html")   


def supplierhome(request):
    uid=request.session["id"]
    user=Supplier.objects.get(id=uid)
    return render(request,"supplierhome.html",{"data":user})

def viewproductsfarmer(request):
    return render(request,"viewproductsfarmer.html")


def farmerseed(request):
    data=Products.objects.all()

    return render(request,"farmerseed.html",{"data":data})

def farmercapital(request):
    data=Plans.objects.all()
    return render(request,"farmercapital.html",{"data":data})

def farmerselfyield(request):
    fid=request.session["id"]
    data=Yield.objects.exclude(fid=fid)
    # data=Yield.objects.all()
    return render(request,"farmerselfyield.html",{"data":data})


def farmerequip(request):
    return render(request,"farmerequip.html")


def farmerpest(request):
    return render(request,"farmerpest.html")

def farmersell(request):
    data=Category.objects.filter(type="Yield")
    fid=request.session["id"]
    user=Registration.objects.get(id=fid)
    if request.POST:
        name=request.POST["name"]
        price=request.POST["price"]
        qty=request.POST["qty"]
        photo=request.FILES["photo"]
        cat=request.POST["cat"]
        c = Category.objects.get(id=cat)
        s=Yield.objects.create(Name=name,price=price,quantity=qty,image=photo,category=c,fid=user)
        s.save()


    return render(request,"farmersell.html",{"data":data})

def supplierequip(request):
    data=Category.objects.filter(type="equipments")
    if request.POST:
        name=request.POST["name"]
        price=request.POST["price"]
        qty=request.POST["qty"]
        photo=request.FILES["photo"] 
        cat=request.POST["cat"]
        cata=Category.objects.get(id=cat)
        desc=request.POST["desc"]
        user=Products.objects.filter(Name=name).exists()
        if not user:
            try:
                r=Products.objects.create(Name=name,price=price,quantity=qty,desc=desc,category=cata,image=photo)
                r.save()
            except:
                messages.info(request,'sorry some error occured')

    return render(request,"supplierequip.html",{"data":data})

def suppliervbooking(request):

    data=Payment.objects.all()
    return render(request,"suppliervbooking.html",{"data":data})

def suppliervequip(request):
    data=Products.objects.all()
    return render(request,"suppliervequip.html",{"data":data})

def adminfarmers(request):
    data=Registration.objects.all()
    return render(request,"adminfarmers.html",{"data":data})

def adminsuppliers(request):
    data=Supplier.objects.all()
    return render(request,"adminsuppliers.html",{"data":data})


def admininvestors(request):
    data=Investors.objects.all()
    return render(request,"admininvestors.html",{"data":data})


def adminapprovefar(request):
    cid=request.GET.get("id")
    d=Registration.objects.get(id=cid)

    demail=d.Email
    # print(demail)
    try:
        s=CustomUser.objects.get(email=demail)
        print(s.id)
        s.is_active=1
        s.save()
        ct=Registration.objects.get(Email=demail)
        ct.status=1
        ct.save()
    except:
        print("Error occured")
    return redirect("/adminfarmers")

def adminrejectfar(request):
    cid=request.GET.get("id")
    d=Registration.objects.get(id=cid)
    demail=d.Email
    print(demail)
    s=CustomUser.objects.get(email=demail).delete()
    ct=Registration .objects.get(Email=demail).delete()
    return redirect("/adminfarmers")


def adminapproveinv(request):
    cid=request.GET.get("id")
    d=Investors.objects.get(id=cid)

    demail=d.Email
    # print(demail)
    try:
        s=CustomUser.objects.get(email=demail)
        print(s.id)
        s.is_active=1
        s.save()
        ct=Investors.objects.get(Email=demail)
        ct.status=1
        ct.save()
    except:
        print("Error occured")
    return redirect("/admininvestors")

def adminrejectinv(request):
    cid=request.GET.get("id")
    d=Investors.objects.get(id=cid)
    demail=d.Email
    print(demail)
    s=CustomUser.objects.get(email=demail).delete()
    ct=Investors.objects.get(Email=demail).delete()
    return redirect("/admininvestors")


def adminapprovesup(request):
    cid=request.GET.get("id")
    d=Supplier.objects.get(id=cid)

    demail=d.Email
    # print(demail)
    try:
        s=CustomUser.objects.get(email=demail)
        print(s.id)
        s.is_active=1
        s.save()
        ct=Supplier.objects.get(Email=demail)
        ct.status=1
        ct.save()
    except:
        print("Error occured")
    return redirect("/adminsuppliers")

def adminrejectsup(request):
    cid=request.GET.get("id")
    d=Supplier.objects.get(id=cid)
    demail=d.Email
    print(demail)
    s=CustomUser.objects.get(email=demail).delete()
    ct=Supplier.objects.get(Email=demail).delete()
    return redirect("/adminsuppliers")




def admincateq(request):
    if request.POST:
        cat=request.POST["cat"]
        try:
            c=Category.objects.create(cat=cat,type="equipments")
            c.save()
        except Exception as e:
            messages.info(request,"Some error occurred")
        else:
            messages.info(request,"Added successfully")

    return render(request,"admincateq.html")




def admincatfer(request):
    if request.POST:
        cat=request.POST["cat"]
        try:
            c=Category.objects.create(cat=cat,type="Yield")
            c.save()
        except Exception as e:
            messages.info(request,"Some error occurred")
        else:
            messages.info(request,"Added successfully")
    return render(request,"admincatfer.html")




def investorvplans(request):
    uid = request.session['id']
    data=Plans.objects.filter(iid=uid)
    return render(request,"investorvplans.html",{"data":data})

def investoraddplans(request):
    uid = request.session['id']
    d=Investors.objects.get(id=uid)
    if request.POST:
        name=request.POST["name"]
        amt=request.POST["amt"]
        time=request.POST["time"]
        rate=request.POST["rate"]
        emi=request.POST["emi"]
        file=request.FILES["file"]
        user=Plans.objects.filter(Name=name).exists()
        r=Plans.objects.create(iid=d,Name=name,Amount=amt,Time=time,rate=rate,emi=emi,image=file)
        r.save()
        # if not user:
        #     try:
        #         r=Plans.objects.create(iid=d,Name=name,Amount=amt,Time=time,rate=rate,emi=emi)
        #         r.save()
        #     except Exception as e:
        #         # messages.info(request,'sorry some error occured')
        #           messages.info(request,e)
        # else:
        #       messages.info(request,'Plan already exists')

    return render(request,"investoraddplans.html")

def buyyield(request):
    fid = request.session['id']
    user=Public.objects.get(id=fid)
    semail=user.Email
    wd=request.GET.get("id")
    w=Yield.objects.get(id=wd)  
    email=w.fid.Email
    amt=w.price
    dte=date.today()

    data=Yield.objects.filter(id=wd)
    work=Payment.objects.filter(id=wd).exists()
    
    
    if request.POST:
            dte=date.today()
            amt=request.POST['amount']
            qty=request.POST["qty"]
            qty=int(qty)
            p=Payment.objects.create(sender=user.Email,receiver=email,date=dte,amt=amt)
            p.save()
            w.quantity=w.quantity-qty
            w.save()
            if w.quantity == 0:
                w.delete()
            return redirect("/pubStore")
            
                
            
                

    
        # messages.info(request, 'already paid ')
            

    return render(request,"buyyield.html",{"data":w})


def farmerbuyequip(request):
    rd=request.GET.get("id")
   
    # s=Supplier.objects.get(id=r.sid.id)
    pb=ProdBook.objects.get(id=rd)
    qty=pb.qty
    r=Products.objects.get(id=pb.pid.id)
    cid = request.session['id']
    d=Registration.objects.get(id=cid)
    dte=date.today()
    if request.POST:
        amt=request.POST["amt"]
        p=Payment.objects.create(sender=d.Email,receiver="admin",date=dte,amt=amt)
        p.save()
        r.quantity=r.quantity-qty
        r.save()
        pb.status="Paid"
        pb.save()
        # if r.quantity == 0:
            # r.delete()
        return redirect("/farmerseed")

        
    return render(request,"farmerbuyequip.html",{"data":pb})


def equipqselect(request):
    pid=request.GET.get("id")
    uid=request.session["id"]
    user=Registration.objects.get(id=uid)
    pd=Products.objects.get(id=pid)
    dte=date.today()
    if request.POST:
        rate=request.POST["rate"]
        qty=request.POST["qty"]
        tot=request.POST["tot"]
        try:
            pb=ProdBook.objects.create(pid=pd,amt=tot,qty=qty,user=user,date=dte,status="booked")
            pb.save()
        except Exception as e:
            messages.info(request,e)
        else:
            messages.info(request,"Product booked successfully")
            return redirect("/farmerseed")
    return render(request,"equipqselect.html",{"data":pd})


def supviewprodbook(request):
    data=ProdBook.objects.all()
    return render(request,"supviewprodbook.html",{"data":data})

def supdeliver(request):
    pid=request.GET.get("id")
    pd=ProdBook.objects.get(id=pid)
    pd.status="delivered"
    pd.save()

    return redirect("/supviewprodbook")

def farvprodbook(request):
    uid=request.session["id"]
    data=ProdBook.objects.filter(user=uid)

    return render(request,"farvprodbook.html",{"data":data})

def supupdateequip(request):
    pid=request.GET.get("id")
    data=Products.objects.get(id=pid)
    if request.POST:
        rate=request.POST["rate"]
        qty=request.POST["qty"]
        data.price=rate
        data.quantity=qty
        data.save()
        return redirect("/suppliervequip")
    return render(request,"supupdateequip.html",{"data":data})

  

def farmerviewpayment(request):
    uid=request.session["id"]
    user=Registration.objects.get(id=uid)
    email=user.Email
    data=Payment.objects.filter(receiver=email)
    return render(request,"farmerviewpayment.html",{"data":data})


def farupdateyield(request):
    pid=request.GET.get("id")
    data=Yield.objects.get(id=pid)
    if request.POST:
        rate=request.POST["rate"]
        qty=request.POST["qty"]
        data.price=rate
        data.quantity=qty
        data.save()
        return redirect("/farviewyield")

    return render(request,"farupdateyield.html",{"data":data})


def farviewyield(request):
    uid=request.session["id"]
    data=Yield.objects.filter(fid=uid)

    return render(request,"farviewyield.html",{"data":data})

def pubReg(request):
     if request.POST:
        name=request.POST["name"]
        contact=request.POST["con"]
        email=request.POST["email"]
        psw=request.POST["pass"]
        user=CustomUser.objects.filter(username=email).exists()
        if not user:
            try:
                r=Public.objects.create(Name=name,Contact=contact,Email=email,password=psw,status=1)
                r.save()
            except:
                messages.info(request,'sorry some error occured')
            else:
                try:
                    u=CustomUser.objects.create_user(username=email,password=psw,is_superuser=0,is_active=1,is_staff=0,email=email,usertype='public')
                    u.save()
                except:
                    messages.info(request,'Sorry some error occured')
                else:
                    messages.info(request,"Registration Successful")
        else:
            messages.info(request,"User already registered")
     return render(request,"pubreg.html")

def pubVprod(request):
    return render(request,"pubVprod.html")

def pubVBooking(request):
    return render(request,"pubVBooking.html")

def farmerComplaint(request):
    uid = request.session['id']
    u = Registration.objects.get(id=uid)
    if request.POST:
        title = request.POST["title"]
        complaint = request.POST["complaint"]
        cat = request.POST["cat"]
        c = Complaint.objects.create(title=title,complaint=complaint,cat=cat,pid=u)
        c.save()

    return render(request,"farmerComplaint.html")

def krishibhavanhome(request):
    return render(request,"krishibhavanhome.html")

def pubHome(request):
    return render(request,"pubHome.html")

def kbComplaints(request):
    data =Complaint.objects.all()
    return render(request,"kbComplaints.html",{"data":data})

def pubStore(request):
    data=Yield.objects.all()

    return render(request,"pubStore.html",{"data":data})



def farmerreqexp(request):
    data=Expert.objects.all()
    return render(request,"farmerreqexp.html",{"data":data})

def farmervexp(request):
    sid = request.session['id']
    data=Specbook.objects.filter(user=sid)
    return render(request,"farmervexp.html",{"data":data})

def userexpbook(request):
    eid=request.GET.get("id")
    data=Expert.objects.get(id=eid)
    uid=request.session["id"]
    user=Registration.objects.get(id=uid)
    if request.POST:
        
        info=request.POST["info"]
        try:
            pb=Specbook.objects.create(did=data,info=info,user=user,status="requested")
            pb.save()
        except Exception as e:
            messages.info(request,e)
        else:
            messages.info(request,"Expert Requested successfully")
            return redirect("/farmerreqexp")
    return render(request,"userexpbook.html",{"data":data})


def expertreq(request):
    sid = request.session['id']
    data=Specbook.objects.filter(did=sid)
    return render(request,"expertreq.html",{"data":data})
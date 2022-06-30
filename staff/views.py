from django import forms
from django.shortcuts import render, redirect
from staff.utils.BootStrap import BootStrapForm
# Create your views here.
from staff import models
from staff.utils.pagination import Pagination
def admin_list(request):
    '''管理员列表'''

    queryset = models.Admin.objects.all()
    page_object = Pagination(request,queryset)
    info=request.session.get('info')
    print(info)
    return render(request, 'admin_list.html', {'queryset': page_object.page_queryset,'page_string':page_object.html()})

class AdminModelForm(BootStrapForm):
    class Meta:
        model = models.Admin
        fields=['username','password']
        widgets = {
            'password': forms.PasswordInput
        }

def admin_add(request):
    '''添加管理员'''
    if request.method=='GET':
        form =AdminModelForm()
        return render(request,'admin_add.html',{'form':form})
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list')
    return render(request, 'admin_add.html', {'form': form})

def admin_edit(request,nid):
    '''编辑'''
    row_object = models.Admin.objects.filter(id=nid).first()
    if request.method=='GET':
        if not row_object:
            redirect('/admin/list/')

        form = AdminModelForm(instance=row_object)
        return render(request,'admin_edit.html',{'form':form})
    form = AdminModelForm(instance=row_object,data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list')
    return render(request,'admin_edit.html',{'form':form})

def admin_delete(request,nid):
    models.Admin.objects.filter(id=nid).delete()
    return redirect('/admin/list/')

def depart_list(request):
    '''部门列表'''
    from staff.utils.pagination import Pagination
    queryest = models.Department.objects.all()
    page_object = Pagination(request,queryest)
    return render(request, 'depart_list.html', {'queryest': page_object.page_queryset,
                                                'page_string':page_object.html() })

def depart_add(request):
    '''添加部门'''
    if request.method == 'GET':
        return render(request, 'depart_add.html')
    # 获取前端传回来的值
    title = request.POST.get('title')
    # 保存到数据库
    models.Department.objects.create(industry_title=title)

    return redirect('/depart/list/')

def depart_delete(request):
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()

    return redirect('/depart/list/')

def depart_edit(request, nid):
    if request.method == 'GET':
        row_object = models.Department.objects.filter(id=nid).first()
        return render(request, 'depart_edit.html', {'row_object': row_object})

    title = request.POST.get('title')
    models.Department.objects.filter(id=nid).update(industry_title=title)
    return redirect('/depart/list/')

def user_list(request):
    '''用户管理'''
    # 获取所有用户
    from staff.utils.pagination import Pagination
    queryset = models.staff.objects.all()
    page_object = Pagination(request,queryset,)
    return render(request, 'user_list.html', {'queryset': page_object.page_queryset,
                                              'page_string':page_object.html()})

from django import forms
class UserModelForm(BootStrapForm):
    class Meta:
        model = models.staff
        fields = ['name', 'password', 'age', 'account', 'create_time', 'gender', 'department']
        # widgets = {
        #     'name':forms.TextInput(attrs={'class':'form-control'})
        # }

def user_add(request):
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_add.html', {'form': form})
    # post
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'user_add.html', {'form': form})

def user_edit(request, nid):
    # 根据id去数据库获取要编辑的那一行数据
    if request.method == 'GET':
        row_object = models.staff.objects.filter(id=nid).first()
        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit.html', {'form': form})
    row_object = models.staff.objects.filter(id=nid).first()
    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'user_edit.html', {'form': form})

def user_delete(request, nid):
    models.staff.objects.filter(id=nid).delete()
    return redirect('/user/list/')

def phone_list(request):
    dict = {}
    q = request.GET.get('q')
    if q:
        dict['mobile__contains'] = q


    from staff.utils.pagination import Pagination
    queryset = models.beautyPhone.objects.filter(**dict).order_by("-rank")

    page_object = Pagination(request,queryset)
    return render(request, 'phone_list.html',
                  {'queryset': page_object.page_queryset,
                    'q': q,
                   'page_string':page_object.html()})

from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class PhoneModelForm(BootStrapForm):
    mobile = forms.CharField(label='手机号',
                             validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')])

    class Meta:
        model = models.beautyPhone
        fields = '__all__'

    def clean_mobile(self):
        p = self.cleaned_data['mobile']
        exists = models.beautyPhone.objects.filter(mobile=p).exists()
        if exists:
            raise ValidationError('手机号已存在')
        return p

def phone_add(request):
    if request.method == 'GET':
        form = PhoneModelForm()
        return render(request, 'phone_add.html', {'form': form})
    form = PhoneModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/phone/list')
    return render(request, 'phone_add.html', {'form': form})

def phone_edit(request, nid):
    row_obj = models.beautyPhone.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = PhoneModelForm(instance=row_obj)
        return render(request, 'phone_edit.html', {'form': form})
    form = PhoneModelForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/phone/list/')
    return render(request, 'phone_edit.html', {'form': form})

def phone_delete(request, nid):
    models.beautyPhone.objects.filter(id=nid).delete()
    return redirect('/phone/list/')
class LoginModelForm(BootStrapForm):
    class Meta:
        model = models.Admin
        fields = ['username','password']
        widgets={
            'password':forms.PasswordInput(render_value=True),
        }
def login(request):
    """登录"""
    if request.method=='GET':
        form = LoginModelForm()
        return render(request,'login.html',{'form':form})
    form = LoginModelForm(data=request.POST)
    if form.is_valid():
        admin_obj = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_obj:
            form.add_error('password','用户名或密码错误')
            return render(request, 'login.html', {'form': form})
        request.session['info']=admin_obj.username
        return redirect('/admin/list/')
    return render(request, 'login.html', {'form': form})

def logout(request):

    request.session.clear()
    return redirect('/login/')
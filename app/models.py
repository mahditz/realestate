from django.db import models
from django.urls import reverse
from django_jalali.db import models as jmodels
from PIL import Image 



class Area(models.Model):
    
    area =  models.CharField(primary_key=True,max_length=10,verbose_name = "منطقه")
     
    class Meta:
        verbose_name = "منطقه"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.area




class rent(models.Model):
    code = models.CharField(max_length=9, unique=True,verbose_name="کد فایل")
    title = models.CharField(max_length=35,default="خونه",verbose_name="عنوان فایل")
    adress = models.CharField(max_length=68,default="شهرک اکباتان",verbose_name="آدرس")
    nameM = models.CharField(max_length=50,verbose_name="نام مالک")
    CHOICES = (('آپارتمان','آپارتمان'), ('اداری و تجاری','اداری و تجاری'))
    melktype = models.CharField(max_length=20,choices=CHOICES,verbose_name="نوع ملک")
    CHOICES2 = (('1', '1'),('2', '2'),('3', '3'))
    phase = models.CharField(max_length=10,choices=CHOICES2,null=True,blank=True,verbose_name="فاز")
    block = models.CharField(max_length=4,null=True,blank=True,verbose_name="بلوک")
    entry = models.CharField(max_length=20,null=True,blank=True,verbose_name="ورودی")
    CHOICES3 = (('شمالی','شمالی'), ('جنوبی','جنوبی'),('شرقی','شرقی'),('غربی','غربی'))
    side = models.CharField(max_length=10,null=True,blank=True,choices=CHOICES3,verbose_name="جهت")
    area = models.ForeignKey(Area,on_delete=models.CASCADE,verbose_name="منطقه")
    metraj = models.PositiveSmallIntegerField(null=True,blank=True,verbose_name = "متراژ (متر)")
    room_qty = models.PositiveSmallIntegerField(null=True,blank=True, verbose_name = "تعداد اتاق")
    floor = models.PositiveSmallIntegerField(null=True,blank=True,verbose_name="طبقه")
    pelak = models.CharField(max_length=20,null=True,blank=True,verbose_name="پلاک")
    phone = models.CharField(max_length=15,null=True,blank=True,verbose_name="تلفن")
    mobile = models.CharField(max_length=15,verbose_name="موبایل")
    priceR = models.BigIntegerField(null=True,blank=True, default='0',verbose_name="ودیعه  (تومان)")
    priceE = models.BigIntegerField(null=True,blank=True, default='0',verbose_name="اجاره  (تومان)")
    image = models.ImageField(upload_to='static/home',null=True, blank=True,verbose_name ="تصویر اصلی")
    image2 = models.ImageField(upload_to='static/home',null=True, blank=True,verbose_name ="تصویر دوم")
    image3 = models.ImageField(upload_to='static/home',null=True, blank=True,verbose_name ="تصویر سوم")
    parking = models.BooleanField(default=False, verbose_name = "پارکینگ" )
    storage_room = models.BooleanField(default=False, verbose_name = "انباری" )
    elevator = models.CharField(max_length=30,null=True,blank=True,verbose_name = "پوشش کف")
    building_age = models.PositiveSmallIntegerField(null=True,blank=True, verbose_name = "سن بنا (سال)")
    additional_information = models.TextField(max_length=2000,null=True, blank=True,verbose_name = "اطلاعات تکمیلی")
    date = jmodels.jDateField(auto_now_add=True, verbose_name = "تاریخ آگهی")
    relname = models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name="مشاور فروش")
    status = models.BooleanField(default=True, verbose_name = "وضعیت")

    class Meta:
        verbose_name = "رهن"
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return str("کد "+self.code)
      
    def get_absolute_url(self):
        return reverse('detrent', kwargs={'pk': self.pk})

    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        if self.image2 :
            self.image2.storage.delete(self.image2.name)
        if self.image3 : 
            self.image3.storage.delete(self.image3.name)
        super().delete()


    def save(self):
        super().save() 
        if self.image :
                img = Image.open(self.image.path) 
                THUMB_SIZE = (592,444)
                img = img.resize(THUMB_SIZE, Image.ANTIALIAS)
                img.save(self.image.path)
        if self.image2 :
                img = Image.open(self.image2.path) 
                THUMB_SIZE = (592,444)
                img = img.resize(THUMB_SIZE, Image.ANTIALIAS)
                img.save(self.image2.path)  
    
        if self.image3 :
                img = Image.open(self.image3.path) 
                THUMB_SIZE = (592,444)
                img = img.resize(THUMB_SIZE, Image.ANTIALIAS)
                img.save(self.image3.path)    


class sell(models.Model):
    code = models.CharField(max_length=9, unique=True,verbose_name="کد فایل")
    title = models.CharField(max_length=35,default="خونه",verbose_name="عنوان فایل")
    adress = models.CharField(max_length=68,default="شهرک اکباتان",verbose_name="آدرس")
    nameM = models.CharField(max_length=50,verbose_name="نام مالک")
    CHOICES = (('آپارتمان','آپارتمان'), ('اداری و تجاری','اداری و تجاری'))
    melktype = models.CharField(max_length=20,choices=CHOICES,verbose_name="نوع ملک")
    CHOICES2 = (('1', '1'),('2', '2'),('3', '3'))
    phase = models.CharField(max_length=10,choices=CHOICES2,null=True,blank=True,verbose_name="فاز")
    block = models.CharField(max_length=4,null=True,blank=True,verbose_name="بلوک")
    entry = models.CharField(max_length=20,null=True,blank=True,verbose_name="ورودی")
    CHOICES3 = (('شمالی','شمالی'), ('جنوبی','جنوبی'),('شرقی','شرقی'),('غربی','غربی'))
    side = models.CharField(max_length=10,null=True,blank=True,choices=CHOICES3,verbose_name="جهت")
    area = models.ForeignKey(Area,on_delete=models.CASCADE,verbose_name="منطقه")
    metraj = models.PositiveSmallIntegerField(null=True,blank=True,verbose_name = "متراژ (متر)")
    room_qty = models.PositiveSmallIntegerField(null=True,blank=True, verbose_name = "تعداد اتاق")
    floor = models.PositiveSmallIntegerField(null=True,blank=True,verbose_name="طبقه")
    pelak = models.CharField(max_length=20,null=True,blank=True,verbose_name="پلاک")
    phone = models.CharField(max_length=15,null=True,blank=True,verbose_name="تلفن")
    mobile = models.CharField(max_length=15,verbose_name="موبایل")
    priceM = models.BigIntegerField(null=True,blank=True, default='0',verbose_name="قیمت هر متر  (تومان)")
    priceK = models.BigIntegerField(null=True,blank=True, default='0',verbose_name="قیمت کل  (تومان)")
    image = models.ImageField(upload_to='static/home',null=True, blank=True,verbose_name ="تصویر اصلی")
    image2 = models.ImageField(upload_to='static/home',null=True, blank=True,verbose_name ="تصویر دوم")
    image3 = models.ImageField(upload_to='static/home',null=True, blank=True,verbose_name ="تصویر سوم")
    parking = models.BooleanField(default=False, verbose_name = "پارکینگ" )
    storage_room = models.BooleanField(default=False, verbose_name = "انباری" )
    elevator = models.CharField(max_length=30,null=True,blank=True,verbose_name = "پوشش کف")
    building_age = models.PositiveSmallIntegerField(null=True,blank=True, verbose_name = "سن بنا (سال)")
    additional_information = models.TextField(max_length=2000,null=True, blank=True,verbose_name = "اطلاعات تکمیلی")
    date = jmodels.jDateField(auto_now_add=True, verbose_name = "تاریخ آگهی")
    relname = models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name="مشاور فروش")
    status = models.BooleanField(default=True, verbose_name = "وضعیت")

    class Meta:
        verbose_name = "فروش"
        verbose_name_plural = verbose_name

   
    def __str__(self):
        return str("کد "+self.code)
    
    def get_absolute_url(self):
        return reverse('detsell', kwargs={'pk': self.pk})

    def save(self):
        super().save() 
        if self.image :
                img = Image.open(self.image.path) 
                THUMB_SIZE = (592,444)
                img = img.resize(THUMB_SIZE, Image.ANTIALIAS)
                img.save(self.image.path)
        if self.image2 :
                img = Image.open(self.image2.path) 
                THUMB_SIZE = (592,444)
                img = img.resize(THUMB_SIZE, Image.ANTIALIAS)
                img.save(self.image2.path)  
    
        if self.image3 :
                img = Image.open(self.image3.path) 
                THUMB_SIZE = (592,444)
                img = img.resize(THUMB_SIZE, Image.ANTIALIAS)
                img.save(self.image3.path) 
    

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        if self.image2 :
            self.image2.storage.delete(self.image2.name)
        if self.image3 : 
            self.image3.storage.delete(self.image3.name)
        super().delete()



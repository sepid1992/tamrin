from django.shortcuts import render,HttpResponse
# Create your views here.


def home (request):
    
    
    media=[
        {"onvan":"اخبار فرهنگی","title":"نمایشگاه نقاشی «خاطرات پری و گنجشک‌ها» را به مدت دَه روز برپا می‌کند."},
        {"onvan":"اخبارسیاسی","title":"خنثی شدن برنامه تروریستها در تاسوعا و عاشورا با اعزام پنج تیپ تکاور سپاه به مناطق مرزی"},
        {"onvan":"اخبار بین الملل","title":"چرایی اقدام داعش در انجام گسترده‌ترین حمله خود در شرق سوریه؛ شبح بازگشت داعش با حمایت آمریکا؟"},
        {"onvan":"اخبار ورزشی ","title":"تیم نونهالان استقلال در دربی مقابل پرسپولیس به برتری رسید.."},
        {"onvan":"اخبار مجلس","title":"انتقال سازمان ثبت اسناد به زیرمجموعه دولت در کمیسیون تلفیق تصویب شد"},
    ]
    
    return render(request,"news\index.html",context={"khabar":media})
def entrancenews(request,adad):
    return render(request,"news\entrance.html")


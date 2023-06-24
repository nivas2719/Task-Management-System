
# import path when u use urls separately for each app
from django.urls import path

# import views from DailyWorkStatus app
from DailyWorkStatus import views

# for login functionality
from django.contrib.auth import views as g 


urlpatterns=[
	path("",views.home,name="hm"),
	path("abt/",views.about,name="ab"),
	path("cnt/",views.contact,name="ct"),
	path("rg/",views.register,name="reg"),
	path("ds/",views.dashboard,name="dsh"),
	path('pf/',views.prfle,name="pfe"),
	path('upf/',views.updf,name="upfe"),
	path('wrk/',views.wrklg,name='wk'),
	path('crwrk/',views.creationwk,name="crw"),
	path("lgg/",g.LogoutView.as_view(template_name="html/logout.html"),name="lgo"),
	path("lg/",g.LoginView.as_view(template_name="html/login.html"),name="lgn"),
]
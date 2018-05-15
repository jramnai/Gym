from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
# from mysite.account import views as core_views
# from account.ivew import views

app_name = 'account'
urlpatterns = [
    # account/signup
    # url(r'^login/$', auth_views.login,
    #     {'template_name': 'account/login.html'}, name='login'),
    url(r'^login/$', auth_views.LoginView.as_view(redirect_authenticated_user=True,
                                                  template_name='account/login.html'), name='login'),

    url(r'^logout/$', auth_views.logout,
        {'next_page': 'gym:index'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^detail/$', views.detail, name='detail'),
]

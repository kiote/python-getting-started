from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views
import line.views
import viber.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("login/", hello.views.login, name="login"),
    path("admin/", admin.site.urls),
    path("logout/", hello.views.logout, name="logout"),

    path("line-message-callback/", line.views.message_callback, name="line_message_callback"),
    path("line-message-reply/", line.views.message_reply, name="line_message_reply"),

    path("viber-callback/", viber.views.callback_url, name="viber_callback_url"),
    path("viber-send/", viber.views.send_message, name="viber_send"),

    # seems like routes are somehow dpendent, so this one goes last
    # to not mess up with the rest
    path("send/", hello.views.send_message, name="send"),
    path("message/", hello.views.message, name="message")
]

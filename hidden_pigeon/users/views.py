from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import RedirectView

User = get_user_model()


def user_detail_view(request, username):

    this_user = User.objects.get(username=username)

    return render(request, "../templates/users/user_detail.html", {"object": this_user})


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()

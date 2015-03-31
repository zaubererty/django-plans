from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.http import HttpResponseRedirect

from plans.decorators import company_required


class LoginRequired(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequired, self).dispatch(*args, **kwargs)


class UserObjectsOnlyMixin(object):
    def get_queryset(self):
        return super(UserObjectsOnlyMixin, self).get_queryset().filter(user=self.request.user)


class OrgAdminRequired(View):
    def dispatch(self, request, *args, **kwargs):
        if self.request.org_user.is_admin:
            self.organization = self.request.organization
            print "User is admin for %s" % self.organization
            return super(OrgAdminRequired, self).dispatch(request, *args, **kwargs)
        else:
            print "User is not admin"
            return HttpResponseRedirect('/dashboard/')


# not working
class CompanyRequired(View):
    @method_decorator(login_required)
    @method_decorator(company_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CompanyRequired, self).dispatch(request, *args, **kwargs)

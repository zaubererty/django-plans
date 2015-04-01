from functools import wraps
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.exceptions import PermissionDenied
from django.utils.decorators import available_attrs
from django.utils.six.moves.urllib.parse import urlparse
from django.shortcuts import resolve_url
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import user_passes_test

from organizations.models import Organization


def company_required(function=None, login_url=None, raise_exception=False):
    """
    Decorator for views that checks if the user has company, redirecting
    to the company creation page if necessary.
    """
    # login_url = resolve_url('/organizations/add/')
    login_url = '/organizations/add/'
    print login_url
    def check_organizations(user):
        print user
        organizations = Organization.objects.filter(owner__organization_user__user=user)
        print organizations

        if organizations:
            return True
        else:
            return False
    return user_passes_test(check_organizations, login_url=login_url)

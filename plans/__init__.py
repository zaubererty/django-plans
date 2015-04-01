from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured, PermissionDenied


def get_user_model():
    """
    Returns the model that acts as users that owns plans.
    It could be any model.
    """
    if getattr(settings, 'PLANS_USER_MODEL', ''):
        user_model = settings.PLANS_USER_MODEL
    else:
        user_model = settings.AUTH_USER_MODEL
    try:
        return django_apps.get_model(user_model)
    except ValueError:
        raise ImproperlyConfigured("PLANS_USER_MODEL and AUTH_USER_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured("USER_MODEL refers to model '%s' that has not been installed" % user_model)



def get_user_model_settings():
    if getattr(settings, 'PLANS_USER_MODEL', ''):
        return settings.PLANS_USER_MODEL
    else:
        return settings.AUTH_USER_MODEL

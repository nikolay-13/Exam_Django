from django.http import Http404


def check_user_group_dec(*groups):
    def decorator(group):
        def wrapper(request, *args, **kwargs):
            if request.user.groups.filter(name__in=groups).exists():
                return group(request, *args, **kwargs)
            elif request.user.is_superuser:
                return group(request, *args, **kwargs)
            raise Http404

        return wrapper

    return decorator

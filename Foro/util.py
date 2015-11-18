from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def reverse2(name, *args, **kwargs):
    return reverse(name, args=args, kwargs=kwargs)


def redir(to, *args, **kwargs):
    if not (to.startswith('/') or to.startswith("http://") or to.startswith("../") or to=='#'):
        to = reverse(to, args=args, kwargs=kwargs)
    return HttpResponseRedirect(to)
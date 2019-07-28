from urllib.parse import urlencode


def get_args(request):
    """
    Gets page arguments and strips 'page' from them, then returns the
    arguments in a URL format.
    """
    args = request.GET.copy()
    if "page" in args:
        del args["page"]
    return {"get_args": "&{0}".format(args.urlencode())}

from urllib.parse import urlencode

def get_args(request):
    args = request.GET.copy()
    if "page" in args:
        del args["page"]
    return {"get_args": "&{0}".format(args.urlencode())}

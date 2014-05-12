from config import constants

def site_config_constants(request):
    context = {}

    context["LC_NAME"] = constants.LC_NAME

    return context

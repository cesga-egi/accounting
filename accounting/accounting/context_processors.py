from django.conf import settings # import the settings file

def support_server(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'SUPPORT_SERVER': settings.SUPPORT_SERVER}

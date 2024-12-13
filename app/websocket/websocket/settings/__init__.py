import environ

# def get_variables(var, default=None):
#         return os.environ.get(var, default)

if environ.Env().str('PIPELINE') == 'production':
        from .production import *
else:
        from .local import *
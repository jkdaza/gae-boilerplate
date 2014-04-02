from webapp2_extras.routes import RedirectRoute
from bp_content.themes.default.plugins.test.handlers import handlers

secure_scheme = 'https'

_routes = [
    RedirectRoute('/test/', handlers.TestHandler, name='editor', strict_slash=True),
]

def get_routes():
    return _routes

#This is called on import from defalt/routes/__init__.py

def add_routes(app):
    if app.debug:
        secure_scheme = 'http'
    for r in _routes:
        app.router.add(r)

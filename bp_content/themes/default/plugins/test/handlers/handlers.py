# -*- coding: utf-8 -*-

"""
    A test plugin that render its template
    Routes are setup in plugins/test/routes/__init__.py
"""
# standard library imports


from bp_includes.lib.basehandler import BaseHandler

class TestHandler(BaseHandler):
    """
    Handler for test
    """

    def get(self):
        params = {
            
        }

        return self.render_template('test.html', **params)
    

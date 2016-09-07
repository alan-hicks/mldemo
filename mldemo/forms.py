#----------------------------------------------------------------------
# Copyright (c) 2014-2016, Persistent Objects Ltd http://p-o.co.uk/
#
# License: BSD
#----------------------------------------------------------------------

"""
Multilingual demo models
"""

from django import forms
from django.contrib.staticfiles.storage import staticfiles_storage

class TinyMceWidget(forms.Textarea):
    """
    Setup the JS files and targetting CSS class for a textarea to
    use TinyMCE.
    """
    #pylint: disable=super-on-old-class

    def __init__(self, *args, **kwargs):
        super(TinyMceWidget, self).__init__(*args, **kwargs)
        self.attrs["class"] = "mceEditor"

    class Media(object):
        """
        Media class for TinyMceWidget
        """
        #pylint: disable=invalid-name,too-few-public-methods
        _tinymce_js = (
            staticfiles_storage.url("js/tinymce/tinymce.min.js"),
            staticfiles_storage.url("js/tinymce_setup.js"),
        )
        js = _tinymce_js

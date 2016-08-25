from __future__ import absolute_import, unicode_literals

import logging
import os

from mopidy import config, exceptions, ext
from .actor import moplcdFrontend


__version__ = '0.1.1'


class Extension(ext.Extension):

    dist_name = 'moplcd'
    ext_name = 'moplcd'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)
        
    

    def setup(self, registry):
        registry.add('frontend', moplcdFrontend)

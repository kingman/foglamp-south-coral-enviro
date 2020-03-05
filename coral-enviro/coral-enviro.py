# -*- coding: utf-8 -*-

# FOGLAMP_BEGIN
# See: http://foglamp.readthedocs.io/
# FOGLAMP_END

from datetime import datetime
from coral.enviro.board import EnviroBoard
import uuid

from foglamp.common import logger
from foglamp.services.south import exceptions

__author__ = "Charlie Wang"
__copyright__ = "Copyright 2020 Google Inc."
__license__ = "Apache 2.0"
__version__ = "${VERSION}"

_DEFAULT_CONFIG = {
    'plugin': {
         'description': 'Python module name of the plugin to load',
         'type': 'string',
         'default': 'coral-enviro'
    },
    'pollInterval': {
        'description': 'The interval between poll calls to the device poll routine expressed in milliseconds.',
        'type': 'integer',
        'default': '10000'
    }
}

_LOGGER = logger.setup(__name__)
""" Setup the access to the logging system of FogLAMP """


def plugin_info():
    return {
        'name': 'Coral Environmental Sensor Board',
        'version': '1.0',
        'mode': 'poll',
        'type': 'south',
        'interface': '1.0',
        'config': _DEFAULT_CONFIG
    }

def plugin_init(config):
    return {} 

def plugin_poll(handle):
    try:
        enviro = EnviroBoard()
        time_stamp = str(datetime.now())
        readings = {
            'temperature': enviro.temperature,
            'humidity': enviro.humidity,
            'ambient_light': enviro.ambient_light,
            'pressure': enviro.pressure
        }
        wrapper = {
                'asset':     'enviro',
                'timestamp': time_stamp,
                'key':       str(uuid.uuid4()),
                'readings':  readings
        }
        return wrapper
    except Exception as ex:
        raise exceptions.DataRetrievalError(ex)

    return None

def plugin_reconfigure(handle, new_config):
    return {}

def plugin_shutdown(handle):
    pass
# -*- coding: utf-8 -*-

# FOGLAMP_BEGIN
# See: http://foglamp.readthedocs.io/
# FOGLAMP_END

from datetime import datetime
from coral.enviro.board import EnviroBoard
import copy
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
    },
    'temperatureSensor': {
        'description': 'Enable Temperature sensor',
        'type': 'boolean',
        'default': 'true',
        'order': '3',
        'displayName': 'Temperature Sensor'
    },
    'pressureSensor': {
        'description': 'Enable Barometric Pressure sensor',
        'type': 'boolean',
        'default': 'true',
        'order': '4',
        'displayName': 'Pressure Sensor'
    },
    'humiditySensor': {
        'description': 'Enable Humidity sensor',
        'type': 'boolean',
        'default': 'true',
        'order': '5',
        'displayName': 'Humidity Sensor'
    },
    'ambientLightSensor': {
        'description': 'Enable Ambient Light sensor',
        'type': 'boolean',
        'default': 'true',
        'order': '6',
        'displayName': 'Ambient Light Sensor'
    },
    'groveAnalogSensor': {
        'description': 'Enable Grove Analog sensor',
        'type': 'boolean',
        'default': 'false',
        'order': '7',
        'displayName': 'Grove Analog Sensor'
    }
}

_LOGGER = logger.setup(__name__)
""" Setup the access to the logging system of FogLAMP """

_enviro = None

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
    data = copy.deepcopy(config)
    global _enviro
    _enviro = EnviroBoard() 
    return data

def plugin_poll(handle):
    try:
        time_stamp = str(datetime.utcnow())
        readings = {}
        if handle['temperatureSensor']['value'] == 'true':
            readings['temperature'] = _enviro.temperature

        if handle['pressureSensor']['value'] == 'true':
            readings['pressure'] = _enviro.pressure

        if handle['humiditySensor']['value'] == 'true':
            readings['humidity'] = _enviro.humidity

        if handle['ambientLightSensor']['value'] == 'true':
            readings['ambient_light'] = _enviro.ambient_light

        if handle['groveAnalogSensor']['value'] == 'true':
            readings['grove_analog'] = _enviro.grove_analog

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
    new_handle = copy.deepcopy(new_config)
    return new_handle

def plugin_shutdown(handle):
    pass

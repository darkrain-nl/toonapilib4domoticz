import Domoticz
import toonapilib
from devices.device_container import container
from devices.gas import DeviceGas
from devices.heating_active import DeviceHeatingActive
from devices.hotwater_active import DeviceHotWaterActive
from devices.modulation_level import DeviceModulationLevel
from devices.power import DevicePower
from devices.preheat_active import DevicePreHeatActive
from devices.program_state import DeviceProgramState
from devices.set_point import DeviceSetPoint
from devices.temperature import DeviceTemperature
from devices.thermostat_state import DeviceThermostatState


class DeviceFactory:
    def __init__(self):
        return

    @staticmethod
    def create_devices(toon, plugin_devices):
        Domoticz.Log("Check and create Toon devices")

        """Adding standard devices"""
        container.add_device(DevicePower(plugin_devices, toon).create())
        container.add_device(DeviceGas(plugin_devices, toon).create())
        container.add_device(DeviceTemperature(plugin_devices, toon).create())
        container.add_device(DeviceSetPoint(plugin_devices, toon).create())
        container.add_device(DeviceHeatingActive(plugin_devices, toon).create())
        container.add_device(DeviceHotWaterActive(plugin_devices, toon).create())
        container.add_device(DevicePreHeatActive(plugin_devices, toon).create())
        container.add_device(DeviceThermostatState(plugin_devices, toon).create())
        container.add_device(DeviceProgramState(plugin_devices, toon).create())
        container.add_device(DeviceModulationLevel(plugin_devices, toon).create())

        return container

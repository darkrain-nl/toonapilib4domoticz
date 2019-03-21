import Domoticz
from devices.configuration import config
from devices.device import Device
from devices.device import DeviceCreateException
from devices.device import DeviceUpdateException


class DeviceModulationLevel(Device):
    domoticz_device_type = 243
    domoticz_subtype = 6
    domoticz_switch_type = 0

    def __init__(self, plugin_devices, toon):
        super().__init__(config.STR_UNIT_MODULATION_LEVEL,
                         config.STD_UNIT_MODULATION_LEVEL,
                         plugin_devices,
                         toon)

    def create(self):
        if not self.exists:
            try:
                Domoticz.Log("Creating modulation level device " + self.name)
                Domoticz.Device(Name=self.name, Unit=self.unit, Type=self.domoticz_device_type,
                                Subtype=self.domoticz_subtype, Switchtype=self.domoticz_switch_type).Create()

            except DeviceCreateException as ex:
                Domoticz.Log("An error occurred creating " + self.name)
                Domoticz.Log("Exception: " + str(ex))
        elif config.debug:
            Domoticz.Log("Unit " + str(self.unit) + " exists - nothing to do")
        return self

    def update(self):
        super().update()
        str_value = ""

        try:
            modulation_level = self.toon.thermostat_info.current_modulation_level
            str_value = str(modulation_level)

            if str_value != self.previous_value:
                if config.debug:
                    Domoticz.Log("Update modulation level: " + str_value)
                self.plugin_devices[self.unit].Update(modulation_level, str_value)

        except DeviceUpdateException as ex:
            Domoticz.Log("An error occurred updating " + self.name)
            Domoticz.Log("Exception: " + str(ex))

        self.set_previous_value(str_value)

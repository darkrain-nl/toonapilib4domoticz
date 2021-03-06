import Domoticz
from devices.configuration import config
from devices.device import Device
from devices.device import DeviceCreateException
from devices.device import DeviceUpdateException


class DeviceHeatingActive(Device):
    domoticz_device_type = 244
    domoticz_subtype = 62
    domoticz_switch_type = 0
    domoticz_image = 9

    def __init__(self, plugin_devices, toon):
        super().__init__(config.STR_UNIT_HEATING_ACTIVE,
                         config.STD_UNIT_HEATING_ACTIVE,
                         plugin_devices,
                         toon)

    def create(self):
        if not self.exists:
            try:
                Domoticz.Log("Creating heating active device " + self.name)
                Domoticz.Device(Name=self.name, Unit=self.unit, Type=self.domoticz_device_type,
                                Subtype=self.domoticz_subtype, Switchtype=self.domoticz_switch_type,
                                Image=self.domoticz_image).Create()

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
            heating_on = 1 if self.toon.burner_state == "on" else 0
            str_value = str(heating_on)

            if str_value != self.previous_value:
                if config.debug:
                    Domoticz.Log("Update heating active: " + str_value)
                self.plugin_devices[self.unit].Update(heating_on, str(heating_on))

        except DeviceUpdateException as ex:
            Domoticz.Log("An error occurred updating " + self.name)
            Domoticz.Log("Exception: " + str(ex))

        self.set_previous_value(str_value)

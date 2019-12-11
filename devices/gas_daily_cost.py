import Domoticz
from devices.configuration import config
from devices.device import Device
from devices.device import DeviceCreateException
from devices.device import DeviceUpdateException


class DeviceGasDailyCost(Device):
    domoticz_device_type = 243
    domoticz_subtype = 31

    def __init__(self, plugin_devices, toon):
        super().__init__(config.STR_UNIT_GAS_DAILY_COST,
                         config.STD_UNIT_GAS_DAILY_COST,
                         plugin_devices,
                         toon)

    def create(self):
        if not self.exists:
            try:
                Domoticz.Log("Creating daily cost device gas " + self.name)
                Domoticz.Device(Name=self.name, Unit=self.unit, Type=self.domoticz_device_type,
                                Subtype=self.domoticz_subtype, Options={"Custom": "1;EUR"}).Create()

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
            str_value = str(self.toon.gas.daily_cost)

            if str_value != self.previous_value:
                if config.debug:
                    Domoticz.Log("Update daily cost gas: " + str_value)
                self.plugin_devices[self.unit].Update(0, str_value)

        except DeviceUpdateException as ex:
            Domoticz.Log("An error occurred updating " + self.name)
            Domoticz.Log("Exception: " + str(ex))

        self.set_previous_value(str_value)

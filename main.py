from src.device import DeviceType
from src.device_manager import DeviceManager
from src.devices.switch import SwitchState
from src.devices.thermostat import ThermostatStateRepr
from src.dwelling_manager import DwellingManager
from src.hub import Hub


# Driver function
def main():
    # Instantiate the Manager classes
    device_manager = DeviceManager()
    dwelling_manager = DwellingManager()

    # Create a dwelling and set it to occupied
    home = dwelling_manager.create_dwelling("home_1")
    home.set_occupancy()

    # Create hub and install it in dwelling
    hub = Hub("hub_1")
    home.install_hub(hub)

    # Create devices
    switch = device_manager.create_device(DeviceType.SWITCH, "switch_1", "Family room lights")
    lock = device_manager.create_device(DeviceType.LOCK, "lock_1", "Back Door Lock")
    lock_with_pincode = device_manager.create_device(DeviceType.LOCK, "lock_2", "Front Door Lock", pin_code="1234")
    thermostat = device_manager.create_device(DeviceType.THERMOSTAT, "thermo_1", "Main Thermostat", temperature=72.5)
    dimmer = device_manager.create_device(DeviceType.DIMMER, "dimmer_1", "Bedroom Dimmer")

    # Pair the device with the hub
    hub.add_device(switch)
    hub.add_device(lock)
    hub.add_device(lock_with_pincode)
    hub.add_device(thermostat)
    hub.add_device(dimmer)

    # Modify device states

    lock.update_state()
    lock_with_pincode.update_state(pin_code="124")
    dimmer.update_state(brightness=70)
    switch.update_state()
    thermostat.update_state(mode=ThermostatStateRepr.HEAT)

    # List of devices and dwellings
    print(f"Paired devices: {hub.get_paired_devices()}")
    print(f"All devices: {device_manager.list_devices()}")
    print(f"All dwelllings: {dwelling_manager.list_dwellings()}")


if __name__ == "__main__":
    main()

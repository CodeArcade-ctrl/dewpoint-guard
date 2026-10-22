"""Binary sensor for Dewpoint Guard."""
from __future__ import annotations
from homeassistant.components.binary_sensor import BinarySensorEntity, BinarySensorDeviceClass
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([RiskSensor(coordinator, entry)])

class RiskSensor(CoordinatorEntity, BinarySensorEntity):
    """Report the configured threshold condition."""
    _attr_has_entity_name = True
    _attr_device_class = BinarySensorDeviceClass.PROBLEM
    _attr_name = "Condensation risk"
    def __init__(self, coordinator, entry):
        super().__init__(coordinator)
        self._attr_unique_id = f"{entry.entry_id}_risk"
        self._attr_device_info = {"identifiers": {(DOMAIN, entry.entry_id)}, "name": "Dewpoint Guard", "manufacturer": "CodeArcade-ctrl"}
    @property
    def is_on(self):
        return self.coordinator.data.get("risk")

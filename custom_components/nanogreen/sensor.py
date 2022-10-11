from datetime import datetime

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.util import dt as dt_util

from .const import (
    ATTR_API_TODAY_HOURLY_PRICES,
    ATTR_API_TOMORROW_HOURLY_PRICES,
    DOMAIN,
    ENTRY_COORDINATOR,
    ENTRY_NAME,
    SENSOR_TYPES,
)


class NanogreenPriceSensor(SensorEntity):
    def __init__(
        self,
        name: str,
        unique_id: str,
        description: SensorEntityDescription,
        coordinator: DataUpdateCoordinator,
    ):
        super().__init__()
        self.entity_description = description
        self._coordinator = coordinator
        self._attr_name = f"{name} {description.name}"
        self._attr_unique_id = unique_id

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        return self._coordinator.last_update_success

    async def async_added_to_hass(self) -> None:
        """Connect to dispatcher listening for entity data notifications."""
        self.async_on_remove(
            self._coordinator.async_add_listener(self.async_write_ha_state)
        )

    async def async_update(self) -> None:
        """Get the latest data from OWM and updates the states."""
        await self._coordinator.async_request_refresh()

    @property
    def native_value(self) -> StateType:
        """Return the state of the device."""
        return self._coordinator.data.get(self.entity_description.key, None)

    @property
    def extra_state_attributes(self):
        """Return entity specific state attributes."""
        return {
            ATTR_API_TODAY_HOURLY_PRICES: self._coordinator.data.get(
                ATTR_API_TODAY_HOURLY_PRICES
            ),
            ATTR_API_TOMORROW_HOURLY_PRICES: self._coordinator.data.get(
                ATTR_API_TOMORROW_HOURLY_PRICES
            ),
        }


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up OpenWeatherMap sensor entities based on a config entry."""
    domain_data = hass.data[DOMAIN][config_entry.entry_id]
    name = domain_data[ENTRY_NAME]
    coordinator = domain_data[ENTRY_COORDINATOR]

    entities: list[SensorEntity] = [
        NanogreenPriceSensor(
            name,
            f"{config_entry.unique_id}-{description.key}",
            description,
            coordinator,
        )
        for description in SENSOR_TYPES
    ]

    async_add_entities(entities)

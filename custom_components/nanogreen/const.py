"""Consts for the NanoGreen energy."""

from homeassistant.components.sensor import SensorEntityDescription, SensorDeviceClass
from homeassistant.const import Platform


DOMAIN = "nanogreen"
DEFAULT_NAME = "Nanogreen prices"
DEFAULT_LANGUAGE = "en"
ENTRY_NAME = "name"
ENTRY_COORDINATOR = "nanogreen_coordinator"
CONFIG_FLOW_VERSION = 1
CONF_LANGUAGE = "language"
UPDATE_LISTENER = "update_listener"
PLATFORMS = [Platform.SENSOR]


ATTR_API_CURRENT_PRICE = "current_price"
ATTR_API_IS_CURRENTLY_CHEAPEST_HOUR = "is_currently_cheapest_hour"
ATTR_API_TODAY_BASE_CHEAPEST_HOUR = "today_base_cheapest_hour"
ATTR_API_TODAY_PEAK_CHEAPEST_HOUR = "today_peak_cheapest_hour"
ATTR_API_TODAY_OFFPEAK_CHEAPEST_HOUR = "today_offpeak_cheapest_hour"
ATTR_API_TODAY_BASE_SECOND_CHEAPEST_HOUR = "today_base_second_cheapest_hour"
ATTR_API_TODAY_PEAK_SECOND_CHEAPEST_HOUR = "today_peak_second_cheapest_hour"
ATTR_API_TODAY_OFFPEAK_SECOND_CHEAPEST_HOUR = "today_offpeak_second_cheapest_hour"
ATTR_API_TODAY_HOURLY_PRICES = "today_hourly_prices"
ATTR_API_TOMORROW_HOURLY_PRICES = "tomorrow_hourly_prices"

SENSOR_TYPES: tuple[SensorEntityDescription, ...] = (
    SensorEntityDescription(
        key=ATTR_API_CURRENT_PRICE,
        name="Current kWh price in CZK",
    ),
    SensorEntityDescription(
        key=ATTR_API_IS_CURRENTLY_CHEAPEST_HOUR,
        name="Is currently cheapest electricity hour in day",
    ),
    SensorEntityDescription(
        key=ATTR_API_TODAY_BASE_CHEAPEST_HOUR,
        name="Base cheapest hour",
    ),
    SensorEntityDescription(
        key=ATTR_API_TODAY_PEAK_CHEAPEST_HOUR,
        name="Peak cheapest hour",
    ),
    SensorEntityDescription(
        key=ATTR_API_TODAY_OFFPEAK_CHEAPEST_HOUR,
        name="Offpeak cheapest hour",
    ),
    SensorEntityDescription(
        key=ATTR_API_TODAY_BASE_SECOND_CHEAPEST_HOUR,
        name="Base second cheapest hour",
    ),
    SensorEntityDescription(
        key=ATTR_API_TODAY_PEAK_SECOND_CHEAPEST_HOUR,
        name="Peak second cheapest hour",
    ),
    SensorEntityDescription(
        key=ATTR_API_TODAY_OFFPEAK_SECOND_CHEAPEST_HOUR,
        name="Offpeak second cheapest hour",
    ),
    SensorEntityDescription(
        key=ATTR_API_TODAY_OFFPEAK_SECOND_CHEAPEST_HOUR,
        name="Offpeak second cheapest hour",
    ),
)

LANGUAGES = ["cz", "en"]

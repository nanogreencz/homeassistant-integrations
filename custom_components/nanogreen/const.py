"""Consts for the NanoGreen energy."""

from homeassistant.components.sensor import SensorEntityDescription
from homeassistant.const import Platform


DOMAIN = "nanogreen"
DEFAULT_NAME = "nanogreen"
DEFAULT_LANGUAGE = "en"
ENTRY_NAME = "name"
ENTRY_COORDINATOR = "nanogreen_coordinator"
CONFIG_FLOW_VERSION = 1
CONF_LANGUAGE = "language"
UPDATE_LISTENER = "update_listener"
PLATFORMS = [Platform.SENSOR]


ATTR_API_CURRENT_MARKET_PRICE = "current_market_price"
ATTR_API_CURRENT_CONSUMPTION_PRICE = "current_consumption_price"
ATTR_API_CURRENT_PRODUCTION_WITH_NANO_PRICE = "current_production_price_with_nano"
ATTR_API_CURRENT_PRODUCTION_WITHOUT_NANO_PRICE = "current_production_price_without_nano"
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
        key=ATTR_API_CURRENT_MARKET_PRICE,
        name="Current market price [CZK/kWh]",
        native_unit_of_measurement="CZK/kWh",
    ),
    SensorEntityDescription(
        key=ATTR_API_CURRENT_CONSUMPTION_PRICE,
        name="Current consumption price [CZK/kWh]",
        native_unit_of_measurement="CZK/kWh",
    ),
    SensorEntityDescription(
        key=ATTR_API_CURRENT_PRODUCTION_WITH_NANO_PRICE,
        name="Current production price (consumption with Nano) [CZK/kWh]",
        native_unit_of_measurement="CZK/kWh",
    ),
    SensorEntityDescription(
        key=ATTR_API_CURRENT_PRODUCTION_WITHOUT_NANO_PRICE,
        name="Current production price (consumption NOT with Nano) [CZK/kWh]",
        native_unit_of_measurement="CZK/kWh",
    ),
    SensorEntityDescription(
        key=ATTR_API_IS_CURRENTLY_CHEAPEST_HOUR,
        name="Day cheapest hour [bool]",
    ),
    SensorEntityDescription(
        key=ATTR_API_TODAY_BASE_CHEAPEST_HOUR,
        name="Day cheapest hour",
    ),
    SensorEntityDescription(
        key=ATTR_API_TODAY_BASE_SECOND_CHEAPEST_HOUR,
        name="Day second cheapest hour",
    ),
    SensorEntityDescription(
        key=ATTR_API_TODAY_PEAK_CHEAPEST_HOUR,
        name="Peak cheapest hour",
    ),
    SensorEntityDescription(
        key=ATTR_API_TODAY_PEAK_SECOND_CHEAPEST_HOUR,
        name="Peak second cheapest hour",
    ),
    SensorEntityDescription(
        key=ATTR_API_TODAY_OFFPEAK_CHEAPEST_HOUR,
        name="Offpeak cheapest hour",
    ),
    SensorEntityDescription(
        key=ATTR_API_TODAY_OFFPEAK_SECOND_CHEAPEST_HOUR,
        name="Offpeak second cheapest hour",
    ),
)

LANGUAGES = ["cz", "en"]

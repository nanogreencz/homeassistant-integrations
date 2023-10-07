"""Consts for the NanoGreen energy."""

from homeassistant.components.sensor import SensorEntityDescription
from homeassistant.components.binary_sensor import BinarySensorEntityDescription
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
VAT = 1.21  # DPH 21%

# Fees per kWh, VAT excluded
KWH_FEE = (350 + 28.3 + 113.53)/1000

ATTR_API_CURRENT_MARKET_PRICE = "current_market_price"
ATTR_API_CURRENT_CONSUMPTION_PRICE = "current_consumption_price"
ATTR_API_CURRENT_CONSUMPTION_PRICE_INCL_VAT = "current_consumption_price_incl_vat"
ATTR_API_CURRENT_PRODUCTION_WITH_NANO_PRICE = "current_production_price_with_nano"
ATTR_API_CURRENT_PRODUCTION_WITHOUT_NANO_PRICE = "current_production_price_without_nano"
ATTR_API_TODAY_BASE_CHEAPEST_HOUR = "today_base_cheapest_hour"
ATTR_API_TODAY_PEAK_CHEAPEST_HOUR = "today_peak_cheapest_hour"
ATTR_API_TODAY_OFFPEAK_CHEAPEST_HOUR = "today_offpeak_cheapest_hour"
ATTR_API_TODAY_BASE_SECOND_CHEAPEST_HOUR = "today_base_second_cheapest_hour"
ATTR_API_TODAY_PEAK_SECOND_CHEAPEST_HOUR = "today_peak_second_cheapest_hour"
ATTR_API_TODAY_OFFPEAK_SECOND_CHEAPEST_HOUR = "today_offpeak_second_cheapest_hour"
ATTR_API_TODAY_HOURLY_PRICES = "today_hourly_prices"
ATTR_API_TODAY_HOURLY_CONSUMPTION_PRICES_INCL_VAT = "today_hourly_consumption_prices_incl_vat"
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
        key=ATTR_API_CURRENT_CONSUMPTION_PRICE_INCL_VAT,
        name="Current consumption price including VAT [CZK/kWh]",
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

ATTR_API_IS_CURRENTLY_CHEAPEST_HOUR = "is_currently_cheapest_hour"
ATTR_API_IS_CURRENTLY_SECOND_CHEAPEST_HOUR = "is_currently_second_cheapest_hour"
ATTR_API_IS_CURRENTLY_THIRD_CHEAPEST_HOUR = "is_currently_third_cheapest_hour"
ATTR_API_IS_CURRENTLY_FOURTH_CHEAPEST_HOUR = "is_currently_fourth_cheapest_hour"
ATTR_API_IS_CURRENTLY_FIFTH_CHEAPEST_HOUR = "is_currently_fifth_cheapest_hour"
ATTR_API_IS_CURRENTLY_SIXTH_CHEAPEST_HOUR = "is_currently_sixth_cheapest_hour"

ATTR_API_IS_CURRENTLY_IN_TWO_CHEAPEST_HOURS = "is_currently_in_two_cheapest_hours"
ATTR_API_IS_CURRENTLY_IN_THREE_CHEAPEST_HOURS = "is_currently_in_three_cheapest_hours"
ATTR_API_IS_CURRENTLY_IN_FOUR_CHEAPEST_HOURS = "is_currently_in_four_cheapest_hours"
ATTR_API_IS_CURRENTLY_IN_FIVE_CHEAPEST_HOURS = "is_currently_in_five_cheapest_hours"
ATTR_API_IS_CURRENTLY_IN_SIX_CHEAPEST_HOURS = "is_currently_in_six_cheapest_hours"


BINARY_SENSOR_TYPES: tuple[BinarySensorEntityDescription, ...] = (
    BinarySensorEntityDescription(
        key=ATTR_API_IS_CURRENTLY_CHEAPEST_HOUR,
        name="Is currently cheapest hour",
    ),
    BinarySensorEntityDescription(
        key=ATTR_API_IS_CURRENTLY_SECOND_CHEAPEST_HOUR,
        name="Is currently second cheapest hour",
    ),
    BinarySensorEntityDescription(
        key=ATTR_API_IS_CURRENTLY_THIRD_CHEAPEST_HOUR,
        name="Is currently third cheapest hour",
    ),
    BinarySensorEntityDescription(
        key=ATTR_API_IS_CURRENTLY_FOURTH_CHEAPEST_HOUR,
        name="Is currently fourth cheapest hour",
    ),
    BinarySensorEntityDescription(
        key=ATTR_API_IS_CURRENTLY_FIFTH_CHEAPEST_HOUR,
        name="Is currently fifth cheapest hour",
    ),
    BinarySensorEntityDescription(
        key=ATTR_API_IS_CURRENTLY_SIXTH_CHEAPEST_HOUR,
        name="Is currently sixth cheapest hour",
    ),
    BinarySensorEntityDescription(
        key=ATTR_API_IS_CURRENTLY_IN_TWO_CHEAPEST_HOURS,
        name="Is currently in two cheapest hours",
    ),
    BinarySensorEntityDescription(
        key=ATTR_API_IS_CURRENTLY_IN_THREE_CHEAPEST_HOURS,
        name="Is currently in three cheapest hours",
    ),
    BinarySensorEntityDescription(
        key=ATTR_API_IS_CURRENTLY_IN_FOUR_CHEAPEST_HOURS,
        name="Is currently in four cheapest hours",
    ),
    BinarySensorEntityDescription(
        key=ATTR_API_IS_CURRENTLY_IN_FIVE_CHEAPEST_HOURS,
        name="Is currently in five cheapest hours",
    ),
    BinarySensorEntityDescription(
        key=ATTR_API_IS_CURRENTLY_IN_SIX_CHEAPEST_HOURS,
        name="Is currently in six cheapest hours",
    ),
)

LANGUAGES = ["cz", "en"]

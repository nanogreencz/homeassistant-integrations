import asyncio
import json
import logging
from datetime import timedelta

import aiohttp
import async_timeout
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import (
    DOMAIN,
    ATTR_API_CURRENT_PRICE,
    ATTR_API_IS_CURRENTLY_CHEAPEST_HOUR,
    ATTR_API_TODAY_BASE_CHEAPEST_HOUR,
    ATTR_API_TODAY_BASE_SECOND_CHEAPEST_HOUR,
    ATTR_API_TODAY_OFFPEAK_CHEAPEST_HOUR,
    ATTR_API_TODAY_OFFPEAK_SECOND_CHEAPEST_HOUR,
    ATTR_API_TODAY_PEAK_CHEAPEST_HOUR,
    ATTR_API_TODAY_PEAK_SECOND_CHEAPEST_HOUR,
    ATTR_API_TODAY_HOURLY_PRICES,
    ATTR_API_TOMORROW_HOURLY_PRICES,
)

_LOGGER = logging.getLogger(__name__)
UPDATE_INTERVAL = timedelta(minutes=1)


class NanogreenUpdateCoordinator(DataUpdateCoordinator):
    """Nanogreen data update coordinator."""

    def __init__(self, websession: aiohttp.ClientSession, hass):
        """Initialize coordinator."""
        super().__init__(hass, _LOGGER, name=DOMAIN, update_interval=UPDATE_INTERVAL)
        self._websession = websession

    async def _async_update_data(self):
        """Update the data."""
        data = {}
        async with async_timeout.timeout(20):
            try:
                response = await self._websession.get(
                    "https://moje.nanogreen.cz/api/prices/daily"
                )
                data = await self._convert_response(response)
            except (asyncio.TimeoutError, aiohttp.ClientError) as err:
                _LOGGER.error("Could not get data from API: %s", err)

        return data

    async def _convert_response(self, response):
        text = await response.text()
        data = json.loads(text)
        return {
            ATTR_API_CURRENT_PRICE: data.get("currentPrice"),
            ATTR_API_IS_CURRENTLY_CHEAPEST_HOUR: data.get("isCurrentlyCheapestHour"),
            ATTR_API_TODAY_BASE_CHEAPEST_HOUR: data.get("todayBaseCheapestHour"),
            ATTR_API_TODAY_BASE_SECOND_CHEAPEST_HOUR: data.get(
                "todayBaseSecondCheapestHour"
            ),
            ATTR_API_TODAY_OFFPEAK_CHEAPEST_HOUR: data.get("todayOffpeakCheapestHour"),
            ATTR_API_TODAY_OFFPEAK_SECOND_CHEAPEST_HOUR: data.get(
                "todayOffpeakSecondCheapestHour"
            ),
            ATTR_API_TODAY_PEAK_CHEAPEST_HOUR: data.get("todayPeakCheapestHour"),
            ATTR_API_TODAY_PEAK_SECOND_CHEAPEST_HOUR: data.get(
                "todayPeakSecondCheapestHour"
            ),
            ATTR_API_TODAY_HOURLY_PRICES: data.get("todayHourlyPrices", []),
            ATTR_API_TOMORROW_HOURLY_PRICES: data.get("tomorrowHourlyPrices", []),
        }

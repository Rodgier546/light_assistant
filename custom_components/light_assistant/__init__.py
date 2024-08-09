import logging
from homeassistant.core import HomeAssistant

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Light Assistant component."""
    _LOGGER.debug("Setting up Light Assistant")
    return True

async def async_setup_entry(hass: HomeAssistant, entry):
    """Set up Light Assistant from a config entry."""
    _LOGGER.debug(f"Setting up Light Assistant entry: {entry.data}")
    return True

async def async_unload_entry(hass: HomeAssistant, entry):
    """Unload Light Assistant config entry."""
    _LOGGER.debug(f"Unloading Light Assistant entry: {entry.data}")
    return True

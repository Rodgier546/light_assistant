import logging
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers import config_validation as cv
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

class LightAssistantConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        _LOGGER.debug("Starting user step")
        if user_input is not None:
            _LOGGER.debug(f"User input: {user_input}")
            return self.async_create_entry(title=user_input["name"], data=user_input)

        _LOGGER.debug("Showing form")
        data_schema = vol.Schema({
            vol.Required("name"): str,
            # vol.Required("light_sensor"): cv.entity_id,
            # vol.Required("light_entity"): cv.entity_id
        })

        _LOGGER.debug("Form schema created successfully")
        return self.async_show_form(
            step_id="user",
            data_schema=data_schema
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return LightAssistantOptionsFlowHandler(config_entry)

class LightAssistantOptionsFlowHandler(config_entries.OptionsFlow):
    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        data_schema = vol.Schema({
            vol.Required("name"): str,
            # vol.Required("light_sensor"): cv.entity_id,
            # vol.Required("light_entity"): cv.entity_id
        })

        return self.async_show_form(
            step_id="init",
            data_schema=data_schema
        )

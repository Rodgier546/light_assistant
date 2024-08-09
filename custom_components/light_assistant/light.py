from homeassistant.components.light import LightEntity
from homeassistant.const import STATE_ON, STATE_OFF
from homeassistant.core import callback
from homeassistant.helpers.event import async_track_state_change_event

from .const import DOMAIN

async def async_setup_entry(hass, config_entry, async_add_entities):
    config = hass.data[DOMAIN][config_entry.entry_id]
    async_add_entities([LightAssistantEntity(hass, config)])


class LightAssistantEntity(LightEntity):
    def __init__(self, hass, config):
        self._hass = hass
        self._name = config["name"]
        self._sensor = config["light_sensor"]
        self._light = config["light_entity"]

        self._is_on = False
        self._brightness = 0

        async_track_state_change_event(hass, self._sensor, self._update_brightness)

    @property
    def name(self):
        return self._name

    @property
    def is_on(self):
        return self._is_on

    @property
    def brightness(self):
        return self._brightness

    async def async_turn_on(self, **kwargs):
        self._is_on = True
        await self._hass.services.async_call(
            "light", "turn_on", {"entity_id": self._light, "brightness": self._brightness}
        )
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs):
        self._is_on = False
        await self._hass.services.async_call(
            "light", "turn_off", {"entity_id": self._light}
        )
        self.async_write_ha_state()

    async def _update_brightness(self, event):
        new_state = event.data.get("new_state")
        if new_state:
            light_level = float(new_state.state)
            self._brightness = min(max(int(light_level / 100.0 * 255), 0), 255)
            if self._is_on:
                await self.async_turn_on()

    @callback
    def async_update(self):
        pass

'''from homeassistant import config_entries
from .const import DOMAIN

class MyServiceIntegrationFlowHandler(config_entries.ConfigFlow, domain="firstservice"):
    async def async_step_user(self, user_input=None):
        if user_input is not None:
            # Perform validation or checks on user_input
            # If input is valid, create entry and return result
            return self.async_create_entry(title="First Service", data=user_input)

        # Show form to gather user input
        return self.async_show_form(step_id="user", data_schema=vol.Schema({
            vol.Required("influxdb_user"): str,
            vol.Optional("influxdb_pass"): str
        }))


class ExampleConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Example config flow."""
    # The schema version of the entries that it creates
    # Home Assistant will call your migrate method if the version changes
    VERSION = 1'''

"""Config flow for My Integration."""

from homeassistant import config_entries
import voluptuous as vol

DOMAIN = "influxdbintegration"

class MyIntegrationConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for My Integration."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            # Validate and store the user input
            # Your validation and storage logic here

            # Return the created entry
            return self.async_create_entry(title="Influxdb Integration", data=user_input)

        # Show the user form
        return self._show_config_form()

    def _show_config_form(self, errors=None):
        """Show the configuration form to the user."""
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required("skarpt"): str,
                    vol.Required("skarpt"): str,
                }
            ),
            errors=errors or {},
        )

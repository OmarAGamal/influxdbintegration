
DOMAIN = "influxdbintegration"

def setup(hass, config):
    """Set up the My Integration component."""

    # Create the service handler function
    def on_homeassistant_loaded(event):
        import time
        print("hassio service running")
        print(event.data)
        # time.sleep(20)
        from influxdb import InfluxDBClient
        from datetime import datetime

        client = InfluxDBClient('192.168.100.135', 8086, 'skarpt', 'skarpt', 'skarpt')
        client.create_database('test')
        client.get_list_database()
        json_payload = []
        data = {
            "measurement": "Tzone",
            "tags": {
                "sensor": "824682349"
            },
            "time": datetime.now(),
            "fields": {
                'value': 252
            }
        }
        json_payload.append(data)
        client.write_points(json_payload)
        print("json_payload of Tzone data=", json_payload)
        json_payload.append(event.data)
        client.write_points(json_payload)
        print("json_payload of zwave data=",json_payload)
        # json_payload.append(event.data)
        # client.write_points(json_payload)
        result = client.query('select * from Tzone;')
        print("res=", result)
    
    listener = hass.bus.async_listen("homeassistant_started", on_homeassistant_loaded)

    # hass.services.register(DOMAIN, "firstservice", handle_influxdb)
    # Return boolean to indicate that initialization was successful.
    return True


# DOMAIN = "firstservice"
# from homeassistant.core import Event
# from homeassistant.const import *
# def setup(hass, config):
#     """Set up the My Integration component."""
#     # Create the service handler function
#     # def handle_influxdb(call):
#     from homeassistant.helpers.event import async_track_time_interval
#     def on_homeassistant_loaded(event):
#         if event.data['component'] == 'influxdb':
#             print("hassio service running")
#             print(event.data)
#             # save event.data to influx
#             # from influxdb import InfluxDBClient
#             # from datetime import datetime
#             # client = InfluxDBClient('192.168.100.144', 8086, 'skarpt', 'skarpt', 'skarpt')
#             # client.create_database('start')
#             # client.get_list_database()
#             # json_payload = []
#             # # data = {
#             # #     "measurement": "Tzone",
#             # #     "tags": {
#             # #         "sensor": "88880000"
#             # #     },
#             # #     "time": datetime.now(),
#             # #     "fields": {
#             # #         'value': 252
#             # #     }
#             # # }
#             # json_payload.append(event.data)
#             # json_payload.append(data)

#         # async def on_homeassistant_started(event):
#         #     print("hassio service running")
#         #     print(event.data)
        
#         # print(json.payload)s
#         # client.write_points(json_payload)
#     # hass.services.register(DOMAIN, "firstservice",on_homeassistant_started)
#     # Register the listener
    
#     listener = hass.bus.async_listen("homeassistant_started", on_homeassistant_started)
#     # listener2 = hass.bus.async_listen(EVENT_COMPONENT_LOADED, on_homeassistant_loaded)
#     print("listener=",listener)

#     # unsub = hass.bus.async_track_state_change_event(hass, MATCH_ALL, on_homeassistant_started)

#     # changeListener = hass.bus.async_listen_once(
#     #     "state_changed", on_homeassistant_started) 

#     #hass.services.register(DOMAIN, "firstservice",on_homeassistant_started)
#     # hass.services.register(DOMAIN, "firstservice", handle_influxdb)
#     # Return boolean to indicate that initialization was successful.
#     return True

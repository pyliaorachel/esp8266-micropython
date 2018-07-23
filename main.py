import urequests
import network
import time
import machine

import config


def do_connect():
    # Set to station mode for connecting to network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to network...')
        sta_if.active(True)
        sta_if.connect(config.SSID, config.PASSWORD)

        # Wait until connected
        while not sta_if.isconnected():
            pass
        print('Network connected!')

def flash_led():
    led = machine.Pin(2, machine.Pin.OUT)
    led.value(0) # In some hardware modules, the on/1 and off/0 is reversed; so here the 0 represents on on my module
    time.sleep(0.5)
    led.value(1)

def get_data():
    # Now dummy, should be retrieved from sensors
    return { 'temperature': 25.6 }

def send_data(data):
    print('Sending data...')
    res = urequests.put(config.URL, json=data)
    print('Response: {}'.format(res.text))
    flash_led() # Indicate successful data transmission

def main():
    # Connect to network
    do_connect()

    # Keep posting sensor data at a certain interval
    while True:
        send_data(get_data())
        time.sleep(10)

main()

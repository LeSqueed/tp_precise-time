import datetime
import os
import threading

import TouchPortalAPI as TP

TPClient = TP.Client("cy_advanced_time")


# Pad input to a minimum of 2 characters.
def pad_number(num):
    return str(num).zfill(2)


def update_time():

    # Create a date object holding the values we need for our update later.
    date = datetime.datetime.strptime(str(datetime.datetime.now()), "%Y-%m-%d %H:%M:%S.%f")

    threading.Timer(1.0, update_time).start() # Call self every second to loop

    # Update all the states.
    TPClient.stateUpdate("pr_second", str(pad_number(date.second)))
    TPClient.stateUpdate("pr_minute", str(pad_number(date.minute)))
    TPClient.stateUpdate("pr_hour", str(pad_number(date.hour)))
    TPClient.stateUpdate("pr_day", str(pad_number(date.day)))
    TPClient.stateUpdate("pr_month", str(pad_number(date.month)))
    TPClient.stateUpdate("pr_year", str(date.year))


# Event when client connects
@TPClient.on(TP.TYPES.onConnect)
def onStart(data):
    print("Connected!", data)
    # Update state value
    update_time()


# Shutdown
@TPClient.on(TP.TYPES.onShutdown)
def onShutdown(data):
    print("Shutting down at request of TP.")
    TPClient.disconnect()
    os._exit(0)


def main():
    TPClient.connect()


if __name__ == "__main__":
    main()


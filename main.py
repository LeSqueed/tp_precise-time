import datetime
import sys
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
    TPClient.stateUpdate("Second", str(pad_number(date.second)))
    TPClient.stateUpdate("Minute", str(pad_number(date.minute)))
    TPClient.stateUpdate("Hour", str(pad_number(date.hour)))
    TPClient.stateUpdate("Day", str(pad_number(date.day)))
    TPClient.stateUpdate("Month", str(pad_number(date.month)))
    TPClient.stateUpdate("Year", str(date.year))

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
    sys.exit()


def main():
    TPClient.connect()


if __name__ == "__main__":
    main()



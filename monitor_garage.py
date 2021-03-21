import homeautomation as ha
import garage_door
import time
import json

if __name__ == "__main__":
    ha.logging.info("checking garage door")
    door_open = garage_door.isDoorOpen()
    ha.logging.info("garage door is {}".format("open" if door_open else "closed"))

    try:
        with open("monitor_garage_info.json", "r") as f:
            monitor_info = json.loads(f.read())
    except:
        monitor_info = {"last_closed_time" : 0}

    monitor_info["door_open"] = door_open

    cur_time = time.time()
    if door_open:
        open_duration = (cur_time - monitor_info["last_closed_time"]) / 60

        ha.logging.info("garage door has been open for {:.2f} minutes".format(open_duration))

        print(garage_door.getConfig()["open_time_limit_min"])
        if open_duration > garage_door.getConfig()["open_time_limit_min"]:
            send_notification = True
            if "last_notification_time" in monitor_info:
                time_since_last_notification = (cur_time - monitor_info["last_notification_time"]) /  60
                ha.logging.info("time since last notification {:.2f} minutes".format(time_since_last_notification))
                if (time_since_last_notification < garage_door.getConfig()["notification_interval_min"]):
                    print("skip")
                    send_notification = False
                
            if send_notification:
                ha.sendNotification("Garage door has been open for {} minutes.".format(int(open_duration)))
                monitor_info["last_notification_time"] = cur_time

    else:
        monitor_info["last_closed_time"] = time.time()
        monitor_info["last_notification_time"] = 0

    with open("monitor_garage_info.json", "w") as f:
        f.write(json.dumps(monitor_info))

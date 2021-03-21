import homeautomation as ha
import cv2 as cv

def getConfig():
    return ha.readConfig()["garage_door"]

def isDoorOpen():
    config = getConfig()
    cap = cv.VideoCapture(config["url"])
    ret, frame = cap.read()

    roi_min = config["roi_min"]
    roi_max = config["roi_max"]
    roi = frame[roi_min[0]:roi_min[1], roi_max[0]:roi_max[1]]

    ret, points, straight = cv.QRCodeDetector().detectAndDecode(roi)

    # TODO: I accidentally printed a QR containing the text "open". Switch to
    # "closed".
    if ret and "open" == ret:
        return False
    else:
        return True

if __name__ == "__main__":
    print("isDoorOpen: {}".format(isDoorOpen()))


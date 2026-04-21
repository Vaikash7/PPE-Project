import cv2
from ultralytics import YOLO
import time
import winsound
from tkinter import Tk, filedialog

# 🔥 MODELS
person_model = YOLO("yolov8n.pt")
helmet_model = YOLO("runs/detect/train2/weights/best.pt")
vest_model = YOLO("runs/detect/train5/weights/best.pt")

CONF = 0.25
last_alert_time = 0
ALERT_DELAY = 2


# 🔹 FILE PICKER
def choose_image():
    root = Tk()
    root.withdraw()
    return filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image Files", "*.jpg *.png *.jpeg")]
    )


# 🔹 IMPROVED OVERLAP (returns ratio)
def box_overlap_ratio(px1, py1, px2, py2, x1, y1, x2, y2):
    x_left = max(px1, x1)
    y_top = max(py1, y1)
    x_right = min(px2, x2)
    y_bottom = min(py2, y2)

    if x_right < x_left or y_bottom < y_top:
        return 0.0

    overlap_area = (x_right - x_left) * (y_bottom - y_top)
    box_area = (x2 - x1) * (y2 - y1)

    return overlap_area / box_area


# 🔥 MENU
print("\nSelect Mode:")
print("1️⃣  Image Detection")
print("2️⃣  Live Webcam")
choice = input("Enter 1 or 2: ")


# =========================
# 🔥 IMAGE MODE
# =========================
if choice == "1":

    img_path = choose_image()

    if not img_path:
        print("❌ No image selected")
        exit()

    frame = cv2.imread(img_path)

    person_results = person_model(frame)
    helmet_results = helmet_model(frame)
    vest_results = vest_model(frame)

    helmet_boxes = []
    vest_boxes = []

    for box in helmet_results[0].boxes:
        if float(box.conf[0]) >= CONF:
            helmet_boxes.append(tuple(map(int, box.xyxy[0])))

    for box in vest_results[0].boxes:
        if float(box.conf[0]) >= CONF:
            vest_boxes.append(tuple(map(int, box.xyxy[0])))

    for box in person_results[0].boxes:

        if int(box.cls[0]) != 0:
            continue

        px1, py1, px2, py2 = map(int, box.xyxy[0])
        height = py2 - py1
        width = px2 - px1
        center_x = (px1 + px2) // 2

        # 🔥 HEAD
        head_h = int(0.16 * height)
        head_y1 = max(0, py1 - int(0.05 * height))
        head_y2 = head_y1 + head_h

        head_w = int(0.38 * width)
        hx1 = center_x - head_w // 2
        hx2 = center_x + head_w // 2

        # 🔥 CHEST
        chest_y1 = py1 + int(0.38 * height)
        chest_y2 = py1 + int(0.72 * height)

        chest_w = int(0.55 * width)
        cx1 = center_x - chest_w // 2
        cx2 = center_x + chest_w // 2

        # 🔥 HELMET CHECK (STRICT)
        has_helmet = False
        for h in helmet_boxes:
            if box_overlap_ratio(hx1, head_y1, hx2, head_y2, *h) > 0.2:
                has_helmet = True
                break

        # 🔥 VEST CHECK (STRICT)
        has_vest = False
        for v in vest_boxes:
            if box_overlap_ratio(cx1, chest_y1, cx2, chest_y2, *v) > 0.2:
                has_vest = True
                break

        helmet_text = "HELMET OK" if has_helmet else "NO HELMET"
        vest_text = "VEST OK" if has_vest else "NO VEST"

        helmet_color = (0, 255, 0) if has_helmet else (0, 0, 255)
        vest_color = (0, 255, 0) if has_vest else (0, 0, 255)

        cv2.rectangle(frame, (hx1, head_y1), (hx2, head_y2), helmet_color, 2)
        cv2.putText(frame, helmet_text, (hx1, head_y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, helmet_color, 2)

        cv2.rectangle(frame, (cx1, chest_y1), (cx2, chest_y2), vest_color, 2)
        cv2.putText(frame, vest_text, (cx1, chest_y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, vest_color, 2)

    cv2.imshow("PPE IMAGE RESULT", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# =========================
# 🔥 LIVE MODE
# =========================
elif choice == "2":

    cap = cv2.VideoCapture(0)
    print("Press Q to exit")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        person_results = person_model(frame)
        helmet_results = helmet_model(frame)
        vest_results = vest_model(frame)

        helmet_boxes = []
        vest_boxes = []

        for box in helmet_results[0].boxes:
            if float(box.conf[0]) >= CONF:
                helmet_boxes.append(tuple(map(int, box.xyxy[0])))

        for box in vest_results[0].boxes:
            if float(box.conf[0]) >= CONF:
                vest_boxes.append(tuple(map(int, box.xyxy[0])))

        for box in person_results[0].boxes:

            if int(box.cls[0]) != 0:
                continue

            px1, py1, px2, py2 = map(int, box.xyxy[0])
            height = py2 - py1
            width = px2 - px1
            center_x = (px1 + px2) // 2

            head_h = int(0.16 * height)
            head_y1 = max(0, py1 - int(0.05 * height))
            head_y2 = head_y1 + head_h

            head_w = int(0.38 * width)
            hx1 = center_x - head_w // 2
            hx2 = center_x + head_w // 2

            chest_y1 = py1 + int(0.38 * height)
            chest_y2 = py1 + int(0.72 * height)

            chest_w = int(0.55 * width)
            cx1 = center_x - chest_w // 2
            cx2 = center_x + chest_w // 2

            # 🔥 HELMET CHECK
            has_helmet = False
            for h in helmet_boxes:
                if box_overlap_ratio(hx1, head_y1, hx2, head_y2, *h) > 0.2:
                    has_helmet = True
                    break

            # 🔥 VEST CHECK
            has_vest = False
            for v in vest_boxes:
                if box_overlap_ratio(cx1, chest_y1, cx2, chest_y2, *v) > 0.2:
                    has_vest = True
                    break

            helmet_text = "HELMET OK" if has_helmet else "NO HELMET"
            vest_text = "VEST OK" if has_vest else "NO VEST"

            helmet_color = (0, 255, 0) if has_helmet else (0, 0, 255)
            vest_color = (0, 255, 0) if has_vest else (0, 0, 255)

            if not (has_helmet and has_vest):
                current_time = time.time()
                if current_time - last_alert_time > ALERT_DELAY:
                    winsound.PlaySound("SystemHand", winsound.SND_ASYNC)
                    last_alert_time = current_time

            cv2.rectangle(frame, (hx1, head_y1), (hx2, head_y2), helmet_color, 2)
            cv2.putText(frame, helmet_text, (hx1, head_y1 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, helmet_color, 2)

            cv2.rectangle(frame, (cx1, chest_y1), (cx2, chest_y2), vest_color, 2)
            cv2.putText(frame, vest_text, (cx1, chest_y1 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, vest_color, 2)

        cv2.imshow("PPE SHOWCASE SYSTEM", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

else:
    print("❌ Invalid choice!")
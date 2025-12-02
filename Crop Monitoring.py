import cv2
import numpy as np

def analyze_crop_health(image_path):
    # قراءة الصورة
    img = cv2.imread(image_path)
    img = cv2.resize(img, (600, 600))

    # تحويل للصيغة HSV (أسهل في تحليل الألوان)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # ---- تحديد نطاق الأخضر ----
    lower_green = np.array([25, 40, 40])
    upper_green = np.array([85, 255, 255])
    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    # ---- تحديد نطاق الأصفر ----
    lower_yellow = np.array([15, 40, 40])
    upper_yellow = np.array([35, 255, 255])
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # ---- تحديد نطاق البني (تقريب) ----
    lower_brown = np.array([5, 50, 50])
    upper_brown = np.array([20, 255, 200])
    brown_mask = cv2.inRange(hsv, lower_brown, upper_brown)

    # حساب النسب
    total_pixels = img.shape[0] * img.shape[1]
    green_ratio = np.sum(green_mask > 0) / total_pixels
    yellow_ratio = np.sum(yellow_mask > 0) / total_pixels
    brown_ratio = np.sum(brown_mask > 0) / total_pixels

    print(f"Green: {green_ratio*100:.2f}%")
    print(f"Yellow: {yellow_ratio*100:.2f}%")
    print(f"Brown: {brown_ratio*100:.2f}%")

    # تحديد الحالة
    if green_ratio > 0.6:
        status = "Healthy "
    elif green_ratio > 0.35:
        status = "Moderate "
    else:
        status = "Unhealthy "

    return status


# جرب
print(analyze_crop_health("crop.jpg"))

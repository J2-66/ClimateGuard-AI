import cv2
import numpy as np
from PIL import Image

from granite_service import ask_granite


def analyze_image(file_path):
    """
    Perform basic computer-vision analysis of an
    environmental image and generate a Granite-based
    interpretation.
    """

    # -------------------------------------------------
    # 1. Read image
    # -------------------------------------------------

    image = cv2.imread(file_path)

    if image is None:
        return "Unable to read the uploaded image."

    height, width, channels = image.shape

    # -------------------------------------------------
    # 2. Convert image formats
    # -------------------------------------------------

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    rgb_image = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB
    )

    # -------------------------------------------------
    # 3. Detect possible water-like regions
    # -------------------------------------------------

    # Blue/cyan water-like colors
    lower_water = np.array([80, 30, 30])
    upper_water = np.array([130, 255, 255])

    water_mask = cv2.inRange(
        hsv,
        lower_water,
        upper_water
    )

    water_pixels = np.count_nonzero(water_mask)

    total_pixels = height * width

    water_percentage = (
        water_pixels / total_pixels
    ) * 100

    # -------------------------------------------------
    # 4. Detect green vegetation-like regions
    # -------------------------------------------------

    lower_green = np.array([35, 40, 30])
    upper_green = np.array([85, 255, 255])

    green_mask = cv2.inRange(
        hsv,
        lower_green,
        upper_green
    )

    green_pixels = np.count_nonzero(green_mask)

    vegetation_percentage = (
        green_pixels / total_pixels
    ) * 100

    # -------------------------------------------------
    # 5. Calculate average brightness
    # -------------------------------------------------

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    average_brightness = float(
        np.mean(gray)
    )

    # -------------------------------------------------
    # 6. Generate observations
    # -------------------------------------------------

    observations = []

    if water_percentage >= 30:
        observations.append(
            "A relatively large proportion of blue/cyan "
            "pixels was detected."
        )

    elif water_percentage >= 10:
        observations.append(
            "A moderate proportion of blue/cyan "
            "pixels was detected."
        )

    else:
        observations.append(
            "Only a small proportion of blue/cyan "
            "pixels was detected."
        )

    if vegetation_percentage >= 30:
        observations.append(
            "A relatively large proportion of "
            "green vegetation-like pixels was detected."
        )

    elif vegetation_percentage >= 10:
        observations.append(
            "A moderate proportion of green "
            "vegetation-like pixels was detected."
        )

    else:
        observations.append(
            "Only a small proportion of green "
            "vegetation-like pixels was detected."
        )

    if average_brightness < 70:
        observations.append(
            "The image has relatively low brightness."
        )

    elif average_brightness > 180:
        observations.append(
            "The image has relatively high brightness."
        )

    else:
        observations.append(
            "The image has moderate brightness."
        )

    observation_text = "\n".join(
        f"- {item}" for item in observations
    )

    # -------------------------------------------------
    # 7. Send structured observations to Granite
    # -------------------------------------------------

    prompt = f"""
You are ClimateGuard AI, an environmental
awareness assistant.

A computer-vision preprocessing system analyzed
an uploaded environmental image.

IMAGE INFORMATION:

Width: {width} pixels
Height: {height} pixels

Estimated blue/cyan pixel percentage:
{water_percentage:.2f}%

Estimated green vegetation-like pixel percentage:
{vegetation_percentage:.2f}%

Average image brightness:
{average_brightness:.2f}

Computer-vision observations:
{observation_text}

Analyze these observations.

Provide:

1. Image Analysis Summary
2. Possible Environmental Interpretation
3. Possible Flood/Water-Related Interpretation
4. Possible Vegetation-Related Interpretation
5. Important Limitations

IMPORTANT:
- Blue/cyan pixels do NOT automatically mean water.
- Green pixels do NOT automatically mean vegetation.
- Do not claim that a flood is confirmed.
- Do not identify people, locations, buildings, or
  objects unless reliable information is available.
- Explain that this is an educational computer-vision
  analysis and not an official disaster assessment.

Use simple English.
"""

    response = ask_granite(
        prompt,
        max_new_tokens=500,
        temperature=0.2
    )

    return response
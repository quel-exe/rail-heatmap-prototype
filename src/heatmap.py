"""Enhanced local-intensity-variation heatmap from the user's baseline script."""

import cv2
import numpy as np


def make_heatmap(frame: np.ndarray) -> np.ndarray:
    """Return an INFERNO heatmap of local intensity differences.

    The result highlights image brightness variation. It is not a depth map.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    broad_intensity = cv2.GaussianBlur(gray, (0, 0), sigmaX=25)
    differences = cv2.absdiff(gray, broad_intensity)
    smooth_differences = cv2.GaussianBlur(
        differences, (0, 0), sigmaX=15
    )
    normalized = cv2.normalize(
        smooth_differences, None, 0, 255, cv2.NORM_MINMAX
    )
    return cv2.applyColorMap(normalized, cv2.COLORMAP_INFERNO)

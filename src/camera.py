"""Webcam setup and frame-reading helpers."""

import cv2


def open_camera(camera_index: int, width: int, height: int) -> cv2.VideoCapture:
    """Open one camera and request a processing resolution."""
    # CAP_DSHOW often starts USB webcams more reliably on Windows.
    camera = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
    if not camera.isOpened():
        camera.release()
        raise RuntimeError(
            f"Could not open camera {camera_index}. Try another --camera index "
            "and check Windows camera permissions."
        )

    camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    return camera


def read_frame(camera: cv2.VideoCapture, width: int, height: int):
    """Read and resize one frame, or return None if capture failed."""
    success, frame = camera.read()
    if not success or frame is None:
        return None
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

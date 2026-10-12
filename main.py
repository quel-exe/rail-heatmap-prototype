"""Run the webcam heatmap prototype."""

import argparse

import cv2

from src.camera import open_camera, read_frame
from src.heatmap import make_heatmap


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Show a webcam feed and an image-intensity-variation heatmap."
    )
    parser.add_argument("--camera", type=int, default=0, help="Camera index (default: 0).")
    parser.add_argument("--width", type=int, default=640, help="Processing width (default: 640).")
    parser.add_argument("--height", type=int, default=360, help="Processing height (default: 360).")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.width < 1 or args.height < 1:
        print("Width and height must be positive integers.")
        return 2

    camera = None
    try:
        camera = open_camera(args.camera, args.width, args.height)
        print("BRO! Enhanced heatmap is running.")
        print("Press Q or Esc in a preview window to quit.")

        while True:
            frame = read_frame(camera, args.width, args.height)
            if frame is None:
                print("Could not read a frame from the camera; stopping.")
                break

            heatmap = make_heatmap(frame)
            overlay = cv2.addWeighted(frame, 0.35, heatmap, 0.65, 0)

            cv2.imshow("1 - Original Webcam", frame)
            cv2.imshow("2 - Broader Heatmap", heatmap)
            cv2.imshow("3 - Heatmap Overlay", overlay)

            key = cv2.waitKey(1) & 0xFF
            if key in (ord("q"), 27):
                break

    except (RuntimeError, cv2.error) as error:
        print(f"Webcam error: {error}")
        return 1
    finally:
        if camera is not None:
            camera.release()
        cv2.destroyAllWindows()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

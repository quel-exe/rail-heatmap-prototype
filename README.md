# Rail Vision Prototype

A small Windows-friendly webcam prototype for exploring image intensity variation. The heatmap in this repository is a reconstruction from the written description in the project brief. The original `webcam_heatmap.py` was not present in the inspected workspace, so its exact implementation could not be preserved or compared.

## What it does

- Opens one webcam and resizes frames to 640 × 360 by default.
- Shows the live camera, a broad local-intensity-variation heatmap, and an overlay.
- Quits with **Q** or **Esc**, and releases the camera when the window closes or an error occurs.
- Lets you choose a camera index and processing dimensions on the command line.

This heatmap visualizes image-intensity differences. It does not measure physical depth, identify objects, or detect rail defects.

## Setup on Windows

Open PowerShell in this folder. Create and activate a virtual environment, then install the listed packages:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If PowerShell blocks activation, you can run the environment's Python directly instead:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

## Run

With the environment activated:

```powershell
python main.py
```

Choose a camera index (the default is `0`) and resolution if needed:

```powershell
python main.py --camera 1 --width 640 --height 360
```

Try camera indices `0`, `1`, and so on if the default camera does not open. Close the windows with **Q** or **Esc**. If startup fails, check that another app is not using the camera and that Windows has granted camera access to desktop apps.

## What to look for

1. Confirm that the original window updates smoothly.
2. Move an object or your hand and observe how the heatmap and overlay respond.
3. Keep the camera still for a few seconds and notice any changes caused by noise, auto-exposure, or lighting.
4. Try a different camera index only if necessary.

The processing is intentionally simple and explains broad intensity changes; it cannot reliably distinguish a tabletop from a floor. A useful next experiment is selectable grayscale and Canny edge views, followed by optional, user-calibrated color/region segmentation. Those are image-processing experiments, not depth measurements.

## Project layout

```text
main.py                 Webcam loop and keyboard controls
src/camera.py           Camera setup and frame-reading helper
src/heatmap.py          Local-intensity-variation heatmap
requirements.txt        Runtime dependencies
```

No pretrained model or dataset is downloaded. Relative monocular depth is a later, optional experiment that will need separate packages/model weights and will not provide calibrated distances in meters.

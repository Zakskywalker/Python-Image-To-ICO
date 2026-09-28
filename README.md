# Convert Image to ICO

A small Python script that converts an image into a Windows `.ico` file with multiple embedded resolutions. The image is cropped to its visible pixels, given a small transparent margin, centered on a square canvas, and enhanced with a light outline for readability on light and dark desktop backgrounds.

## Requirements

- Python 3.8 or newer
- [Pillow](https://pillow.readthedocs.io/)

Install Pillow with:

```powershell
python -m pip install Pillow
```

## Usage

1. Open `convert_to_ico.py`.
2. Set `source_path` to the image you want to convert.
3. Set `output_path` to the `.ico` file to create.

For example:

```python
source_path = r"C:\path\to\source.png"
output_path = r"C:\path\to\output.ico"
```

Run the script from this directory:

```powershell
python .\convert_to_ico.py
```

The generated icon includes these sizes:

`16x16`, `24x24`, `32x32`, `48x48`, `64x64`, `128x128`, and `256x256`

## Notes

- Images are converted to RGBA before processing.
- Transparent margins are removed automatically.
- The default transparent padding is 32 pixels. Adjust `padding` in the script if needed.
- The source image must contain at least one visible pixel.
- The script is intended for images with transparency, such as PNG files.

## License

This project does not currently specify a license.
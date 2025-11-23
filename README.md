# Glyph Atlas Generator

A powerful Python tool for automatically generating glyph atlases from
input images.\
This program organizes images into a clean 16×16 grid and outputs a
single optimized PNG file --- perfect for font development, game
engines, sprite sheets, icon libraries, and more.

------------------------------------------------------------------------

## ✨ Features

-   🖼️ **Multi-format Support:** PNG, JPG, JPEG\
-   🔢 **Smart 16×16 Grid Layout**\
-   📏 **Automatic Cell Sizing Based on Largest Image**\
-   🎯 **Precise Center Alignment Inside Each Cell**\
-   🔄 **Auto-sorting for Consistent Ordering**\
-   💾 **High-quality PNG Output With Transparent Background**\
-   ♾️ **Batch Processing Support**

------------------------------------------------------------------------

## 🚀 Quick Start

### Installation

``` bash
pip install Pillow
```

### Usage

``` bash
python glyph_generator.py
```

Follow the interactive prompts:

    Images Folder -> path/to/your/images
    Glyph Name (e.g., E3) -> E5

Example:

    Images Folder -> images
    Glyph Name (e.g., E3) -> E5

------------------------------------------------------------------------

## 📁 Project Structure

    glyph-atlas-generator/
    ├── glyph_generator.py
    ├── images/
        ├── image_1.png
        ├── image_2.png
        └── ...

------------------------------------------------------------------------

## 🛠️ How It Works

1.  **Scan Input Folder** -- detects all supported image formats\
2.  **Determine Optimal Cell Size** -- based on the largest image\
3.  **Create 16×16 Canvas**\
4.  **Center Each Image** inside its cell\
5.  **Export Final PNG** with transparency

------------------------------------------------------------------------

## 🐛 Troubleshooting

-   **"No images found"** → Ensure files use `.png`, `.jpg`, or `.jpeg`\
-   **"Exceeds 16×16"** → Maximum supported images: 256\
-   **Permission errors** → Check write access to the output directory

------------------------------------------------------------------------

## 🤝 Contributing

Contributions are welcome! Feel free to open issues, submit PRs, or
suggest new features.

------------------------------------------------------------------------

## 📄 License

This project is licensed under the **MIT License**.

# Generate a QR Code for Base64 Encoded HTML Content

This Python script generates a QR code that, when scanned, opens an HTML document encoded as a Base64 `data:` URL. The QR code can be saved as an image and shared for easy access to the HTML content without hosting it on a server.

---

## Features

- **Base64 Encoding**: Encodes your HTML content into Base64 format.
- **Data URL Creation**: Wraps the encoded HTML into a `data:text/html;base64,` URL.
- **QR Code Generation**: Creates a scannable QR code pointing to the encoded content.
- **Customizable Appearance**: Allows you to customize the QR code's size, version, and colors.
- **Output**: Saves the generated QR code as a PNG image.

---

## How It Works

1. **Prepare HTML Content**:  
   Add your HTML content to the `html_content` variable as a string.

2. **Encode to Base64**:  
   The script encodes the HTML into Base64 format and appends it to the `data:text/html;base64,` prefix.

3. **Generate the QR Code**:  
   A QR code is created using the `qrcode` library in Python.

4. **Save the QR Code**:  
   The generated QR code is saved as a PNG file for sharing or distribution.

---


## Requirements

Install the required Python library:

```
pip install qrcode[pil]
```

## Installtion / Usage

### 1 -  
Star and Clone the Github Repo

```
git clone https://github.com/The-UnknownHacker/Html-To-QR/
```
Or Download the Zip

```
https://github.com/The-UnknownHacker/Html-To-QR/archive/refs/heads/main.zip
```
### 2 -
Extract it and run the utlity using `python script.py` or `python3 script.py`
Make sure that you have replaced your code in the `html_content` variable

---

## Output

- The QR code is saved as `img_name.png` in the current working directory.
- When scanned, the QR code opens the embedded HTML content in a browser.

---

## Use Cases

- Sharing standalone HTML content without hosting.
- Quick previews of HTML designs or templates.
- Embedding interactive content directly in a QR code.

---

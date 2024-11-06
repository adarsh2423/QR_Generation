import qrcode

def generate_qr():
  # Get user input for the data
  data = input("Enter the data for the QR code: ")

  # Create the QR code object
  qr = qrcode.QRCode(
      version=1,  # Adjust version for complexity
      error_correction=qrcode.constants.ERROR_CORRECT_H,  # Error correction level
  )

  # Add data to the QR code
  qr.add_data(data)
  qr.make(fit=True)

  # Create an image from the QR code data
  img = qr.make_image(fill_color="black", back_color="white")

  # Get user input for the filename (optional)
  filename = input("Enter a filename for the QR code (or press Enter to use default): ")
  if not filename:
    filename = "qr_code.png"  # Default filename

  # Save the QR code image
  img.save(filename)

  print("QR code generated successfully!")

# Run the function to generate QR code
generate_qr()

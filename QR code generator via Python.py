#How to create a QR code Generator in python || Python complete project

#first of all import all necessary library . just like import qr code
#but first do in cmd prompt like 
#import qrcode library
import qrcode
#lets run the code 
#zero errors
def generate_qr_code(data, filename="qrcode.png"):
    #lets generate qr code 
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    #lets create an image from the QR code 
    img = qr.make_image(fill_color="red", back_color="white")
    #save the image
    #we are using red color just for better understanding
    img.save(filename)
    print(f"QR code saved as {filename}")
if __name__ == "__main__":
    data_to_encode = "thesadiqali"
    data_to_encode = "sadiqsmasher@gmail.com"
    generate_qr_code(data_to_encode)
#now everything is perfect . let see 

import qrcode

#Taking UPI id as a input
upi_id = input("Enter You UPI ID:")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#DEFINING THE PAYMENT URL BASED ON THE UPI ID AND THE PAYMENT APP
#YOU CAN MODIFY IT

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recpient%20Name$mc=1234'
googlepay_url = f'upi://pay?pa={upi_id}&pn=Recpient%20Name$mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recpient%20Name$mc=1234'

#Creating QR codes for each payment app

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
googlepay_qr = qrcode.make(googlepay_url)

#Save the QR code to image file(OPTIONAL)

#phonepe_qr.save('phonepe_qr.png')
#paytm_qr.save('paytm_qr.png')
#googlepay_url_qr.save('googlepay_qr.png')

#DISPLAY THE QR CODES
phonepe_qr.show()
paytm_qr.show()
googlepay_qr.show()

 



import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep
from PIL import Image
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"/usr/local/Cellar/tesseract/5.0.1/bin/tesseract"
def main(contract , receipt):
    option = webdriver.ChromeOptions()

    # Removes navigator.webdriver flag

    # For older ChromeDriver under version 79.0.3945.16
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_experimental_option('useAutomationExtension', False)

    # For ChromeDriver version 79.0.3945.16 or over
    option.add_argument('--disable-blink-features=AutomationControlled')
    # Use a breakpoint in the code line below to debug your script.
    chrome_driver_path = '/usr/local/bin/chromedriver'
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=option)
    driver.get("https://www.iec.co.il/payments/single")
    d =5
    # assert "Python" in driver.title
    sleep(2)
    elem1 = driver.find_element(By.XPATH , '/html/body/div/div[2]/div/mat-dialog-container/app-invoice-payments-wizard/app-dialog-container/div/app-payments-container/div/div[1]/app-form-wizard/div/wizard-step[1]/div/app-invoice-search/div/form/app-form-field-wrapper/app-basic-input[1]/div/fieldset/input')
    elem1.send_keys(contract)
    # elem1.clear()

    elem2 = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/mat-dialog-container/app-invoice-payments-wizard/app-dialog-container/div/app-payments-container/div/div[1]/app-form-wizard/div/wizard-step[1]/div/app-invoice-search/div/form/app-form-field-wrapper/app-basic-input[2]/div/fieldset/input')
    elem2.send_keys(receipt)
    # elem2.clear()

    elem2 = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/mat-dialog-container/app-invoice-payments-wizard/app-dialog-container/div/app-payments-container/div/div[1]/app-form-wizard/div/wizard-step[1]/div/app-invoice-search/div/form/div[3]/app-button/button')
    elem2.click()
    c = 7
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source
    # driver.close()
def get_price(path):
    im = Image.open(path)
    width, height = im.size

    # Setting the points for cropped image
    left = 220
    top = (height / 3) +130
    right = 370
    bottom = (2 * height / 3 ) -120

    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))
    im2 = im1.convert('RGB')
    im2 = im2.convert('L')
    im2.save(r"/Users/assafbashiri/Desktop/price.jpg")

    # Shows the image in image viewer
    im2.show()

def get_contract(path):
    im = Image.open(path)
    width, height = im.size

    # Setting the points for cropped image
    left = 180
    top = 135
    right = 265
    bottom = 160

    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))
    im2 = im1.convert('RGB')
    im2 = im2.convert('L')
    im2.save(r"/Users/assafbashiri/Desktop/contract.jpg")
    # Shows the image in image viewer
    im1.show()

def get_receipt(path):
    im = Image.open(path)
    width, height = im.size

    # Setting the points for cropped image
    left = 161
    top = 80
    right = 225
    bottom = 110

    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))
    im2 = im1.convert('RGB')
    im2 = im2.convert('L')
    im2.save(r"/Users/assafbashiri/Desktop/receipt.jpg")
    # Shows the image in image viewer
    im1.show()

def recognize_number(path):
    image = cv2.imread(path)
    img = cv2.resize(image, None, fx=3, fy=3)
    # text = pytesseract.image_to_string(image)
    kernel = np.ones((1, 1), np.uint8)
    cv2.imwrite('thresh.png', img)
    for psm in range(6, 13 + 1):
        config = '--oem 3 --psm %d' % psm
    txt = pytesseract.image_to_string(img, lang='eng')
    number = float(txt)
    return number
        # print('psm ', psm, ':', txt)
    # print(text)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # main()
    # a =8
    # print("Orel's account")
    # get_price(r"/Users/assafbashiri/Desktop/orel2.png")
    # recognize_number(r"/Users/assafbashiri/Desktop/price.jpg")
    # get_contract(r"/Users/assafbashiri/Desktop/orel2.png")
    # recognize_number(r"/Users/assafbashiri/Desktop/contract.jpg")
    # get_receipt(r"/Users/assafbashiri/Desktop/orel2.png")
    # recognize_number(r"/Users/assafbashiri/Desktop/receipt.jpg")

    # print("Etel's account")
    # get_price(r"/Users/assafbashiri/Desktop/abc.png")
    price = recognize_number(r"/Users/assafbashiri/Desktop/price.jpg")
    get_contract(r"/Users/assafbashiri/Desktop/abc.png")
    contract = recognize_number(r"/Users/assafbashiri/Desktop/contract.jpg")
    get_receipt(r"/Users/assafbashiri/Desktop/abc.png")
    receipt = recognize_number(r"/Users/assafbashiri/Desktop/receipt.jpg")
    receipt = receipt%10000
    main(contract, receipt)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

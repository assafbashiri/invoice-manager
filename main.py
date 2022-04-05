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
    option.add_experimental_option("excludeSwitches", ["enable-automation"]) #work without this
    option.add_experimental_option('useAutomationExtension', False)          #work without this
    option.add_argument('--ignore-certificate-errors')                       #work without this
    option.add_argument('--allow-running-insecure-content')                  #work without this
    # user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    # option.add_argument(f'user-agent={user_agent}')
    option.add_argument("--window-size=1920,1200")
    option.add_argument("--disable-gpu")
    # option.add_argument("--headless")
    # option.add_argument("no-sandbox")
    a = 9
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
    driver.get_screenshot_as_file(r"/Users/assafbashiri/Desktop/screenshot.png")
    a =8
    elem1 = driver.find_element(By.XPATH , '/html/body/div/div[2]/div/mat-dialog-container/app-invoice-payments-wizard/app-dialog-container/div/app-payments-container/div/div[1]/app-form-wizard/div/wizard-step[1]/div/app-invoice-search/div/form/app-form-field-wrapper/app-basic-input[1]/div/fieldset/input')
    elem1.send_keys(contract)
    # elem1.clear()

    elem2 = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/mat-dialog-container/app-invoice-payments-wizard/app-dialog-container/div/app-payments-container/div/div[1]/app-form-wizard/div/wizard-step[1]/div/app-invoice-search/div/form/app-form-field-wrapper/app-basic-input[2]/div/fieldset/input')
    elem2.send_keys(receipt)
    # elem2.clear()

    elem2 = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/mat-dialog-container/app-invoice-payments-wizard/app-dialog-container/div/app-payments-container/div/div[1]/app-form-wizard/div/wizard-step[1]/div/app-invoice-search/div/form/div[3]/app-button/button')
    elem2.click()
    option2 = webdriver.ChromeOptions()

    # Removes navigator.webdriver flag

    # For older ChromeDriver under version 79.0.3945.16
    option2.add_experimental_option("excludeSwitches", ["enable-automation"])
    option2.add_experimental_option('useAutomationExtension', False)
    # option2.add_argument('--headless')
    a =-0
    # For ChromeDriver version 79.0.3945.16 or over
    option2.add_argument('--disable-blink-features=AutomationControlled')
    driver2 = webdriver.Chrome(service=service, options=option2)
    driver2.get(driver.current_url)
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
    # im2.show()

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

def recognize_number(path, flag):
    image = cv2.imread(path)
    img = cv2.resize(image, None, fx=3, fy=3)
    # text = pytesseract.image_to_string(image)
    kernel = np.ones((1, 1), np.uint8)
    cv2.imwrite('thresh.png', img)
    for psm in range(6, 13 + 1):
        config = '--oem 3 --psm %d' % psm
    txt = pytesseract.image_to_string(img, lang='eng')
    if flag == 'n':
        txt = float(txt)
    return txt
        # print('psm ', psm, ':', txt)
    # print(text)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    f = open(r"/Users/assafbashiri/Desktop/demofile2.txt", "a")
    # f.write("\nNow the file has more content!;")
    f.close()

    # open and read the file after the appending:
    f = open(r"/Users/assafbashiri/Desktop/demofile2.txt", "r")
    file = f.read()
    split_file = file.split(";")
    # main(contract, receipt)
    a =8
    # print("Orel's account")
    # get_price(r"/Users/assafbashiri/Desktop/orel2.png")
    # recognize_number(r"/Users/assafbashiri/Desktop/price.jpg")
    # get_contract(r"/Users/assafbashiri/Desktop/orel2.png")
    # recognize_number(r"/Users/assafbashiri/Desktop/contract.jpg")
    # get_receipt(r"/Users/assafbashiri/Desktop/orel2.png")
    # recognize_number(r"/Users/assafbashiri/Desktop/receipt.jpg")

    # print("Etel's account")
    # get_price(r"/Users/assafbashiri/Desktop/abc.png")
    price = recognize_number(r"/Users/assafbashiri/Desktop/price.jpg", "n")
    get_contract(r"/Users/assafbashiri/Desktop/abc.png")
    contract = recognize_number(r"/Users/assafbashiri/Desktop/contract.jpg", "s")
    get_receipt(r"/Users/assafbashiri/Desktop/abc.png")
    receipt = recognize_number(r"/Users/assafbashiri/Desktop/receipt.jpg", "n")
    receipt = receipt%10000
    receipt = str(receipt)
    receipt = receipt[:4]
    # main(contract, receipt)
    print("the contract number is: ", contract)
    print("the receipt last 4 digits is: ", receipt)
    print("the bill is: ", price)
    main(contract, receipt)
    a = 8
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

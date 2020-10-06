# AutomationFlight

This app is made specifically for https://www.makemytrip.com/

Requirements:
  1. Chrome driver - (Can be installed from : https://chromedriver.chromium.org/)   PS: CHECK FOR THE VERTION AND DOWNLOAD THE SUITABLE ONE
  2. install all packages from requiremnts.txt
  
Give the proper location for Chrome Driver installed path at line 5
    - driver = webdriver.Chrome(executable_path=r"YOUR PATH TO CHROMEDRIVER")
    
CITY given : Trivandrum.
DATE given : 16th October 2020

The app will generate 5 flight lists based on descending order of price.

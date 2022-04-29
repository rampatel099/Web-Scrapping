To run the scrape.py script first one needs to install selenium and beautiful soup libraries using pip. 
The commands to install them using pip are:
1) pip install bs4
2) pip install selenium

Also the webdriver for chrome needs to be downloaded. Check the version of your chrome. "example: 100.0.4896.60"
Visit the site https://chromedriver.chromium.org/downloads and download the driver matching your version.
Extract the chromedriver.exe file and copy it's path and paste it in the line - driver = webdriver.Chrome(r"C:\Users\Rohan Nemade\Downloads\chromedriver_win32\chromedriver.exe") in the scrape.py file.
Now you can run the script and it will collect all the data in a pandas dataframe and download it as a .csv file.
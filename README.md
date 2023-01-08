# Pharmacy Scrapper
Small app for comparing prices in biggest Polish online pharmacies. Creates a spreadsheet with the results from up to five stores.

The app has a fully functional GUI. The user can enter any desired product's name to compare the prices between the selected pharmacies. The store’s website gets scraped using the Selenium library, extracts the prices data and generates an .xlsx spreadsheet containing a list of the results.

![toolbar](https://github.com/paulinacyran/pharmacy-scrapper/blob/master/images/pharmacy_scrapper_01.png)

## Technologies 
Project is created with: 
* Python version: 3.10.0 (base logic)
* PyQt5 version: 5.15.7 (GUI)
* Selenium version: 4.7.2 (web scraping)
* OpenPyXL version: 3.0.10 (spreadsheet)

## Setup 
1) **Create and activate a virtual environment.**

    **Windows** 
    ``` 
    pip install virtualenv 
    python -m virtualenv <your-env> 
    <your-env>\Scripts\activate 
    ``` 
    **Mac/Linux** 
    ``` 
    pip3 install virtualenv 
    python3 -m virtualenv <your-env> 
    source <your-env>/bin/activate 
    ```

2) **Clone this repository.** 
    ``` 
    git clone https://github.com/paulinacyran/pharmacy-scrapper.git 
    ```

3) **Go into the repository.** 
    ``` 
    cd pharmacy-scrapper 
    ```

4) **Install all dependencies.**

    **Windows** 
    ``` 
    pip install -r requirements.txt 
    ```

    **Mac/Linux** 
    ``` 
    pip3 install -r requirements.txt 
    ```
5)  **From https://chromedriver.chromium.org/downloads, download the chromedriver.exe file appropriate for your version of Chrome browser.**

6)  **Create a folder called 'chromedriver' and place the chromedriver.exe file in it.**

7) **Run the app.**

    **Windows** 
    ``` 
    python run.py 
    ```

    **Mac/Linux** 
    ``` 
    python3 run.py 
    ``` 

8) **Use the app.**

   Adjust pharmacy selection by clicking the buttons with the store names in the 'Select pharmacies to scrap' section. All pharmacies are checked by default.

   Next, enter the name of the product of which prices you want to compare. You can add more product names with the 'Add next product' button. The 'Remove last product' button allows you to remove the last product from the list.
   Afterwards click the 'RUN' button.
   
   ![toolbar](https://github.com/paulinacyran/pharmacy-scrapper/blob/master/images/pharmacy_scrapper_02.png)

   After the scrapping is done, a new window appears with information about the completed process. Click the 'SELECT LOCATION' button to choose the location for the .xlsx file. After you click the button, the .xlsx file opens.
   
   ![toolbar](https://github.com/paulinacyran/pharmacy-scrapper/blob/master/images/select_location.png)
   
   The spreadsheet contains individual sheets for each product initially entered in the beginning. Every sheet contains four columns: product name, pharmacy name, product price, product website.
   
   ![toolbar](https://github.com/paulinacyran/pharmacy-scrapper/blob/master/images/spreadsheet.png)
  
     

    
    
    

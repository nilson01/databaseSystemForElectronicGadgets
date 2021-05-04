# CSE305HW5

####Database system we chose.
* SQLite DB 

#### URL used to access the pages.
* We have added all the links to each question in "/" i.e. homepage for local lost.
* You can easily click A, B, C, D, E to access each question solution.

##TO run this file:

**Step: 1**
* Open the folder in the Pycharm

**Step: 2** 
Install the dependencies from requirements folder(run this in the terminal): 

    => pip install -r requirements.txt 
    or  
    => pip install --user -r requirements.txt

**STEP: 3**  
* Double-click on createDB.py and run this file in the pycharm.
* This will create "ncps5.db" file in the assignment5 folder. 
* This stores the database information we will be using in the application.

**Step: 4** 
* Double-click "app.py" file and run this file in the pycharm.

**Step: 5**

Click A, B, C, D, E for each part implementation.

##  For testing: 
**use the following values for each attribute on respective models**

1. **Products**: 
   * maker: Microsoft, Dell, Apple, Samsung, Lenovo, Sony, Toshiba and Acer
   * model: PC => 333, 343, etc , Laptops => 111, 141, 161, etc and Printers => 222, 555, 666, etc 
   * type: Laptops, Printer, PC
    
2. **PCs**: 
   * speed => [8, 64], 
   * ram => [5, 19], 
   * hd => [12, 50],
   * price => [100, 1000]
    
3. **Laptops**: 
   * speed => [12, 99],
   * ram => [6, 60],
   * hd => [13, 67],
   * Screen => [10, 77]
   * price => [100, 1234]
    
4. **Printers**: 
   * Price => [123, 777]



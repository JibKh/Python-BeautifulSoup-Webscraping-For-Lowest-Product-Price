=== ABOUT ===
Based on your search input, I search reputable websites and output the name and prices to an excel file ordered from low to high prices.

Why?
There are numerous websites for custom parts and it becomes too difficult to search for the best price.
It becomes much easier to compare the prices of two different online stores when it is automatically tabulated for you.

How?
Using beautifulsoup I webscrape reputable websites and export it to excel using pandas library.


=== WEBSITES SEARCHED ===
IndusTech
EaseTec


=== HOW TO RUN ===
Download all the files
Open your terminal and enter the following command: python main.py Your Search
An excel workbook will be created with your results in the same directory as the download

EXAMPLE:
Command: python main.py Gtx 1660 Super
Open file: Gtx_1660_Super.xlsx


=== FUTURE UPDATES ===
Another sheet with a list of all the products from all the sites ordered from low to high prices
More websites such as Czone and PakDukaan


== LIMITATIONS ==
1) The number of items retrieved from each site is based on their default setting of how many items they display. So if they display 10 items on default, then at most the 10 cheapest items are retrieved.
2) The relevance of the results are based on how good the user search is and the website.
3) Speed of code depends on user internet speed.

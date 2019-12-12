# Social Networks Final Project
## -Raymond Shi (rs5955), Alexander Sosnovsky (as10507)
To run our Airbnb search engine, please download the files (genresult.py, nycincome.csv, income.csv, and rooms.csv) in the program directory. 

1. From terminal, run 
> $python genresult.py **zipcode1* *zipcode2** 

    where zipcode1 is the hometown zip code and zipcode2 is the current zip code. 
2. The program will output 10 lines, each containing the room ID (first column in rooms.csv), room score, nightly price, borough, neighborhood, room type, and name. All of this data is separated by a semicolon.

*Important* -  the US census median income data doesn't include any zip codes from New England (CT, MA, RI, VT, NH, ME) due to a legal quirk. So a zip code from any of those states will be treated as an invalid zip code. The way the algorithm handles an invalid zip code depends on the other zip code given in the input. If both are invalid, their income level is set to a predetermined value.

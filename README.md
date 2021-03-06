# Social Networks Project (Fall 2019)
___
# Predictive Listings of Airbnb Accommodations
## -Raymond Shi, Alexander Sosnovsky

To run the project, download the files (genresult.py, nycincome.csv, income.csv, and rooms.csv) in the src directory. 

run:

> $python genresult.py **zipcode1* *zipcode2** 

    where zipcode1 is the hometown zip code and zipcode2 is the current zip code. 
Output: 10 Airbnb listings sorted by order of importance, each containing the room ID (first column in rooms.csv), room score, nightly price, borough, neighborhood, room type, and name. All of this data is separated by a semicolon.

*Important* -  the US census median income data doesn't include any zip codes from New England (CT, MA, RI, VT, NH, ME) due to a legal quirk. So a zip code from any of those states will be treated as an invalid zip code. The way the algorithm handles an invalid zip code depends on the other zip code given in the input. If both are invalid, their income level is set to a predetermined value.
***
*The miscellaneous directory contains all the other files and resources we used for this project.*

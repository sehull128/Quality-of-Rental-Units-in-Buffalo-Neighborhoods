# Quality-of-Rental-Units-in-Buffalo-Neighborhoods


# Summary

Housing quality is a complex issue to analyze as it is difficult to gauge whether data is accurate or collected at all. With many legislative packages coming aimed to help infrastructure, I was interested in looking at what variables could determine housing quality within a numeric value to be able to analzye. Specifically, I wanted to see if the neighborhoods one lived in had any affect on whether they were more likely to rent a home that was not-lead compliant, and not making mortgage payments. Further, this project examines whether there is an association between demographic variables and rental housing quality in Buffalo, New York.

# Input Data

There are three input files: **Rental_Registry.csv**, **Census Demographic Data.csv** and **Census Tracts 2020.zip**

The **Census Tracts 2020.zip** file was used to read and create the census tract variable, which then was merged with the **Census Demographic Data.csv** on their respective GEOID codes. This was done in order to gain demographic data on the shapefile that will later be merged with another file. 
The **Rental_Registry.csv"** file was used to read and query two specific neighborhood, "Fruit Belt", and "Pratt_Willert", as they were the two highest rates of non lead compliant rental homes neighborhods. I merged this file with the **Census Tracts 2020.zip** file again in order to have my demographic variables joined on the same key and in the same file. 

# Deliverables 

There are seven deliverables within this project:

Three scripts -  **Census Tract and Demographics.py** and, **Buffalo_figures.py** and **Race_by_County.py**

Four figures attached as png files - **Top 10 Neighborhoods in Buffalo.png** and **rental.png**, and **Neighborhoods.png** and, **Delinquency.png**



# Instructions for figures

Where to get input data - 

The three files needed are located in the folder "Quality of Rental Units in Buffalo Neighborhoods" titled: **Census Tracts 2020.zip**, **Census Demographic Data.csv**, and **Rental_Registry.csv"**. All three files were found at data.buffalony.gov. The API call illustrated in part B is from the "American Community Survey 5-Year Data (2019)" with 
variables = {'B02003_003E':'HC01_VC54.Estimate..RACE...One.race...White',
            'B02003_004E':'HC01_VC55.Estimate..RACE...One.race...Black.or.African.American'
            }.
            
  
The first script to run is: **Census Tract and Demographics.py**. 

A. Downloading files 

Using the "read" call, we will read the zip file and csv file by their Geoid numbers, as a why to identify them. It is important to note tha the geoid numerical values match up and are both tract groups. From there, I merged the variable 'censustract' that contains the "read" file, with the 'demographic' variable, which also contains the "read" file for its respective csv. This is a 1:1, outer join on the "Geoid tract code". 

B. Using the API Census, I was able to create a new variable named "variables". "Variables" is a join key for the data set in Buffalo for Race split into White or Black. 
Note: variables = {'B02003_003E':'HC01_VC54.Estimate..RACE...One.race...White',
            'B02003_004E':'HC01_VC55.Estimate..RACE...One.race...Black.or.African.American'
            }

Continuing on, setting the api equal to the link the data is from links the demographic variables together through the for and in clause. Specifically here, we are looking at county and city level for the 36th state (NY). 

C. Creating new **Race_by_County.csv**

Through setting "response" equal to the request.get function for the API, you are able to call on the above API file to gather the demographic data that matches with the aboved merged GEOid codes.
From then, creating the race variable through the pd.DataFrame function allows for a new DataFrame to be created and filled with the new data from the request call API. This call is then saved under **Race_by_County.csv**

response = requests.get(api, payload)
print(response)
row_list = response.json()
colnames = row_list[0]
datarows = row_list[1:]
race = pd.DataFrame(columns=colnames, data=datarows)
race = race.replace('White','Black')
race = race.rename(columns=variables)
race = race.rename(columns={ 'county': 'geoid20'})
race = race.astype(str)
race.to_csv('Race_by_County.csv')

D. Merging the **Rental_Registry.csv** file onto Specific Neighborhoods
Here I am merging the **Rental_Registry**onto Specific Neighborhoods through a query. I will then merge it with
the race variable that we just created (Race_by_county.csv), so that I can get demographic data to analyze in my other .py file.

The second script to run is: **Buffalo_figures.py**

A. Downloading files
import geopandas as gpd
import pandas as pd
import numpy as np 
import requests

I then created the "registry" variable to read the CSV file that is needed in this script, **Rental_Registry.csv**. I then created the variable "leadcomp" to group the variables within "Rental_Registry.csv" file of '[Neighborhood]', '[Lead Compliance]'.

The code below creates the figure 'rental.png'
![import geopandas as gpd
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['figure.dpi'] = 300
sns.set_theme(style="white")

registry = ![rental.png](image.png)

Then, I decided I wanted to break down the "leadcomp" variable into percentages of homes that are lead compliant and those that are not. By doing this, I was able to create a figure that shows the percentage of total rental units in Buffalo in each neighborhood, that are not lead compliant
![Neighborhoods.png](image.png).

From there, I was interested in looking at the "Milestone" variable found in the "Rental_Registry.csv" file that showed the status of a landlords payment history. After 30 days from their last warning, the landlord's information is posted as being delinquent. This is important to track and see if there are more bad landlord's in one neighborhood and why that might be. 

In order to do this, I created "delinquency" why grouped the variables 'Neighborhood', and 'Milestone' by size from the "Rental_Registry.csv" file. I unstacked it on the 'Milestone' variable and was able to compute a bar plot figure. 

![Delinquency.png](image.png)


The fourth figure I have is looking further at the Top 5 Neighborhoods with late mortgage payments and percentage of non lead compliant homes.  I created a by_milstone variable to group the thirtyday_pct by its variable of "Neighborhood". I had to use an .astype(float) function here as it was a series before and the calculation was not working. I then sorted it by the top 5 highest percentage neighborhoods with rental units with late mortgage payments. 


![Top 10 Neighborhoods in Buffalo.png](image.png)

# Main Findings
The main findings in this analysis were that due to the change in map from 2020 to the new census tract model, the difference in years from 2017 to 2020 skewed the data. In order to combat this, I performed an API call that was able to retrieve the demographic data from 2020 as well. 

After conducting analyses of the block groups and neighborhoods in Buffalo, it showed that neighborhoods extended into several different block groups. This made it difficult to join on block group variables. 

Looking at the figures, in "rental.png" it shows the lead compliance rate of Buffalo neighborhoods. It shows a positive relationship, but there were a few higher outliers that I was interested to explore. 

From there, I created "Neighborhoods.png" to breakdown each neighborhood in Buffalo with a registered rental unit, and chart the percentage of those that are non lead compliant. The most interesting component I noticed was that none of the neighborhoods were below 50%. Also, looking at neighborhoods like "Central", "Fruit Belt", "Pratt-Willert", they are signicantly higher than the other neighborhoods. 

I wanted to see if there were any other variables that caused spikes in neighborhood like Lead Compliancy did, so I looked at Delinquency rates of landlords payment on mortgage. This is important to see if there is an association with delinquency rates and quality of housing. Pratt-Willart in this figure, is the only neighborhood from the previous analysis to stay an outlier as "Fruit Belt" and "Central both decreased. 

From here, I created a horizontal and vertical bargraph of the top ten highest rates of delinquent mortgage payments and lead non compliance in the neighborhoods of Buffalo. Overall, the biggest take away is that based on looking at the neighborhood identity alone, there are specific ones like, Fruit Belt, Allentown, Pratt-Wallart that have a higher rate of bad quality of life indicators. 

To further this study, I would look deeper into the race, age, and income demographics of each neighborhood. From there, I would create a heat map in GIS to show if there were higher concentrations based on these variables in different neighborhoods of the map to see if there are any associations.





# Quality-of-Rental-Units-in-Buffalo-Neighborhoods


# Summary

Housing quality is a complex issue to analyze as it is difficult to gauge whether data is accurate or collected at all. With many legislative packages coming aimed to help infrastructure, I was interested in looking at what variables could determine housing quality within a numeric value to be able to analzye. Specifically, I wanted to see if the neighborhoods one lived in had any affect on whether they were more likely to rent a home that was not-lead compliant, and not making mortgage payments. Further, this project examines whether there is an association between demographic variables and rental housing quality in Buffalo, New York.

# Input Data

There are four input files: **Rental_Registry.csv**, **Census Demographic Data.csv** and **Census Tracts 2020.zip**

The **Census Tracts 2020.zip** file was used to read and create the census tract variable, which then was merged with the **Census Demographic Data.csv** on their respective GEOID codes. This was done in order to gain demographic data on the shapefile that will later be merged with another file. 
The **Rental_Registry.csv"** file was used to read and query two specific neighborhood, "Fruit Belt", and "Pratt_Willert", as they were the two highest rates of non lead compliant rental homes neighborhods. I merged this file with the **Census Tracts 2020.zip** file again in order to have my demographic variables joined on the same key and in the same file. 

# Deliverables 

There are seven deliverables within this project:

Three scripts -  **Census Tract and Demographics.py* and, **Buffalo_figures.py** and **Race_by_County.py

Four figures attached as png files - **Top 10 Neighborhoods in Buffalo.png** and **rental.png**, and **Neighborhoods.png** and, **Delinquency.png**


# Instructions for figures

Where to get input data - 

The three files needed are located in the folder "Quality of Rental Units in Buffalo Neighborhoods" titled: **Census Tracts 2020.zip**, **Census Demographic Data.csv**, and **Rental_Registry.csv"**. All three files were found at data.buffalony.gov. The API call illustrated in part B is from the "American Community Survey 5-Year Data (2019)



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

registry = pd.read_csv('Rental_Registry.csv', dtype=str)
leadcomp = registry.groupby(['Neighborhood', 'Lead Compliance']).size()
leadcomp = leadcomp.unstack('Lead Compliance')
print(leadcomp)


fig, ax1 = plt.subplots()
sns.scatterplot(data=leadcomp,x="Y", y="N")
ax1.set_title("Buffalo Neighborhood Lead Compliance")
ax1.set_xlabel("# of Non-Lead Compliant Rental Units")
ax1.set_ylabel("# of Lead Compliant Rental Units")
fig.tight_layout()
fig.savefig('rental.png')](image.png)





 
# Main Finding


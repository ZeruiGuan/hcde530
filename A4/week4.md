### Competency Claim

I used the REST Countries API to retrieve structured data about countries. The endpoint `https://restcountries.com/v3.1/all?fields=name,population,region` returns a list of JSON objects, where each object represents a country.

In my script (`countries_api.py`), I sent a GET request using `requests.get()` and parsed the response using `response.json()`, which returned a list of dictionaries. One detail I had to handle was that the country name is nested inside a dictionary under `name` and `common`. If I tried to treat it as a flat field, the output would be incorrect. To avoid this, I accessed it using `country.get("name", {}).get("common", "Unknown")`.

I extracted the country name, population, and region fields and saved them into a CSV file. This required understanding the structure of the API response rather than assuming a fixed format.

This work shows how to retrieve data from an API and convert it into a usable structured format.

### Reflection

This data can be used to answer questions about how countries are distributed by region and population.

Before using the data, I would verify whether the dataset is complete and whether all countries are included. I would also check for missing or inconsistent values across entries.

If the data is incomplete or interpreted incorrectly, any conclusions based on it would be unreliable even if the script runs without errors.
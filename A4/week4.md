### Competency Claim

I used the REST Countries API to retrieve structured data about countries. The endpoint `https://restcountries.com/v3.1/all?fields=name,population,region` returns a list of JSON objects, where each object represents a country.

In my script (`countries_api.py`), I sent a GET request using `requests.get()` and parsed the response using `response.json()`, which returned a list of dictionaries. One detail I had to handle was that the country name is nested inside a dictionary under `name` and `common`. If I tried to treat it as a flat field, the output would be incorrect. To avoid this, I accessed it using `country.get("name", {}).get("common", "Unknown")`.

I extracted the country name, population, and region fields and saved them into a CSV file. This required understanding the structure of the API response rather than assuming a fixed format.

This work shows how to retrieve data from an API and convert it into a usable structured format.

### HCD Reflection

This data helps users understand how countries are distributed by region and population, which can support basic comparisons and analysis.

From an HCD perspective, the choice of fields affects what users can learn. While name, population, and region provide a clear overview, they may not give enough context for deeper understanding, which could lead to oversimplified conclusions.

I would also check that the data is complete and consistent to avoid misleading users. In the future, I would consider adding more fields or allowing users to customize the data to better meet different needs.
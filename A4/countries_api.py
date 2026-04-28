import csv
import requests


def main() -> None:
    # This API endpoint requests data from the REST Countries API.
    # The URL includes a `fields` parameter, which limits the response
    # to only the fields we need: name, population, and region.
    api_url = "https://restcountries.com/v3.1/all?fields=name,population,region"

    # Send a GET request to the API.
    # The API returns structured JSON data (a list of countries).
    response = requests.get(api_url, timeout=30)
    response.raise_for_status()  # Raise an error if the request fails

    # Parse the JSON response into a Python list of dictionaries.
    # Each dictionary represents one country.
    countries = response.json()

    extracted_rows = []

    # Loop through each country in the response
    for country in countries:
        # Extract specific fields from each country:
        # - name.common → country name
        # - population → total population
        # - region → geographic region
        name = country.get("name", {}).get("common", "Unknown")
        population = country.get("population", 0)
        region = country.get("region", "Unknown")

        extracted_rows.append((name, population, region))

    # Sort results alphabetically by country name for readability
    extracted_rows.sort(key=lambda row: row[0])

    # Print results in a clean, readable format
    print(f"Total countries returned: {len(extracted_rows)}\n")
    print(f"{'Country':35} {'Population':>15}  {'Region'}")
    print("-" * 65)

    for name, population, region in extracted_rows:
        print(f"{name:35} {population:15,d}  {region}")

    # Save the results to a CSV file
    output_file = "countries_output.csv"
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["country_name", "population", "region"])
        writer.writerows(extracted_rows)

    print(f"\nSaved CSV to: {output_file}")


if __name__ == "__main__":
    main()
import csv


INPUT_FILE = "responses.csv"
OUTPUT_FILE = "rseponses_cleaned.csw"


def clean_rows(rows):
    for row in rows:
        name = (row.get("name") or "").strip()
        if not name:
            continue

        if "role" in row and row["role"] is not None:
            row["role"] = str(row["role"]).upper()

        yield row


def main():
    with open(INPUT_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        cleaned = list(clean_rows(reader))

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(cleaned)


if __name__ == "__main__":
    main()


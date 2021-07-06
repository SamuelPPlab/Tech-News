from tech_news import database
import csv

header = [
    "url",
    "title",
    "timestamp",
    "writer",
    "shares_count",
    "comments_count",
    "summary",
    "sources",
    "categories",
]


def csv_exporter(filepath):
    """Seu código deve vir aqui"""
    news = database.find_news()
    print(news)
    try:
        assert filepath.endswith(".csv")
        with open(filepath, "w") as file:
            writer = csv.DictWriter(file, fieldnames=header, delimiter=";")

            writer.writeheader()

            for rows in news:
                for key in rows:
                    if type(rows[key]) == list:
                        # https://stackoverflow.com/questions/44778/how-would-you-make-a-comma-separated-string-from-a-list-of-strings
                        rows[key] = ",".join(rows[key])

                writer.writerow(rows)

    except AssertionError:
        raise ValueError("Formato invalido")


# csv_exporter("teste.")

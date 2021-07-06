import csv


def csv_importer(filepath):
    """Seu código deve vir aqui"""
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
    res = []
    try:
        assert filepath.endswith(".csv")
        with open(filepath) as file:
            file_content = csv.reader(file, delimiter=";", quotechar='"')
            file_header, *data = file_content

            assert file_header == header
            res = [
                {header[i]: content[i] for i in range(len(content))}
                for content in data
            ]
            return res
    except AssertionError:
        raise ValueError("Formato invalido")

    except FileNotFoundError:
        raise ValueError(f"Arquivo {filepath} não encontrado")

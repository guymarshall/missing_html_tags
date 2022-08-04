import pprint

file_path = input("Enter the filepath: ")
html_base_words = ["div", "article", "label", "section", "form", "span", "strong", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "li", "header", "i", "button", "select", "option", "table", "thead", "tbody", "tfooter", "th"]
element_counts = {}

with open(file_path, "r") as file:
    file_contents = ""

    for line in file:
        file_contents += line

    for word in html_base_words:
        opening_tag = f"<{word}"
        closing_tag = f"</{word}"

        opening_count = file_contents.count(opening_tag)
        if opening_count > 0:
            element_counts[opening_tag] = opening_count

        closing_count = file_contents.count(closing_tag)
        if closing_count > 0:
            element_counts[closing_tag] = closing_count

pprint.pprint(element_counts, sort_dicts=False)
user_input = input("Press enter to close...")

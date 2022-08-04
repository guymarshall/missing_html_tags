import pprint

file_path = input("Enter the filepath: ")
# html_base_words = ["div", "article", "label", "section", "form", "span", "strong", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "li", "header", "i", "button", "select", "option", "table", "thead", "tbody", "tfooter", "th"]
html_base_words = ["a", "abbr", "acronym", "address", "applet", "area", "article", "aside", "audio", "b", "base", "basefont", "bdi", "bdo", "big", "blockquote", "body", "br", "button", "canvas", "caption", "center", "cite", "code", "col", "colgroup", "data", "datalist", "dd", "del", "details", "dfn", "dialog", "dir", "div", "dl", "dt", "em", "embed", "fieldset", "figcaption", "figure", "font", "footer", "form", "frame", "frameset", "h1", "h2", "h3", "h4", "h5", "h6", "head", "header", "hr", "html", "i", "iframe", "img", "input", "ins", "kbd", "label", "legend", "li", "link", "main", "map", "mark", "meta", "meter", "nav", "noframes", "noscript", "object", "ol", "optgroup", "option", "output", "p", "param", "picture", "pre", "progress", "q", "rp", "rt", "ruby", "s", "samp", "script", "section", "select", "small", "source", "span", "strike", "strong", "style", "sub", "summary", "sup", "svg", "table", "tbody", "td", "template", "textarea", "tfoot", "th", "thead", "time", "title", "tr", "track", "tt", "u", "ul", "var", "video", "wbr"]
programming_characters = ["{", "}", "(", ")", "[", "]"]
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

    for character in programming_characters:
        character_count = file_contents.count(character)
        if character_count > 0:
            element_counts[character] = character_count

pprint.pprint(element_counts, sort_dicts=False)
user_input = input("Press enter to close...")

def parse_sections(text):
    sections = {}

    current_heading = None

    for line in text.split("\n"):

        if line.startswith("## "):
            current_heading = line.replace("## ", "").strip()
            sections[current_heading] = ""

        elif current_heading:
            sections[current_heading] += line + "\n"

    return sections
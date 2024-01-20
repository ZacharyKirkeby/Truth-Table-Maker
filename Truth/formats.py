def format_as_markdown(truth_table):
    # Implement logic to format truth_table as Markdown
    # Example: | Column 1 | Column 2 |
    #          |----------|----------|
    #          |   True   |  False   |
    formatted_table = "| " + " | ".join(truth_table[0]) + " |\n"
    formatted_table += "| " + " | ".join(["---"] * len(truth_table[0])) + " |\n"
    for row in truth_table[1:]:
        formatted_table += "| " + " | ".join(row) + " |\n"
    return formatted_table

def format_as_latex(truth_table):
    # Implement logic to format truth_table as LaTeX
    # Example: \begin{tabular}{|c|c|}
    #          \hline
    #          Column 1 & Column 2 \\
    #          \hline
    #          True & False \\
    formatted_table = "\\begin{tabular}{|" + "|".join(["c"] * len(truth_table[0])) + "|}\n"
    formatted_table += "\\hline\n"
    formatted_table += " & ".join(truth_table[0]) + " \\\\\n"
    formatted_table += "\\hline\n"
    for row in truth_table[1:]:
        formatted_table += " & ".join(row) + " \\\\\n"
    formatted_table += "\\hline\n\\end{tabular}"
    return formatted_table

def format_as_ascii(truth_table):
    # Implement logic to format truth_table as ASCII
    # Example: +----------+----------+
    #          | Column 1 | Column 2 |
    #          +----------+----------+
    #          |   True   |  False   |
    formatted_table = "+" + "+".join(["-" * (len(col) + 2) for col in truth_table[0]]) + "+\n"
    formatted_table += "| " + " | ".join(truth_table[0]) + " |\n"
    formatted_table += "+" + "+".join(["-" * (len(col) + 2) for col in truth_table[0]]) + "+\n"
    for row in truth_table[1:]:
        formatted_table += "| " + " | ".join(row) + " |\n"
    formatted_table += "+" + "+".join(["-" * (len(col) + 2) for col in truth_table[0]]) + "+\n"
    return formatted_table

def format_as_csv(truth_table):
    # Implement logic to format truth_table as CSV
    # Example: Column 1,Column 2
    #          True,False
    formatted_table = ",".join(truth_table[0]) + "\n"
    for row in truth_table[1:]:
        formatted_table += ",".join(row) + "\n"
    return formatted_table

# Add your custom format function if needed
def format_as_custom(truth_table):
# to be determined, likely markdown

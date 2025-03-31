import re

class Token:
    def __init__(self, token_type, extra_info):
        self.token_type = token_type
        self.extra_info = extra_info

    def __str__(self):
        return f"<{self.token_type}, {self.extra_info}>"

# Symbol table (global for simplicity)
symbol_table = []

def add_to_symbol_table(identifier):
    if identifier not in symbol_table:
        symbol_table.append(identifier)
    return symbol_table.index(identifier)

def show_symbol_table():
    if not symbol_table:
        print("Symbol table is empty")
    else:
        print("Symbol Table:")
        for i, ident in enumerate(symbol_table):
            print(f"Index {i}: {ident}")

# Regex pattern for token matching
pattern = re.compile(
    r'(?P<token>'  # Capture the entire token
    r'&&|'         # Logical AND
    r'\|\||'       # Logical OR
    r'&|'          # Bitwise AND
    r'\||'         # Bitwise OR
    r'-?\d*\.\d+|' # Float
    r'-?\d+|'      # Integer
    r'[a-zA-Z][a-zA-Z0-9]*|'  # Identifier
    r'[^\s]+'      # Error (catch-all)
    r')(?=\s|$)',  # Ensure token ends at whitespace or end of string
    re.MULTILINE   # Handle multi-line input
)

def lex(file_content):
    tokens = []
    line_number = 1

    # Find all matches in the file content
    for match in pattern.finditer(file_content):
        lexeme = match.group('token')
        start_pos = match.start()

        # Update line number based on newlines before this token
        newlines = file_content[:start_pos].count('\n')
        line_number = 1 + newlines

        # Determine token type
        if lexeme == "&&":
            tokens.append(Token("LOGICAL_AND", "nothing"))
        elif lexeme == "||":
            tokens.append(Token("LOGICAL_OR", "nothing"))
        elif lexeme == "&":
            tokens.append(Token("BITWISE_AND", "nothing"))
        elif lexeme == "|":
            tokens.append(Token("BITWISE_OR", "nothing"))
        elif re.fullmatch(r'-?\d*\.\d+', lexeme):
            tokens.append(Token("FLOAT", float(lexeme)))
        elif re.fullmatch(r'-?\d+', lexeme):
            tokens.append(Token("INTEGER", int(lexeme)))
        elif re.fullmatch(r'[a-zA-Z][a-zA-Z0-9]*', lexeme):
            index = add_to_symbol_table(lexeme)
            tokens.append(Token("ID", index))
        else:
            tokens.append(Token("ERROR", f'"{lexeme}" at line {line_number}'))

    return tokens

# Main program
def main():
    filename = input("Enter the name of the input file: ")
    try:
        with open(filename, 'r') as f:
            file_content = f.read()
    except FileNotFoundError:
        print("File not found. Exiting...")
        return

    # Get all tokens at once
    all_tokens = lex(file_content)
    token_index = 0  # Track current position in the token list

    while True:
        print("\n=== Lexical Analyzer Menu ===")
        print("1. Call lex()")
        print("2. Show symbol table")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            for token in all_tokens:
                print(token)
        elif choice == "2":
            show_symbol_table()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
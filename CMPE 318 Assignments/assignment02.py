import re

class Token:
    def __init__(self, token_type, extra_info):
        self.token_type = token_type
        self.extra_info = extra_info

    def __str__(self):
        return f"<{self.token_type}, {self.extra_info}>"

# Global variables for file content and position
file_content = ""
position = 0

# Regex pattern to match all tokens
# Groups: (int) | (float) | (id) | (&&) | (||) | (&) | (|) | (error)
pattern = re.compile(
    r'\s*('  # Skip leading spaces and capture the token
    r'[+-]*\d+'  # Integer
    r'|'
    r'[+-]*\d*\.\d+'  # Float
    r'|'
    r'[a-zA-Z][a-zA-Z0-9]*'  # Identifiers
    r'|'
    r'&&'  # Logical AND
    r'|'
    r'\|\|'  # Logical OR
    r'|'
    r'&'  # Bitwise AND
    r'|'
    r'\|'  # Bitwise OR
    r'|'
    r'[^\s]+'  # Anything else (error)
    r')'
)

def lex():
    global position, file_content
    if position >= len(file_content):
        return None  # End of file

    # Find the next token from the current position
    match = pattern.match(file_content, position)
    if not match:
        return None  # No more tokens

    lexeme = match.group(1)  # The matched token
    position = match.end()   # Update position to end of match

    # Determine token type and extra info
    if re.fullmatch(r'[+-]*\d+', lexeme):
        return Token("INTEGER", int(lexeme))
    elif re.fullmatch(r'[+-]*\d*\.\d+', lexeme):
        return Token("FLOAT", float(lexeme))
    elif re.fullmatch(r'[a-zA-Z][a-zA-Z0-9]*', lexeme):
        index = add_to_symbol_table(lexeme)
        return Token("ID", index)
    elif lexeme == "&&":
        return Token("LOGICAL_AND", "nothing")
    elif lexeme == "||":
        return Token("LOGICAL_OR", "nothing")
    elif lexeme == "&":
        return Token("BITWISE_AND", "nothing")
    elif lexeme == "|":
        return Token("BITWISE_OR", "nothing")
    else:
        return Token("ERROR", lexeme)
    
# --------------------------------------------------- #
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


# ---------------------------------------------------------- #

def main():
    global file_content, position
    
    
    filename = input("Enter the name of the input file: ")
    try:
        with open(filename, 'r') as f:
            file_content = f.read()
        position = 0
    except FileNotFoundError:
        print("File not found. Exiting...")
        return

    while True:
        print("\nMenu:")
        print("1. Call lex()")
        print("2. Show symbol table")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            token = lex()
            if token:
                print(token)
            else:
                print("End of file reached")
        elif choice == "2":
            show_symbol_table()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
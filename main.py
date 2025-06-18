from stats import get_num_words, get_char_counts, create_char_count_records
import sys

def get_book_text(filepath: str) -> str:
    with open(filepath, "r") as file:
        file_contents = file.read()
    return file_contents


def build_report(filepath: str) -> str:
    book_text = get_book_text(filepath) 
    report = f"=========== BOOKBOT ============\n"
    report += f"Analyzing book found at {filepath}...\n"
    report += "----------- Word Count ----------\n"
    report += f"Found {get_num_words(book_text)} total words\n"
    report += "--------- Character Count -------\n"
    char_count_records = create_char_count_records(get_char_counts(book_text))
    for record in char_count_records:
        if record['char'].isalpha():
            report += f"{record['char']}: {record['num']}\n"
    report += "============= END ==============="
    return report


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    try:
        report = build_report(book_path)
        print(report)
    except FileNotFoundError:
        print(f"Error: The file '{book_path}' does not exist.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

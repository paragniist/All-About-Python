import re
from typing import List
import argparse


# Step 2 - Text Search and Extraction

def find_all_digits(text: str) -> List[str]:
    """	Return all sequences of digits in the text."""
    return re.findall(r"\d+", text)


def find_all_words(text: str) -> List[str]:
    """Return a list of all words (alphanumeric + underscore) in the text."""
    return re.findall(r"\w+", text)


def find_all_whitespace(text: str) -> List[str]:
    """Return a list of all whitespace characters in the text."""
    return re.findall(r"\s", text)


def find_capitalized_words(text: str) -> List[str]:
    """Return words that start with a capital letter followed by lowercase letters."""
    return re.findall(r"\b[A-Z][a-z]+\b", text)


def find_five_digit_numbers(text: str) -> List[str]:
    """Return all digit sequences that are exactly 5 digits long."""
    return re.findall(r"\b\d{5}\b", text)


def find_words_starting_with_capital(text: str) -> List[str]:
    """Return all words that begin with a capital letter, regardless of what's after."""
    return re.findall(r"\b[A-Z]\w*\b", text)


def match_lines_starting_with(text: str, prefix: str) -> List[str]:
    """Return lines from the text that start with a given prefix."""
    return [line for line in text.splitlines() if re.match(fr'^{re.escape(prefix)}', line)]


def match_lines_ending_with(text: str, suffix: str) -> List[str]:
    """Return lines from the text that end with a given suffix."""
    return [line for line in text.splitlines() if re.search(fr'{re.escape(suffix)}$', line)]


def replace_vowels_with_astrisks(text: str) -> str:
    """Returns a string where all vowels from the input string have been replaced with an asterisks."""
    return re.sub(r'[aeiouAEIOU]', '*', text)


def double_every_digit(text: str) -> str:
    """Return a new string where all integers have been doubled."""
    return re.sub(r'\d', lambda m: str(int(m.group()) * 2), text)


def split_on_digits(text: str) -> List[str]:
    """Return an array of strings that where each string comes from the original and has been split on digits."""
    return re.split(r'\d', text)


def split_on_a_specific_symbol(text: str) -> List[str]:
    """Return an array of strings that are the original string split on any symbol that matches '-', ':', or '|'."""
    return re.split('[-:|]', text)


def split_on_capital_letters(text: str) -> List[str]:
    """Return a list of strings split before each capital letter."""
    return re.split(r'(?=[A-Z])', text)


# Step 4 - Real Life Examples

def extract_dates(text: str) -> List[str]:
    """
    Extract and return a dictionary with 'month', 'day', and 'year' keys if a date is found.
    """
    pattern = r'\b(0[1-9]|1[0-2])[-/](0[1-9]|[12][0-9]|3[01])[-/](\d{4})\b'
    return re.findall(pattern, text)


def is_valid_email(email: str) -> bool:
    """
    Return True if the input is a valid email address, otherwise False.
    """
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.fullmatch(pattern, email))


def extract_named_date(text: str) -> dict[str, str] | None:
    """
    Extracts a date and returns a dictionary with 'month', 'day', and 'year' keys.
    Return a dictionary that contains month, day, and year with the appropiate values.
    """
    pattern = r"(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{4})"
    match = re.search(pattern, text)
    return match.groupdict() if match else None


def normalize_phone_number(text: str) -> str:
    """
    Normalize phone numbers in the text to the format (XXX) XXX-XXXX.
    Return a new string that replaces provided numbers with the normalized format.
    """
    pattern = r"(\d{3})[-.\s]?(\d{3})[-.\s]?(\d{4})"
    return re.sub(pattern, r"(\1) \2-\3", text)


def is_valid_zip(zipcode: str) -> bool:
    """
    Return True if the input is a valid US ZIP code (5-digit or ZIP+4 format), otherwise False.
    """
    pattern = r"\d{5}(-\d{4})?"
    return bool(re.fullmatch(pattern, zip_code))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run regex functions.")
    parser.add_argument("step", choices=["step2", "step3", "step4"], help="Which step to run")
    parser.add_argument("task", help="Which task to run")
    parser.add_argument("text", help="Text to process")
    parser.add_argument("prefixOrSuffix", nargs="?", help="Prefix or suffix (only needed for some tasks)")

    args = parser.parse_args()

    # Step 2 mappings
    step2_tasks = {
        "task1": find_all_digits,
        "task2": find_all_words,
        "task3": find_all_whitespace,
        "task4": find_capitalized_words,
        "task5": find_five_digit_numbers,
        "task6": find_words_starting_with_capital,
        "task7": match_lines_starting_with,  # Needs prefixOrSuffix
        "task8": match_lines_ending_with  # Needs prefixOrSuffix
    }

    # Step 3 mappings
    step3_tasks = {
        "task1": replace_vowels_with_astrisks,
        "task2": double_every_digit,
        "task3": split_on_digits,
        "task4": split_on_a_specific_symbol,
        "task5": split_on_capital_letters
    }

    # Step 4 mappings
    step4_tasks = {
        "task1": extract_dates,
        "task2": is_valid_email,
        "task3": extract_named_date,
        "task4": normalize_phone_number,
        "task5": is_valid_zip
    }

    # Which step to use
    steps = {
        "step2": step2_tasks,
        "step3": step3_tasks,
        "step4": step4_tasks
    }

    selected_tasks = steps.get(args.step)

    if selected_tasks is None:
        print(f"Invalid step: {args.step}")
    else:
        func = selected_tasks.get(args.task)

        if func is None:
            print(f"Invalid task {args.task} for {args.step}")
        else:
            if args.step == "step2" and args.task in ("task7", "task8"):
                # Special case: match_lines_starting_with or match_lines_ending_with need two arguments
                if args.prefixOrSuffix is None:
                    print(f"Error: 'prefixOrSuffix' argument is required for {args.task}.")
                else:
                    print(func(args.text, args.prefixOrSuffix))
            else:
                print(func(args.text))

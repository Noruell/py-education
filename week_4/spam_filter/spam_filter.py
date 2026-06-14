import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EMAILS_PATH = os.path.join(BASE_DIR, "emails.txt")
CLEAN_PATH = os.path.join(BASE_DIR, "clean.txt")
SPAM_PATH = os.path.join(BASE_DIR, "spam.txt")

spam_words = {"спам", "акция", "бесплатно", "выигрыш", "выиграли"}

def is_spam(line):
    for word in spam_words:
        if word in line:
            return True
    return False


def filter_emails():
    clean = []
    spam = []
    
    with open(EMAILS_PATH, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip().lower()
            if line:
                if is_spam(line):
                    spam.append(line)
                else:
                    clean.append(line)
    return clean, spam

def save_emails(filename, emails):
    with open(filename, "w", encoding="utf-8") as file:
        for email in emails:
            file.write(f"{email}\n")


def main():
    print("=== СПАМ-ФИЛЬТР ===")

    clean, spam = filter_emails()

    save_emails(CLEAN_PATH, clean)
    save_emails(SPAM_PATH, spam)

    total = len(clean) + len(spam)
    print(f"Обработано писем: {total}")
    print(f"Спам: {len(spam)}")
    print(f"Чистых: {len(clean)}")
    print(f"\nЧистые письма сохранены в 'clean.txt'")
    print(f"Спам сохранёе в 'spam.txt'")

if __name__ == "__main__":
    main()

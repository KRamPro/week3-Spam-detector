"""Create a small example dataset for the spam detector."""

import random
import re
from pathlib import Path

import pandas as pd


# The assignment's template was not provided, so these examples are substitutes.
# Each tuple contains the label (1 = spam, 0 = legitimate) and an email.
EMAILS = [
    (1, "WIN a free prize! Claim your cash now at https://prize.example!"),
    (1, "URGENT! Earn money fast! Visit https://offer.example for your reward!"),
    (1, "FREE credit offer! Apply now at https://credit.example!"),
    (1, "You won a cash prize! Click https://winner.example today!"),
    (1, "Limited offer! Get free money at https://deal.example!"),
    (1, "ACT NOW! Win a prize! Go to https://win.example!"),
    (1, "Earn cash from home! Sign up at https://earn.example!"),
    (1, "Your FREE reward is waiting! Claim it at https://gift.example!"),
    (1, "Congratulations! You have won free tickets at https://tickets.example!"),
    (1, "Confirm your account details to receive your cash reward."),
    (1, "Final notice: earn a bonus today at https://bonus.example!"),
    (1, "You've been selected for a prize. Reply now to collect it!"),
    (1, "Special credit offer available at https://loan.example today!"),
    (1, "FREE vacation waiting for you! Visit https://travel.example!"),
    (1, "Make extra money from home by signing up today!"),
    (1, "WIN a new phone! Claim your reward at https://phone.example!"),
    (0, "Hi, can we meet on Tuesday to discuss the project?"),
    (0, "The meeting notes are ready. Please review them before Friday."),
    (0, "Thanks for helping with the presentation yesterday."),
    (0, "Your appointment is scheduled for Monday at ten."),
    (0, "Could you send me the updated report when you have time?"),
    (0, "Dinner is at six tonight. See you there!"),
    (0, "Here is the class schedule: https://school.example/schedule"),
    (0, "Please let me know if you can cover my shift tomorrow."),
    (0, "The library books are due next week. Can you return them?"),
    (0, "Your order has shipped and should arrive on Wednesday."),
    (0, "Here is the link to our shared project: https://class.example/project"),
    (0, "Thank you for your application. We would like to schedule an interview."),
    (0, "Could you bring the notes to class tomorrow?"),
    (0, "The office will be closed on Monday for the holiday."),
    (0, "Happy birthday! I hope you have a wonderful day!"),
    (0, "Your credit card statement is available in your account."),
]


def email_features(text):
    """Turn an email into the six numbers used by the classifier."""
    words = re.findall(r"[A-Za-z]+", text)
    money_words = ["cash", "credit", "earn", "free", "money", "offer", "prize", "win", "won"]

    money_count = 0
    caps_count = 0
    for word in words:
        if word.lower() in money_words:
            money_count += 1
        if len(word) > 1 and word.isupper():
            caps_count += 1

    return {
        "word_count": len(words),
        "exclamations": text.count("!"),
        "money_words": money_count,
        "all_caps": caps_count,
        "links": len(re.findall(r"https?://", text)),
        "questions": text.count("?"),
    }


def main():
    random.seed(42)
    rows = []

    # Keep the original and make nine small numerical variations of each email.
    for original_id, (label, text) in enumerate(EMAILS, start=1):
        original_features = email_features(text)
        for variation in range(10):
            features = original_features.copy()
            if variation > 0:
                for name in features:
                    features[name] = max(0, features[name] + random.choice([-1, 0, 1]))
            row = {"original_id": original_id, "variation": variation,
                   "label": label, "original_text": text}
            row.update(features)
            rows.append(row)

    data_dir = Path(__file__).resolve().parent / "data"
    data_dir.mkdir(exist_ok=True)
    data_file = data_dir / "emails.csv"
    pd.DataFrame(rows).to_csv(data_file, index=False)
    print(f"Saved {len(rows)} rows from {len(EMAILS)} original emails to {data_file}")
    print("Variation rows contain adjusted numbers, not rewritten email text.")


if __name__ == "__main__":
    main()

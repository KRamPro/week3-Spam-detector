# Spam detector analysis

## Data and features

The assignment referred to a template that wasn't provided, so we used 32 invented emails: 16 spam and 16 legitimate. That's twice the 16 originals requested. The script keeps each original and makes nine variations by randomly adjusting its feature values. These are variations of the numbers, not rewritten emails, so the values don't always match the original text.

The four original features are word count, exclamation marks, money-related words, and all-caps words. We added two more:

- **Links:** Spam may direct a reader to a website, although legitimate emails can contain links too.
- **Question marks:** Questions might be more common in ordinary conversations, though spam can ask them too.

The model uses these six numbers; it doesn't read the email text.

## Training and results

We split the rows into training and test sets so we could check the model against rows it hadn't trained on. As the leakage check below shows, though, many of those test rows are closely related to the training rows.

The logistic regression model scored **0.85 accuracy** on 80 test rows:

| Actual | Predicted legitimate | Predicted spam |
|---|---:|---:|
| Legitimate | 38 | 2 |
| Spam | 10 | 30 |

Precision was **0.9375**: 30 of the 32 rows marked as spam were spam. Recall was **0.75**: the filter caught 30 of the 40 spam rows.

## Which mistake matters more?

A legitimate email sent to spam could be a job offer or another important message. That makes a false positive more serious here than an unwanted email reaching the inbox. Raising the probability threshold for marking a message as spam could reduce false positives, but it could also let more spam through. We'd need better data to test that tradeoff.

## Feature weights

The model standardized the features before training so their weights could be compared on a common scale. `money_words` had the largest absolute weight, followed by `exclamations`. That makes sense for these examples: many of the invented spam emails contain money-related words, so the way we built the dataset shaped what the model learned.

## Attempts to fool the filter

1. A phishing-style message asking for a bank password was labeled legitimate. It fooled the filter.
2. A legitimate class announcement offering free pizza and a prize was labeled spam. It fooled the filter.
3. A legitimate urgent question about a credit report was labeled spam. It also fooled the filter.

The labels describe the intended context. The first message, for example, is meant to be a malicious request even though it sounds polite.

## Data leakage and limitations

Variations of all 32 original emails appeared in both the training and test sets. The test rows were close relatives of messages the model had already seen, so I wouldn't trust the 0.85 accuracy as a prediction for new mail.

The emails are invented and much less varied than real messages. The random changes can also produce feature values that don't match the stored text. To test a real filter, we'd need more varied labeled emails, a test set separated by original message, and a careful look at both types of error.

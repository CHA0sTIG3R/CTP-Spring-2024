from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

article = """ New York (CNN)When Liana Barrientos was 23 years old, she got married in Westchester County, New York.
A year later, she got married in Westchester County, New York, but to a different man and without divorcing her first husband.
Only 18 days after that marriage, she got hitched again. Then, Barrientos declared "I do" five more times, sometimes only within two weeks of each other.
In 2010, she married once more, this time in the Bronx. In an application for a marriage license, she stated it was her "first and only" marriage.
Barrientos, now 39, is facing two criminal counts of "offering a false instrument for filing in the first degree," referring to her false statements on the
2010 marriage license application, according to court documents.
"""

print(summarizer(article, max_length=130, min_length=30, do_sample=False))
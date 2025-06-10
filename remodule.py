import re

pattern = r"[A-Z]eries"
story = (
    "The second season of the series was scheduled to be released on 20 May 2022. "
    "However, all the episodes were released two days before the actual release date. "
    "In this season, Abhishek is seen taking more interest in village politics and developments alongside preparing for CAT exam. "
    "and and And And"
)

matches = re.finditer(pattern, story)

for match in matches:
    print("Span:", match.span())       
    print("Matched Text:", match.group())  

# src/parsers/regex_patterns.py
import re

#Defining the possible tags which is any letter(upper or lowercase), numbers from 0 to 9 and other symbols
Tags = re.compile(r'@([A-Za-z0-9_-]+)')

#Defining priority which could be #high, #medium or #low
Priority = re.compile(r'#(high|medium|low)\b', re.IGNORECASE)

# due date like due:2025-10-20 or due:tomorrow or due:next week
Due = re.compile(r'due:([0-9]{4}-[0-9]{2}-[0-9]{2}|tomorrow|next week)', re.IGNORECASE)

# assigned:email@example.com
Assigned = re.compile(r'assigned:([A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,})', re.IGNORECASE)

# time: at 3pm or by 5:30 PM
Time = re.compile(r'\b(?:at|by)\s+(\d{1,2}(?::\d{2})?\s*(?:am|pm)?)', re.IGNORECASE)

# duration e.g. 1h, 30m
Duration = re.compile(r'(\d+\s*h|\d+\s*m)\b', re.IGNORECASE)

# generic keyword pattern for search (user supplied)
Keyword = re.compile

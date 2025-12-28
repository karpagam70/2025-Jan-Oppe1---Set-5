'''
Key Stroke Analysis
Given a list of tuples representing key press events in the format (key, press_time, release_time), where press_time and release_time are in milliseconds, implement the following functions.

average_hold_time(data: list, key: str) -> float: Computes the average duration a specific key is held before release.
average_transition_time(data: list, key1: str, key2: str) -> float: Computes the average time taken to transition between two specific keys.
get_typed_text(data: list) -> string - Computes the final text considering the character keys and backspaces typed.
words_per_minute(data: list) -> float: Computes the words per minute based on the total time taken for the key press events. Words can be separated by varying number or spaces. The total time is the duration between the first key press and the last key release.
The keys will one of be A to Z, SPACE and BACKSPACE.

Assume the key presses are sorted in the order in which they are typed and there is no overlap in key timings, that is only one key is pressed at a time.

NOTE: This is a function-type question. You don't have to take input or print the output, just have to complete the required function definitions. You can define helper functions if needed, but the actual solution should be in the given function template.

Example

data = [
    ('A', 500, 800),
    ('B', 1300, 1600),
    ('A', 2300, 2600),
    ('B', 3500, 3600),
    ('SPACE', 3700, 3800),
    ('SPACE', 3900, 4100),
    ('A', 4700, 4800),
    ('B', 5700, 5800),
    ('BACKSPACE', 6600, 6700),
    ('SPACE', 7600, 7900),
    ('BACKSPACE', 8300, 8500),
    ('A', 8700, 9000),
    ('B', 9200, 9400),
    ('SPACE', 10300, 10500),
    ('A', 10900, 11000),
    ('B', 11900, 12200),
]

>>> average_hold_time(data, 'A')
220.0 # ((800-500) + (2600-2300) + (4800-4700) + (9000-8700) + (11000-10900)) / 5
>>> average_transition_time(data, 'A', 'B')
680.0 # ((1300 - 800) + (3500-2600) + (5700-4800) + (9200-9000) + (11900-11000)) /5
>>> get_typed_text(data)
"ABAB  AAB AB" # ABAB  A[B][ ]AB AB , text within [] is remove by backspace
>>> round(words_per_minute(data)) # total words 3, duration = 12200 - 500 = 11700
15 # 3/11700*60*1000
>>> round(words_per_minute(data[len(data)//2:])) # total words 2, duration = 12200 - 6600  = 5600
21 # 2/5600*60*1000
Explanation on typed text

S.no	Current key	Typed text
0	A	'A'
1	B	'AB'
2	A	'ABA'
3	B	'ABAB'
4	SPACE	'ABAB '
5	SPACE	'ABAB '
6	A	'ABAB A'
7	B	'ABAB AB'
8	BACKSPACE	'ABAB A'
9	SPACE	'ABAB A '
10	BACKSPACE	'ABAB A'
11	A	'ABAB AA'
12	B	'ABAB AAB'
13	SPACE	'ABAB AAB '
14	A	'ABAB AAB A'
15	B	'ABAB AAB AB'
Explanation for word per minute

word_per_minute(data)
Total text typed is 'ABAB AAB AB'
Number of words is 3
Total time taken = release time of last key - press time of first key = 12200 - 500 = 11700 ms
words per minute = 3/11700 * 1000 * 60 (words/minute) = 15.38 ~= 15
word_per_minute(data[len(data)//2:]) = word_per_minute(data[8:])
Total text typed is the second half 'AB AB'
Number of words is 2
Total time taken = release time of last key - press time of first key = 12200 - 6600 = 5600 ms
words per minute = 2/5600 * 1000 * 60 (words/minute) = 21.42 ~= 21
'''

grade_to_score = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}

total_credit = 0.0
total_score = 0.0
import sys

input = sys.stdin.read
lines = input().strip().split("\n")

for line in lines:
    parts = line.split()
    credit = float(parts[1])
    grade = parts[2]

    if grade != "P":
        score = grade_to_score[grade]
        total_score += credit * score
        total_credit += credit

gpa = total_score / total_credit if total_credit != 0 else 0.0

print(f"{gpa:.6f}")

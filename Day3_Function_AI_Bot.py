# Day 3: AI Study Bot by Unzila
# What it does: Tracks Python learning progress
# Date: 5 May 2026

def ai_study_bot(name, completed_days):
    print(f"Hello {name}! Main tumhara AI Study Bot hun")
    print(f"Tumne ab tak {len(completed_days)} din complete kiye hain:")
    for day in completed_days:
        print(f"- {day}")
    if len(completed_days) >= 3:
        print("Shabaash! Tum ready ho agle level ke liye 🚀")

my_days = ["Day 0", "Day 1", "Day 2", "Day 3"]
ai_study_bot("Unzila", my_days)

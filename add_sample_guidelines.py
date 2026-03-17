from db.database import SessionLocal, engine, Base
from models.guideline_model import Guideline
import models

# Ensure tables are created
Base.metadata.create_all(bind=engine)

db = SessionLocal()

sample_data = [
    {
        "month": 1,
        "healthy_eating": "Start prenatal vitamins\nEat folate-rich foods like spinach and beans\nAvoid raw meat and unpasteurized dairy",
        "exercise_meditation": "Light walking for 15-20 minutes daily\nGentle stretching\nPractice deep breathing exercises",
        "daily_habits": "Drink at least 8-10 glasses of water\nEnsure 8 hours of sleep\nSchedule your first prenatal visit",
        "mental_wellbeing": "Journal your thoughts and feelings about pregnancy\nTalk to your partner or a friend\nRest when you feel tired"
    },
    {
        "month": 2,
        "healthy_eating": "Eat small frequent meals to manage nausea\nInclude ginger and lemon to settle stomach\nFocus on calcium-rich foods",
        "exercise_meditation": "Continue light walking\nTry prenatal yoga (gentle poses only)\nListen to calming music",
        "daily_habits": "Wear comfortable, loose clothing\nWash hands frequently to avoid infections\nLimit caffeine intake",
        "mental_wellbeing": "Acknowledge mood swings are normal\nPractice positive affirmations\nConnect with other expectant mothers"
    }
]

# Auto-generate for remaining months
for idx in range(3, 11):
    sample_data.append({
        "month": idx,
        "healthy_eating": f"Month {idx} Nutrition: Focus on lean proteins, iron-rich foods, and complex carbohydrates.\nContinue taking prenatal vitamins.",
        "exercise_meditation": f"Month {idx} Exercise: Maintain regular light workouts, such as swimming or walking.\nPractice daily relaxation times.",
        "daily_habits": f"Month {idx} Habits: Stay well hydrated.\nPrepare baby essentials and rest whenever possible.",
        "mental_wellbeing": f"Month {idx} Wellbeing: Read up on childbirth and newborn care to alleviate anxiety.\nCommunicate openly with your partner."
    })

print("Adding sample guidelines...")
added_count = 0
for data in sample_data:
    existing = db.query(Guideline).filter(Guideline.month == data["month"]).first()
    if not existing:
        db.add(Guideline(**data))
        added_count += 1

db.commit()
print(f"Sample guidelines added successfully! Inserted {added_count} new records.")
db.close()

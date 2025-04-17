# fortune.py (v1.1)
import random

print("🔮 Welcome to Yash Choudhary's Fortune Teller (21JE1066) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral/stressed): ")

fortunes = {
    "happy": [
        "✨ Great things await you, Yash! Keep smiling. ✨",
        "🌞 Your happiness will spread to others today!"
    ],
    "sad": [
        "💧 Storms don’t last forever. Better days are ahead.",
        "💙 A kind surprise is coming your way."
    ],
    "neutral": [
        "🌀 Stay curious — surprises are on the horizon.",
        "📚 A new idea will spark something big."
    ],
    "stressed": [
        "🧘‍♂️ Take a deep breath. Peace is just around the corner.",
        "🌿 Calmness will come through nature and rest."
    ]
}

if mood.lower() in fortunes:
    print("Your fortune:", random.choice(fortunes[mood.lower()]))
else:
    print("Hmm... that's a mood I don't recognize. Try again later!")

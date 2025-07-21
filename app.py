from backend.tools import reflect_emotions, gita_verse_for_emotion
from db.journal_db import insert_journal

if __name__ == "__main__":
    print("Welcome to SilentSky 🌌")
    user_id = input("Enter your user ID: ")
    while True:
        print("\n1. Write Journal\n2. Get Reflection\n3. Get Gita Verse\n4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            entry = input("\nWhat happened today? ")
            emotion = input("How did you feel (e.g., anxious, happy, confused)? ")
            insert_journal(user_id, entry, emotion)
            print("✔️ Journal saved!")

        elif choice == "2":
            print("\n🤖 Reflection:")
            print(reflect_emotions(user_id))

        elif choice == "3":
            emo = input("\nEnter your current emotion: ")
            print("🕉️ Gita Verse:")
            print(gita_verse_for_emotion(emo))

        elif choice == "4":
            print("Good night 🌙")
            break
        else:
            print("Invalid choice.")

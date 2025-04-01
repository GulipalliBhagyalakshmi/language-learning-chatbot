# db_manager.py

import sqlite3

# 🔥 Initialize the SQLite database
def initialize_db():
    """Create a SQLite database with a table for storing chatbot interactions."""
    connection = sqlite3.connect("chatbot.db")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS conversation (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_input TEXT,
        bot_response TEXT,
        mistake INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    connection.commit()
    connection.close()


# 🔥 Store conversation data in the SQLite database
def store_response(user_input, bot_response, mistake):
    """Store chatbot interactions in the database."""
    connection = sqlite3.connect("chatbot.db")
    cursor = connection.cursor()

    cursor.execute('''
    INSERT INTO conversation (user_input, bot_response, mistake)
    VALUES (?, ?, ?)
    ''', (user_input, bot_response, mistake))

    connection.commit()
    connection.close()


# 🔥 Display chat history
def display_chat_history():
    """Retrieve and display conversation history from the database."""
    connection = sqlite3.connect("chatbot.db")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM conversation')
    rows = cursor.fetchall()

    connection.close()

    if rows:
        print("\n✅ Chat history:")
        for row in rows:
            print(f"👉 User: {row[1]}")
            print(f"🤖 Bot: {row[2]}")
            print(f"❗ Mistake: {'Yes' if row[3] else 'No'}")
            print(f"📅 Timestamp: {row[4]}")
            print("-" * 50)
    else:
        print("\n❗ No chat history found.")


# 🔥 Generate a final review summary
def display_final_review(mistake_count, mistake_log):
    """Display the final review and summary of mistakes."""
    print("\n📊 🔥 Final Review:")
    print(f"❗ You made {mistake_count} mistake(s) during the conversation.\n")

    if mistake_log:
        print("🔎 **Common Mistake Patterns:**")
        mistake_patterns = {}
        
        for mistake in mistake_log:
            if mistake in mistake_patterns:
                mistake_patterns[mistake] += 1
            else:
                mistake_patterns[mistake] = 1
        
        for pattern, count in mistake_patterns.items():
            print(f"- {pattern} (Occurred {count} time{'s' if count > 1 else ''})")

    # Suggestions for Improvement
    print("\n💡 **Suggestions for Improvement:**")
    if mistake_count > 0:
        print("- Focus on grammar rules, especially tense and sentence structure.")
    else:
        print("- Great job! Keep practicing to maintain accuracy.")
    
    print("\n🔥 Keep practicing to improve! 💪")

# 🔥 Generate a final review summary


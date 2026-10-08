from transformers import pipeline


# ============================================
# LOAD THE AI MODEL
# ============================================

print("Loading AI model...")
print("The first run may take a little while.\n")

generator = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct"
)

print("================================")
print("       MY LOCAL AI CHATBOT")
print("================================")
print("Type 'quit' to exit.\n")


# ============================================
# CHAT LOOP
# ============================================

while True:

    user_message = input("You: ")

    # Exit command
    if user_message.lower() == "quit":
        print("\nGoodbye!")
        break

    # Build conversation
    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful, friendly AI assistant. "
                "Give clear and concise answers."
            )
        },
        {
            "role": "user",
            "content": user_message
        }
    ]

    # Generate response
    response = generator(
        messages,
        max_new_tokens=150,
        do_sample=True,
        temperature=0.7
    )

    # Extract assistant's response
    assistant_message = response[0]["generated_text"][-1]["content"]

    print(f"\nBot: {assistant_message}\n")
# INITIALIZE OPENAI API CONNECTION FOR QUIZE GENERATION
# =============================================================================
#   API SETUP & CONFIGURATION
# Responsibility: Connect the program to OpenAI API
# =============================================================================


from openai import OpenAI

# Initialize the OpenAI client with your API key
# Replace "your_api_key_here" with your real API key
# This creates the connection to OpenAI servers
client = OpenAI(api_key="your_api_key_here")



# =============================================================================
#   QUIZ GENERATION LOGIC (AI INTERACTION)
# Responsibility: Send user input to AI and process response
# =============================================================================

# Function to generate a quiz using AI
# Takes a prompt (topic or paragraph) as input
def generate_quiz(prompt):
    try:
        # Send request to OpenAI API
        # This is where AI generates the quiz
        response = client.chat.completions.create(
            
            # Use a fast and cost-effective model
            model="gpt-4o-mini",
            
            # Define conversation messages
            messages=[
                # System message: tells AI its role
                {"role": "system", "content": "You are a helpful quiz generator."},
                
                # User message: sends the actual input
                {"role": "user", "content": prompt}
            ],
            
            # Controls creativity level
            temperature=0.7
        )

        # Extract the generated quiz from the response
        quiz = response.choices[0].message.content
        
        # Return the quiz result
        return quiz

    # Handle possible errors (e.g., no internet, wrong API key)
    except Exception as e:
        return f"❌ Error generating quiz: {str(e)}"



# =============================================================================
#   USER INTERFACE & PROGRAM EXECUTION
# Responsibility: Handle user input and display output
# =============================================================================

# Main program starts here
# Ensures the code runs only when this file is executed directly
if __name__ == "__main__":
    
    # Prompt user to enter a topic or paragraph
    user_input = input("Enter a topic or paragraph: ")
    
    # Call the quiz generation function
    result = generate_quiz(user_input)
    
    # Display the generated quiz
    print("\nGenerated Quiz:\n")
    print(result)

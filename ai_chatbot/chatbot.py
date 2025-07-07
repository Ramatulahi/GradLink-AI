def chatbot_response(user_input):
    user_input = user_input.lower()
    if "improve my gpa" in user_input:
        return "You can improve your GPA by attending tutorials, studying past questions, and managing your time better."
    elif "internship" in user_input:
        return "You can find internships on Jobberman, LinkedIn, and through your department's notice board."
    elif "career path" in user_input:
        return "I recommend you check the Career Roadmap feature to find paths based on your course."
    else:
        return "Sorry, I don't understand that yet. Please try another question."

# Example usage
print(chatbot_response("How do I improve my GPA?"))
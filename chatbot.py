def chatbot_response(user_input):

    user_input = user_input.lower()

    if "cold" in user_input:
        return "Hunza, Skardu and Swat are best cold destinations."

    elif "cheap" in user_input:
        return "Murree is affordable and budget friendly."

    elif "adventure" in user_input:
        return "Skardu and Naran are great for adventure trips."

    elif "family" in user_input:
        return "Swat and Hunza are perfect for family trips."

    elif "historical" in user_input:
        return "Lahore is best for historical tourism."

    elif "summer" in user_input:
        return "Hunza and Naran are excellent in summer."

    elif "winter" in user_input:
        return "Murree is beautiful during winter snowfall."

    elif "shopping" in user_input:
        return "Murree and Lahore are good for shopping."

    else:
        return "Please ask about weather, budget, family trips, adventure or tourist places."
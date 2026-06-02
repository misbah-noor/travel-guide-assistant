def chatbot_response(user_input):

    user_input = user_input.lower()

    # Weather-based recommendations
    if "cold" in user_input:
        return "Hunza, Skardu, Swat and Fairy Meadows are excellent for cold destinations."

    elif "hot" in user_input:
        return "Karachi, Gwadar and Multan are known for warm and hot weather."

    elif "rain" in user_input or "rainy" in user_input:
        return "Murree, Kaghan Valley and Neelum Valley are beautiful during rainy weather."

    elif "summer" in user_input:
        return "Hunza, Naran, Skardu and Swat are ideal summer destinations."

    elif "winter" in user_input:
        return "Murree, Malam Jabba and Skardu offer amazing winter snowfall experiences."

    # Budget-based recommendations
    elif "cheap" in user_input :
        return " Patriata and Taxila are affordable tourist destinations."

    elif  "budget-friendly" in user_input or "budget" in user_input:
        return "Murree,Naran and Kaghan are budget-Friendly places"

    elif "luxury" in user_input:
        return "Hunza, Skardu and Bhurban offer luxury tourism experiences."

    # Trip type recommendations
    elif "adventure" in user_input:
        return "Skardu, Naran, Fairy Meadows and Chitral are great for adventure trips."

    elif "family" in user_input:
        return "Swat, Hunza, Murree and Naran are perfect for family vacations."

    elif "honeymoon" in user_input:
        return "Hunza, Murree and Neelum Valley are popular honeymoon destinations."

    elif "friends" in user_input:
        return "Skardu, Naran and Fairy Meadows are great places to visit with friends."

    # Tourism categories
    elif "historical" in user_input:
        return "Lahore, Taxila and Mohenjo-Daro are famous historical destinations."

    elif "shopping" in user_input:
        return "Lahore, Karachi and Murree are excellent for shopping."

    elif "nature" in user_input:
        return "Neelum Valley, Swat, Hunza and Naran offer beautiful natural scenery."

    elif "mountain" in user_input:
        return "Hunza, Skardu, Naran and Fairy Meadows are famous mountain destinations."

    elif "lake" in user_input:
        return "Saif-ul-Malook, Attabad Lake and Shangrila Lake are must-visit lakes."

    elif "beach" in user_input:
        return "Clifton Beach, Hawksbay Beach and Gwadar Beach are popular coastal attractions."

    # Tourist places
    elif "hunza" in user_input:
        return "Hunza is famous for Attabad Lake, Altit Fort, Baltit Fort and breathtaking mountain views."

    elif "skardu" in user_input:
        return "Skardu is known for Shangrila Resort, Deosai Plains, Satpara Lake and K2 expeditions."

    elif "murree" in user_input:
        return "Murree offers Mall Road, Patriata Chair Lift and beautiful hill station views."

    elif "lahore" in user_input:
        return "Lahore is famous for Badshahi Mosque, Lahore Fort, Minar-e-Pakistan and Food Street."
    elif "best places" in user_input  or "top-rated travel places" in user_input:
        return "Hunza, Skardu , Murree , Fairy Meadows and Nathia Gali are all top-rated travel destinations but a little bit expensive"

    else:
        return ("Please ask about weather, budget, family trips, adventure, "
                "historical places, mountains, lakes, beaches or top-rated travel destinations.")
# 1. Import random Module
import random 

# 2. List for Subjects
subjects = [
    "Zaid",
    "Group of Students",
    "Elon Musk riding a Dogecoin",
    "ChatGPT (AI Assistant)",
    "MrBeast with a Backpack of Cash",
    "Mark Zuckerberg's Hologram",
    "Nvidia CEO Jensen Huang in Leather Jacket",
    "Hacker named Rose 🌹",
    "YouTube Algorithm",
    "Anonymous Coder from Reddit",
    "A Talking Robot",
    "The CEO of Mars",
    "An AI Cat Influencer",
    "Indian Prime Minister Narendra Modi on Hoverboard",
    "Group of Sleep-Deprived Coders",
    "Time-Traveling Banana 🍌",
    "Bill Gates Playing Minecraft",
    "Alien from Bihar 😂"
]


# 3. List of Actions 
actions = [
    "Discovered Secret of Immortality in Code",
    "Launched a Flying Laptop",
    "Banned All Mondays Forever",
    "Declared Free Wi-Fi for Entire Galaxy",
    "Increased Everyone's Salary to ₹10 Crore",
    "Fired Google Maps for Getting Lost",
    "Gave $100K Bonus to Everyone Wearing Crocs",
    "Started Hiring Memers as Engineers",
    "Started Selling Air in Bottles",
    "Took Loan from Aliens",
    "Accidentally Deleted the Internet",
    "Started Coding on a Coconut",
    "Created AI that Can Cry",
    "Launched a Tech Company on the Moon",
    "Turned Coffee into Electricity ☕⚡",
    "Installed Windows on a Toaster",
    "Built a Robot that Only Dances",
    "Offered Free Pizza to All Coders"
]

# 4. List of Places and Things
places_or_things = [
    "Near a UFO Landing Site",
    "From an Alternate Dimension",
    "Inside a Crypto Mine",
    "Under the White House",
    "In Metaverse PubG Server",
    "On Mars Highway 🚀",
    "Inside a Potato Farm",
    "in Hogwarts Lab",
    "in a 404 Not Found Zone",
    "Inside a Minecraft Server",
    "In Zoom Call with Aliens",
    "On a Cloud Made of Data",
    "Using 5G-powered Chapati Maker",
    "In Deep Ocean Datacenter",
    "from Parallel Universe Zaid-2.0",
    "During a TikTok Live",
    "On the Back of a Turtle",
    "in Area 51's Server Room"
]


# Welcome Message 
print("Welcome to Fake News Headline Generator | It's Just for Entertenment Purpose")

# 5. Use random.choice() to Pick Random Words and While Loop for Repetation
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    fake_Headline = f"TODAY's BREAKING NEWS IS : {subject} {action} {place_or_thing}"
    print(fake_Headline)

    user = input("Do You Want Another Headline (yes/no): ").strip().lower()
    if user == "no":
        break

print("\nThanks for Use FNHG 💕")

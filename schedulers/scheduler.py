import openai, re

def parse_schedule(schedule):
    event_list = []

    pattern = re.compile(r'<\[([^@]*?)\s@([^f]*?)f/\s(\d+)\s-\s(\d+)\svia\s([^\]]*)\]>')

    for match in pattern.findall(schedule):
        event_list.append({
            'Activity': match[0].strip(),
            'Place': match[1].strip(),
            'Start time': match[2].strip(),
            'End time': match[3].strip(),
            'Transportation': match[4].strip(),
        })

    return event_list

def scheduler(person):
    textQuery = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=[
            {"role" : "system", "content" : "Follow all instructions."},
            {"role" : "system", "content" : "These are the buildings that you have available. You can not deviate from these. {'', 'greenhouse', 'terrace', 'university', 'yes', 'hotel', 'garage', 'warehouse', 'house', 'supermarket', 'public', 'kindergarten', 'industrial', 'college', 'roof', 'carport', 'static_railcar', 'bridge', 'dormitory', 'shed', 'residential', 'parking', 'train_station', 'grandstand', 'civic', 'retail', 'church', 'garages', 'temple', 'boathouse', 'detached', 'government', 'fire_station', 'construction', 'commercial', 'semidetached_house', 'hospital', 'sports_centre', 'kiosk', 'toilets', 'sports_hall', 'water_works', 'no', 'office', 'apartments', 'canopy', 'service', 'school'}"},
            {"role" : "system", "content" : """
            Describe what this person's schedule might look like.
            It should be based on events. 
            You must follow this format for each event <[event_name] @ [event_location] f/ [startTime] - [endTime] via [transportation]> for it to be parsed correctly. 
            You can add multiple events with a new line.
            Format starts and ends in military time without colons.
            IE: 7:20 AM is 720, and 2:00 PM is 1400 Be incredibly descriptive. Do not add anything not encapsulated in <>.

            Example:
            <[Wake up and freshen up, starting the day with a refreshing shower and grooming @ house f/ 530 - 600 via Walk]>
            <[Stretching and warm-up exercises before the jog, to prepare the body for the workout @ terrace f/ 600 - 610 via Walk]>
            <[Morning jog for exercise on the terrace, following doctor's advice to improve heart health @ terrace f/ 610 - 700 via Walk]>
            <[Cool down and relaxation exercises after the jog, to bring the heart rate back to normal @ terrace f/ 700 - 710 via Walk]>
            <[Morning Prayers at home in the prayer room, a daily ritual for inner peace and reflection @ house f/ 710 - 730 via Walk]>
            <[Reading the morning newspaper, staying updated with the world @ house f/ 730 - 740 via Walk]>
            <[Preparing breakfast in the kitchen, cooking a healthy and delicious meal @ house f/ 740 - 750 via Walk]>
            <[Breakfast at home in the dining room, a hearty meal of eggs, toast, and coffee to start the day right @ house f/ 750 - 810 via Walk]>
            <[Cleaning up after breakfast, maintaining a clean and tidy kitchen @ house f/ 810 - 820 via Walk]>
            <[Getting ready for work, dressing up in professional attire @ house f/ 820 - 830 via Walk]>
            <[Drive to Work in the city, the daily commute in the car to the bustling office @ commercial f/ 830 - 900 via Car]>
            <[Work at office in the personal cabin, a productive day of meetings, calls, and emails in the corporate world @ commercial f/ 900 - 1030 via Walk]>
            <[Coffee break at the office, a quick caffeine boost to keep the energy levels up @ commercial f/ 1030 - 1040 via Walk]>
            <[Team meeting at the office, discussing projects and strategies @ commercial f/ 1040 - 1130 via Walk]>
            <[Work at office, continuing the productive day @ commercial f/ 1130 - 1300 via Walk]>
            <[Lunchtime at the local Italian restaurant, a quick and tasty bite of pasta and salad @ retail f/ 1300 - 1400 via Walk]>
            <[Work at the office in the personal cabin, the afternoon hustle of reports, presentations, and client interactions @ commercial f/ 1400 - 1530 via Walk]>
            <[Afternoon coffee break at the office, another round of caffeine to maintain productivity @ commercial f/ 1530 - 1540 via Walk]>
            <[Work at the office, wrapping up the day's tasks @ commercial f/ 1540 - 1800 via Walk]>
            <[Drive Home in the car, the return journey through the city to the cozy haven @ house f/ 1800 - 1830 via Car]>
            <[Evening Prayers at home in the prayer room, a serene moment of spirituality and gratitude @ house f/ 1830 - 1900 via Walk]>
            <[Evening snack at home, a light and healthy snack to keep the hunger at bay @ house f/ 1900 - 1930 via Walk]>
            <[Dinner at home in the dining room, a delightful family mealtime with homemade dishes @ house f/ 1930 - 2030 via Walk]>
            <[Cleaning up after dinner, washing dishes and tidying up the dining area @ house f/ 2030 - 2040 via Walk]>
            <[Family time at home in the living room, bonding and making memories over board games and conversations @ house f/ 2040 - 2200 via Walk]>
            <[Reading time at home, indulging in a good book for personal growth @ house f/ 2200 - 2230 via Walk]>
            <[Night Prayers at home in the prayer room, a peaceful evening ritual for a good night's sleep @ house f/ 2230 - 2300 via Walk]>
            <[Night skincare routine at home, taking care of skin before bed @ house f/ 2300 - 2330 via Walk]>
            <[Meditation before sleep, calming the mind for a peaceful sleep @ house f/ 2330 - 2400 via Walk]>
            <[Bedtime at home in the bedroom, a well-deserved rest after a long day, reading a book before sleep @ house f/ 2400 - 530 via Walk]>
            """},
            {"role": "user", "content": str(person) + "Make sure you factor in the demographic of the person; make their activities fit who they are. For example, if someone lives in a small town they might have a long drive, if they are unhealthy they might eat 4 meals, etc."}
        ],
    )
    
    data = textQuery["choices"][0]["message"]["content"]
    return parse_schedule(data)

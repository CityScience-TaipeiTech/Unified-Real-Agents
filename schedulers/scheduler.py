import openai, re

def parse_schedule(schedule):
    event_list = []

    pattern = re.compile(r'<\[([^@]*?)\s@([^f]*?)f/\s(\d+)\s-\s(\d+)\svia\s([^\]]*)\]>')

    for match in pattern.findall(schedule):
        event_list.append({
            'Activity': match[0].strip(),
            'Address': match[1].strip(),
            'Time': match[2].strip(),
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
            <[Morning jog for exercise, as the doctor said they had to improve their heart health @ terrace f/ 600 - 700 via Walk]>
            <[Morning Prayers at home, a daily ritual for inner peace and reflection @ house f/ 710 - 730 via Walk]>
            <[Breakfast at home, a hearty meal to start the day right @ house f/ 740 - 810 via Walk]>
            <[Drive to Work, the daily commute to the bustling office @ commercial f/ 830 - 900 via Car]>
            <[Work at office, a productive day in the corporate world @ commercial f/ 900 - 1300 via Walk]>
            <[Lunchtime at the local restaurant, a quick and tasty bite @ retail f/ 1300 - 1400 via Walk]>
            <[Work at the office, the afternoon hustle @ commercial f/ 1400 - 1800 via Walk]>
            <[Drive Home, the return journey to the cozy haven @ house f/ 1800 - 1830 via Car]>
            <[Evening Prayers at home, a serene moment of spirituality @ house f/ 1830 - 1900 via Walk]>
            <[Dinner at home, a delightful family mealtime @ house f/ 1930 - 2030 via Walk]>
            <[Family time at home, bonding and making memories @ house f/ 2040 - 2200 via Walk]>
            <[Night Prayers at home, a peaceful evening ritual @ house f/ 2210 - 2230 via Walk]>
            <[Bedtime at home, a well-deserved rest after a long day @ house f/ 2300 - 600 via Walk]>
            """},
            {"role": "user", "content": str(person) + "Make sure you factor in the demographic of the person; make their activities fit who they are. For example, if someone lives in a small town they might have a long drive, if they are unhealthy they might eat 4 meals, etc."}
        ],
    )
    
    data = textQuery["choices"][0]["message"]["content"]
    return parse_schedule(data)

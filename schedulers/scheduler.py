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
            IE: 7:20 AM is 720, and 2:00 PM is 1400 Be incredibly descriptive. Do not add anything not encapsulated in <>.\

            Example:
            <[Morning Jog @ terrace f/ 600 - 700 via Walk]>
            <[Morning Prayers @ house f/ 710 - 730 via Walk]>
            <[Breakfast @ house f/ 740 - 810 via Walk]>
            <[Drive to Work @ commercial f/ 830 - 900 via Car]>
            <[Work @ commercial f/ 900 - 1300 via Walk]>
            <[Lunchtime @ retail f/ 1300 - 1400 via Walk]>
            <[Work @ commercial f/ 1400 - 1800 via Walk]>
            <[Drive Home @ house f/ 1800 - 1830 via Car]>
            <[Evening Prayers @ house f/ 1830 - 1900 via Walk]>
            <[Dinner @ house f/ 1930 - 2030 via Walk]>
            <[Family time @ house f/ 2040 - 2200 via Walk]>
            <[Night Prayers @ house f/ 2210 - 2230 via Walk]>
            <[Bedtime @ house f/ 2300 - 600 via Walk]>
            """},
            {"role": "user", "content": str(person)}
        ],
    )
    
    data = textQuery["choices"][0]["message"]["content"]
    return parse_schedule(data)
def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, 1):
        output = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            output = output.replace(f'{{{key}}}', attendee.get(key, 'N/A') or 'N/A')
        with open(f'output_{i}.txt', 'w') as file:
            file.write(output)


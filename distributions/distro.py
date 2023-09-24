from .methods.data.data import data
from .methods.stats import getRandom
from .methods.rules import rules

class Distro:
    def __init__(self, customPrompt = None):
        if customPrompt: self.customPrompt = customPrompt
    
    def generate(self):
        auxillary = {}
        for item in data:
            if item == "name":
                auxillary.update({item : getRandom("name", data[item])})
            elif item == "age":
                auxillary.update({item : getRandom("gaussian", data[item])})
            else:
                auxillary.update({item : getRandom("weighted", data[item])})
        auxillary = rules(auxillary)
        return auxillary
    
    def unpack(self, mbti):
        schema = ""
        match mbti[0]:
            case "I": 
                schema = schema + "This person tends to focus on their inner thoughts and energies, finding solitude or small-group interactions more energizing than large social gatherings. "
            case "E": 
                schema = schema + "This person tends to be energized by external stimuli and social interactions, often enjoying larger gatherings and seeking out new experiences. "
        match mbti[1]:
            case "N":
                schema = schema + "This person tends to see patterns, possibilities, and connections beyond the surface, often valuing abstract concepts and future-oriented thinking. "
            case "S":
                schema = schema + "This person tends to be grounded in the present and focus on concrete details, relying on their five senses to understand the world. "
        match mbti[2]:
            case "T":
                schema = schema + "This person tends to make decisions based on logical analysis and objective criteria, striving for consistency and impartiality. "
            case "F":
                schema = schema + "This person tends to prioritize empathy, values, and interpersonal harmony when making decisions, considering the emotional impact on themselves and others. "
        match mbti[3]:
            case "J":
                schema = schema + "This person tends to prefer structure, planning, and closure, often being decisive and organized in their approach to tasks and life. "
            case "P":
                schema = schema + "This person tends to be more adaptable and spontaneous, comfortable with ambiguity, and open to new information and experiences."
        return schema

    def format(self, auxillary):
        fp = self.unpack(auxillary["personality"])
        formatted_paragraph = f"""
        The individual, known as {auxillary['name']}, has a life experience spanning {auxillary['age']} years.
        They possess an educational background in {auxillary['education']} and belong to the {auxillary['race']} ethnic group.
        Their gender identity is {auxillary['gender']} and their beliefs are influenced by {auxillary['religion']} principles.
        Professionally, they are {auxillary['employment']}, resulting in an income level of {auxillary['income']}.
        They currently reside in {auxillary['location']}, and work as a {auxillary["occupation"]}.
        Their political orientation is aligned with {auxillary['political']} ideologies, and they have participated in {auxillary['votes']} voting events.
        Their immigration status is categorized as {auxillary['immigration']}.
        As for health, they are {auxillary["weight"]} pounds.
        In terms of personal relationships, they presently identify as {auxillary['relation']}.
        {fp}
        """
        return formatted_paragraph




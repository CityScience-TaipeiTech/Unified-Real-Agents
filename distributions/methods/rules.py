from .stats import getRandom
from .data.data import data

def rules(auxillary):

        match auxillary["personality"]:
            case "INFP":
                auxillary["preferred"] = [1, 2, 3, 4]  # Walk/Bike/Car/Public
            case "INFJ":
                auxillary["preferred"] = [4, 1, 2, 3]  # Car/Walk/Bike/Public
            case "INTP":
                auxillary["preferred"] = [3, 4, 1, 2]  # Car/Public/Walk/Bike
            case "INTJ":
                auxillary["preferred"] = [2, 3, 4, 1]  # Bike/Car/Public/Walk
            case "ISFJ":
                auxillary["preferred"] = [4, 3, 2, 1]  # Car/Public/Bike/Walk
            case "ISFP":
                auxillary["preferred"] = [1, 4, 2, 3]  # Walk/Car/Bike/Public
            case "ISTJ":
                auxillary["preferred"] = [3, 4, 2, 1]  # Car/Public/Bike/Walk
            case "ISTP":
                auxillary["preferred"] = [2, 1, 4, 3]  # Bike/Walk/Car/Public
            case "ENFJ":
                auxillary["preferred"] = [4, 1, 3, 2]  # Car/Walk/Public/Bike
            case "ENFP":
                auxillary["preferred"] = [1, 2, 3, 4]  # Walk/Bike/Car/Public
            case "ENTJ":
                auxillary["preferred"] = [3, 2, 4, 1]  # Car/Bike/Public/Walk
            case "ENTP":
                auxillary["preferred"] = [2, 4, 3, 1]  # Bike/Public/Car/Walk
            case "ESFJ":
                auxillary["preferred"] = [4, 3, 1, 2]  # Car/Public/Walk/Bike
            case "ESFP":
                auxillary["preferred"] = [1, 4, 3, 2]  # Walk/Car/Public/Bike
            case "ESTJ":
                auxillary["preferred"] = [3, 4, 1, 2]  # Car/Public/Walk/Bike
            case "ESTP":
                auxillary["preferred"] = [2, 1, 4, 3]  # Bike/Walk/Car/Public
            case _:
                auxillary["preferred"] = [0, 0, 0, 0]  # Default case with all options ranked as 0

        edulevels = list(data["education"].keys())
        # Makes sure name matches gender.
        if "male" in auxillary["gender"] and auxillary["name"] not in data["name"]["male"]:
            while auxillary["name"] not in data["name"]["male"]:
                auxillary["name"] = getRandom("name", data["name"])
        if "female" in auxillary["gender"] and auxillary["name"] not in data["name"]["female"]:
            while auxillary["name"] not in data["name"]["female"]:
                auxillary["name"] = getRandom("name", data["name"])
        # Makes sure retirement makes sense.
        if "retired" in auxillary["employment"] and auxillary["age"] < 50:
            while "retired" in auxillary["employment"]:
                auxillary["employment"] = getRandom("weighted", data["employment"])
        # Makes sure income makes sense for minors.
        if "Under $20,000" not in auxillary["income"] and auxillary["age"] < 18:
            auxillary["income"] = "Under $20,000"
        # Makes sure age makes sense and doesn't defy anything weird.
        if auxillary["age"] < 0:
            auxillary["age"] = getRandom("gaussian", data["age"])
        # Makes sure nothing weird happens with education levels.
        if auxillary["age"] < 28:
            while edulevels[4] in auxillary["education"]:
                auxillary["education"] = getRandom("weighted", data["education"])
        if auxillary["age"] < 25:
            while edulevels[3] in auxillary["education"]:
                auxillary["education"] = getRandom("weighted", data["education"])
        if auxillary["age"] < 22:
            while edulevels[2] in auxillary["education"]:
                auxillary["education"] = getRandom("weighted", data["education"])
        if auxillary["age"] < 17:
            auxillary["education"] = edulevels[0]
        
        if auxillary["age"] < 18:
            auxillary["occupation"] = "Student"
        return auxillary

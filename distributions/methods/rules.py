from .stats import getRandom
from .data.data import data

def rules(auxillary):
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
        # Makes sure age and weight aren't too weird.
        if auxillary["age"] < 12 and auxillary["weight"] == "Obese":
            while auxillary["weight"] == "Obese":
                auxillary["weight"] = getRandom("gaussian", data["weight"])
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
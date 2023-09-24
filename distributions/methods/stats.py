import random

def getRandom(distType, weights):
    if distType == "weighted":
        options, weights = zip(*weights.items())
        option = random.choices(options, weights=weights)[0]
        return option
    if distType == "gaussian": 
        mean = weights["mean"]
        sd = weights["sd"]
        return round(random.gauss(mean, sd),2)
    if distType == "name":
        if "John" in weights:
            return random.choice(weights["male"])
        elif "Jane" in weights:
            return random.choice(weights["female"])
        else:
            return random.choice(weights["male"] + weights["female"])

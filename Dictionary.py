monthConversions = {
    "jan" : "january",
    "feb" : "february",
    "mar" : "march",
    "apr" : "april",
    "may" : "may",
    "jun" : "june",
    "jul" : "july",
    "aug" : "august",
    "sep" : "september",
    "oct" : "october",
    "nov" : "november",
    "dec" : "december"
}

print(monthConversions["aug"])

# or

print(monthConversions.get("stupid", "not a valid key"))
# "not a valid key" is a default value that I passed in this Get function so if any invalid key is passed, it will show "not a valid key" instead of "None"


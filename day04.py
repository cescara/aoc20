import re

required = {"ecl", "eyr", "hcl", "pid", "iyr", "byr", "hgt"}
hgt_pattern = re.compile(r"(?P<num>\d{2,3})(?P<unit>cm|in)")
hcl_pattern = re.compile(r"#[a-z0-9]{6}")
pid_pattern = re.compile(r"\d{9}")
eyecolors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def parse(data):
    passports = [{}]
    for line in data:
        if not line:
            passports.append({})
            continue

        fields = line.split(" ")
        for field in fields:
            key, value = field.split(":")
            passports[-1][key] = value
    return passports


def part1(passports):
    valid = 0
    for passport in passports:
        if required.issubset(passport):
            valid += 1

    return valid


def part2(passports):
    valid = 0

    def hgt_valid(value):
        match = hgt_pattern.match(value)
        if match is None:
            return False
        if match["unit"] == "cm":
            return 150 <= int(match["num"]) <= 193
        else:
            return 59 <= int(match["num"]) <= 76

    for passport in passports:
        if not required.issubset(passport):
            continue

        byr = 1920 <= int(passport["byr"]) <= 2002
        iyr = 2010 <= int(passport["iyr"]) <= 2020
        eyr = 2020 <= int(passport["eyr"]) <= 2030
        hgt = hgt_valid(passport["hgt"])
        hcl = hcl_pattern.fullmatch(passport["hcl"])
        ecl = passport["ecl"] in eyecolors
        pid = pid_pattern.fullmatch(passport["pid"])

        if byr and iyr and eyr and hgt and hcl and ecl and pid:
            valid += 1

    return valid


with open("input/day04.txt") as file:
    inp = [line.strip() for line in file]

print(part1(parse(inp)))
print(part2(parse(inp)))

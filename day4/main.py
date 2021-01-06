import re


def is_valid(passport):
    assert isinstance(passport, str)
    if passport.count(':') == 8:
        return True
    elif passport.count(':') == 7 and passport.count('cid:') == 0:
        return True
    else:
        return False


def validate(passport):
    d = {}
    for field in passport.split(' '):
        d.setdefault(*field.split(':'))
    if int(d['byr']) < 1920 or int(d['byr']) > 2002:
        print('byr', d['byr'])
        return False
    if int(d['iyr']) < 2010 or int(d['iyr']) > 2020:
        print('iyr', d['iyr'])
        return False
    if int(d['eyr']) < 2020 or int(d['eyr']) > 2030:
        print('eyr', d['eyr'])
        return False
    if d['hgt'].count('cm') != 1 and d['hgt'].count('in') != 1:
        print('hgt', d['hgt'])
        return False
    if d['hgt'].count('cm') == 1:
        x = int(d['hgt'].replace('cm', ''))
        if x < 150 or x > 193:
            print('hgt', d['hgt'])
            return False
    if d['hgt'].count('in') == 1:
        x = int(d['hgt'].replace('in', ''))
        if x < 59 or x > 76:
            print('hgt', d['hgt'])
            return False
    if not re.match(r'#[0-9A-Fa-f]{6}', d['hcl']):
        print('hcl', d['hcl'])
        return False
    if d['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        print('ecl', d['ecl'])
        return False
    if not re.match(r'[0-9]{9}', d['pid']):
        print('pid', d['pid'])
        return False
    print(d)
    return True


if __name__ == '__main__':
    lines = []

    with open('input.txt', 'r') as reader:
        for line in reader:
            lines.append(line.replace('\n', ''))
    passports, passport = [], []
    for line in lines:
        if line != '':
            passport.append(line)
        else:
            passports.append(' '.join(passport))
            passport.clear()

    passports = list(filter(None.__ne__, [passport if is_valid(passport) else None for passport in passports]))
    print('Part One: ', len(passports))

    for passport in passports:
        passport = passport.split(' ')
        passport.sort()

    passports = list(filter(None.__ne__, [passport if validate(passport) else None for passport in passports]))
    print('Part Two: ', len(passports) - 1)

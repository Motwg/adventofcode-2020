def apply_rule(number, rule):
    return ((int(rule[0].split('-')[0]) > number or number > int(rule[0].split('-')[1]))
            and (int(rule[1].split('-')[0]) > number or number > int(rule[1].split('-')[1])))


if __name__ == '__main__':
    with open('input.txt', 'r') as reader:
        rules, my_ticket, tickets = [x.split('\n') for x in ''.join(reader.readlines()).split('\n\n')]
    rules = {rule.split(': ')[0]: (rule.split(': ')[1]).split(' or ') for rule in rules}
    my_ticket = [int(x) for x in my_ticket[1].split(',')]
    tickets = [list(map(int, ticket.split(','))) for ticket in tickets[1:]]

    valid_tickets, invalids = tickets.copy(), []
    for ticket in tickets:
        for number in ticket:
            if all(apply_rule(number, rule) for rule in rules.values()):
                invalids.append(number)
                valid_tickets.remove(ticket)

    print('Part One:', sum(invalids))

    new_rules = {}
    for k, rule in rules.items():
        indexes = set([])
        for idx in range(len(my_ticket)):
            if all(not apply_rule(ticket[idx], rule) for ticket in valid_tickets):
                indexes.add(idx)
            new_rules[k] = indexes

    for _ in range(15):
        for k, rule in new_rules.items():
            if len(rule) == 1:
                for k1, v1 in new_rules.items():
                    new_rules[k1] = v1.difference(rule)
                rule_key = k
                rules[k] = rule.pop()
        try:
            new_rules.pop(rule_key)
        except KeyError:
            pass

    value = 1
    for k, v in rules.items():
        assert isinstance(k, str)
        if k.count('departure') > 0:
            value *= my_ticket[v]
    print('Part Two:', value)

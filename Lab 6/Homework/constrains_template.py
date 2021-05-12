from random import shuffle


class CSP:
    def __init__(self, variables, domains, neighbours, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbours = neighbours
        self.constraints = constraints

    def backtracking_search(self):
        return self.recursive_backtracking({})

    def recursive_backtracking(self, assignment):
        if self.is_complete(assignment):
            return assignment
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            if self.is_consistent(var, value, assignment):
                assignment.update({var: value})
                result = self.recursive_backtracking(assignment)
                if result != False:
                    return result
                assignment.pop()
        return False



    def select_unassigned_variable(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return variable

    def is_complete(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return False
        return True

    def order_domain_values(self, variable, assignment):
        all_values = self.domains[variable][:]
        # shuffle(all_values)
        return all_values

    def is_consistent(self, variable, value, assignment):
        if not assignment:
            return True

        for constraint in self.constraints.values():
            for neighbour in self.neighbours[variable]:
                if neighbour not in assignment:
                    continue

                neighbour_value = assignment[neighbour]
                if not constraint(variable, value, neighbour, neighbour_value):
                    return False
        return True


def create_australia_csp():
    wa, q, t, v, sa, nt, nsw = 'WA', 'Q', 'T', 'V', 'SA', 'NT', 'NSW'
    values = ['Red', 'Green', 'Blue']
    variables = [wa, q, t, v, sa, nt, nsw]
    domains = {
        wa: values[:],
        q: values[:],
        t: values[:],
        v: values[:],
        sa: values[:],
        nt: values[:],
        nsw: values[:],
    }
    neighbours = {
        wa: [sa, nt],
        q: [sa, nt, nsw],
        t: [],
        v: [sa, nsw],
        sa: [wa, nt, q, nsw, v],
        nt: [sa, wa, q],
        nsw: [sa, q, v],
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        wa: constraint_function,
        q: constraint_function,
        t: constraint_function,
        v: constraint_function,
        sa: constraint_function,
        nt: constraint_function,
        nsw: constraint_function,
    }

    return CSP(variables, domains, neighbours, constraints)

def create_south_america_csp():
    co, ve, gu, su, guf, br, ec, pe, bo, pa, ch, ar, ur, cor, pan = 'co', 've', 'gu', 'su', 'guf', 'br', 'ec', 'pe', 'bo', 'pa', 'ch', 'ar', 'ur', 'cor', 'pan'
    values = ['Red', 'Green', 'Blue', 'Yellow']
    variables = [co, ve, gu, su, guf, br, ec, pe, bo, pa, ch, ar, ur, cor, pan]
    domains = {
        co: values[:],
        ve: values[:],
        gu: values[:],
        su: values[:],
        guf: values[:],
        br: values[:],
        ec: values[:],
        pe: values[:],
        bo: values[:],
        pa: values[:],
        ch: values[:],
        ar: values[:],
        ur: values[:],
        cor: values[:],
        pan: values[:]
    }
    neighbours = {
        co: [ec, ve, br, pe],
        ve: [co, gu, br],
        gu: [ve, su, br],
        su: [gu,guf,br],
        guf: [su, br],
        br: [pe, co, ve, gu, su, guf, bo, pa, ur, ar],
        ec: [co, pe],
        pe: [ec, co, br, bo, ch],
        bo: [pe, br, pa, ch, ar],
        pa: [bo, br, ar],
        ch: [pe, bo, ar],
        ar: [bo, pa, br, ur, ch],
        ur: [ar, br],
        cor: [pan],
        pan: [cor, co]
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        co: constraint_function,
        ve: constraint_function,
        gu: constraint_function,
        su: constraint_function,
        guf: constraint_function,
        br: constraint_function,
        ec: constraint_function,
        pe: constraint_function,
        bo: constraint_function,
        pa: constraint_function,
        ch: constraint_function,
        ar: constraint_function,
        ur: constraint_function,
        cor: constraint_function,
        pan: constraint_function
    }

    return CSP(variables, domains, neighbours, constraints)

if __name__ == '__main__':
    australia = create_australia_csp()
    result = australia.backtracking_search()
    print('Australia: ')
    for area, color in sorted(result.items()):
        print("{}: {}".format(area, color))
    south_america = create_south_america_csp()
    result = south_america.backtracking_search()
    print('\nSouth America: ')
    for area, color in sorted(result.items()):
        print("{}: {}".format(area, color))

    # Check at https://mapchart.net/australia.html

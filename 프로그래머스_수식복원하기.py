def solution(expressions):
    def decimal_to_base(number, base):
        if number == 0:
            return 0
        result = []
        while number:
            result.append(str(number % base))
            number //= base
        return int(''.join(result[::-1]))
    
    def calculate_X(expression, base):
        exp = expression.split()
        op1, op2, result = int(exp[0], base), int(exp[2], base), 0
        result = op1 + op2 if exp[1] == '+' else op1 - op2
        return decimal_to_base(result, base)
    
    def check_possible(expression, base):
        exp = expression.split()
        op1, op2, result = int(exp[0], base), int(exp[2], base), int(exp[4], base)
        if exp[1] == '+':
            return op1 + op2 == result
        else:
            return op1 - op2 == result
        
    def find_base(expression):
        result = [i for i in range(2,10)]
        exp = expression.split()

        for i in [0,2,4]:
            if exp[i] != 'X':
                n = len(exp[i])
                min_base = 2
                for j in range(n):
                    temp = int(exp[i][j]) + 1
                    min_base = temp if min_base < temp else min_base
                result = list(filter(lambda x: x>=min_base, result))
        if exp[4] != 'X':
            temp = []
            for base in result:
                if not check_possible(expression, base):
                    temp.append(base)
            for t in temp:
                result.remove(t)
        return result
    
    candidate = set(i for i in range(2, 10))
    unknown = []
    
    for exp in expressions:
        if exp.split()[4] == 'X':
            unknown.append(exp)
        if len(candidate) > 1:
            temp_set = set(find_base(exp))
            candidate.intersection_update(temp_set)
    
    answer = []
    for expression in unknown:
        results = set()
        for base in candidate:
            results.add(calculate_X(expression, base))
        temp = str(results.pop()) if len(results) == 1 else '?'
        answer.append(expression[: -1] + temp)
    return answer
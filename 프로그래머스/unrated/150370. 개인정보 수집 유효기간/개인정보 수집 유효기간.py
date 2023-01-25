def solution(today, terms, privacies):
    answer = []
    termsDict = {}
    year, month, day = map(int, today.split('.'))
    
    for term in terms:
        alpha, num = term.split()
        termsDict[alpha] = int(num)
        
    for i in range(len(privacies)):
        date, alpha = privacies[i].split()
        dateYear, dateMonth, dateDay = map(int, date.split('.'))
        dateMonth += termsDict[alpha]
        
        while dateMonth >12:
            dateMonth -= 12
            dateYear += 1
            
        if dateYear > year:
            continue
        elif dateYear == year:
            if dateMonth > month:
                continue
            elif dateMonth == month:
                if dateDay > day:
                    continue
        answer.append(i+1)
    return answer
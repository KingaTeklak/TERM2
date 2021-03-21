import sys

year = sys.argv[1]
try:
    int(year)
    
    year = int(year)
    
    def easter(data):
        """return date of easter, takes year as argument"""
        months = {2: "luty", 3:'marzec', 4:'kwiecień', 5:"maj"}
        if data <=0:
            return "Błędny rok"
        a = year%19
        b = int(year/100)
        c = year%100
        d = int(b/4)
        e = b%4
        f = int((b+8)/25)
        g = int((b-f+1)/3)
        h = (19*a+b-d-g+15)%30
        i = int(c/4)
        k = c%4
        l = (32+2*e+2*i-h-k)%7
        m = int((a+11*h+22*l)/451)
        p = (h+l-7*m+114)%31
        day = p+1
        month = int(int(h+l-7*m+114)/31)
        return f" Dzień: {day}\n Miesiąc: {months[month]}\n Rok: {year}"
    print(easter(year))
except:
     print("Wpisz rok za pomocą cyfr")


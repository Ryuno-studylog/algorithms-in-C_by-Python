def gcd(u,v):
    t = 0
    while u > 0:
        if u < v:
            t = u
            u = v
            v = t
        u = u-v
    return v

def main():
    x = input("一つ目の数字>>>")
    y = input("二つ目の数字>>>")
    g = gcd(int(x),int(y))
    if int(x) > 0 and int(y) > 0:
        print(x,"と",y,"の最大公約数は",g)
    else:
        print("error")

main()
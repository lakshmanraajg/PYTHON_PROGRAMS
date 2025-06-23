value = "three"
match value:                             #switch case statement like in c
    case "one":
        print(1)
    case "two":
        print(2)
    case "three" | "four":
        print(3,4)
    case _:                                  #default in c
        print("Valid number")

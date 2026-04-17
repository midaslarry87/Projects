
Answer = input("what is the Answer to the Great Question of Life, the Universe, and Everything? ")

match Answer:
    case "42" | "forty-two" | "forty two" | 42 | "Forty two" | "Forty-two":
        print("Yes")
    case _ :
        print("No")
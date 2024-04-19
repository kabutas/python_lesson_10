def war_of_numbers(warriors: list) -> str:
    even_warriors = []
    odd_warriors = []
    for i in warriors:
        if i % 2 == 0:
            even_warriors.append(i)
        else:
            odd_warriors.append(i)
    if sum(even_warriors) == sum(odd_warriors):
        return "ITS A WAR WITHOUT AN ENDING (draw)"
    if sum(even_warriors) > sum(odd_warriors):
        return (f"{sum(even_warriors)} EVEN warriors WINS against {sum(odd_warriors)}"
                f" ODD warriors by {sum(even_warriors) - sum(odd_warriors)}")
    else:
        return (f"{sum(even_warriors)} EVEN warriors LOSES to {(sum(odd_warriors))}"
                f" ODD warriors by {sum(odd_warriors) - sum(even_warriors)}")


print(war_of_numbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]))
print(war_of_numbers([12, 90, 75]))
print(war_of_numbers([2, 8, 7, 5]))
print(war_of_numbers([2, 8, 7, 3]))

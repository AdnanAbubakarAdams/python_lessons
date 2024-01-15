# 
def square(x):
    result = x*x
    return result
print(square(5))

# ------ From pounds to kilograms-----
weight_lbs = 155
kg_in_lb = 0.453592
weight_kg = weight_lbs * kg_in_lb
print(f"{weight_lbs} lbs is {weight_kg} kgs")

# now we put it into a function
def convert_pounds_to_kilograms(lbs):
    kg_in_lb = 0.453592
    kilograms = lbs * kg_in_lb
    return kilograms
# using the function
weight_in_pounds = 199
weight_in_kilograms = convert_pounds_to_kilograms(weight_in_pounds)
print(f"{weight_in_pounds} lbs is {weight_in_kilograms} kgs")

'''Meal with tip and tax
Now let's revisit our example from the earlier sessions in the class: Compute the total cost of a meal.
Suppose that we buy food for $30. We also need to pay the tax on top (which is 8.875% in NY), and put a tip, say 15%, on the pre-tax amount. The code for doing this calculation:'''

food = 30
tax = 8.875/100
tip = 15/100

def cost_meal(food_cost, tax_rate, tip_percentage):
    total_cost_of_meal = food_cost + food_cost * (tax_rate / 100) + food_cost * (tip_percentage / 100)
    total_cost_of_meal = round(total_cost_of_meal, 2)
    return total_cost_of_meal

meal_total = cost_meal(food, tax, tip)
print(f"The cost of the meal will be: ${meal_total}") # assign it to variable OR
print(f"The cost of meals sums up to: ${cost_meal(food, tax, tip)}") # call the function in here

article = """One person was believed to be missing after an oil rig storage platform exploded Sunday night on Lake Pontchartrain, just north and west of New Orleans. Seven people were taken to hospitals after the explosion, and three of them remained in critical condition Monday morning, Mike Guillot, the director of emergency medical services at East Jefferson General Hospital, said at a news conference. The other four were released. Sheriff Joe Lopinto of Jefferson Parish said at the news conference, We are fairly confident there is an eighth person, adding that search efforts were continuing, and the Coast Guard had contacted the family of the person. No fatalities had been reported as of Monday morning. The blast occurred shortly after seven pm near St Charles Parish and the city of Kenner. The platform is in unincorporated Jefferson Parish. Officials are still investigating the cause of the explosion, but the City of Kenner said on its Facebook page that authorities on the scene report that cleaning chemicals ignited on the surface of the oil rig platform."""
print(article)

def length_of_the_article(texts):
    splitted_into_words = texts.split(" ")
    length = len(splitted_into_words)
    return length

len_words = length_of_the_article(article)
print(f"The article has {len_words} words")
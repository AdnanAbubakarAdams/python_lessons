# Find out how many names we have in the list of names names_list that is the list that we created earlier, from the names_string multiline string.
# Add the name "Mia Lopez" in the list of names
# Add the list of names ["John Miller", "Jane Nelson"] in the list of names, using the extend command

names_list = [
    "Jacob Adams",
    "Emily Brown",
    "Michael Campbell",
    "Madison Davis",
    "Andrew Edwards",
    "Olivia Flores",
    "David Garcia",
    "Sophia Ingram",
    "Nathan Jones",
    "Natalie King",
]

# length of list
length_of_list = len(names_list)
print(length_of_list)

# add to list
names_list.append("Mia Lopez")
print(names_list)

# add to list with extend
names_list.extend(["John Miller", "Jane Nelson"])
print(names_list)

# checking the new length
new_length = len(names_list)
print(new_length)


'''
Find the name "Josh" in the list. In what position does the name appear?
Try to find a name that does not exist in the list. What do you get?
Now let's practice the if-else command:

Define a variable search with the name that you want to search for.
Check if the name appears in the list
If yes, then return the index number for its first apperance, and the number of times that you see the name in the list
If not, print that the name does not appear in the list
'''
names = ["Panos", "John", "Chris", "Josh", "Mary", "Anna", "John"]
search = "John"
if search in names:
    location = names.index(search)
    count = names.count(search)
    print("The name", search, "appears", count, "time(s)")
    print("First appearance at location", location)
else:
    print("The name", search, " does not appear in the list")




washington_post = """Russian officials vehemently defended the country s airstrikes in Syria on Thursday as blows to Islamic State militants even as evidence mounted suggesting that US backed rebels and others were facing the brunt of Moscow s attacks
And while Russian officials and diplomats rallied behind President Vladimir Putin the Kremlin s stance appeared further clouded by acknowledgments that the missions have already extended beyond solely the Islamic State
In Paris the Russian ambassador to France Alexander Orlov said the Russian attacks also targeted an al Qaeda linked group Jabhat al Nusra or al Nusra Front
Syrias ambassador to Russia Riad Haddad echoed that the joint hit list for Russia and the Syrian government included Jabhat al Nusra which is believed to have some coordination with the Islamic State but is still seen mostly as a rival
We are confronting armed terrorist groups in Syria regardless of how they identify themselves whether it is Jabhat al Nusra the ISIL or others he said using one of the acronyms for the Islamic State
They all are pursuing ISIL ends he added according to the Interfax news agency
The ambassadors did not specifically mention any US and Western backed rebel groups
But the comment was certain to deepen suspicions by Washington and allies that Putin s short term aim is to give more breathing space to Syria s embattled President Bashar al Assad whose government is strongly supported by Moscow
Syrian activists meanwhile ramped up their own claims that Moscow was hitting groups seeking to bring down Assad who has managed to hang on during more than four years of civil war
Russia s expanding military intervention in Syria added urgency to separate efforts by Russia and US officials to coordinate strategies against the Islamic State and avoid potential airspace missteps between the two powers so called deconfliction talks The Pentagon said the discussions will begin Thursday
One monitoring group the Britain based Syrian Observatory for Human Rights said Russian airstrikes again struck strongholds of an American backed rebel group Tajamu Alezzah in central Hama province
The actions quickly criticized by Washington add an unpredictable element to a multilayered war
The observatory also reported that airstrikes hit the northwestern city Jisr al Shughour which is in the hands of rebel groups including al Nusra after battles last month to drive back Assad s forces
Among the locations hit was a site near Kafr Nabl the northern Syrian town whose weekly protests against the government often featuring pithy slogans in English won it renown as a symbol of what began as a peaceful protest movement against the Assad regime The local council receives US assistance and the rebel unit there has received support under a covert CIA program aimed at bolstering moderate rebels
Raed Fares one of the leaders of the protest movement in Kafr Nabl said warplanes struck a Free Syrian Army checkpoint guarding Roman ruins on the outskirts of the town He said the explosion was bigger than anything local residents had seen in three years of airstrikes conducted by Syrian warplanes
It made a fire six kilometers wide he told The Washington Post
Other sites hit on the second day of Russian bombing included locations in the province of Hama The targets suggested the main intention of the strikes was to shore up government control over a corridor of territory linking the capital Damascus to the Assad family s coastal heartland where the Russians are operating out of an expanded air base
Syrian rebels some of them US backed had been making slow but steady gains in the area considered one of the government s biggest vulnerabilities There has been no Islamic State presence there since January when moderate rebels rose up against the extremists and forced them to retreat to eastern Syria
In Washington Sen John McCain R Ariz told CNN he could absolutely confirm that airstrikes hit Western backed groups such as the Free Syrian Army and other factions armed and trained by the CIA
We have communications with people there said McCain chairman of the Senate Armed Services Committee
The accounts could not be independently assessed but the main focus of the Russian attacks appeared to be in areas not known to have strong Islamic State footholds
In Moscow the reply was blunt
Total rubbish Gennady Zyuganov a member of parliament and leader of Russia s Communist Party said of the US accusations
In televised remarks Thursday Putin called accusations that Russian airstrikes had killed civilians in Syria information attacks
He also addressed concerns about an accidental military clash between Russian and US led coalition forces saying that his intelligence and military agencies were establishing contacts with counterparts in the United States
This work is ongoing and I hope that it will conclude with the creation of a regularly acting mechanism he said
A spokesman for Russia s Defense Ministry Igor Konashenkov said Thursday that warplanes hit a dozen Islamic State sites in the past hours destroying targets including a command center and two arms depots
The United States and Russia agree on the need to fight the Islamic State but not about what to do with the Syrian president The Syrian civil war which grew out of an uprising against Assad has killed more than people since March and sent millions of refugees fleeing to countries in the Middle East and Europe
Accusing Russia of pouring gasoline on the fire Defense Secretary Ashton B Carter vowed that US pilots would continue their year long bombing campaign against the Islamic State in Syria despite Moscow s warning that American planes should stay away from its operations
I think what they re doing is going to backfire and is counterproductive Carter said on Wednesday
Yet Russia s military flexing in Syria brought quick overtures from neighboring Iraq where the Islamic State also holds significant territory but the government is within Washington s fold
Iraq s prime minister Haider al Abadi told France that he would welcome Russia joining the US led airstrikes against Islamic State targets but there have been no specific discussions
Joining the protests against the Russian airstrikes was Saudi Arabia a leading foe of Assad and one of Washington s top Middle East allies
At the United Nations late Wednesday the Saudi ambassador Abdallah al Mouallimi demanded that the Russian air campaign stop immediately and accused Moscow of carrying out attacks in areas outside the control of the Islamic State
In Iran Assad s main regional backer Foreign Ministry spokeswoman Marzieh Afkham called Russia s military role a step toward resolving the current crisis in Syria"""



'''
What is the length of the document above in characters? In words? In paragraphs (we have one paragraph per line)?
What is the average length of a paragraph in words?
What is the average length of a word in characters? (Remember that the document contains spaces and newlines, that should not count as parts of a word)
'''
length_of_chars = len(washington_post)
print("there are", length_of_chars, "characters")

words_in_post = washington_post.split()
length_of_words = len(words_in_post)
print("there are", length_of_words, "words")

paragraphs_in_post = washington_post.split("\n")
length_of_paragraph = len(paragraphs_in_post)
print("there are", length_of_paragraph, "paragraphs")

words_per_paragraph = length_of_words / length_of_paragraph
print(f"There are {words_per_paragraph:.2f} words per paragraph")

# The document contains spaces and newlines, which should not be counted
# If you compute the average word length as len_characters/len_words you will get 6.07, which is incorrect
# length_of_letters_only = (length_of_chars - washington_post.count(" ") - washington_post.count("\n"))
# letters_per_word = len_letters_only / len_words
# print(f"There are {letters_per_word:.2f} letters per word")

# ------ TUPLES --------- #
# A tuple is similar to a list and consists of a number of values separated by commas. For instance:
t = (12345, 54321, 54321, "hello!")
print(t)
print(t[3])
print(t.index("hello!"))
# However, a tuple but is immutable. This means that we cannot modify its contents. So the other operators that modify a list do not apply to a tuple.
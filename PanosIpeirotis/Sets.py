'''A set is a data structure where all elements are unique. While they are similar to lists, in sets there is no order among the items in a set, and sets do not support indexing. Sets are ideal for membership queries, i.e., checking if an items appears in the set or not.'''# creating sets
one_set = {4, 2, 1, 3}
print(one_set)
# 
two_set = {6, 5, 4, -2}
print(two_set)
# 
three_set = {5, 0, -3, 4, 4, 4, 4}
print(three_set)
# 
# creating an empty set; notice that we do *not* use the "empty set = {}" command
# as someone would expect based on the way that we create an empty list
empty_set = set()
print(empty_set)
# 
my_list = [1, 2, 3, 0, 5, 10, 11, 1, 5]
my_set = set(my_list)
print(my_list)
print(my_set)
# 
print("Length of list:", len(my_list))
print("Length of set:", len(my_set))



washington_post = """Russian officials vehemently defended the country s airstrikes in Syria on Thursday as blows to Islamic State militants even as evidence mounted suggesting that U S backed rebels and others were facing the brunt of Moscow s attacks
And while Russian officials and diplomats rallied behind President Vladimir Putin the Kremlin s stance appeared further clouded by acknowledgments that the missions have already extended beyond solely the Islamic State
In Paris the Russian ambassador to France Alexander Orlov said the Russian attacks also targeted an al Qaeda linked group Jabhat al Nusra or al Nusra Front
Syrias ambassador to Russia Riad Haddad echoed that the joint hit list for Russia and the Syrian government included Jabhat al Nusra which is believed to have some coordination with the Islamic State but is still seen mostly as a rival
We are confronting armed terrorist groups in Syria regardless of how they identify themselves whether it is Jabhat al Nusra the ISIL or others he said using one of the acronyms for the Islamic State
They all are pursuing ISIL ends he added according to the Interfax news agency
The ambassadors did not specifically mention any U S and Western backed rebel groups
But the comment was certain to deepen suspicions by Washington and allies that Putin s short term aim is to give more breathing space to Syria s embattled President Bashar al Assad whose government is strongly supported by Moscow
Syrian activists meanwhile ramped up their own claims that Moscow was hitting groups seeking to bring down Assad who has managed to hang on during more than four years of civil war
Russia s expanding military intervention in Syria added urgency to separate efforts by Russia and U S officials to coordinate strategies against the Islamic State and avoid potential airspace missteps between the two powers so called deconfliction talks The Pentagon said the discussions will begin Thursday
One monitoring group the Britain based Syrian Observatory for Human Rights said Russian airstrikes again struck strongholds of an American backed rebel group Tajamu Alezzah in central Hama province
The actions quickly criticized by Washington add an unpredictable element to a multilayered war
The observatory also reported that airstrikes hit the northwestern city Jisr al Shughour which is in the hands of rebel groups including al Nusra after battles last month to drive back Assad s forces
Among the locations hit was a site near Kafr Nabl the northern Syrian town whose weekly protests against the government often featuring pithy slogans in English won it renown as a symbol of what began as a peaceful protest movement against the Assad regime The local council receives U S assistance and the rebel unit there has received support under a covert CIA program aimed at bolstering moderate rebels
Raed Fares one of the leaders of the protest movement in Kafr Nabl said warplanes struck a Free Syrian Army checkpoint guarding Roman ruins on the outskirts of the town He said the explosion was bigger than anything local residents had seen in three years of airstrikes conducted by Syrian warplanes
It made a fire six kilometers wide he told The Washington Post
Other sites hit on the second day of Russian bombing included locations in the province of Hama The targets suggested the main intention of the strikes was to shore up government control over a corridor of territory linking the capital Damascus to the Assad family s coastal heartland where the Russians are operating out of an expanded air base
Syrian rebels some of them U S backed had been making slow but steady gains in the area considered one of the government s biggest vulnerabilities There has been no Islamic State presence there since January when moderate rebels rose up against the extremists and forced them to retreat to eastern Syria
In Washington Sen John McCain R Ariz told CNN he could absolutely confirm that airstrikes hit Western backed groups such as the Free Syrian Army and other factions armed and trained by the CIA
We have communications with people there said McCain chairman of the Senate Armed Services Committee
The accounts could not be independently assessed but the main focus of the Russian attacks appeared to be in areas not known to have strong Islamic State footholds
In Moscow the reply was blunt
Total rubbish Gennady Zyuganov a member of parliament and leader of Russia s Communist Party said of the U S accusations
In televised remarks Thursday Putin called accusations that Russian airstrikes had killed civilians in Syria information attacks
He also addressed concerns about an accidental military clash between Russian and U S led coalition forces saying that his intelligence and military agencies were establishing contacts with counterparts in the United States
This work is ongoing and I hope that it will conclude with the creation of a regularly acting mechanism he said
A spokesman for Russia s Defense Ministry Igor Konashenkov said Thursday that warplanes hit a dozen Islamic State sites in the past hours destroying targets including a command center and two arms depots
The United States and Russia agree on the need to fight the Islamic State but not about what to do with the Syrian president The Syrian civil war which grew out of an uprising against Assad has killed more than people since March and sent millions of refugees fleeing to countries in the Middle East and Europe
Accusing Russia of pouring gasoline on the fire Defense Secretary Ashton B Carter vowed that U S pilots would continue their year long bombing campaign against the Islamic State in Syria despite Moscow s warning that American planes should stay away from its operations
I think what they re doing is going to backfire and is counterproductive Carter said on Wednesday
Yet Russia s military flexing in Syria brought quick overtures from neighboring Iraq where the Islamic State also holds significant territory but the government is within Washington s fold
Iraq s prime minister Haider al Abadi told France that he would welcome Russia joining the U S led airstrikes against Islamic State targets but there have been no specific discussions
Joining the protests against the Russian airstrikes was Saudi Arabia a leading foe of Assad and one of Washington s top Middle East allies
At the United Nations late Wednesday the Saudi ambassador Abdallah al Mouallimi demanded that the Russian air campaign stop immediately and accused Moscow of carrying out attacks in areas outside the control of the Islamic State
In Iran Assad s main regional backer Foreign Ministry spokeswoman Marzieh Afkham called Russia s military role a step toward resolving the current crisis in Syria """

# What is the number of distinct words in the washington_post variable?
# 
splitted_to_list = washington_post.split()
# print(splitted_to_list)
# 
# Let's see the first few words that we extracted
print(splitted_to_list[:10])
# 
# By using a set, we will eliminate duplicates
unique_words_no_dups = set(splitted_to_list)
print(unique_words_no_dups)
print(len(splitted_to_list))
print(len(unique_words_no_dups))

# However, if we take a look at the set, we will see that capitalization
# messes things up. We count as different words variations of the same word
# with different capitalization (e.g, 'President' and 'president'; 'They' and 'they'; etc)
splitted_lower_case_words = washington_post.lower().split()
print(len(splitted_lower_case_words))
unique_words_no_dups2 = set(splitted_lower_case_words)
print(len(unique_words_no_dups2))

# For sets, we can only check if an item appears within the set or not. We achieve this using the in operator:

my_set = {1, 2, 3, 4}

val = 1
if val in my_set:
    print("The value", val ,"appears in the set", my_set)
else:
    print("The value", val ,"does not appear in the set", my_set)

val = 0
if val in my_set:
    print("The value", val ,"appears in the set", my_set)
else:
    print("The value", val ,"does not appear in the set", my_set)

if val not in my_set:
    print("The value", val ,"does not appear in the set", my_set)
else:
    print("The value", val ,"appears in the set", my_set)


# To add and remove elements in a set, we use, respectively the add and remove commands:
# set_a.add(x): add an element to a set
# set_a.remove(x): remove an element from a set
set_A = set()
set_A.add(1)
set_A.add(2)
set_A.add(3)
set_A.add(4)
set_A.add(5)
set_A.add(6)
print(set_A)
set_A.remove(6)
print(set_A)

"""Set operators: Union, intersection, difference, subset. Plus, Jaccard Similarity
Sets also support operations that allow us to quickly compute the difference, intersection, and union of two sets. For example:

set_a - set_b: elements in a but not in b. Equivalent to set_a.difference(set_b)
set_a | set_b: elements in a or b. Equivalent to set_a.union(set_b)
set_a & set_b: elements in both a and b. Equivalent to set_a.intersection(set_b)
set_a ^ set_b: elements in a or b but not both. Equivalent to set_a.symmetric_difference(set_b)
set_a <= set_b: tests whether every element in set_a is in set_b. Equivalent to set_a.issubset(set_b)"""

set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7}
print("Set A", set_A)
print("Set B", set_B)
print("Difference A-B", set_A.difference(set_B))
print("Union", set_A | set_B)
print("Intersection", set_A & set_B)
print("Symmetric Difference", set_A ^ set_B)

# ----------------------------------
print("Difference A-B", set_A - set_B)
print("Difference A-B", set_A.difference(set_B))
print("Union", set_A | set_B)
print("Union", set_A.union(set_B))
print("Intersection", set_A & set_B)
print("Intersection", set_A.intersection(set_B))
print("Symmetric Difference", set_A ^ set_B)
print("Symmetric Difference", set_A.symmetric_difference(set_B))

# Now, lets try to use the Jaccard index similarity to compute the similarity of the two sets. The Jaccard coefficient is defined as the ratio of the size of the intersection of the two sets, divided by the size of the union of the two sets.
intersection = set_A & set_B
print("The intersection has", len(intersection), "items")

union = set_A | set_B
print("The union has", len(union), "items")

jaccard = len(intersection) / len(union)
print("The similarity of set_A with set_B is", jaccard)

wsj = """
Yahoo Inc  disclosed a massive security breach by a  state sponsored actor  affecting at least 500 million users  potentially the largest such data breach on record and the latest hurdle for the beaten down internet company as it works through the sale of its core business
Yahoo said certain user account information including names  email addresses  telephone numbers  dates of birth  hashed passwords and  in some cases  encrypted or unencrypted security questions and answers was stolen from the company s network in late 2014 by what it believes is a state sponsored actor
Yahoo said it is notifying potentially affected users and has taken steps to secure their accounts by invalidating unencrypted security questions and answers so they can t be used to access an account and asking potentially affected users to change their passwords
Yahoo recommended users who haven t changed their passwords since 2014 do so  It also encouraged users change their passwords as well as security questions and answers for any other accounts on which they use the same or similar information used for their Yahoo account
The company  which is working with law enforcement  said the continuing investigation indicates that stolen information didn t include unprotected passwords  payment card data or bank account information
With 500 million user accounts affected  this is the largest ever publicly disclosed data breach  according to Paul Stephens  director of policy and advocacy with Privacy Rights Clearing House  a not for profit group that compiles information on data breaches
No evidence has been found to suggest the state sponsored actor is currently in Yahoo s network  and Yahoo didn t name the country it suspected was involved  In August  a hacker called  Peace  appeared in online forums  offering to sell 200 million of the company s usernames and passwords for about  1 900 in total  Peace had previously sold data taken from breaches at Myspace and LinkedIn Corp
"""

ust = """
SAN FRANCISCO   Information from at least 500 million Yahoo accounts was stolen from the company in 2014  and the  company said Thursday it believes that a state sponsored actor was behind the hack
The information may have included names  email addresses  telephone numbers  dates of birth  and  in some cases  encrypted or unencrypted security questions and answers  Yahoo said
Claims surfaced in early August that a hacker using the name  Peace  was trying to sell the usernames  passwords and dates of birth of Yahoo account users on the dark web   a black market of thousands of secret websites
The FBI said it was aware of the matter  The compromise of public and private sector systems is something the agency takes very seriously and it said it will continue to investigate and hold accountable all who pose a threat in cyberspace  the agency said in an emailed statement
Yahoo recommends that users who haven t changed their passwords since 2014 do so  The company said it was notifying potentially affected users and taking steps to secure their accounts  That included invalidating unencrypted security questions and answers and asking users to change their passwords
The announcement comes as Yahoo looks to complete its  4 8  billion sale of its core Internet business to media giant Verizon Communications  which said it was notified of the Yahoo breach  within the last two days
 We understand that Yahoo is conducting an active investigation of this matter  but we otherwise have limited information and understanding of the impact   Verizon said
Given the unsettled nature of Yahoo s ownership just now   regulators should be concerned with who will take responsibility for the response to this compromise  It can be easy for the  right thing to do  to slip through the cracks in a multi billion dollar transition   said Tim Erlin  senior director of IT security and risk strategy at Tripwire  a computer security firm
Yahoo Chief Executive Officer Marissa Mayer has pledged to stay on with the company through the close of the merger  which is being overseen by Verizon s Marni Walden and AOL CEO Tim Armstrong  Yahoo shares  YHOO  were flat Thursday  Verizon  VZ  shares were up 1  at  52 39
"""
# Below we have two news articles discussing a security breach at Yahoo. We want to compute the similarity of these articles using the Jaccard similarity. (For the sake of simplicity, we have removed all punctuation from the text.)

# word from wsj article
words_from_wsj_article = wsj.lower().split()
print("the WSJ article has", len(words_from_wsj_article), "words")
print("the WSJ article has", len(set(words_from_wsj_article)), "distinct or unique words")

# words from ust article
words_from_ust_article = ust.lower().split()
print("the UST article has", len(words_from_ust_article), "words")
print("the UST article has", len(set(words_from_ust_article)), "distinct or unique words")

# intersection of words from the two articles
intersection = set(words_from_wsj_article) & set(words_from_ust_article)
print("The intersection has", len(intersection), "words")

# Union of the wors from the two articles
# And the union of the words across the two articles
union = set(words_from_wsj_article) | set(words_from_ust_article)
print("The union has", len(union), "words")

# And now we can compute hte similarity
similarity = len(intersection) / len(union)
print("The similarity of the two articles is", similarity)
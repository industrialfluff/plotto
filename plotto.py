from lxml import objectify
from lxml import html
from lxml import etree

import random

def find_conflict(id):
    for c in plotto.conflicts.conflict:
        if c.attrib["id"] == id:
            return c

def random_item():
    return random.choice(["potion", "family ornament", "Holy symbol", "Bible", "favorite book", "wallet", "bag of gold", "shard", "piece of paper", "notes", "scrolls", "journal", "hunting trophy", "satchel", "set of playing cards",
    "laptop", "pencil", "feather and ink", "charger", "keys", "screws", "handkerchief", "business card", "romantic photo", "family photo", "necklace", "ring", "lunch box"])

def any_name():
    if random.choice([1,2]) == 2:
        return female_name()
    else:
        return male_name()

def female_name():
    return random.choice(['Aaliyah','Abby','Acadia','Ada','Adrena','Adrienne','Agnes','Alessandra','Alessia','Alexa','Alison','Aly','Alyona','Amanda','Amelia','Anais','Angel','Angelique','Anya','April','Aria','Arielle','Artemesia','Ashley','Aurora','Aviva','Beatrix','Becky','Blair','Brandy','Brenda','Brianna','Bridgette','Briony','Brooke','Buffy','Callie','Candice','Candy','Carina','Carmen','Caroline','Cece','Celestina','Chanel','Charis','Charlie','Charlotte','Cher','Chloe','Claire','Clarise','Clementine','Connie','Courtney','Cynthia','Dahlia','Dana','Daniella','Daphne','Debra','Delilah','Delphine','Dixie','Dominique','Edie','Eileen','Eldora','Elena','Elina','Eliza','Elle','Emelda','Emily','Emma','Erika','Esmeralda','Etta','Faina','Fern','Fiorella','Flora','Francesca','Freya','Galina','Gaynor','Gia','Giada','Gigi','Giuliana','Greta','Gretchen','Hazel','Inez','Irina','Iris','Isla','Ivy','Jackie','Jade','Janet','Jenna','Jessa','Jessica','Juliet','Juniper','Kai','Karen','Karly','Kassandra','Kate','Katie','Katiya','Kayla','Kelly','Kiera','Klara','Lacey','Lana','Larissa','Laura','Leighton','Leila','Leilani','Lena','Lenore','Lexi','Liliana','Lindsey','Liza','Luciana','Lulu','Mabel','Mae','Maria','Mariella','Meave','Megan','Mia','Molly','Monique','Nadia','Naomi','Natalia','Natasha','Neve','Nicolette','Nina','Octavia','Odette','Olivia','Ondina','Paisley','Paulina','Paz','Phoebe','Quinn','Radinka','Rae','Raisa','Ramona','Rebecca','Regina','Renee','Rosalie','Roxanne','Ruby','Sasha','Scarlett','Seraphina','Serena','Shay','Shirley','Sia','Simone','Skylar','Sloan','Sophia','Soraya','Spencer','Stella','Stevie','Sybil','Talisa','Tallulah','Taryn','Tatyana','Taylor','Tessa','Thora','Ursula','Vanessa','Veronica','Violet','Yazmin','Yesenia','Zara','Zarya','Zenaida','Zita'])

def male_name():
    return random.choice(['Liam','Noah','Oliver','Elijah','James','William','Benjamin','Lucas','Henry','Theodore','Jack','Levi','Alexander','Jackson','Mateo','Daniel','Michael','Mason','Sebastian','Ethan','Logan','Owen','Samuel','Jacob','Asher','Aiden','John','Joseph','Wyatt','David','Leo','Luke','Julian','Hudson','Grayson','Matthew','Ezra','Gabriel','Carter','Isaac','Jayden','Luca','Anthony','Dylan','Lincoln','Thomas','Maverick','Elias','Josiah','Charles','Caleb','Christopher','Ezekiel','Miles','Jaxon','Isaiah','Andrew','Joshua','Nathan','Nolan','Adrian','Cameron','Santiago','Eli','Aaron','Ryan','Angel','Cooper','Waylon','Easton','Kai','Christian','Landon','Colton','Roman','Axel','Brooks','Jonathan','Robert','Jameson','Ian','Everett','Greyson','Wesley','Jeremiah','Hunter','Leonardo','Jordan','Jose','Bennett','Silas','Nicholas','Parker','Beau','Weston','Austin','Connor','Carson','Dominic','Xavier','Jaxson','Jace','Emmett','Adam','Declan','Rowan','Micah','Kayden','Gael','River','Ryder','Kingston','Damian','Sawyer','Luka','Evan','Vincent','Legend','Myles','Harrison','August','Bryson','Amir','Giovanni','Chase','Diego','Milo','Jasper','Walker','Jason','Brayden','Cole','Nathaniel','George','Lorenzo','Zion','Luis','Archer','Enzo','Jonah','Thiago','Theo','Ayden','Zachary','Calvin','Braxton','Ashton','Rhett','Atlas','Jude','Bentley','Carlos','Ryker','Adriel','Arthur','Ace','Tyler','Jayce','Max','Elliot','Graham','Kaiden','Maxwell','Juan','Dean','Matteo','Malachi','Ivan','Elliott','Jesus','Emiliano','Messiah','Gavin','Maddox','Camden','Hayden','Leon','Antonio','Justin','Tucker','Brandon','Kevin','Judah','Finn','King','Brody','Xander','Nicolas','Charlie','Arlo','Emmanuel','Barrett','Felix','Alex','Miguel','Abel','Alan','Beckett','Amari','Karter'])

with open('plotto.xml', encoding='utf8') as f:
    contents = f.read()

plotto = objectify.fromstring(contents)

character = list(plotto.characters.character)
story_cast = {
"A": male_name(), #male protagonist
"A-2": male_name(), #male friend of A
"A-3": male_name(), #male rival or enemy of A
"A-4": male_name(), #male stranger
"A-5": male_name(), #male criminal
"A-6": male_name(), #male officer of the law
"A-7": male_name(), #male inferior, employee
"A-8": male_name(), #male utility symbol
"A-9": male_name(), #male superior, employer, one in authority
"B": female_name(), #female protagonist
"B-2": female_name(), #female friend of B
"B-3": female_name(), #female rival or enemy of B
"B-4": female_name(), #female stranger
"B-5": female_name(), #female criminal
"B-6": female_name(), #female officer of the law
"B-7": female_name(), #female inferior, employee
"B-8": female_name(), #female utility symbol
"B-9": female_name(), #female superior, employer. one in authority
"F-A": male_name(), #father of A
"M-A": female_name(), #mother of A
"BR-A": male_name(), #brother of A
"SR-A": female_name(), #sister of A
"SN-A": male_name(), #son of A
"D-A": female_name(), #daughter of A
"U-A": male_name(), #uncle of A
"AU-A": female_name(), #aunt of A
"CN-A": male_name(), #male cousin of A
"NW-A": male_name(), #nephew of A
"NC-A": female_name(), #niece of A
"GF-A": male_name(), #grandfather of A
"GM-A": female_name(), #grandmother of A
"SF-A": male_name(), #stepfather of A
"SM-A": female_name(), #stepmother of A
"GCH-A": any_name(), #grandchild of A
"F-B": male_name(), #father of B
"M-B": female_name(), #mother of B
"BR-B": male_name(), #brother of B
"SR-B": female_name(), #sister of B
"SN-B": male_name(), #son of B
"D-B": female_name(), #daughter of B
"U-B": male_name(), #uncle of B
"AU-B": female_name(), #aunt of B
"CN-B": female_name(), #female cousin of B
"NW-B": male_name(), #nephew of B
"NC-B": female_name(), #niece of B
"GF-B": male_name(), #grandfather of B
"GM-B": female_name(), #grandmother of B
"SF-B": male_name(), #stepfather of B
"SM-B": female_name(), #stepmother of B
"GCH-B": any_name(), #grandchild of B
"CH": female_name(),   # a child
"AX": male_name(), #a mysterious male person, or one of unusual character
"BX": female_name(), #a mysterious female person, or one of unusual character
"X": random_item() #an inanimate object, an object of mystery, an uncertain quantity
}

# basic character descriptions
subject = list(plotto.subjects.subject)

# predicate -> conflict -> outcome
predicate = list(plotto.predicates.predicate)
outcome = list(plotto.outcomes.outcome)
conflict = list(plotto.conflicts.conflict)

# predicates do not have leadups or carryons, just conflicts
predicate1 = random.choice(plotto.predicates.predicate)

# one predicate,  #62, does not have any conflict_links
# thus we must always check
predicate1 = random.choice(plotto.predicates.predicate)
if hasattr(predicate1, "conflict_link"):
    conflict1t = random.choice(predicate1.conflict_link)
    conflict1 = find_conflict(conflict1t.attrib["ref"])
    permutation1 = random.choice(conflict1.permutations.permutation)

predicate2 = random.choice(plotto.predicates.predicate)    
if hasattr(predicate2, "conflict_link"):
    conflict2t = random.choice(predicate2.conflict_link)
    conflict2 = find_conflict(conflict2t.attrib["ref"])
    permutation2 = random.choice(conflict2.permutations.permutation)

predicate3 = random.choice(plotto.predicates.predicate)    
if hasattr(predicate3, "conflict_link"):
    conflict3t = random.choice(predicate3.conflict_link)
    conflict3 = find_conflict(conflict3t.attrib["ref"])
    permutation3 = random.choice(conflict3.permutations.permutation)

if hasattr(conflict1, "lead_ups"):
    leadup1 = random.choice(conflict1.lead_ups.group).conflict_link.attrib["ref"]
    leadup1c = find_conflict(leadup1)
    leadup1cp = random.choice(leadup1c.permutations.permutation)
if hasattr(conflict1, "carry_ons"):
    carryon1 = random.choice(conflict1.carry_ons.group).conflict_link.attrib["ref"] 
    carryon1c = find_conflict(carryon1)
    carryon1cp = random.choice(carryon1c.permutations.permutation)
if hasattr(conflict2, "lead_ups"):
    leadup2 = random.choice(conflict2.lead_ups.group).conflict_link.attrib["ref"]
    leadup2c = find_conflict(leadup2)
    leadup2cp = random.choice(leadup2c.permutations.permutation)
if hasattr(conflict2, "carry_ons"):
    carryon2 = random.choice(conflict2.carry_ons.group).conflict_link.attrib["ref"] 
    carryon2c = find_conflict(carryon2)
    carryon2cp = random.choice(carryon2c.permutations.permutation)
if hasattr(conflict3, "lead_ups"):
    leadup3 = random.choice(conflict3.lead_ups.group).conflict_link.attrib["ref"]
    leadup3c = find_conflict(leadup3)
    leadup3cp = random.choice(leadup3c.permutations.permutation)
if hasattr(conflict3, "carry_ons"):
    carryon3 = random.choice(conflict3.carry_ons.group).conflict_link.attrib["ref"] 
    carryon3c = find_conflict(carryon3)
    carryon3cp = random.choice(carryon3c.permutations.permutation)

# Finally print out the plot
# Add cast of characters first
masterplot = "*** Protaganists ***\n"
masterplot = masterplot + "%A%: male, protagonist - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%B%: female, protagonist - " + random.choice(subject).description + "\n"
masterplot = masterplot + "\n"
masterplot = masterplot + "*** %A%'s Family***\n"
masterplot = masterplot + "%F-A%: male, father of %A% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%M-A%: female, mother of %A% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%BR-A%: male, brother of %A% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%SR-A%: female, sister of %A% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%SN-A%: male, son of %A% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%D-A%: female, daughter of %A% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%U-A%: male, uncle of %A% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%AU-A%: female, aunt of %A% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%CN-A%: male, cousin of %A% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%NW-A%: male, nephew of %A% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%NC-A%: female, niece of %A% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%GF-A%: male, grandfather of %A% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%GM-A%: female, grandmother of %A% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%SF-A%: male, stepfather of %A% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%SM-A%: female, stepmother of %A% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%GCH-A% any grandchild of %A% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "\n"
masterplot = masterplot + "*** Team %A% ***\n"
masterplot = masterplot + "%A-2%: male, friend of %A% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%A-3%: male, rival or enemy of %A% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%A-4%: male, stranger - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%A-5%: male, criminal - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%A-6%: male, officer of the law - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%A-7%: male, inferior, employee - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%A-8%: male, utility symbol - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%A-9%: male, superior, employer, one in authority - " + random.choice(subject).description + "\n"
masterplot = masterplot + "\n"
masterplot = masterplot + "*** %B%'s Family***\n"
masterplot = masterplot + "%F-B%: male, father of %B% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%M-B%: female, mother of %B% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%BR-B%: male, brother of %B% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%SR-B%: female, sister of %B% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%SN-B%: male, son of %B% - " + random.choice(subject).description + "\n" 
masterplot = masterplot + "%D-B%: female, daughter of %B% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%U-B%: male, uncle of %B% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%AU-B%: female, aunt of %B% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%CN-B%: female, cousin of %B% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%NW-B%: male, nephew of %B% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%NC-B%: female, niece of %B% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%GF-B%: male, grandfather of %B% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%GM-B%: female, grandmother of %B% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%SF-B%: male, stepfather of %B% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%SM-B%: female, stepmother of %B% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%GCH-B%: grandchild of %B% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "\n"
masterplot = masterplot + "*** Team %B% ***\n"
masterplot = masterplot + "%B-2%: female, friend of %B% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%B-3%: female, rival or enemy of %B% - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%B-4%: female, stranger - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%B-5%: female, criminal - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%B-6%: female, officer of the law - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%B-7%: female, inferior, employee - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%B-8%: female, utility symbol - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%B-9%: female, superior, employer. one in authority - " + random.choice(subject).description + "\n"
masterplot = masterplot + "\n"
masterplot = masterplot + "*** Unaffiliated Cast ***\n"
masterplot = masterplot + "%CH%: a child - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%AX%: male, a mysterious male person, or one of unusual character - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%BX%: female, a mysterious female person, or one of unusual character - " + random.choice(subject).description + "\n"
masterplot = masterplot + "%X% an inanimate object, an object of mystery, an uncertain quantity - " + random.choice(subject).description + "\n"
masterplot = masterplot + "\n"
masterplot = masterplot + f"Lead-up: {leadup1cp.description}\n"
masterplot = masterplot + f"Plot: {predicate1.description} - {permutation1.description}\n"
masterplot = masterplot + f"Carry-on: {carryon1cp.description}\n"
masterplot = masterplot + f"Outcome: {random.choice(plotto.outcomes.outcome).description}\n"
masterplot = masterplot + "\n"
masterplot = masterplot + f"Lead-up: {leadup2cp.description}\n"
masterplot = masterplot + f"Plot: {predicate2.description} - {permutation2.description}\n"
masterplot = masterplot + f"Carry-on: {carryon2cp.description}\n"
masterplot = masterplot + f"Outcome: {random.choice(plotto.outcomes.outcome).description}\n"
masterplot = masterplot + "\n"
masterplot = masterplot + f"Lead-up: {leadup3cp.description}\n"
masterplot = masterplot + f"Plot: {predicate3.description} - {permutation3.description}\n"
masterplot = masterplot + f"Carry-on: {carryon3cp.description}\n"
masterplot = masterplot + f"Outcome: {random.choice(plotto.outcomes.outcome).description}\n"


# clean up all the character references with names
for key in story_cast:
    masterplot = masterplot.replace(f'%{key}%', story_cast[key])

masterplot = masterplot.replace('“','"')
masterplot = masterplot.replace('”','"')
masterplot = masterplot.replace("’","'")
print (masterplot)
# subject-predicate-outcome
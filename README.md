## Introduction

Plotto By William Wallace Cook (1928) https://en.wikipedia.org/wiki/William_Wallace_Cook

Uses xml from https://github.com/eykd/plottoxml but modified slightly to work better with lxml.

Creates characters with first names and displays them, along with 3 different plot scenarios.  Although all characters mentioned in the system are generated, not all are used.

If you're looking for a quick and easy skeleton of a fictional story, this will help you.

## Requirements

Tested with Python 3.10
Uses lxml
If you do not have lxml:

```sh
pip install lxml
```

## Using Plotto

```sh
python plotto.py
```
If you would like to save the output to a file:
```sh
python plotto.py > plot.txt
```
## Wish List
Implement transform tags, currently unused.

Physical descriptions of characters, duplicate detection of names, some logic with character type.

Cleaner code for the output.

## Example
```sh Output
*** Protaganists ***
Alan: male, protagonist - A Person Influenced by an Obligation
Kai: female, protagonist - A Person Subjected to Adverse Conditions

*** Alan's Family***
Ezekiel: male, father of Alan - A Protecting Person
Zita: female, mother of Alan - A Married Person
Colton: male, brother of Alan - A Person Influenced by the Occult and the Mysterious
Molly: female, sister of Alan - A Person Subjected to Adverse Conditions
Chase: male, son of Alan - A Person Swayed by Pretense
Angelique: female, daughter of Alan - A Benevolent Person
Nathaniel: male, uncle of Alan - A Person Subjected to Adverse Conditions
Aurora: female, aunt of Alan - A Person in Love
Theodore: male, cousin of Alan - Any Person
Ace: male, nephew of Alan - A Benevolent Person
Nina: female, niece of Alan - A Person Influenced by the Occult and the Mysterious
Charles: male, grandfather of Alan - A Lawless Person
Abby: female, grandmother of Alan - A Person of Ideals
Mason: male, stepfather of Alan - A Person in Love
Jenna: female, stepmother of Alan - A Resentful Person
Aria any grandchild of Alan - A Person of Ideals

*** Team Alan ***
Weston: male, friend of Alan - A Person Influenced by the Occult and the Mysterious
Alex: male, rival or enemy of Alan - A Lawless Person
Milo: male, stranger - A Normal Person
August: male, criminal - An Erring Person
Cole: male, officer of the law - A Normal Person
Luka: male, inferior, employee - A Benevolent Person
Austin: male, utility symbol - A Married Person
Ryker: male, superior, employer, one in authority - A Resentful Person

*** Kai's Family***
Asher: male, father of Kai - A Person Influenced by an Obligation
Liza: female, mother of Kai - A Resentful Person
Aiden: male, brother of Kai - A Married Person
Aaliyah: female, sister of Kai - A Person Swayed by Pretense
Emmanuel: male, son of Kai - A Benevolent Person
Emelda: female, daughter of Kai - A Person Influenced by an Obligation
Juan: male, uncle of Kai - A Resentful Person
Ursula: female, aunt of Kai - A Normal Person
Jade: female, cousin of Kai - A Person in Love
Benjamin: male, nephew of Kai - A Person Swayed by Pretense
Hazel: female, niece of Kai - A Subtle Person
Axel: male, grandfather of Kai - A Protecting Person
Rosalie: female, grandmother of Kai - An Erring Person
Ryder: male, stepfather of Kai - An Erring Person
Eileen: female, stepmother of Kai - A Protecting Person
Matteo: grandchild of Kai - A Person in Love

*** Team Kai ***
Tatyana: female, friend of Kai - A Person Swayed by Pretense
Mae: female, rival or enemy of Kai - A Benevolent Person
Mae: female, stranger - A Protecting Person
Jessa: female, criminal - A Person Influenced by the Occult and the Mysterious
Carmen: female, officer of the law - A Person Swayed by Pretense
Thora: female, inferior, employee - A Lawless Person
Juliet: female, utility symbol - A Subtle Person
Vanessa: female, superior, employer. one in authority - A Resentful Person

*** Unaffiliated Cast ***
Esmeralda: a child - A Person Swayed by Pretense
Vincent: male, a mysterious male person, or one of unusual character - A Person Influenced by the Occult and the Mysterious
Kelly: female, a mysterious female person, or one of unusual character - A Resentful Person
shard an inanimate object, an object of mystery, an uncertain quantity - A Lawless Person

Lead-up: Alan mistakenly supposes his son, SN, to have perished in a tragic accident.
Plot: Rebelling against a power that controls personal abilities and holds them in subjection. - Alan struggles against an overwhelming sorrow that proves an obstacle to enterprise and holds his abilities in subjection.
Carry-on: Alan, hearing by chance a familiar name, finds his long-lost son, SN.
Outcome: Achieves success and happiness in a hard undertaking.

Lead-up: Alan leaves his coat on a cliff at the seaside, drops his hat in a stunted tree below the brink, and vanishes from the scenes that know him.
Plot: Devising a clever and plausible delusion in order to forward certain ambitious plans - Alan craftily fosters the delusion of his own death.
Carry-on: Alan, as a means of forcing a confession of guilt from Alex, throws both himself and Alex into a situation where death for both of them seems imminent.
Outcome: Reverses certain opinions when their fallacy is revealed.

Lead-up: Kai, an attractive girl, is so absorbed in serious pursuits that she subordinates everything else, even love, to her high ambition.
Plot: Seeking by unusual methods to conquer personal limitations. - Alan, seeking desperately his chance to propose marriage to Kai, rescues her from drowning, and proposes while they are clinging to an overturned boat.
Carry-on: Kai is unable to marry Alan because her father, Asher, in using Kai for his subject in a scientific experiment, has instilled a poison into her blood.
Outcome: Reverses certain opinions when their fallacy is revealed.
```

import re
# search regular expression website (regexr.com) to check the search of what will search when what we put

pattern = r"[a-z]ale"
text = '''
Sex is the trait that determines whether a sexually reproducing organism produces male or female gametes. 
During sexual reproduction, a male and a female gamete fuse to form a zygote, which develops into an offspring 
that inherits traits from each parent. By convention, organisms that produce smaller, more mobile gametes 
(spermatozoa, sperm) are called male, while organisms that produce produce larger, non-mobile gametes 
(ova, often called egg cells) are called female.[4] An organism that produces both types of gamete is hermaphrodite.

In non-hermaphroditic species, the sex of an individual is determined through one of several biological sex-determination 
systems. Most mammalian species have the XY sex-determination system, where the male usually carries an X and a Y chromosome (XY), 
and the female usually carries two X chromosomes (XX). Other chromosomal sex-determination systems in animals include the 
ZW system in birds, and the XO system in insects. Various environmental systems include temperature-dependent sex 
determination in reptiles and crustaceans.
'''

# match = re.search(pattern, text)
# print(match)

matches = re.finditer(pattern, text)
for match in matches:
    print(match)


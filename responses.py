import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'j!roll':
        return str(random.randint(1, 6))

    if p_message == 'j!copypasta':
        with open("copyPasta.txt", 'r') as file:
            total_lines = sum(1 for _ in file)

        random_line_number = random.randint(1, total_lines)

        random_line = None
        with open("copyPasta.txt", 'r') as file:
            for current_line_number, line in enumerate(file, 1):
                if current_line_number == random_line_number:
                    random_line = line.strip()
                    break

        if random_line:
            return random_line
        else:
            return "Error: Failed to make a CopyPasta."

    if p_message == 'j!smash':
        list =" Mario, Donkey Kong, Link, Samus, Dark Samus, Yoshi, Kirby, Fox, Pikachu, Luigi, Ness, Captain Falcon, Jigglypuff, Peach, Daisy, Bowser, Ice Climbers, Sheik, Zelda, Dr.Mario, Pichu, Falco, Marth, Lucina, Young Link, Ganondorf, Mewtwo, Roy, Chrom, Mr.Game & Watch, Meta Knight, Pit, Dark Pit, Zero Suit Samus, Wario, Snake, Ike, Pokemon Trainer, Diddy Kong, Lucas, Sonic, King Dedede, Olimar, Lucario, R.O.B., Toon Link, Wolf, Villager, Mega Man, Wii Fit Trainer, Rosalina & Luma, Little Mac, Greninja, Mii Fighter, Palutena, Pac - Man, Robin, Shulk, Bowser Jr., Duck Hunt, Ryu, Ken, Cloud, Corrin, Bayonetta, Inkling, Ridley, Simon, Richter, King K.Rool, Isabelle, Incineroar, Piranha Plant, Joker, Hero, Banjo & Kazooie, Terry, Byleth, Min Min, Steve, Sephiroth, Pyra / Mythra, Kazuya"
        list = list.split(',')
        randNum = random.randint(0, 82)
        return "Here is your random character: " + list[randNum]

    if p_message == 'j!val':
        list = "Astra, Breach, Brimstone, Chamber, Cypher, Jett, Kay / O, Killjoy, Neon, Omen, Phoenix, Raze, Reyna, Sage, Skye, Sova, Viper, Yoru, Gecco, Fade, Harbor"
        list = list.split(',')
        randNum = random.randint(0, 21)
        return "You should play: " + list[randNum]

    if p_message == "j!help":
        return "Here is the listed commands:\n j!roll\n j!smash\n j!val\n j!copypasta\n" \
               " j!spotify [*insert genre/word*] [*+/-* album]\n You can also add \"~\" for " \
               "the command to become a private dm! "

    if p_message.find('j!') == 0:
        return "This is not a listed command, try j!help for all the possible commands"








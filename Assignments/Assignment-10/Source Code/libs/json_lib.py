structure_characterSheet = {}
structure_item = {}




import PyPDF2
import json

def insert_data_into_pdf(template_path, json_path, output_path):
    # Read data from JSON file
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)

    # Create a PDF writer object
    pdf_writer = PyPDF2.PdfWriter()

    # Open the PDF template
    with open(template_path, 'rb') as template_file:
        # Create a PDF reader object for the template
        pdf_reader = PyPDF2.PdfReader(template_file)

        # Create a PDF file to store the merged result
        with open(output_path, 'wb') as output_file:
            # Iterate through each page in the template
            for page_num in range(pdf_reader.numPages):
                # Get the page from the template
                template_page = pdf_reader.getPage(page_num)

                # Create a new page with the same dimensions
                new_page = pdf_writer.addPage(template_page.mediaBox)

                # Overlay the template page with the data
                new_page.merge_page(template_page)
                page_text = new_page.extract_text()

                # Insert data into the PDF template
                for key, value in data.items():
                    page_text = page_text.replace(f'{{{key}}}', str(value))

                # Set the modified text to the new page
                new_page.mergeTranslatedPage(template_page, 0, 0)
                new_page.extract_text = lambda: page_text

            # Write the result to the output PDF file
            pdf_writer.write(output_file)


# Below is all testing stuff
if __name__ == "__main__":
    # Replace 'template.pdf' with the path to your PDF template
    template_path = 'template.pdf'

    # Replace 'input.json' with the path to your JSON data file
    json_path = 'input.json'

    # Replace 'output.pdf' with the desired output PDF file path
    output_path = 'output.pdf'

    # Insert data into PDF
    insert_data_into_pdf(template_path, json_path, output_path)

    print(f'Data inserted into PDF. Output saved to {output_path}')


# this is generated via a dnd 5e character sheet
structure_characterSheet = {
 'CharacterName': '',
 'Age': '',
 'Height': '',
 'Weight': '',
 'Eyes': '',
 'Skin': '',
 'Hair': '',
 'Allies': '',
 'FactionName': '',
 'Backstory': '',
 'Feat+Traits': '',
 'Treasure': '',
 'ClassLevel': None,
 'Background': None,
 'PlayerName': None,
 'CharacterName': None,
 'Race ': None,
 'Alignment': None,
 'XP': None,
 'Inspiration': None,
 'STR': None,
 'ProfBonus': None,
 'AC': None,
 'Initiative': None,
 'Speed': None,
 'PersonalityTraits ': None,
 'STRmod': None,
 'HPMax': None,
 'ST Strength': None,
 'DEX': None,
 'HPCurrent': None,
 'Ideals': None,
 'DEXmod ': None,
 'HPTemp': None,
 'Bonds': None,
 'CON': None,
 'HDTotal': None,
 'CONmod': None,
 'HD': None,
 'Flaws': None,
 'INT': None,
 'ST Dexterity': None,
 'ST Constitution': None,
 'ST Intelligence': None,
 'ST Wisdom': None,
 'ST Charisma': None,
 'Acrobatics': None,
 'Animal': None,
 'Athletics': None,
 'Deception ': None,
 'History ': None,
 'Insight': None,
 'Intimidation': None,
 'Wpn Name': None,
 'Wpn1 AtkBonus': None,
 'Wpn1 Damage': None,
 'INTmod': None,
 'Wpn Name 2': None,
 'Wpn2 AtkBonus ': None,
 'Wpn2 Damage ': None,
 'Investigation ': None,
 'WIS': None,
 'Wpn Name 3': None,
 'Wpn3 AtkBonus  ': None,
 'Arcana': None,
 'Wpn3 Damage ': None,
 'Perception ': None,
 'WISmod': None,
 'CHA': None,
 'Nature': None,
 'Performance': None,
 'Medicine': None,
 'Religion': None,
 'Stealth ': None,
 'Persuasion': None,
 'SleightofHand': None,
 'CHamod': None,
 'Survival': None,
 'AttacksSpellcasting': None,
 'Passive': None,
 'CP': None,
 'ProficienciesLang': None,
 'SP': None,
 'EP': None,
 'GP': None,
 'PP': None,
 'Equipment': None,
 'Features and Traits': None,
 'Spellcasting Class 2': '',
 'SpellcastingAbility 2': '',
 'SpellSaveDC  2': '',
 'SpellAtkBonus 2': '',
 'SlotsTotal 19': '',
 'SlotsRemaining 19': '',
 'Spells 1014': '',
 'Spells 1015': '',
 'Spells 1016': '',
 'Spells 1017': '',
 'Spells 1018': '',
 'Spells 1019': '',
 'Spells 1020': '',
 'Spells 1021': '',
 'Spells 1022': '',
 'Spells 1023': '',
 'Spells 1024': '',
 'Spells 1025': '',
 'Spells 1026': '',
 'Spells 1027': '',
 'Spells 1028': '',
 'Spells 1029': '',
 'Spells 1030': '',
 'Spells 1031': '',
 'Spells 1032': '',
 'Spells 1033': '',
 'SlotsTotal 20': '',
 'SlotsRemaining 20': '',
 'Spells 1034': '',
 'Spells 1035': '',
 'Spells 1036': '',
 'Spells 1037': '',
 'Spells 1038': '',
 'Spells 1039': '',
 'Spells 1040': '',
 'Spells 1041': '',
 'Spells 1042': '',
 'Spells 1043': '',
 'Spells 1044': '',
 'Spells 1045': '',
 'Spells 1046': '',
 'SlotsTotal 21': '',
 'SlotsRemaining 21': '',
 'Spells 1047': '',
 'Spells 1048': '',
 'Spells 1049': '',
 'Spells 1050': '',
 'Spells 1051': '',
 'Spells 1052': '',
 'Spells 1053': '',
 'Spells 1054': '',
 'Spells 1055': '',
 'Spells 1056': '',
 'Spells 1057': '',
 'Spells 1058': '',
 'Spells 1059': '',
 'SlotsTotal 22': '',
 'SlotsRemaining 22': '',
 'Spells 1060': '',
 'Spells 1061': '',
 'Spells 1062': '',
 'Spells 1063': '',
 'Spells 1064': '',
 'Spells 1065': '',
 'Spells 1066': '',
 'Spells 1067': '',
 'Spells 1068': '',
 'Spells 1069': '',
 'Spells 1070': '',
 'Spells 1071': '',
 'Spells 1072': '',
 'SlotsTotal 23': '',
 'SlotsRemaining 23': '',
 'Spells 1073': '',
 'Spells 1074': '',
 'Spells 1075': '',
 'Spells 1076': '',
 'Spells 1077': '',
 'Spells 1078': '',
 'Spells 1079': '',
 'Spells 1080': '',
 'Spells 1081': '',
 'SlotsTotal 24': None,
 'SlotsRemaining 24': '',
 'Spells 1082': '',
 'Spells 1083': '',
 'Spells 1084': '',
 'Spells 1085': '',
 'Spells 1086': '',
 'Spells 1087': '',
 'Spells 1088': '',
 'Spells 1089': '',
 'Spells 1090': '',
 'SlotsTotal 25': '',
 'SlotsRemaining 25': '',
 'Spells 1091': '',
 'Spells 1092': '',
 'Spells 1093': '',
 'Spells 1094': '',
 'Spells 1095': '',
 'Spells 1096': '',
 'Spells 1097': '',
 'Spells 1098': '',
 'Spells 1099': '',
 'SlotsTotal 26': '',
 'SlotsRemaining 26': '',
 'Spells 10100': '',
 'Spells 10101': '',
 'Spells 10102': '',
 'Spells 10103': '',
 'Spells 10104': '',
 'Spells 10105': '',
 'Spells 10106': '',
 'SlotsTotal 27': '',
 'SlotsRemaining 27': '',
 'Spells 10107': '',
 'Spells 10108': '',
 'Spells 10109': '',
 'Spells 101010': '',
 'Spells 101011': '',
 'Spells 101012': '',
 'Spells 101013': ''}


structure_spell = {
  "name": "",
  "level": 0,
  "school": "",
  "casting_time": "",
  "range": "",
  "components": [],
  "duration": "",
  "description": "",
  "classes": [],
  "higher_levels": "",
  "damage": {
    "type": "",
    "dice_count": 0,
    "dice_value": 0
  }
}

fireball_example = {
  "name": "Fireball",
  "level": 3,
  "school": "Evocation",
  "casting_time": "1 action",
  "range": "150 feet",
  "components": ["V", "S", "M (a tiny ball of bat guano and sulfur)"],
  "duration": "Instantaneous",
  "description": "A bright streak flashes from your pointing finger to a point you choose within range and then blossoms with a low roar into an explosion of flame.",
  "classes": ["Sorcerer", "Wizard"],
  "higher_levels": "When you cast this spell using a spell slot of 4th level or higher, the damage increases by 1d6 per level.",
  "damage": {
    "type": "Fire",
    "dice_count": 8,
    "dice_value": 6
  }
}

structure_item = {
  "name": "",
  "type": "",
  "rarity": "",
  "attunement": false,
  "attunement_requirements": "",
  "description": "",
  "properties": [],
  "modifiers": [],
  "requires_attunement": "",
  "weight": 0,
  "value": {
    "quantity": 0,
    "unit": ""
  },
  "source": {
    "book": "",
    "page": 0
  }
}


flametongue_example = {
  "name": "Flame Tongue",
  "type": "Weapon",
  "rarity": "Rare",
  "attunement": true,
  "attunement_requirements": "Requires attunement by a creature with the ability to speak Ignan.",
  "description": "This sword, forged with magical flames, grants its wielder the ability to deal additional fire damage.",
  "properties": ["Versatile (1d10)", "Finesse"],
  "modifiers": ["Deals an extra 2d6 fire damage on a successful hit."],
  "requires_attunement": "This sword requires attunement by a creature with the ability to speak Ignan.",
  "weight": 3,
  "value": {
    "quantity": 4500,
    "unit": "gold pieces"
  },
  "source": {
    "book": "Dungeon Master's Guide",
    "page": 170
  }
}

longsword_example = {
  "name": "Longsword",
  "type": "Weapon",
  "rarity": "Common",
  "attunement": false,
  "attunement_requirements": "",
  "description": "A standard longsword made of finely crafted steel.",
  "properties": ["Versatile (1d8)", "Melee"],
  "modifiers": [],
  "requires_attunement": "",
  "weight": 3,
  "value": {
    "quantity": 15,
    "unit": "gold pieces"
  },
  "source": {
    "book": "Player's Handbook",
    "page": 149
  }
}


WOT_PATH_DEFAULT = 'E:\\Games\\World_of_Tanks_CN'
DEST_DIR = 'E:\\Games\\World_of_Tanks_CN\\res_mods\\mods\\minimapData'

STANDARD_BATTLE_CODE = 'ctf'
ENCOUNTER_BATTLE_CODE = 'domination'
ASSAULT_CODE = 'assault'
ATT_DEF_CODE = 'assault2'
GRAND_BATTLE_CODE = 'ctf30x30'
ONSLAUGHT_CODE = 'comp7'

STANDARD_BATTLE = 'standard_battle'
ENCOUNTER_BATTLE = 'encounter_battle'
ASSAULT = 'assault'
ATT_DEF = 'att_def'
GRAND_BATTLE = '30x30'
ONSLAUGHT = 'onslaught'


def get_game_mode(code):
    if code == STANDARD_BATTLE_CODE:
        return STANDARD_BATTLE
    if code == ENCOUNTER_BATTLE_CODE:
        return ENCOUNTER_BATTLE
    if code == ASSAULT_CODE:
        return ASSAULT
    if code == ATT_DEF_CODE:
        return ATT_DEF
    if code == GRAND_BATTLE_CODE:
        return GRAND_BATTLE
    if code == ONSLAUGHT_CODE:
        return ONSLAUGHT


def get_event_type(code):
    if code == 'airstrike':
        return '1'
    if code == 'comms':
        return '2'

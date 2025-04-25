import subprocess

import os
from pathlib import Path

dir_path = Path(os.path.dirname(os.path.realpath(__file__)))


def weapon_command_list(list, default=True, description=None):
    return weapon_command(
        list[0],
        list[1],
        list[2],
        list[3],
        list[4],
        list[5],
        list[6:],
        default=default,
        description=description,
    )


def weapon_command(
    name, dmg, dtype, defense, rang, arch, tlist, default=True, description=None
):
    output = [
        "python3",
        str(dir_path / "create-weapon.py"),
        "-n",
        name,
        "-d",
        dmg,
        "-b",
        dtype,
        "-f",
        defense,
        "-r",
        rang,
        "-a",
        arch,
        "-t",
    ]
    output.extend(tlist)
    if not default:
        output.append("-x")
    if description:
        output.extend(["-j", description])
    return output


def fname(name):
    return name.lower().replace(" ", "-") + "-weapon.md"


weapons = [
    (
        [
            "Bastard Sword",
            "1d8",
            "S",
            "3",
            "adjacent",
            "long-blade",
            "Versatile(P, B)",
            "Metallic",
        ],
        """A sword that can effectively wielded in one or two hands. Comparable to a longsword but with a shorter handle and blade.""",
    ),
    (
        ["Battleax", "1d8", "S", "3", "adjacent", "ax", "Metallic"],
        """A single or double bladed ax wielded in one or two hands with a short haft.""",
    ),
    (
        ["Blowgun", "1d4", "P", "1", "short", "short-arm", "Loaded(1)"],
        """A tube or reed used to shoot small ammunition using your mouth.""",
    ),
    (
        ["Club", "1d4", "B", "2", "adjacent", "cudgel", "Light"],
        """A short, single handed blunt weapon.""",
    ),
    (
        [
            "Curved Blade",
            "1d6",
            "S",
            "2",
            "adjacent",
            "short-blade",
            "Light",
            "Metallic",
        ],
        """A short curved blade wielded in one hand.""",
    ),
    (
        [
            "Dagger",
            "1d4",
            "P",
            "1",
            "adjacent",
            "short-blade",
            "Light",
            "Thrown(close)",
            "Versatile(S)",
            "Metallic",
        ],
        """A small bladed, single handed weapon used for stabbing.""",
    ),
    (
        ["Dart", "1d4", "P", "1", "close", "short-arm", "-"],
        """A piercing weapon that is thrown, looks like a thin spike.""",
    ),
    (
        ["Flail", "1d8", "B", "2", "adjacent", "cudgel", "Metallic"],
        """A one or two handed half with a blunted weight suspended from a chain.""",
    ),
    (
        [
            "Glaive",
            "1d10",
            "S",
            "2",
            "adjacent",
            "polearm",
            "Counter",
            "Two-handed",
            "Metallic",
        ],
        """A polearm of war primarily used by slashing, wielded in two hands.""",
    ),
    (
        ["Greatax", "1d12", "S", "2", "adjacent", "ax", "Two-handed", "Metallic"],
        """A long half, two-handed ax.""",
    ),
    (
        [
            "Greatsword",
            "2d6",
            "S",
            "3",
            "adjacent",
            "long-blade",
            "Two-handed",
            "Versatile(P)",
            "Metallic",
        ],
        """A two handed sword of great length and weight. Used most effectively in large sweeping motions.""",
    ),
    (
        ["Greatclub", "1d10", "B", "3", "adjacent", "cudgel", "Two-handed"],
        """A large blunt weapon.""",
    ),
    (
        [
            "Halberd",
            "1d10",
            "S",
            "2",
            "adjacent",
            "polearm",
            "Counter",
            "Two-handed",
            "Versatile(P)",
            "Metallic",
        ],
        """A pole arm of war used to slash and pierce. A spear and ax on a long stick.""",
    ),
    (
        ["Hand Crossbow", "1d6", "P", "1", "close", "short-arm", "Loaded(1)"],
        """A crossbow able to be wielded in one hand. Fires bolts.""",
    ),
    (
        [
            "Hammer",
            "1d4",
            "B",
            "2",
            "adjacent",
            "cudgel",
            "Light",
            "Thrown(close)",
            "Metallic",
        ],
        """A short haft weapon ended with a hammer head.""",
    ),
    (
        [
            "Handax",
            "1d4",
            "S",
            "2",
            "adjacent",
            "ax",
            "Light",
            "Thrown(close)",
            "Metallic",
        ],
        """Short haft weapon ended with an ax head.""",
    ),
    (
        [
            "Heavy Crossbow",
            "1d10",
            "P",
            "1",
            "long",
            "long-arm",
            "Loaded(1)",
            "Two-handed",
        ],
        """A crossbow properly wielded in two hands. Fires bolts.""",
    ),
    (
        ["Javelin", "1d6", "P", "1", "close", "short-arm", "Metallic"],
        """A short spear used primarily for throwing.""",
    ),
    (
        [
            "Knife",
            "1d4",
            "S",
            "1",
            "adjacent",
            "short-blade",
            "Light",
            "Versatile(P)",
            "Metallic",
        ],
        """Any knife that is primarily used to slash.""",
    ),
    (
        [
            "Lance",
            "1d10",
            "P",
            "2",
            "adjacent",
            "polearm",
            "Two-handed (one handed while mounted)",
        ],
        """A long heavy spear used while on horseback.""",
    ),
    (
        ["Light Crossbow", "1d8", "P", "1", "long", "long-arm", "Loaded(1)"],
        """A medium sized crossbow. Fires bolts.""",
    ),
    (
        ["Longbow", "1d8", "P", "1", "long", "long-arm", "Two-handed", "Loaded(0)"],
        """A proper bow for war. Fires arrows.""",
    ),
    (
        [
            "Longsword",
            "1d8",
            "S",
            "3",
            "adjacent",
            "long-blade",
            "Two-handed",
            "Versatile(P, B)",
        ],
        """A long blade wielded in two hands. Versatile and jack-of-all-trades sword.""",
    ),
    (
        ["Mace", "1d6", "B", "3", "adjacent", "cudgel", "Metallic"],
        """A heavy one handed metal club.""",
    ),
    (
        ["Maul", "2d6", "B", "3", "adjacent", "cudgel", "Two-handed", "Metallic"],
        """A purpose built great club used to bludgeon.""",
    ),
    (
        [
            "Morningstar",
            "1d8",
            "B",
            "2",
            "adjacent",
            "cudgel",
            "Versatile(P)",
            "Metallic",
        ],
        """A mace with spikes.""",
    ),
    (
        ["Pike", "1d10", "P", "1", "adjacent", "polearm", "Counter", "Two-handed"],
        """Crude long-spear. The weapon of peasants.""",
    ),
    (
        ["Rapier", "1d8", "P", "3", "adjacent", "short-blade", "Counter", "Metallic"],
        """A thin bladed sword wielded in one hand.""",
    ),
    (
        ["Shortbow", "1d6", "P", "1", "short", "long-arm", "Two-handed", "Loaded(0)"],
        """Shorter than a longbow. Fires arrows.""",
    ),
    (
        [
            "Shortsword",
            "1d6",
            "P",
            "2",
            "adjacent",
            "short-blade",
            "Light",
            "Versatile(S)",
            "Metallic",
        ],
        """A one handed short blade, longer than a dagger and knife.""",
    ),
    (
        ["Sling", "1d4", "B", "1", "short", "short-arm", "Loaded(0)"],
        """A length of rope that is used to throw stones. Fires stones or pellets.""",
    ),
    (
        [
            "Spear",
            "1d6",
            "P",
            "1",
            "adjacent",
            "polearm",
            "Counter",
            "Thrown(close)",
            "Metallic",
        ],
        """A long haft ended with a sharp point.""",
    ),
    (
        ["Staff", "1d6", "B", "2", "adjacent", "cudgel", "Counter"],
        """A walking staff or the like.""",
    ),
    (
        [
            "Trident",
            "1d6",
            "P",
            "2",
            "adjacent",
            "polearm",
            "Counter",
            "Thrown(close)",
            "Metallic",
        ],
        """A spear that is ended with three points, like a big fork.""",
    ),
    (
        [
            "Bident",
            "1d6",
            "P",
            "2",
            "adjacent",
            "polearm",
            "Counter",
            "Thrown(close)",
            "Metallic",
        ],
        """A spear that is ended with two points.""",
    ),
    (
        ["War pick", "1d8", "P", "2", "adjacent", "ax", "Metallic"],
        """Simpler to a pickax, used to fight.""",
    ),
    (
        ["Whip", "1d4", "P", "1", "adjacent", "whip", "Counter", "Light"],
        """A length of rope or leather used to strike at foes.""",
    ),
    (
        ["Buckler", "1d4", "B", "5", "adjacent", "shield", "Light", "Metallic"],
        """A small round shield. Offers some protection.""",
    ),
    (
        ["Shield", "1d4", "B", "10", "adjacent", "shield", "Metallic"],
        """Standard kite or heater shield. Offers good protection.""",
    ),
    (
        ["Round Shield", "1d4", "B", "7", "adjacent", "shield", "-"],
        """A round wooden shield.""",
    ),
    (
        ["Heavy Shield", "1d4", "B", "15", "adjacent", "shield", "Metallic"],
        """Larger shields, heavy to carry around.""",
    ),
    (
        ["Tower Shield", "1d4", "B", "20", "adjacent", "shield", "Metallic"],
        """Full body shields that are carried. Very heavy shields.""",
    ),
    (
        [
            "Pavise",
            "1d4",
            "B",
            "20",
            "adjacent",
            "shield",
            "Two-handed",
            "Planted",
            "Metallic",
        ],
        """A tower shield that is designed to be planted as cover during battle.""",
    ),
]

for weapon, description in weapons:
    with open(
        str(dir_path.parent / "content/core/ref" / fname(weapon[0])),
        "w+",
        encoding="utf-8",
    ) as file:
        if type(weapon[-1]) is bool and not weapon[-1]:
            subprocess.run(
                weapon_command_list(
                    weapon[:-1], default=False, description=description
                ),
                stdout=file,
            )
        else:
            subprocess.run(
                weapon_command_list(weapon, description=description), stdout=file
            )

print("May need to run again for an active server to register changes")

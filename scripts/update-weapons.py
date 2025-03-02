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
        ["Bastard Sword", "1d8", "S", "3", "adjacent", "long-blade", "Versatile(P, B)"],
        None,
    ),
    (["Battleax", "1d8", "S", "3", "adjacent", "ax", "-"], None),
    (["Blowgun", "1d4", "P", "1", "short", "short-arm", "Loaded(1)"], None),
    (["Club", "1d4", "B", "2", "adjacent", "cudgel", "Light"], None),
    (
        ["Curved Blade", "1d6", "S", "2", "adjacent", "short-blade", "Light"],
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
        ],
        None,
    ),
    (["Dart", "1d4", "P", "1", "close", "short-arm", "-"], None),
    (["Flail", "1d8", "B", "2", "adjacent", "cudgel", "-"], None),
    (
        ["Glaive", "1d10", "S", "2", "adjacent", "polearm", "Counter", "Two-handed"],
        None,
    ),
    (["Greatax", "1d12", "S", "2", "adjacent", "ax", "Two-handed"], None),
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
        ],
        None,
    ),
    (["Greatclub", "1d10", "B", "3", "adjacent", "cudgel", "Two-handed"], None),
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
        ],
        None,
    ),
    (["Hand Crossbow", "1d6", "P", "1", "close", "short-arm", "Loaded(1)"], None),
    (["Hammer", "1d4", "B", "2", "adjacent", "cudgel", "Light", "Thrown(close)"], None),
    (["Handax", "1d4", "S", "2", "adjacent", "ax", "Light", "Thrown(close)"], None),
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
        None,
    ),
    (["Javelin", "1d6", "P", "1", "close", "short-arm", "-"], None),
    (
        ["Knife", "1d4", "S", "1", "adjacent", "short-blade", "Light", "Versatile(P)"],
        None,
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
        None,
    ),
    (["Light Crossbow", "1d8", "P", "1", "long", "long-arm", "Loaded(1)"], None),
    (["Longbow", "1d8", "P", "1", "long", "long-arm", "Two-handed", "Loaded(0)"], None),
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
        None,
    ),
    (["Mace", "1d6", "B", "3", "adjacent", "cudgel", "-"], None),
    (["Maul", "2d6", "B", "3", "adjacent", "cudgel", "Two-handed"], None),
    (["Morningstar", "1d8", "B", "2", "adjacent", "cudgel", "Versatile(P)"], None),
    (["Pike", "1d10", "P", "1", "adjacent", "polearm", "Counter", "Two-handed"], None),
    (["Rapier", "1d8", "P", "3", "adjacent", "short-blade", "Counter"], None),
    (
        ["Shortbow", "1d6", "P", "1", "short", "long-arm", "Two-handed", "Loaded(0)"],
        None,
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
        ],
        None,
    ),
    (["Sling", "1d4", "B", "1", "short", "short-arm", "Loaded(0)"], None),
    (
        ["Spear", "1d6", "P", "1", "adjacent", "polearm", "Counter", "Thrown(close)"],
        None,
    ),
    (["Staff", "1d6", "B", "2", "adjacent", "cudgel", "Counter"], None),
    (
        ["Trident", "1d6", "P", "2", "adjacent", "polearm", "Counter", "Thrown(close)"],
        None,
    ),
    (
        ["Bident", "1d6", "P", "2", "adjacent", "polearm", "Counter", "Thrown(close)"],
        None,
    ),
    (["War pick", "1d8", "P", "2", "adjacent", "ax", "-"], None),
    (["Whip", "1d4", "P", "1", "adjacent", "whip", "Counter", "Light"], None),
    (["Buckler", "1d4", "B", "5", "adjacent", "shield", "Light"], None),
    (["Shield", "1d4", "B", "10", "adjacent", "shield", "-"], None),
    (["Heavy Shield", "1d4", "B", "15", "adjacent", "shield", "-"], None),
    (["Tower Shield", "1d4", "B", "20", "adjacent", "shield", "-"], None),
    (["Pavise", "1d4", "B", "20", "adjacent", "shield", "Two-handed", "Planted"], None),
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

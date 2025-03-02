import subprocess

import os
from pathlib import Path

dir_path = Path(os.path.dirname(os.path.realpath(__file__)))


def armor_command_list(list, default=True, description=None):
    return armor_command(
        list[0], list[1], list[2], list[3:], default=default, description=description
    )


def armor_command(name, defense, arch, tlist, default=True, description=None):
    output = [
        "python3",
        str(dir_path / "create-armor.py"),
        "-n",
        name,
        "-f",
        defense,
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
    return name.lower().replace(" ", "-") + "-armor.md"


armors = [
    (
        ["Clothing", "-", "unarmored", "Comfortable"],
        """Any type of normal clothing not meant as armor.""",
    ),
    (["Robes", "-", "unarmored", "Comfortable"], None),
    (["Leather", "5", "light", "Comfortable"], None),
    (["Studded Leather", "7", "light", "-"], None),
    (["Padded Armor", "10", "light", "-"], None),
    (["Hide Armor", "10", "medium", "-"], None),
    (["Chain Mail", "12", "medium", "Noisy", "Metallic"], None),
    (["Scale Mail", "14", "medium", "Noisy", "Restrictive", "Metallic"], None),
    (["Partial Plate", "15", "medium", "Noisy", "Restrictive", "Metallic"], None),
    (["Half Plate", "17", "heavy", "Noisy", "Bulwark", "Metallic"], None),
    (["Full Plate", "20", "heavy", "Noisy", "Bulwark", "Metallic"], None),
]

for armor, description in armors:
    with open(
        str(dir_path.parent / "content/core/ref" / fname(armor[0])),
        "w+",
        encoding="utf-8",
    ) as file:
        if type(armor[-1]) is bool and not armor[-1]:
            subprocess.run(
                armor_command_list(armor[:-1], default=False, description=description),
                stdout=file,
            )
        else:
            subprocess.run(
                armor_command_list(armor, description=description), stdout=file
            )

print("May need to run again for an active server to register changes")

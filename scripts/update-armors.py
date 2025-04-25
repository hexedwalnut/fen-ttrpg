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
    (
        ["Robes", "-", "unarmored", "Comfortable"],
        """Loose flowing robes or garments, often worn by nobility and scholars.""",
    ),
    (
        ["Leather", "5", "light", "Comfortable"],
        """Special made clothes reinforced with hardened leather to offer moderate protection. Might include a helmet, leather chest plate, and arm and leg protection.""",
    ),
    (
        ["Studded Leather", "7", "light", "-"],
        """Leather armor reinforced with metal studs that offer increased protection and defensive ability.""",
    ),
    (
        ["Padded Armor", "10", "light", "-"],
        """Armor worn under medium and heavy armor. Thick padded cloth offers the greatest amount of protection for light armor.""",
    ),
    (
        ["Hide Armor", "10", "medium", "-"],
        """Extra heavy and hardened leather armor.""",
    ),
    (
        ["Chain Mail", "12", "medium", "Noisy", "Metallic"],
        """A simple chain shirt and basic helmet. Worn over padded armor, included in this armor description. Sometimes augmented with gloves, shin/leg protection, or shoulder armor.""",
    ),
    (
        ["Scale Mail", "14", "medium", "Noisy", "Restrictive", "Metallic"],
        """A metal shirt made of singular plate scales, basic armor and leg protection, and a helmet. Worn over padded armor, included in this armor description.""",
    ),
    (
        ["Partial Plate", "15", "medium", "Noisy", "Restrictive", "Metallic"],
        """A simple chain shirt, heavy helm, and either a fully plated arm or leg augmentation. Worn over padded armor, included in this armor description.""",
    ),
    (
        ["Half Plate", "17", "heavy", "Noisy", "Bulwark", "Metallic"],
        """A simple chain shirt, heavy helm, and full plated upper body, including arm protection, gauntlets, and chest plate. Worn over padded armor, included in this armor description.""",
    ),
    (
        ["Full Plate", "20", "heavy", "Noisy", "Bulwark", "Metallic"],
        """A simple chain shirt, heavy helm, and full plated protection, including arm and leg protection, chest plate, and gauntlets. Worn over padded armor, included in this description.""",
    ),
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

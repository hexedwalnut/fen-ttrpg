import subprocess
import os
from pathlib import Path

dir_path = Path(os.path.dirname(os.path.realpath(__file__)))


def specialization_command(name, kind, cost, tlist, plist, description, addition=None):
    output = [
        "python3",
        str(dir_path / "create-specialization.py"),
        "-n",
        name,
        "-k",
        kind,
        "-t",
    ]
    output.extend(tlist)
    output.append("-p")
    output.extend(plist)
    output.append("-d")
    output.append(description)
    output.append("-c")
    output.append(cost)
    if addition:
        output.append("-a")
        output.extend(addition)
    return output


def specialization_command_entry(entry, addition=None):
    return specialization_command(
        entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], addition=addition
    )


def fname(name):
    return name.lower().replace(" ", "-") + "-specialization.md"


specializations = [
    (
        (
            "Talent",
            "basic",
            "0",
            ["Repeatable"],
            ["-"],
            """Select a skill your actor has that was not selected by the [Assurance]({{< ref "/core/ref/assurance-specialization.md" >}}) specialization. Increase its die by one increment.""",
        ),
        None,
    ),
    (
        (
            "Assurance",
            "basic",
            "0",
            ["Repeatable(4) per skill"],
            ["-"],
            """Pick a skill your actor has. Increase the number of dice rolled for this skill by 1. For example, if your actor has 1d6 in the Fight skill, after taking this specialization, your actor would roll 2d6 in the Fight skill. Note, once a skill is selected for Assurance it cannot be selected for [Talent]({{< ref "/core/ref/talent-specialization.md" >}}). This means that once you select Assurance on a skill, you can never increase the sides of the die.""",
        ),
        None,
    ),
    (
        (
            "Coordination",
            "basic",
            "0",
            ["Repeatable(4)"],
            ["tactics(1d8+)"],
            """You gain an additional passive action per turn.""",
        ),
        None,
    ),
    (
        (
            "Aggressive",
            "basic",
            "0",
            ["Repeatable(4)"],
            ["fight(1d8+)"],
            """You gain an additional aggressive action""",
        ),
        None,
    ),
    (
        (
            "Opportunity Attack",
            "basic",
            "0",
            ["-"],
            ["tactics(1d6+)"],
            """You gain the [**Opportunity Attack**]({{< ref "/core/ref/opportunity-attack-reaction.md" >}}) reaction.""",
        ),
        None,
    ),
    (
        (
            "Vitality",
            "basic",
            "0",
            ["Repeatable"],
            ["-"],
            """Roll non-explosive [vigor]({{< ref "/core/ref/vigor-skill.md" >}}) (or take half the skill die's sides) and add the result to maximum HP.""",
        ),
        None,
    ),
    (
        (
            "Reactive",
            "basic",
            "0",
            ["Repeatable(4)"],
            ["dodge(1d8+)"],
            """You gain an additional reaction per round.""",
        ),
        None,
    ),
    (
        (
            "Knife Fighter",
            "weapon",
            "0",
            ["Repeatable(4)"],
            ["-"],
            """You gain an additional die when rolling damage using a weapon 
            with the [short-blade]({{< ref "/core/ref/short-blade.md" >}}) 
            archetype. The type of die is determined by the default sides of 
            the weapon. For example, a standard 
            [Dagger]({{< ref "/core/ref/dagger-weapon.md" >}}) has a weapon die 
            of 1d4. When rolling damage after taking this specialization you 
            instead roll 2d4. If, instead, the weapon had multiple default 
            weapon dice you only add one additional die of the highest sides.
            If a weapon by default rolls 1d4+2d6+3d8 you gain an additional 1d8
            after taking this specialization. This specialization applies to 
            offhanded weapons as well.""",
        ),
        ["short-blade-specialization"],
    ),
    (
        (
            "Manuscripts and Codices",
            "weapon",
            "0",
            ["Repeatable(4)"],
            ["-"],
            """You gain an additional die when rolling damage using a weapon 
            with the [long-blade]({{< ref "/core/ref/long-blade.md" >}}) 
            archetype. The type of die is determined by the default sides of 
            the weapon. For example, a standard 
            [Longsword]({{< ref "/core/ref/longsword-weapon.md" >}}) has a weapon die 
            of 1d8. When rolling damage after taking this specialization you 
            instead roll 2d8. If, instead, the weapon had multiple default 
            weapon dice you only add one additional die of the highest sides.
            If a weapon by default rolls 1d4+2d6+3d8 you gain an additional 1d8
            after taking this specialization. This specialization applies to 
            offhanded weapons as well.""",
        ),
        ["long-blade-specialization"],
    ),
    (
        ("", "weapon", "0", ["Repeatable(4)"], ["-"], """"""),
        ["short-arm-specialization"],
    ),
    (
        ("Target Practice", "weapon", "0", ["Repeatable(4)"], ["-"], """"""),
        ["long-arm-specialization"],
    ),
]

for specialization, addition in specializations:
    with open(
        str(dir_path.parent / "content/core/ref" / fname(specialization[0])),
        "w+",
        encoding="utf-8",
    ) as file:
        if addition:
            subprocess.run(
                specialization_command_entry(specialization, addition=addition),
                stdout=file,
            )
        else:
            subprocess.run(specialization_command_entry(specialization), stdout=file)

def validate(sp):
    if not sp["name"]:
        print("No name")
        return False
    if not sp["type"]:
        print(f"{sp["name"]}: no type")
        return False
    if not sp["cost"]:
        print(f"{sp["name"]}: no cost")
        return False
    if not sp["abstract"]:
        print(f"{sp["name"]}: no abstract")
        return False
    if not sp["module"]:
        print(f"{sp["name"]}: no module")
        return False

    if not sp["scale"]:
        print(f"{sp["name"]}: no scale")
        return False
    if sp["scale"].lower().strip() not in ["all", "skirmish", "battle", "war"]:
        print(f"{sp["name"]}: scale not correct ({sp["scale"]})")
        return False

    if sp["traits"] and not isinstance(sp["traits"], list):
        print(f"{sp["name"]}: traits not a list it is a {type(sp["traits"])}")
        return False
    if sp["prereqs"] and not isinstance(sp["prereqs"], list):
        print(f"{sp["name"]}: prereqs not a list")
        return False
    if sp["tags"] and not isinstance(sp["tags"], list):
        print(f"{sp["name"]}: tags not a list")
        return False
    return True

def dict_to_specialization(sp):
    if validate(sp):
        return create_specialization(
            sp["name"].strip(),
            sp["type"].strip(),
            sp["cost"],
            sp["traits"],
            sp["prereqs"],
            sp["text"],
            sp["tags"],
            sp["abstract"].strip(),
            sp["module"].strip(),
            sp["scale"].strip(),
        )
    else:
        return None


def create_specialization(
    name, type, cost, traits, prereqs, text, tags, abstract, module, scale
):
    output = f"""+++
draft=false
title="{name}"
tags=["specialization", "{str(type)}-specialization\", "{str(module)}-module", "{str(scale)}-scale\""""

    if tags:
        for i in range(0, len(tags)):
            output += f', "{tags[i]}"'
    output += "]"

    output += f"""

[params]
  abstract="{abstract}"
  [params.specialization]
    module="{str(module)}"
    cost="{cost} sp"
    scale="{str(scale)}"
    traits=["""

    if traits:
        output += f'"{traits[0]}"'
        for i in range(1, len(traits)):
            output += f', "{traits[i]}"'
    else:
        output += '"-"'
    output += """]
    prereq=["""

    if prereqs:
        output += f'"{prereqs[0]}"'
        for i in range(1, len(prereqs)):
            output += f', "{prereqs[i]}"'
    else:
        output += '"-"'
    output += f"""]
+++

{{{{< specialization-front >}}}}

## Description

{text}
"""

    return output

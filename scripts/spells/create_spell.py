def validate(sp):
    if not sp["name"]:
        print("No name")
        return False
    if not sp["mp"]:
        print(f"{sp["name"]}: No mp cost")
        return False
    if not sp["text"]:
        print(f"{sp["name"]}: No text")
        return False
    if not sp["abstract"]:
        print(f"{sp["name"]}: No abstract")
        return False
    if not sp["module"]:
        print(f"{sp["name"]}: No module")
        return False

    if not sp["action"]:
        print(f"{sp["name"]}: no action")
        return False
    if sp["action"].lower().strip() not in ["major", "minor", "reaction"]:
        print(f"{sp["name"]}: action not correct ({sp["action"]})")
        return False

    if not sp["scale"]:
        print(f"{sp["name"]}: no scale")
        return False
    if sp["scale"].lower().strip() not in ["all", "skirmish", "battle", "war"]:
        print(f"{sp["name"]}: scale not correct ({sp["scale"]})")
        return False

    if sp["traits"] and not isinstance(sp["traits"], list):
        print(f"{sp["name"]}: traits not a list")
        return False
    if sp["list"] and not isinstance(sp["list"], list):
        print(f"{sp["name"]}: list not a list")
        return False
    if sp["tags"] and not isinstance(sp["tags"], list):
        print(f"{sp["name"]}: tags not a list")
        return False

    return True

def dict_to_spell(sp):
    if validate(sp):
        return create_spell(
            sp["name"].strip(),
            sp["mp"],
            sp["action"].strip().lower(),
            sp["traits"],
            sp["list"],
            sp["text"].strip(),
            sp["tags"],
            sp["abstract"].strip(),
            sp["module"].strip().lower(),
            sp["scale"].strip().lower(),
        )
    else:
        return None

def create_spell(
    name, mp, action, traits, spell_list, text, tags, abstract, module, scale
):
    output = f"""+++
draft=false
title="{name}"
tags=["spell", "{str(module)}-module", "{str(scale)}-scale\""""

    if spell_list:
        for l in spell_list:
            output += f', "{l.strip().lower()}-spell-list"'
    
    if tags:
        for t in tags:
            output += f', "{t.strip().lower()}"'

    output += "]"

    output += f"""

[params]
  abstract="{abstract}"
  [params.spell]
    module="{str(module)}"
    mp="{mp} mp"
    action="{str(action)}"
    scale="{str(scale)}"
    traits=["""

    if traits:
        output += f'"{traits[0]}"'
        for i in range (1, len(traits)):
            output += f', "{traits[i]}"'
    else:
        output += '"-"'
    output += """]
    list=["""
    if spell_list:
        output += f'"{spell_list[0]}"'
        for i in range (1, len(spell_list)):
            output += f', "{traits[i]}"'
    else:
        output += '"-"'
    output += f"""]
+++

{{{{< spell-front >}}}}

## Description

{text}
"""
    return output

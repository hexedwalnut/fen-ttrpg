import os
import glob
import yaml
from pathlib import Path
from create_spell import dict_to_spell

def fname(name):
    return name.lower().replace(" ", "-").replace("'", "").replace("/", "-") + "-spell.md"


dir_path = Path(os.path.dirname(os.path.realpath(__file__)))

old_spells = glob.glob("../../content/**/*-spell.md", root_dir=dir_path, recursive=True)
for spell in old_spells:
    os.remove(spell)

spells = glob.glob("./data/**/*.yaml", root_dir=dir_path, recursive=True)

for spell in spells:
    path = Path(spell)
    sp = yaml.safe_load(path.read_text())
    file_text = dict_to_spell(sp)

    # if the file_text does not get converted
    if not file_text:
        continue

    # create the module directory if it doesn't exists
    file_path = dir_path.parent.parent / "content" / sp["module"] / "ref"
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    with open(
        str(
            file_path
            / fname(sp["name"])
        ),
        "w+",
        encoding="utf-8",
    ) as file:
        file.write(file_text)

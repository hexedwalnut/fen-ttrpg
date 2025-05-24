import os
import glob
import yaml
from pathlib import Path
from create_specialization import dict_to_specialization


def fname(name):
    return name.lower().replace(" ", "-").replace("'", "") + "-specialization.md"

dir_path = Path(os.path.dirname(os.path.realpath(__file__)))

old_specializations = glob.glob("../../content/**/*-specialization.md", root_dir=dir_path, recursive=True)
for specialization in old_specializations:
    os.remove(specialization)

# get all specialization `.yaml` files
specializations = glob.glob("./data/**/*.yaml", root_dir=dir_path, recursive=True)

# make all the specialization files
for specialization in specializations:
    path = Path(specialization)
    sp = yaml.safe_load(path.read_text())
    file_text = dict_to_specialization(sp)

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

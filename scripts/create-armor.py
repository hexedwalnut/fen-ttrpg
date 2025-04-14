import argparse
from enum import Enum


class Archetype(Enum):
    unarmored = "unarmored"
    light = "light"
    medium = "medium"
    heavy = "heavy"

    def __str__(self):
        return self.value


parser = argparse.ArgumentParser()
parser.add_argument("--name", "-n", help="The name of the armor", required=True)
parser.add_argument("--defense", "-f", help="The defense of the armor", required=True)
parser.add_argument(
    "--archetype",
    "-a",
    help="The archetype of the armor",
    choices=list(Archetype),
    required=True,
    type=Archetype,
)
parser.add_argument("--traits", "-t", help="The traits of the weapon", nargs="*")
parser.add_argument("--default", "-x", help="If not default", action="store_false")
parser.add_argument(
    "--description", "-j", help="Long description of the weapon", required=False
)

args = parser.parse_args()

output = f"""+++
draft=false
title="{args.name}"
tags=["{'default", "armor"' if args.default else 'armor"'}, "equipment", "{args.archetype}"]

[params]
  abstract = "{args.description}"
  [params.armor]
    def="{args.defense}"
    arch="{str(args.archetype).capitalize()}"
    traits=["""


output += f'"{args.traits[0]}"'
for i in range(1, len(args.traits)):
    output += f', "{args.traits[i]}"'

output += """]
+++

{{< armor-table >}}

"""

if args.description:
    output += "## Description\n" + args.description

print(output)

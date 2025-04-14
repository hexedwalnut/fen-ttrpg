import argparse
from enum import Enum


class Range(Enum):
    adjacent = "adjacent"
    close = "close"
    short = "short"
    long = "long"
    extreme = "extreme"

    def __str__(self):
        return self.value


class Archetype(Enum):
    cudgel = "cudgel"
    short_arm = "short-arm"
    long_arm = "long-arm"
    short_blade = "short-blade"
    long_blade = "long-blade"
    ax = "ax"
    polearm = "polearm"
    shield = "shield"
    ammunition = "ammunition"
    whip = "whip"

    def __str__(self):
        return self.value


parser = argparse.ArgumentParser()
parser.add_argument("--name", "-n", help="The name of the weapon", required=True)
parser.add_argument("--dmg", "-d", help="The damage of the weapon", required=True)
parser.add_argument(
    "--dtype", "-b", help="The damage type of the weapon", required=True
)
parser.add_argument(
    "--defense", "-f", help="The defense of the weapon", type=int, required=True
)
parser.add_argument(
    "--range",
    "-r",
    help="The range of the weapon",
    choices=list(Range),
    required=True,
    type=Range,
)
parser.add_argument(
    "--archetype",
    "-a",
    help="The archetype of the weapon",
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
tags=["{'default", "weapon"' if args.default else 'weapon"'}, "equipment", "{args.archetype}", "{args.range}"]

[params]
  abstract="{args.description}"
  [params.weapon]
    dmg="{args.dmg}"
    type="{args.dtype}"
    def="{args.defense}"
    range="{str(args.range).capitalize()}"
    arch="{str(args.archetype).capitalize()}"
    traits=["""


output += f'"{args.traits[0]}"'
for i in range(1, len(args.traits)):
    output += f', "{args.traits[i]}"'

output += """]
+++

{{< weapon-table >}}

"""

if args.description:
    output += "## Description\n" + args.description

print(output)

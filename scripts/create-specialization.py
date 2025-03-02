import argparse
from enum import Enum


class Specialization(Enum):
    basic = "basic"
    weapon = "weapon"
    armor = "armor"

    def __str__(self):
        return self.value


parser = argparse.ArgumentParser()
parser.add_argument(
    "--name", "-n", help="The name of the specialization", required=True
)
parser.add_argument(
    "--kind",
    "-k",
    help="The kind of specialization",
    required=True,
    choices=list(Specialization),
    type=Specialization,
)
parser.add_argument(
    "--traits", "-t", nargs="*", help="The traits of the specialization"
)
parser.add_argument(
    "--prereq", "-p", nargs="*", help="The prerequisite for the specialization"
)
parser.add_argument(
    "--description", "-d", help="The description of the specialization", required=True
)
parser.add_argument(
    "--cost", "-c", help="The cost of the specialization", required=False
)
parser.add_argument("--add", "-a", nargs="*", help="Additional tags", required=False)

args = parser.parse_args()

output = f"""+++
draft=true
title="{args.name}"
tags=["specialization", "{str(args.kind)}-specialization\""""

if args.add:
    for i in range(0, len(args.add)):
        output += f', "{args.add[i]}"'
output += "]"

output += f"""

[params]
  [params.specialization]
    cost="{args.cost} sp"
    traits=["""

output += f'"{args.traits[0]}"'
for i in range(1, len(args.traits)):
    output += f', "{args.traits[i]}"'
output += """]
    prereq=["""

output += f'"{args.prereq[0]}"'
for i in range(1, len(args.prereq)):
    output += f', "{args.traits[i]}'
output += f"""]
+++

{{{{< specialization-front >}}}}

## Description

{args.description}
"""

print(output)

+++
draft=false
title="Sweep"
tags=["specialization", "weapon-specialization", "armory-module", "all-scale", "polearm-specialization"]

[params]
  abstract="Target more than one actor with one polearm attack."
  [params.specialization]
    module="armory"
    cost="10 sp"
    scale="all"
    traits=["Repeatable(4)"]
    prereq=["Weapon Training(polearm)"]
+++

{{< specialization-front >}}

## Description

You gain the [Sweep]({{< relref "/armory/ref/sweep-action.md" >}}) major action.
Every additional purchase of this specialization you can target one additional
actor with the sweep action. Each additional target still takes half the total
damage as per the sweep action. For example, if you take this specialization 
two times, take the sweep action, and roll 10 damage, three targets would take
5 damage.

If this is not the first time you have taken this specialization **for this archetype**, the cost changes as per the following table:

| Time | Cost (sp) |
| ---- | --------- |
| 1    | 10        |
| 2    | 20        |
| 3    | 40        |
| 4    | 80        |


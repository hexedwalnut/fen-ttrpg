+++
draft=false
title="Averting Armor"
tags=["specialization", "armor-specialization", "core-module", "all-scale"]

[params]
  abstract="Gives the Defensive trait to a specific armor archetype."
  [params.specialization]
    module="core"
    cost="5 sp"
    traits=["Repeatable(4) per each archetype"]
    prereq=["-"]
+++

{{< specialization-front >}}

## Description

Pick an armor archetype X. All armors in the chosen archetype gains 
[Defensive(1)]({{< ref "/core/ref/defensive-trait.md" >}}) while you are 
wearing it.

If you are taking this specialization again after the first for the same archetype, you instead increase the number of defensive by one for that archetype. For example, if you have taken this specialization two time before for light armor and are taking it again, you move from Defensive(2) to
Defensive(3).

If this is not the first time you have taken this specialization **for this archetype**, the cost changes as per the following table:

| Time | Cost (sp) |
| ---- | --------- |
| 1    | 5         |
| 2    | 10        |
| 3    | 20        |
| 4    | 40        |


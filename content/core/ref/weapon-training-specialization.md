+++
draft=false
title="Weapon Training"
tags=["specialization", "weapon-specialization", "core-module", "all-scale"]

[params]
  abstract="Gain an additional die roll when rolling with a specific weapon archetype."
  [params.specialization]
    module="core"
    cost="5 sp"
    scale="all"
    traits=["Repeatable(4) per weapon archetype"]
    prereq=["-"]
+++

{{< specialization-front >}}

## Description

Pick a weapon archetype. You gain an 
[additional]({{< ref "/core/chapters/introduction.md#additional-die" >}}) 
weapon die when rolling damage using the chosen archetype.

For example, a standard [Dagger]({{< ref "/core/ref/dagger-weapon.md" >}})
has a weapon die of 1d4. When rolling damage after taking this specialization
you instead roll 2d4.

If this is not the first time you have taken this specialization **for this archetype**, the cost changes as per the following table:

| Time | Cost (sp) |
| ---- | --------- |
| 1    | 5         |
| 2    | 10        |
| 3    | 20        |
| 4    | 40        | 


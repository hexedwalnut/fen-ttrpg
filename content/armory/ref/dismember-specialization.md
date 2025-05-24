+++
draft=false
title="Dismember"
tags=["specialization", "weapon-specialization", "armory-module", "all-scale", "ax-specialization"]

[params]
  abstract="Allows an ax to hobble or disjoint an actor."
  [params.specialization]
    module="armory"
    cost="25 sp"
    scale="all"
    traits=["-"]
    prereq=["Weapon Training(ax)(4)", "Charage", "Wound", "fight(1d8+)"]
+++

{{< specialization-front >}}

## Description

When you deal damage as part of a 
[charge]({{< relref "/core/ref/charge-action.md" >}}) major action with a weapon 
in the [ax]({{< relref "/core/ref/ax-archetype.md" >}}) archetype, you may use your
reaction to force a fight/vigor contest. If you win, the defender suffers from
your choice of the [hobble]({{< relref "/core/ref/hobble-condition.md" >}}) 
condition or the [disjoint]({{< relref "/core/ref/disjoint-condition.md" >}})
condition for the rest of the combat, in addition you may apply the effects of
the [wound]({{< relref "/core/ref/wound-specialization.md" >}}) specialization
without spending a reaction. You must roll another contest for the wound.


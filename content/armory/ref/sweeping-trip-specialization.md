+++
draft=false
title="Sweeping Trip"
tags=["specialization", "weapon-specialization", "armory-module", "all-scale", "polearm-specialization"]

[params]
  abstract="Trip actors when dealing damage with the sweep action."
  [params.specialization]
    module="armory"
    cost="10 sp"
    scale="all"
    traits=["-"]
    prereq=["Weapon Training(polearm)(2)", "Sweep"]
+++

{{< specialization-front >}}

## Description

As part of taking the [Sweep]({{< relref "/armory/ref/sweep-action.md" >}}) major
action, you force a fight/dodge contest against each target. Any target that 
loses the contest gains the [prone]({{< relref "/core/ref/prone-condition.md" >}})
condition. The effect of the prone condition is applied after the sweep damage
is dealt.


+++
draft=false
title="Bludgeon"
tags=["specialization", "weapon-specialization", "armory-module", "all-scale", "cudgel-specialization"]

[params]
  abstract="Cudgel weapons can be used to cause the dazed condition."
  [params.specialization]
    module="armory"
    cost="10 sp"
    scale="all"
    traits=["-"]
    prereq=["Weapon Training(cudgel)"]
+++

{{< specialization-front >}}

## Description

When you deal damage with a weapon with the cudgel archetype, you may use your
reaction to force a fight/vigor contest. If you win, the defender suffers the
[dazed]({{< relref "/core/ref/dazed-condition.md" >}}) until the end of your 
next turn.


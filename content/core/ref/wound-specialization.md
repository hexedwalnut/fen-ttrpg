+++
draft=false
title="Wound"
tags=["specialization", "weapon-specialization", "core-module", "all-scale"]

[params]
  abstract="Allows your weapons to cause wounds."
  [params.specialization]
    module="core"
    cost="15 sp"
    scale="all"
    traits=["Repeatable"]
    prereq=["Weapon Training(X)(4)"]
+++

{{< specialization-front >}}

## Description

Pick a weapon archetype X. When you cause damage with a weapon from your selected
archetype, you may use your reaction to cause a fight contest versus the
defender's vigor or dodge. On a success your target takes one point of *wp*
and gains the [wounded]({{< ref "/core/ref/wounded-condition.md" >}}).

Taking this specialization more than once for the same archetype as no
additional effect. The cost of this specialization does not increase when you 
purchase it again.


+++
draft=false
title="Bleed"
tags=["specialization", "weapon-specialization", "ax-specialization", "long-blade-specialization", "short-blade-specialization"]

[params]
  abstract="Allows either, ax, long-blade, or short-blade weapons to cause Bleed."
  [params.specialization]
    cost="0 sp"
    traits=["Repeatable"]
    prereq=["Weapon Training(X)(2)"]
+++

{{< specialization-front >}}

## Description

Pick an archetype X from the following list:
* [Ax]({{< ref "core/ref/ax-archetype.md" >}})
* [Long-blade]({{< ref "core/ref/long-blade-archetype.md" >}})
* [Short-blade]({{< ref "core/ref/short-blade-archetype.md" >}})

When you cause damage with a weapon from this archetype, you may use your 
reaction to cause the defender to suffer from the negative condition 
[*bleed(1d4)*]({{< ref "core/ref/bleed-condition.md" >}}). If this is not the 
first time you purchase this specialization, instead you increase the die
by one increment. For example, the second time you take this specialization 
you can use your reaction to inflict *bleed(1d6)* when you cause damage with
a X archetype weapon.


+++
draft=false
title="Sentinel Counter"
tags=["specialization", "weapon-specialization", "armory-module", "all-scale", "polearm-specialization"]

[params]
  abstract="Your opportunity attacks that deal damage stop the target from moving."
  [params.specialization]
    module="armory"
    cost="15 sp"
    traits=["-"]
    prereq=["Weapon Training(polearm)(3)", "Maneuvering Counter"]
+++

{{< specialization-front >}}

## Description

When you damage an actor with an 
[opportunity attack]({{< relref "/core/ref/opportunity-attack-reaction.md" >}})
using a [polearm]({{< relref "/core/ref/polearm-archetype.md" >}}), that actor
gains the [immobile]({{< relref "/core/ref/immobile-condition.md" >}}) condition
until the start of their next turn.


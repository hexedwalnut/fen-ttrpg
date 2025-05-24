+++
draft=false
title="Magic Missile"
tags=["spell", "core-module", "skirmish-scale", "sorcery-spell-list"]

[params]
  abstract="You send a single bolt of magic towards a target."
  [params.spell]
    module="core"
    mp="2 mp"
    action="major"
    scale="skirmish"
    traits=["Sink"]
    list=["sorcery"]
+++

{{< spell-front >}}

## Description

You send a single bolt of magic towards a target you can see within [long]({{< ref "/core/ref/long.md" >}}) range dealing 1d4 [M]({{< ref "/core/ref/damage-types.md#magic" >}}) damage. The magic bolt bypasses *dodge* rolls but is considered a weapon for the purposes defense.

### Sink

For every 2 *mp* you spend over the original amount, you gain another magic bolt as described above. Magic bolts that target the same actor can be treated as the same damage roll. For example, if you pay 4 *mp* and target the same actor with both bolts you roll 2d4 as part of one damage roll. This means that the 2d4 must be defended by one defense roll.

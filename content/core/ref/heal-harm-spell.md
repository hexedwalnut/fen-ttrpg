+++
draft=false
title="Heal/Harm"
tags=["spell", "core-module", "skirmish-scale", "viturgy-spell-list"]

[params]
  abstract="You either heal or harm an actor within adjacent range."
  [params.spell]
    module="core"
    mp="2 mp"
    action="major"
    scale="skirmish"
    traits=["Reversable", "Sink"]
    list=["viturgy"]
+++

{{< spell-front >}}

## Description

### Heal

You heal a target creature within [adjacent]({{< ref "/core/ref/adjacent.md" >}}) range for 1d6 hp.

#### Sink

For every 2 *mp* you spend to cast this spell over the original amount you gain an additional 1d6 dice of healing.

### Harm

You harm a target creature within [adjacent]({{< ref "/core/ref/adjacent.md" >}}) range. You deal 1d6 [I]({{< ref "/core/ref/damage-types.md#internal" >}}) damage to the target. This counts as a weapon for the purposes of defending against the attack.

#### Sink

For every 2 *mp* you spend to cast this spell over the original amount you gain an additional 1d6 to the damage roll.

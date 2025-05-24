+++
draft=false
title="Lightning Bolt"
tags=["spell", "core-module", "skirmish-scale", "sorcery-spell-list"]

[params]
  abstract="You call a lightning bolt down on one target actor that might leap to another."
  [params.spell]
    module="core"
    mp="7 mp"
    action="major"
    scale="skirmish"
    traits=["Sink"]
    list=["sorcery"]
+++

{{< spell-front >}}

## Description

You call a lightning bolt down on one target actor that might leap to another.

You deal 1d6 [Area of Effect]({{< ref "/core/ref/damage.md#area-of-effect" >}}) [L]({{< ref "/core/ref/damage-types.md#lightning" >}}) damage to one target you can see within [long]({{< ref "/core/ref/long.md" >}}) range. That target can make a [dodge]({{< ref "/core/ref/dodge-skill.md" >}}) contest against your [magic]({{< ref "/core/ref/magic-skill.md" >}}), on a success the target takes half as much damage. If the target fails, you can select a different actor and repeat the above process.

### Sink

For every 2 *mp* you spend to cast this spell over the original, increase the damage by 1d6.

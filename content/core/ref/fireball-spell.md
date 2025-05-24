+++
draft=false
title="Fireball"
tags=["spell", "core-module", "skirmish-scale", "sorcery-spell-list"]

[params]
  abstract="You throw a small bead of fire magic that explodes into a ball of fire."
  [params.spell]
    module="core"
    mp="4 mp"
    action="major"
    scale="skirmish"
    traits=["Sink"]
    list=["sorcery"]
+++

{{< spell-front >}}

## Description

You throw a small bead of fire magic that explodes into a ball of fire.

You deal 1d6 [Area of Effect]({{< ref "/core/ref/damage.md#area-of-effect" >}}) [F]({{< ref "/core/ref/damage-types.md#fire" >}}) damage to all actors on the enemy side and all actors in [adjacent]({{< ref "/core/ref/adjacent.md" >}}) range to enemy actors (including allies). Each actor without [immobile]({{< ref "/core/ref/immobile-condition.md" >}}) or [incapacitated]({{< ref "/core/ref/unconscious-condition.md" >}}) can make a [dodge]({{< ref "/core/ref/dodge-skill.md" >}}) contest against your [magic]({{< ref "/core/ref/magic-skill.md" >}}) to reduce the damage to half.

### Sink

For every 2 *mp* you spend over the original spell cost, increase the damage by 1d6.

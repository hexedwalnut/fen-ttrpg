+++
draft=false
title="Fear/Courage"
tags=["spell", "core-module", "skirmish-scale", "sympathetic-spell-list"]

[params]
  abstract="You either case fear or inspire courage in a target actor."
  [params.spell]
    module="core"
    mp="5 mp"
    action="major"
    scale="skirmish"
    traits=["Sink"]
    list=["sympathetic"]
+++

{{< spell-front >}}

## Description

### Fear

A target you can see within [long]({{< ref "/core/ref/long.md" >}}) range must succeed a will/magic contest or gain [fear]({{< ref "/core/ref/fear-condition.md" >}})(1).

#### Sink

You can spend additional *mp* to cast this spell in the following ways:

- *Additional target*: you can spend an additional 2 *mp* to select an additional target with this spell
- *More fear*: you can spend an additional 5 *mp* to increase the number of the fear condition by 1. (i.e., instead of gaining fear(1) they would gain fear(2) if you spend an additional 5 *mp* in this way)

### Courage

A target you can see within [close]({{< ref "/core/ref/close.md" >}}) range becomes more courageous than normal. The target gains 10 temporary hp. While they have temporary hp, the target is immune to the [fear]({{< ref "/core/ref/fear-condition.md" >}})

When cast on a target that is already under the effects of the fear condition, the fear condition is removed but the target does not gain the temporary hp.

#### Sink

For every 3 mp you spend in addition to the original amount, increase the temporary hp gained by 5.

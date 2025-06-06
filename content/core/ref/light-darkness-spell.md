+++
draft=false
title="Light/Darkness"
tags=["spell", "core-module", "skirmish-scale", "thaumaturgy-spell-list", "permanency-spell"]

[params]
  abstract="You either create light or darkness."
  [params.spell]
    module="core"
    mp="5 mp"
    action="major"
    scale="skirmish"
    traits=["Reversible", "Permanency"]
    list=["Thaumaturgy"]
+++

{{< spell-front >}}

## Description

### Light

The light spell can be cast three ways:

First, you can create a magical source of light that allows you to see within [close]({{< ref "/core/ref/close.md" >}}) that lasts for 1 hour. This spell is cast on an object and moves with the object. 

Second, light can be used to blind an actor. When cast this way, you select a target within [close]({{< ref "/core/ref/close.md" >}}) range, they must succeed a notice/magic contest or become [blind]({{< ref "/core/ref/blind-condition.md" >}}) for an hour. Their eyes give off the same light as if light was cast on an object. If they succeed the contest, the spell has no effect.

Lastly, you may cast light to dispel the effects of the darkness spell. When cast this way, both the effects of your light and the effects of the darkness spell are removed.

#### Permanency

You can cast the permanency spell to make the effects of the light spell permanent. You can only make the first way of casting the light spell permanent. A light spell that is made permanent cannot be dispelled by a non-permanent casting of darkness. If your permanent light spell comes in contact with a permanent darkness spell, both spells are dispelled. Any non-permanent darkness spells within the range of your permanent light spell are dispelled.

### Darkness

You create a area of darkness from a point you can see within [short]({{< ref "/core/ref/short.md" >}}) range. While creatures are within a [close]({{< ref "/core/ref/close.md" >}}) range this area of darkness, they are [blind]({{< ref "/core/ref/blind-condition.md" >}}). 

Darkness can also be used to blind an actor as is the case with light. The process is the same, except the actor's eyes give off darkness instead of light. 

#### Permanency

You can cast the permanency spell to make the effects of the darkness spell permanent. You can only make the first way of casting the darkness spell permanent. A darkness spell that is made permanent cannot be dispelled by a non-permanent casting of light. If your permanent darkness spell comes in contact with a permanent light spell, both spells are dispelled. Any non-permanent light spells within the range of your permanent darkness spell are dispelled.

+++
draft=false
title="Bonk"
tags=["specialization", "weapon-specialization", "armory-module", "all-scale", "cudgel-specialization"]

[params]
  abstract="Knock people out with destructive strikes."
  [params.specialization]
    module="armory"
    cost="15 sp"
    scale="all"
    traits=["-"]
    prereq=["Weapon Training(cudgel)(4)", "Bludgeon", "Destructive Strike", "fight(1d8+)"]
+++

{{< specialization-front >}}

## Description

When you deal damage with a 
[destructive strike]({{< relref "/core/ref/destructive-strike-action.md" >}})
major action, you may apply the effects of your 
[bludgeon]({{< relref "/armory/ref/bludgeon-specialization.md" >}}) specialization
without spending a reaction. If you succeed on your contest from the bludgeon 
specialization and the target is under the effects of the  
[dazed]({{< relref "/core/ref/dazed-condition.md" >}}) condition, they become 
[incapacitated]({{< relref "/core/ref/incapacitated-condition.md" >}}) until 
the start of your next turn instead. Likewise, if you succeed on your contest
from the bludgeon specialization and the target is under the effects of the
incapacitated condition, they become 
[unconscious]({{< relref "/core/ref/unconscious-condition.md" >}}).


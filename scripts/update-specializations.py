import subprocess
import os
from pathlib import Path
import re

dir_path = Path(os.path.dirname(os.path.realpath(__file__)))


def specialization_command(name, kind, cost, tlist, plist, description, addition=None):
    output = [
        "python3",
        str(dir_path / "create-specialization.py"),
        "-n",
        name,
        "-k",
        kind,
        "-t",
    ]
    output.extend(tlist)
    output.append("-p")
    output.extend(plist)
    output.append("-d")
    output.append(description)
    output.append("-c")
    output.append(cost)
    if addition:
        output.append("-a")
        output.extend(addition)
    return output


def specialization_command_entry(entry, addition=None):
    return specialization_command(
        entry[0],
        entry[1],
        entry[2],
        entry[3],
        entry[4],
        entry[5],
        addition=addition,
    )


def fname(name):
    return name.lower().replace(" ", "-") + "-specialization.md"


specializations = [
    (
        ## BASIC START ##
        (
            "Talent",
            "basic",
            "0",
            ["Repeatable"],
            ["-"],
            """Select a skill your actor has that was not selected by the 
[Assurance]({{< ref "/core/ref/assurance-specialization.md" >}}) 
specialization. Increase its die by one increment.""",
        ),
        None,
    ),
    (
        (
            "Assurance",
            "basic",
            "0",
            ["Repeatable(4) per skill"],
            ["-"],
            """Pick a skill your actor has. Increase the number of dice rolled 
for this skill by 1. For example, if your actor has 1d6 in the Fight skill, 
after taking this specialization, your actor would roll 2d6 in the Fight skill. 
Note, once a skill is selected for Assurance it cannot be selected for 
[Talent]({{< ref "/core/ref/talent-specialization.md" >}}). This means that 
once you select Assurance on a skill, you can never increase the sides of the 
die.""",
        ),
        None,
    ),
    (
        (
            "Coordination",
            "basic",
            "0",
            ["Repeatable(4)"],
            ["-"],
            """You gain an additional minor action per turn.""",
        ),
        None,
    ),
    (
        (
            "Aggressive",
            "basic",
            "0",
            ["Repeatable(4)"],
            ["-"],
            """You gain an additional major action""",
        ),
        None,
    ),
    (
        (
            "Opportunity Attack",
            "basic",
            "0",
            ["-"],
            ["tactics(1d6+)"],
            """You gain the 
[**Opportunity Attack**]({{< ref "/core/ref/opportunity-attack-reaction.md" >}}) 
reaction.""",
        ),
        None,
    ),
    (
        (
            "Vitality",
            "basic",
            "0",
            ["Repeatable"],
            ["-"],
            """Roll non-explosive [vigor]({{< ref "/core/ref/vigor-skill.md" >}}) 
 (or take half the skill die's sides) and add the result to maximum 
 HP.""",
        ),
        None,
    ),
    (
        (
            "Reactive",
            "basic",
            "0",
            ["Repeatable(4)"],
            ["-"],
            """You gain an additional reaction per round.""",
        ),
        None,
    ),
    ## BASIC END ##
    ## WEAPON START ##
    (
        (
            "Weapon Training",
            "weapon",
            "0",
            ["Repeatable(4)"],
            ["-"],
            """Pick a weapon archetype. You gain an additional die when 
rolling damage using a weapon in the chosen archetype. The type of 
die is determined by the default sides of the weapon. For example, 
a standard [Dagger]({{< ref "/core/ref/dagger-weapon.md" >}}) has 
a weapon die of 1d4. When rolling damage after taking this 
specialization you instead roll 2d4. If, instead, the weapon had 
multiple default weapon dice you only add one additional die of 
the highest sides. If a weapon by default rolls 1d4+2d6+3d8 you 
gain an additional 1d8 after taking this specialization. This 
specialization applies to offhanded weapons as well.""",
        ),
        None,
    ),
    (
        (
            "Target",
            "weapon",
            "0",
            ["-"],
            ["Weapon Training(long-arm)"],
            """You gain the minor action 
[**Target**]({{< ref "/core/ref/target-action.md" >}}).""",
        ),
        None,
    ),
    (
        (
            "Aim",
            "weapon",
            "0",
            ["-"],
            ["Weapon Training(long-arm)(2)", "Target"],
            """You gain the major action 
[**Aim**]({{< ref "/core/ref/aim-action.md" >}})""",
        ),
        ["long-arm-specialization"],
    ),
    (
        (
            "Akimbo",
            "weapon",
            "0",
            ["-"],
            ["Weapon Training(short-arm)(2)"],
            """All short-arms gain the 
[light]({{< ref "/core/ref/light-trait.md" >}}) trait for you.""",
        ),
        ["short-arm-specialization"],
    ),
    (
        (
            "Averting Armory",
            "weapon",
            "0",
            ["Repeatable"],
            ["Weapon Training(X)"],
            """Pick an archetype X. All weapons in chosen archetype gains 
[Defensive(1)]({{< ref "core/ref/defensive-trait.md" >}}) for
you. If you are taking this specialization again after the first
time and select the same weapon archetype, you instead increase 
the number of Defensive by one for that archetype. For 
example, if you have taken this specialization two times before 
for short-arms taking it again, you move from Defensive(2) 
to Defensive(3).""",
        ),
        None,
    ),
    (
        (
            "Resilient Armament",
            "weapon",
            "0",
            ["Repeatable"],
            ["Averting Armory(X)(5)"],
            """Pick an archetype X. You have learned how to best wield a 
weapon when it is close to break. When a weapon is dealt 
enough damage to its defense to be sundered, you may use your
reaction to cause a Vigor/Fight contest between you and the
damage dealer. If you win the contest, the weapon is not 
sundered, instead keeping 1 defense. This reaction cannot be
applied to magical effects that cause damage to armaments.""",
        ),
        None,
    ),
    (
        (
            "Bleed",
            "weapon",
            "0",
            ["Repeatable"],
            ["Weapon Training(X)(2)"],
            """Pick an archetype X from the following list:
* [Ax]({{< ref "core/ref/ax-archetype.md" >}})
* [Long-blade]({{< ref "core/ref/long-blade-archetype.md" >}})
* [Short-blade]({{< ref "core/ref/short-blade-archetype.md" >}})

When you cause damage with a weapon from this archetype, you may use your 
reaction to cause the defender to suffer from the negative condition 
[*bleed(1d4)*]({{< ref "core/ref/bleed-condition.md" >}}). If this is not the 
first time you purchase this specialization, instead you increase the die
by one increment. For example, the second time you take this specialization 
you can use your reaction to inflict *bleed(1d6)* when you cause damage with
a X archetype weapon.""",
        ),
        [
            "ax-specialization",
            "long-blade-specialization",
            "short-blade-specialization",
        ],
    ),
    (
        (
            "Bludgeon",
            "weapon",
            "0",
            ["Repeatable"],
            ["Weapon Training(Cudgel)"],
            """When you deal damage with a cudgel weapon, you may use your 
reaction to force a Fight/Vigor contest. If you win, the defender suffers the
[*dazed*]({{< ref "core/ref/dazed-condition.md" >}}) until the end of your 
next turn. If you take this specialization again, you increase the number of 
rounds your target is affected by *dazed* by one.""",
        ),
        ["cudgel-specialization"],
    ),
    (
        (
            "Destructive Strike",
            "weapon",
            "0",
            ["Repeatable"],
            ["Weapon Training(X)(2)"],
            """Pick a weapon archetype X from the following list:
* [Ax]({{< ref "/core/ref/ax-archetype.md" >}})
* [Cudgel]({{< ref "/core/ref/cudgel-archetype.md" >}})
* [Polearm]({{< ref "/core/ref/polearm-archetype.md" >}})
* [Long-blade]({{< ref "/core/ref/long-blade-archetype.md" >}})

You learn to deal a devastating blow to defenses with this weapon archetype. 
You gain the 
[**Destructive Strike**]({{< ref "/core/ref/destructive-strike-action.md">}})
major action""",
        ),
        [
            "ax-specialization",
            "cudgel-specialization",
            "polearm-specialization",
            "long-blade-specialization",
        ],
    ),
    (
        (
            "Bonk",
            "weapon",
            "0",
            ["-"],
            [
                "Weapon Training(Cudgel)(4)",
                "Bludgeon(2)",
                "Destructive Strike",
                "fight(1d8+)",
            ],
            """When you deal damage with a destructive strike major action.
You apply the effects of your bludgeon specialization. If the target
has the [*dazed*]({{<ref "/core/ref/dazed-condition.md" >}}) condition they
become [*incapacitated*]({{< ref "/core/ref/incapacitated-condition.md" >}})
until the end of your next turn. If they are *incapacitated* they become 
[*unconscious*]({{< ref "/core/ref/unconscious-condition.md" >}}).""",
        ),
        ["cudgel-specialization"],
    ),
    (
        (
            "Charge",
            "weapon",
            "0",
            ["-"],
            ["tactics(1d6+)"],
            """You learn to move and strike quickly. You gain the major 
action [**Charge**]({{< ref "/core/ref/charge-action.md" >}}).""",
        ),
        None,
    ),
    (
        (
            "Quick Draw",
            "weapon",
            "0",
            ["-"],
            ["Weapon Training(short-arm)(3)", "Akimbo"],
            """Firing a [short-arm]({{< ref "/core/ref/short-arm-archetype.md" >}}) 
does not provoke an [attack of opportunity]({{< ref "/core/ref/attack-of-opportunity-reaction.md" >}}).""",
        ),
        ["short-arm-specialization"],
    ),
    (
        (
            "Disarming Shot",
            "weapon",
            "0",
            ["-"],
            ["Quick Draw"],
            """You gain the major action 
[**Disarming Shot**]({{< ref "/core/ref/disarming-shot-action.md" >}}).""",
        ),
        ["short-arm-specialization"],
    ),
    (
        (
            "Dismember",
            "weapon",
            "0",
            ["-"],
            ["Weapon Training(ax)(4)", "Charge", "Bleed", "fight(1d8+)"],
            """When you deal damage with an attack after a charge action with a 
weapon in the [ax]({{< ref "/core/ref/ax-archetype.md" >}}) archetype, you may 
use your reaction to force a fight/vigor contest. If you win, the defender 
suffers your choice of the [*hobble*]({{< ref "/core/ref/hobble-condition.md" >}})
or [*disjoint*]({{< ref "/core/ref/disjoint-condition.md" >}}) condition for the
rest of the combat, in addition you may apply the effects of the 
[*bleed*]({{< ref "/core/ref/bleed-condition.md" >}}) condition per your
[bleed specialization]({{< ref "/core/ref/bleed-specialization.md" >}}) level.""",
        ),
        ["ax-specialization"],
    ),
    (
        (
            "Flurry",
            "weapon",
            "0",
            ["-"],
            ["Weapon Training(short-blade)(4)"],
            """If you deal damage with a short-blade weapon while a 
short-blade weapon is in your off-hand. You may use your reaction to roll 
another attack using the off hand short-blade.""",
        ),
        ["short-blade-specialization"],
    ),
    (
        (
            "Quick Draw",
            "weapon",
            "0",
            ["-"],
            ["Weapon Training(short-arm)(3)", "Akimbo"],
            """When you fire a short-arm it adoes not provoke an attack of opportunity.""",
        ),
        ["short-arm-specialization"],
    ),
    (
        (
            "Kick Start",
            "weapon",
            "0",
            ["-"],
            ["Quick Draw"],
            """You can use your reaction to force a 
[fight]({{< ref "/core/ref/fight-skill.md" >}})/[vigor]({{< ref "/core/ref/vigor-skill.md" >}})
contest when rolling damage with a [short-arm]({{< ref "/core/ref/short-arm-archetype.md" >}})
in [adjacent]({{< ref "/core/ref/adjacent.md" >}}) range. If you win the contest,
you kick your target away from you. Until the start of your next turn, your 
movement does not provoke attacks of opportunity from the target.""",
        ),
        ["short-arm-specialization"],
    ),
    (
        (
            "Maneuvering Counter",
            "weapon",
            "0",
            ["-"],
            ["Weapon Training(polearm)", "Opportunity Attack"],
            """When you use your reaction to make an attack of opportunity
you can move (as per the [move]({{< ref "/core/ref/move-action.md" >}}) 
minor action) as a reaction. This movement doesn't provoke attacks of 
opportunity.""",
        ),
        ["polearm-specialization"],
    ),
    (
        (
            "Quick Load",
            "weapon",
            "0",
            ["-"],
            ["dodge(1d6+)", "shoot(1d6+)"],
            """You can load a weapon with the 
[loaded]({{< ref "/core/ref/loaded-trait.md" >}}) trait as a minor action.""",
        ),
        ["short-arm-specialization", "long-arm-specialization"],
    ),
    (
        (
            "Raise Shield",
            "weapon",
            "0",
            ["-"],
            ["Weapon Training(Shield)"],
            """You gain the major action 
[Raise Shield]({{< ref "/core/ref/raise-shield-action.md" >}}).""",
        ),
        ["shield-specialization"],
    ),
    (
        (
            "Reckless Strikes",
            "weapon",
            "0",
            ["Repeatable(4)"],
            ["Weapon Training(Ax)"],
            """You gain the minor action 
[Reckless Strikes]({{< ref "/core/ref/reckless-strike-action.md" >}}).
If this is not the first time you purchase this specialization, you increase 
the number of additional dice granted by the reckless strike action by one.""",
        ),
        ["ax-specialization"],
    ),
    (
        (
            "Resilient Armament",
            "weapon",
            "0",
            ["Repeatable"],
            ["Averting Armory(X)(%)"],
            """Pick an archetype X. You have learned how to best wield a weapon
when it is soon to break. When a weapon of the X archetype is dealt enough 
damage to be sundered, you may use your reaction to cause a Vigor/Fight contest
between you and the damage dealer. If you win the contest, the weapon is not
sundered, instead is reduced to one defense.""",
        ),
        None,
    ),
    (
        (
            "Counter Attack",
            "weapon",
            "0",
            ["-"],
            ["Weapon Training(X)(3)", "Opportunity Attack"],
            """Successfully defending damage using your 
[*dodge*]({{< ref "/core/ref/dodge-skill.md" >}}) skill triggers an attack
of opportunity against your attacker.""",
        ),
        None,
    ),
    (
        (
            "Sentinel Counter",
            "weapon",
            "0",
            ["-"],
            ["Weapon Training(polearm)(3)", "Maneuvering Counter"],
            """When you damage an actor with an attack of opportunity using a
polearm, that actor gains the [*immobile*]({{< ref "/core/ref/immobile-condition.md" >}})
condition until the start of their next turn.""",
        ),
        ["polearm-specialization"],
    ),
    (
        (
            "Shank",
            "weapon",
            "0",
            ["-"],
            ["Weapon Training(short-blade)(4)", "Bleed(1)"],
            """You gain the major action [Shank]({{< ref "/core/ref/shank-action.md" >}}).""",
        ),
        ["short-blade-specialization"],
    ),
    (
        (
            "Shield Counter",
            "weapon",
            "0",
            ["-"],
            ["Weapon Training(Shield)(1)", "Opportunity Attack"],
            """Successfully defending using a shield provokes and attack of
opportunity.""",
        ),
        ["shield-specialization"],
    ),
    (
        (
            "Shield Bash",
            "weapon",
            "0",
            ["-"],
            ["Weapon Training(Shield)(2)"],
            """Shields wielded by you gain the 
[cudgel]({{< ref "/core/ref/cudgel-archetype.md" >}}) archetype in addition to 
their other archetypes. Base damage for shields you wield are increased by one 
die increment.""",
        ),
        ["shield-specialization"],
    ),
    (
        (
            "Speed Loader",
            "weapon",
            "0",
            ["-"],
            ["Weapon Training(short-arm)", "Quick Load"],
            """You can load a 
[short-arm]({{< ref "/core/ref/short-arm-archetype.md" >}}) as part of an 
[attack]({{< ref "/core/ref/attack-action.md" >}}) action.""",
        ),
        ["short-arm-specialization"],
    ),
    (
        (
            "Stalwart Shield",
            "weapon",
            "0",
            ["-"],
            ["Weapon Training(Shield)(4)", "Raise Shield"],
            """You can use the major action [Raise Shield]({{< ref "/core/ref/raise-shield-action.md" >}})
with two minor actions.""",
        ),
        ["shield-specialization"],
    ),
    (
        (
            "Sweep",
            "weapon",
            "0",
            ["Repeatable(4)"],
            ["Weapon Training(polearm)"],
            """You gain the [Sweep]({{< ref "/core/ref/sweep-action.md" >}}) 
major action. If you take the specialization again, you can target one 
additional target with the sweep action. Each additional target still takes 
half the total damage as per the sweep action.""",
        ),
        ["polearm-specialization"],
    ),
    (
        (
            "Sweeping Trip",
            "weapon",
            "0",
            ["-"],
            ["Weapon Training(polearm)(2)", "Sweep(1)"],
            """As part of taking the [Sweep]({{< ref "/core/ref/sweep-action.md" >}}) 
action, you force a fight/dodge contest against each target. Any target that
loses the contest gains the [*prone*]({{< ref "/core/ref/prone-condition.md" >}}) 
condition. The effect of the *prone* condition is applied after the sweep damage
is dealt.""",
        ),
        ["polearm-specialization"],
    ),
    (
        (
            "Target",
            "weapon",
            "0",
            ["Repeatable(4)"],
            ["Weapon Training(long-arm)"],
            """You gain the minor action [Target]({{< ref "/core/ref/target-action.md" >}}).
If you take this specialization again, you gain one additional shoot die on a target
of the Target minor action.""",
        ),
        ["long-arm-specialization"],
    ),
    (
        (
            "Manuscripts and Codices",
            "weapon",
            "0",
            ["-"],
            ["Weapon Training(long-blade)"],
            """You gain the four guards of [long-blade]({{< ref "/core/ref/long-blade-archetype.md" >}}):
Plow, Ox, Fool, and Boar.

* **Plow**: A primarily defensive guard, your blade held low across your body
ready to block incoming blows. While in Plow you may use [vigor]({{< ref "/core/ref/vigor-skill.md" >}})
dice in place of [dodge]({{< ref "/core/ref/dodge-skill.md" >}}) dice when defending.
* **Ox**: A primarily offensive guard, your blade held high above your head
point out. While in Ox you may add an additional [fight]({{< ref "/core/ref/fight-skill.md" >}})
die to damage rolls.
* **Fool**: A defensive guard that tries to lure in attackers, your blade held
pointing to the ground. While in Fool long-blade weapons gain the [counter]({{< ref "/core/ref/counter-trait.md" >}})
trait while you are wielding them.
* **Boar**: A offensive guard focused on spacing and maneuvering, your sword held
straight towards your target. While in boar your movement doesn't provoke attacks
of opportunity

You can enter a guard as a minor action gaining the benefits as stated above.
""",
        ),
        ["long-blade-specialization"],
    ),
    (
        (
            "Lunge",
            "weapon",
            "0",
            ["-"],
            ["Weapon Training(long-blade)(2)", "Manuscripts and Codices"],
            """You gain the [Lunge]({{< ref "/core/ref/lunge-action.md" >}}) major action""",
        ),
        ["long-blade-specialization"],
    ),
    ## WEAPON END ##
    ## MAGIC START ##
    (
        (
            "Conduit",
            "magic",
            "0",
            ["-"],
            ["-"],
            """Your actor becomes a magical conduit, and gains the ability to 
cast spells. When you select this specialization you gain the following:

* **Magic Skill**: The [magic skill]({{< ref "/core/ref/magic-skill.md" >}})
represents your ability to cast, understand, and control magical sources, spells,
phenomena, and creatures. 
* **Magic Point Statistic**: Works much like hit points, but instead of 
representing available effort to avoid death, it represents your total ability
to cast or preform magic spells.
* **Primary Source**: The source you pull most of your magic from.
* **Starting Spell List**: A list of default spells that you know how to cast.

## Magic Skill

When you take this specialization you gain the [magic skill]({{< ref "/core/ref/magic-skill.md" >}}).
Like stated above, this represents your ability to cast, understand, and control
magical sources, spells, phenomena, and creatures. You initially have a magic
skill of 1d6, it can be increased via the normal means (i.e., [talent specialization]({{< ref "/core/ref/talent-specialization" >}})).

## Magic Point Statistic (mp)

When you take this specialization you gain the magic point statistic. This
represents the total amount of magical ability you have at the current time.
You spend mp to cast spells or to channel magical power. You regain mp by 
engaging with your source. When you take this specialization you gain a maximum
mp of a non-explosive [magic]({{< ref "/core/ref/magic-skill.md" >}}) roll. 
This maximum can be increased via the [magic well specialization]({{< ref "/core/ref/magic-well-specialization.md" >}}).

## Primary Source

As described in the [Magic]({{< ref "/core/chapters/magic.md" >}}) chapter, 
each conduit has a source where they pull their power from. Select one on of the
following sources as your actor's primary source:

- [Divine Source]({{< ref "/core/ref/divine-source.md" >}}): You pull your magic
from a god or other divinity. This source allows you to gain magic from the
worship of something greater than yourself and through your connection with 
you divinity.
- [Natural Source]({{< ref "/core/ref/natural-source.md" >}}): You pull your
magic from the forces of nature itself. This source allows you to gain magic from
natural landmarks and forces and through your deep connection and understanding
of nature and its processes.
- [Collective Source]({{< ref "/core/ref/collective-source.md" >}}): You pull
your magic from the collective study of magic and its proprieties. This source
allows you to gain magic from deep study, collective debate and experimentation,
and the books, papers, and media produced by like minds and the magical 
collective.
- [Sacrificial Source]({{<ref "/core/ref/sacrificial-source.md" >}}): You pull
your magic from self-sacrificial acts. You gain magic from your willingness to
give as much as you take, trading your bodily and mental health from magical 
power, a fair but brutal bargain.

### Pure Source (needs GM approval)

You pull from the pure source as your primary source. This allows you to move
fluidly between any of the above sources. You can pull freely from any of the 
above sources.

## Starting Spell List

No conduit is alone in their manifestations of magical spells. 

""",
        ),
        None,
    ),
    ## MAGIC END ##
]

for specialization, addition in specializations:
    with open(
        str(dir_path.parent / "content/core/ref" / fname(specialization[0])),
        "w+",
        encoding="utf-8",
    ) as file:
        if addition:
            subprocess.run(
                specialization_command_entry(specialization, addition=addition),
                stdout=file,
            )
        else:
            subprocess.run(specialization_command_entry(specialization), stdout=file)

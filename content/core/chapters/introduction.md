+++
draft=false
title="Introduction"
tags=["chapter"]
toc=true
[Params]
  abstract="In this chapter we introduce Fen some common phrases."
+++

### Dice Explode 

When you roll the maximum number on any die in the game, you can roll the die again and add the result to the total.

### Contest

Skill contests are one of the most used mechanics in Fen. When asked to roll a skill contest, each "side" rolls a skill, the actor with the higher result wins. A contest is written as `skill_1`/`skill_2` where the first skill, `skill_1` represents the aggressors skill and `skill_2` represents the defenders skill. For example, a fight/vigor contest would have the aggressor roll a fight skill vs. the defender's vigor skill. Ties are in favor of the defender in a "meet or beat" fashion. For example, in a dodge/notice contest (common when hiding), the defender (the one trying to find the hiding actor) wins if they meet or beat the aggressor's (hider's) dodge.

Skill contest can be one aggressor to many defenders. In this case, the aggressor rolls once and each defender rolls separately. The effects of a win or loss apply individually to each defender.

### Die Increments

Some specializations, materials, and traits talk about die increments. Dice exist along a scale separated by increments. These dice can be increased or decreased by an increment. The dice increments in order are as follows:

1. 1d4
2. 1d6
3. 1d8
4. 1d10
5. 1d12
6. 1d20

If a weapon has a trait that increases its die by one increment a weapon with 1d4 becomes 1d6 instead, conversely decreased by one increment would become a 1d8. At number one on the scale a decrease has no effect, similarly when a die reaches a number six on the scale it cannot be increased by any further increments.

### Additional Die

When told to roll an additional die, you roll one more die of the same sides as you are rolling. When told to roll and additional die for a dice roll that has multiple different sided dice, you roll and additional die with sides equal to the highest sides among the dice rolled. 

For example, if you are told to roll one additional weapon die for your [Dagger]({{< ref "/core/ref/dagger-weapon.md" >}}), which as a weapon die of 1d4, you roll 2d4 instead. Likewise, if told to roll an additional die for a roll of 1d4+1d8+1d20, you would roll 1d4+1d8+2d20 instead.

### Fewer Die

Much like additional but the opposite. You simply roll the specified fewer dice. If you only have one die, regardless of the amount specified, roll the one die twice and take the lower result. Otherwise, you simply remove one die from amount the dice rolled with the highest amount of sides, if two or more dice have the same number of sides, you can select which to remove. 

### Non-explosive

A non-explosive roll means that you roll one dice of the number of sides indicated that cannot explode. For example, if a specialization asks you to roll one non-explosive vigor skill and you have 3d8 in vigor, you roll 1d8 that does not explode. Likewise if it asks you to roll two non-explosive vigor skill with the same vigor, you roll 2d8 where each die does not explode.

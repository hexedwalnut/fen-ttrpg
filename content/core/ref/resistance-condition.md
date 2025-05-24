+++
draft=false
title="Resistance"
tags=["positive-condition"]
[Params]
  abstract="While under the effects of this condition, a specific damage type does less damage."
+++

Resistance is a positive condition that applies a damage reduction to an actor. Resistance is written in the following format:

> Resistance (Resistance Number, Resistance Types)

The *Resistance Number* details how much damage the resistance reduces and the *Resistance Types* tells you which type(s) are affected by the damage resistance. 

For example, if an actor has **Resistance (10, F)** the actor has 10 damage resistance when dealt fire (F) damage. Likewise, if an actor has **Resistance (10, B, P, S)**, the actor has 10 damage resistance to bludgeoning, piercing, and slashing damage. 

If an actor has two resistances for the same damage type, only apply the highest resistance number.

Unless otherwise stated, resistances are applied before all other forms of damage reduction (i.e., defense).

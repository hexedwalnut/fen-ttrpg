+++
draft=false
title = 'Specializations'
tags=["chapter"]
toc=true
[Params]
  abstract="This chapter introduces specilizations and their rules."
+++

Specializations are the mechanisms by which actors can customize and make themselves different. Specializations represent the cumulative knowledge, training, and experience of an actor. Specializations are acquired by spending Specialization Points. Some specializations require prerequisites in the form of other specializations, a skill die level, or combination of theses and other factors.

## Purchasing a Specialization

During downtime (i.e., not in a combat or exploration encounter) an actor can spend any number of *sp* they have earned on any number of specializations. A specialization costs a set number of *sp* points listed alongside the name of the specialization. An actor can choose to save lots of *sp* and buy many specializations at a time, or choose to spend all there *sp* every downtime, it is up to that actor. To purchase a specialization, the actor must meet all prerequisites (if any) and reduce their current amount of *sp* by the cost of the specialization. One the specialization is purchased, its effect takes place immediately. An actor can repeat the process as many times as the choose as long as they meet the prerequisites and have *sp* to spend. Prerequisites are explained below.

## Specialization Structure 

Specializations take the following structure:

1. Name and *sp* cost
2. A list of keywords and prerequisites (if any)
3. A description of the specialization's function

The name is self explanatory, the *sp* cost tells you how much *sp* it costs to buy the specialization, and the description of the specialization explains itself, however, keywords and prerequisites can be more complicated.

### Keywords

Keywords are a set of rules that apply to many different specializations. The keywords of a specialization are listed under the specialization's name. The following keywords are used for specializations:

#### Repeatable

{{< include "/core/ref/repeatable-trait.md" >}}

#### Immediate

{{< include "/core/ref/immediate-trait.md" >}}

### Prerequisites 

The prerequisites of a specialization are listed after all keywords. These prerequisites take two forms:

- **Skill Increment Prerequisite**: Written as Skill(dX), where *Skill* is replaced with the skill name and *X* is replaced with a die increment. An actor can only take the specialization if their skill increment is equal to or greater than the die increment specified in the prerequisite. For example, a specialization that requires at least a d6 in Vigor (i.e., "Vigor(d6)") can be taken by an actor with a d6 or higher die increment in the skill *Vigor*.
- **Specialization Prerequisite**: This prerequisite is represented as a list of other specialization names. An actor can only take the new specialization if they have all the listed specializations. Some listed specializations might need to be taken multiple times before meeting the specialization, written as specialization(X), where *specialization* represents the name of a repeatable specialization and *X* represents a number of times that specialization is taken. 

All prerequisites must be met before an actor can take the new specialization regardless of having the number of *sp* to purchase the specialization.

# All Specializations

{{< page-list "specialization" >}}

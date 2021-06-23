# NLP_Emotional-Chatbot
## Arabic Chatbot
---
## Team members
Nmae  | ID
------------- | -------------
Ahmed Soror  | 40-18290
Islam Mesabah  | 40-19076
Abdelrahman Elbeltagy  | 40-17544
Islam Omar | 40-6583

---
## Contents
* [Description](#Description)
* [How to contribute](#How-to-contribute)
  * [Contribution workflow](#Contribution-workflow)
* [Acceptance policy](#Acceptance-policy)
  * [Format of the Topic Branch naming](#Format-of-the-Topic-Branch-naming)
  * [Format of the Commit Message](#Format-of-the-Commit-Message)

# Description
A chatbot is a program which can do real conversations by simulating human conversations. One challenge for chatbots is recognizing feelings in the conversation partner and replying accordingly. This is a significant challenge for AI systems, however, it is straightforward for humans to recognize and acknowledge others’ feelings. One of the available datasets that helps in recognizing the feelings and improves the conversations in chatbots is the Facebook Empathetic Dialogues, they provide a novel dataset of 25k conversations grounded in emotional situations. There are no freely available similar datasets for Arabic language, however, it is the official language of 24 countries dominantly lying in the middle east, and north Africa. 

The project aims to create our own Arabic dataset by translating the Facebook Empathetic Dialogues data and create an Arabic chatbot.

The trained model could be found on the [drive](https://drive.google.com/drive/folders/19gR0tdd_mzQHpdIcd13NO8T_M0jre1-_?usp=sharing)

# How to contribute

This document outlines some of the conventions on development workflow, commit message formatting, contact points, and other resources to make it easier to get your contribution accepted.

We gratefully welcome improvements to documentation as well as to code.

## Contribution workflow

This is a rough outline of how to prepare a contribution:

- Create a topic branch from where you want to base your work (usually branched from master).
- Make commits of logical units.
- Make sure your commit messages are in the proper format (see below).
- Push your changes to a topic branch in your fork of the repository.
- Submit a pull request to the original repository.

# Acceptance policy

These things will make a PR more likely to be accepted:

 * A well-described requirement
 * A good commit message (see below)

In general, we will merge a PR once one maintainer has endorsed it.
Trivial changes (e.g., corrections to spelling) may get waved through.
For substantial changes, more people may become involved, and you might get asked to resubmit the PR or divide the changes into more than one PR.

## Format of the Topic Branch naming 
We follow a convention for naming our branching naming according to the following branch:   

```
<branch_type>/<branch-name>
```

Branch Types: 

- feature
- bug
- release

Examples: 

```
feature/post-react
```

```
feature/login-api
```

```
feature/landing-page-react
```

```
bug/fixing-eslint
```

```
release/v0.9
```


## Format of the Commit Message

We follow a rough convention for commit messages that are designed to answer the following
questions: 

- Where does the change happen?
- What changed?

### If ONE line
```
app.js: 
implement and integrate react-ga tool api
```

### If MULTIPLE lines
```
app.js: 
1. implement and integrate react-ga tool api
2. testing react-ga tool
3. adding react-hooks
```

The format can be described more formally as follows:

```
<subsystem>: 
<what changed>
```

The first line is the subject and should be no longer than 70 characters,  This allows the message to be easier to read on GitHub as well as in various git tools.

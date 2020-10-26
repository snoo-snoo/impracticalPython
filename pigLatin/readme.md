# Chapter 01-1: Pig Latin

## The Objective
Take an English word that begins with a consonant, move that consonant to the end, and then add "ay" to the end of the word.
If that word begins with an vowel, just add "way" to the end of the word.

## 1. Planning
### Strategy

I will ask the user for an input of a word. 
The words needs to be cut into pieces and checked if it starts with a consonant or a vowel. Then add the appropriate ending to that word and print it out.
### Pseudocode

```
Ask the user for an input
Check that input if its a word
If its a word:
    Check the first character
    If the first character is a vowel:
        Add "way" to the end of that word
    If the first character is a consonant:
        Move that consonant to the end
        Add "ay" to the end of that word
If its not a word:
    Print an error message
    repeat
```

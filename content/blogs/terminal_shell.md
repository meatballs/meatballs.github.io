---
title: "Terminals and Shells: A Beginner's Guide"
date: 2023-11-06
draft: false
author: "Owen"
tags:
image:
description: ""
toc:
---
I often find that there is some confusion for beginner programmers when it comes to understanding the difference between a terminal and a shell.

Let's take a few moments to look at the history of where those terms arose and how that fits withe world of modern computing.

## What is a Terminal?
Computers used to be enormous machines, often filling entire rooms. When I was at University in the late 1980s, there was a large 'mainframe' machine somewhere in the Computer Science building and there were workstations around the university campus from where students and staff could use it.

Those workstations each had a keyboard and a monitor. You typed your commands on the keyboard, those were sent down the wire to the mainframe and the response came back to be displayed on the monitor.

That combination of keyboard and monitor were known as terminals. Why that word? The same reason we use it for some railways stations - they were at the end of a line!

## What is a Shell?
When those keystrokes arrived at the mainframe, you needed some sort of program to process them - it needed to listen for incoming keystrokes, interpret them, request the mainframe's operating system to execute the relevant instructions, get the output of those instructions and send it back to the terminal's monitor.

That program was called a shell. Why that word? It was a program that 'wrapped' the mainframe's operating system in a layer that allowed a user to interact with it - much like the shell of a nut wraps the inner kernel (and there's another word we still use today for the very heart of an operating system)!

## What Happens Today?
For many people (and I'm one of them), that method of interacting with a computer using only a keyboard and a monitor still has much to offer - even when the computer I'm using is sitting on the desk right in front of me, rather than in a separate building.

Today, the physical terminals have been replaced by software - we emulate the behaviour of the older devices using programs known as 'terminal emulators.' Often, that's shortened simply to 'terminal' but we're still talking about a piece of software running on the same machine that we're controlling rather than a physical device of days gone by.

Shells are still required - they do much the same job in much the same way they always did. They provide a wrapper around an operating system, listen for typed keystrokes coming from a terminal emulator, execute whatever is requested and send the output back to the emulator for display.

In some cases, the terminal emulator and the shell are different programs that simply talk to one another. In others, a terminal emulator and shell are bundled together in one software package to provide a complete all-in-one keyboard driven interface to a computer.

For example, on a Mac, the default setup is Apple's 'Terminal' app - a terminal emulator - and the zsh shell. On Windows, you probably have PowerShell - a bundled emulator and shell in one package. Bash is still the most common shell on Linux systems and there are many other emulators and shells available for each of those operating systems.

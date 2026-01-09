---
title: "Deploying Everywhere: Why This Site Lives on Multiple Platforms"
date: 2026-01-09
draft: false
author: "Owen"
tags:
  - decentralisation
  - infrastructure
  - web3
image:
description: "How and why this website is deployed to both traditional platforms and decentralised networks"
toc:
---

If you're reading this, you might have arrived here via `owencampbell.me.uk`, or perhaps through `owencampbell.eth.limo`, or maybe even `owencampbell.bzz.link`. The same website, accessible through multiple different addresses. Why? It's all about resilience.

## The Problem with Putting All Your Eggs in One Basket

We've all experienced it: a website goes down because the hosting company had an outage. A service you rely on shuts down with little notice. GitHub goes offline and suddenly half the internet's documentation is inaccessible. Twitter decides to rebrand and change its APIs, breaking countless integrations.

When you host something on a single platform, you're making a bet that the platform will:
- Stay online when you need it
- Continue to exist in the future
- Maintain policies that work for you
- Remain accessible from wherever your readers are

That's a lot of trust to place in one organisation.

## A Different Approach: Deploy Everywhere

This website takes a different approach. Instead of choosing one platform and hoping for the best, it's deployed to multiple platforms simultaneously:

**Traditional hosting:**
- **[GitHub Pages](https://pages.github.com/)** - The site is deployed automatically via GitHub Actions whenever I push changes. You can access it at `owencampbell.me.uk`.

**Decentralised networks:**
- **Swarm** - The site is also deployed to [Swarm](https://www.ethswarm.org/), a decentralised storage and distribution network. You can access it through gateways like `owencampbell.eth.limo` or `owencampbell.bzz.link`.

If GitHub has an outage, the Swarm version remains accessible. If Swarm gateways have issues, the GitHub version is still there. No single point of failure.

## The Same Goes for Source Code

The website's source code follows the same philosophy. It lives in two places:

**Centralised:**
- **GitHub** - The traditional platform most developers know: [github.com/meatballs/meatballs.github.io](https://github.com/meatballs/meatballs.github.io)

**Decentralised:**
- **Radicle** - A peer-to-peer code collaboration network built on Git. You can browse the source code at [app.radicle.xyz](https://app.radicle.xyz/nodes/seed.radicle.garden/rad%3Az4EJ9CpMN4FiQJpks49K2k9nigBgX).

[Radicle](https://radicle.xyz) is particularly interesting because it means the code isn't dependent on any single company or server. Any Radicle node can host and serve the repository. Even if GitHub disappeared tomorrow, the code would remain accessible through the Radicle network.

I'm also using [Radicle CI](https://github.com/cytechmobile/radicle-ci), a continuous integration system designed for Radicle repositories, to automatically deploy the site to swarm when changes are pushed to the Radicle network.

## What Does "Decentralised" Actually Mean?

You might have noticed I keep using the word "decentralised." If you're not familiar with the concept, here's the simple version:

**Centralised** (traditional): Your content lives on one company's servers. If that company has problems, your content has problems.

**Decentralised**: Your content is distributed across many independent computers. No single entity controls it. If some nodes go offline, others keep serving your content.

Think of it like the difference between:
- Keeping all your photos on one USB drive (centralised)
- Having copies of your photos on multiple drives, in cloud storage, and at a friend's house (decentralised)

## Why This Matters

You might be thinking: "GitHub is huge and reliable. Why bother with alternatives?"

That's fair. But consider:

1. **No company is immune to outages** - Even the biggest tech companies have downtime.

2. **Policies change** - Platforms can change their terms of service, pricing, or even shut down entirely. Remember Google Reader? Or the countless services that have disappeared over the years?

3. **Accessibility varies** - Some countries or networks might block access to certain platforms. Having multiple access points means more people can reach your content.

4. **Control matters** - When you depend on a single platform, you're subject to their rules and decisions. Diversification gives you more independence.

5. **The technology is ready** - Decentralised alternatives have matured to the point where they're practical to use, not just theoretical.

## The Cost of Resilience

I won't pretend this approach is zero-effort. Setting up deployment to multiple platforms takes more initial work than choosing one. Maintaining multiple deployment pipelines requires some ongoing attention.

But the actual deployment is automated. Push to the repository at Github, and GitHub Actions handles the GitHub Pages deployment; Push to radicle and  separate process uploads the built site to Swarm. The incremental effort for each update is minimal.

The Swarm deployment does have a real cost - you need to pay for "postage stamps" to store content on the network. Currently this costs a small amount of BZZ tokens (Swarm's native cryptocurrency). For a personal website, we're talking about the cost of a few cups of coffee per year.

## Try It Yourself

All the gateway URLs should show you the same website:

- [owencampbell.me.uk](https://owencampbell.me.uk) (GitHub Pages)
- [owencampbell.eth.limo](https://owencampbell.eth.limo) (Swarm via eth.limo gateway)
- [owencampbell.eth.link](https://owencampbell.eth.link) (Swarm via eth.link gateway)
- [owencampbell.bzz.link](https://owencampbell.bzz.link) (Swarm via bzz.link gateway)

The fact that you can access the same content through multiple independent routes means that no single organisation can make this website disappear.

## The Bigger Picture

This isn't just about my personal website. It's about exploring what's possible when we build with resilience in mind.

The internet was designed to be decentralised - to route around damage and censorship. Over the decades, we've gradually centralised more and more onto a few major platforms. Projects like Radicle and Swarm are part of a movement to remember those original ideals and build tools that embody them.

Whether these specific technologies become mainstream or fade away, the principle remains valuable: important content deserves to be accessible through multiple independent channels.

You don't need to use blockchain or Web3 buzzwords to appreciate the value of not putting all your eggs in one basket.

## Learn More

If you're interested in exploring these technologies:

- **Swarm**: [ethswarm.org](https://www.ethswarm.org/) - Decentralised storage and distribution
- **Radicle**: [radicle.xyz](https://radicle.xyz/) - Peer-to-peer code collaboration
- **Radicle CI**: [radicle-ci.liw.fi](https://radicle-ci.liw.fi/) - Continuous integration for Radicle

The source code for this website is available on both [GitHub](https://github.com/meatballs/meatballs.github.io) and [Radicle](https://app.radicle.xyz/nodes/seed.radicle.garden/rad%3Az4EJ9CpMN4FiQJpks49K2k9nigBgX). Feel free to explore how it's all set up.

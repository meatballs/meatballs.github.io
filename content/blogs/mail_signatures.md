---
title: PGP Signatures on Email
date: 2008-06-12
draft: false
author: "Owen"
url: /pgp
tags:
  - pgp
  - email
image:
description: ""
toc:
---

You're probably here because you've received an email from me with an attachment called 'signature.asc' or with lines at the top similar to:

    -----BEGIN PGP SIGNED MESSAGE-----
    Hash: SHA512

and a section at the bottom which looks something like:

    -----BEGIN PGP SIGNATURE-----
    Version: GnuPG v1.4.9 (MingW32)
    iEYEARECAAYFAkmr2UAACgkQmnCt8c1NQ98pcACdEpZpqJYifkH0NvE6krEjzA9T
    VoMAn1HIKzpRrnveSEizzQBLMANkh648
    =acdx
    -----END PGP SIGNATURE-----

The attachment, or these two blocks, form a digital signature for the message which can be used to verify that:

* The message genuinely came from me.
* The content of the message has not been altered

This article explains why I've started using this technology and how the signature can be used.

## The Requirement

If I were to send a hand written letter in the post, I would sign it so that the recipient could verify that it was genuine. I believe that my email should provide at least the same level of confidence.

This belief is strengthened by the prevalence of spam, phishing and other malicious attempts to use email fraudulently.

## The Technology

My signatures are produced using tools which adhere to the [OpenPGP standard](http://www.openpgp.org). Whilst there are other technologies available, I chose OpenPGP as it is mature, stable and freely available. There are a variety of software tools which adhere to the standard for all major operating systems and many of these are completely free of charge.

OpenPGP is a protocol for encrypting email using public key cryptography. It is based upon a software tool called PGP which was originally written by Phil Zimmerman and released in 1991. There is an excellent explanation of public key cryptography and PGP itself at the (International PGP website)[http://www.pgpi.org/doc/pgpintro]

There are also some very good Wikipedia articles:

* [http://en.wikipedia.org/wiki/Pretty_Good_Privacy](http://en.wikipedia.org/wiki/Pretty_Good_Privacy)
* [http://en.wikipedia.org/wiki/Public-key_cryptography](http://en.wikipedia.org/wiki/Public-key_cryptography)

## Software Tools

In order to use my signatures, you will need a software tool which implements the OpenPGP standard.

The toolkit I use is based upon [GNU Privacy Guard](http://www.gnupg.org) which is available free of charge for Windows, Linux and MacOS systems.

On my windows based machines, I use [Gpg4win](http://www.gpg4win.org) which bundles the Gnu Privacy Guard engine with some useful utilities to integrate it into my mail system.

On my Mac, I use [GPGTools](https://gpgtools.org) which provides a similar set of functionality and is available free of charge.

On my Android phone, I use [OpenKeyChain](https://www.openkeychain.org/).

Other software implementations are listed on the Wikipedia article and will work perfectly with my signatures.

## Public Keys

You will also need my public key which I have published on the network of PGP key servers (e.g. [http://pgp.mit.edu](http://pgp.mit.edu) ). Most of the software tools will allow you to search the key servers using my email addresses although some will only allow you to search using a key's unique ID. Mine is BE9C2B73.

Some software implementations support importing keys from a QR code:

![My Key]({static}/images/be9c2b73.svg)

If, for whatever reason, you are unable to retrieve the correct key, please reply to the original email and I will gladly send it to you directly.

Once you have your chosen toolkit installed and have obtained the public key, you should be able to verify that one of my signed messages is indeed genuine and has not been altered since it was sent.

## Fully Encrypted Email

If you wish to go one stage further and use fully encrypted email to communicate with me (the equivalent of putting our correspondence in sealed envelopes), I'm happy to do so provided you use the OpenPGP standard.

Simply let me know that you wish to use the technology and, once we have exchanged public keys, I'll encrypt and sign the content of any email I send to you.

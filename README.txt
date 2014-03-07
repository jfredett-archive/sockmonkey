==========
sockmonkey
==========

First and foremost, and experiment in python and natural language processing.

A tool for analyzing reddit accounts to see who is a likely sockpuppet of whom.

## How it works

By and large, people write with predictible patterns -- common sentence
structure, frequently used words or phrases. Similar sentence length and so on.
By analyzing the comment history of known users, we can potentially establish
this pattern of behavior and represent it statistically. Once we have a
statistical representation, we should be able to derive a metric for determining
the similarity between two users.

WARNING
=======

This software is experimental, don't use it.

License
=======

This software is released under the terms of the MIT license, see LICENSE for
details.

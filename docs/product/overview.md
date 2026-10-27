# Pulseboard

Pulseboard is a local analytics product. It records events, rolls them into metrics and funnels, and flags spikes without a language model. An optional on-prem investigator then explains a spike by calling tools and returning the numbers it used.

The investigator is not a general chat and it does not read documents.

Nothing on this page is running yet. The workspace shell only prints a hello line. The investigator, the UI, and alerts are planned.

## Who it is for

Someone who wants a portfolio project they can run on one machine, with no hosted model bill: an operator looking at a conversion drop, not a reader of a PDF.

## What ships first

Events and metrics work with the model turned off. Anomaly detection is classical. The investigator comes after those tools exist.

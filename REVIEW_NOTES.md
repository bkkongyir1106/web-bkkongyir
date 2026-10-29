# Redesign review notes

## Implemented

- Retained Hugo Extended 0.83.1 and pinned Wowchemy modules. No added framework,
  package manager, or runtime dependency.
- Light academic design, system fonts, responsive layouts, keyboard focus,
  native anchor navigation, and six primary navigation sections.
- Updated biography, PhD completion, Gustavus appointment, employment dates,
  documented performance figures, leadership, and award dates using the
  supplied résumé. Retained personal background and community links.
- Retained all four publication records, abstracts, author lists, citations,
  external PDF links, and original paper assets. Removed nonexistent example
  slide links. Added a local copy of the customer attrition paper from the
  supplied materials folder.
- Created a one-page public résumé without the street address and phone, as
  requested. The original document is unchanged.
- Removed inherited STATS 306 materials, notebooks, data, instructor profile
  references, and DistGD material. The existing courses/sessions URL now
  presents Benedict's teaching history.
- Cleared analytics/tag IDs after confirming they matched the original
  author's repository. Retained Benedict's Calendly and contact links.
- Renamed two inherited publication folders to descriptive names. Old page
  URLs redirect to the new URLs; Netlify wildcard redirects also preserve
  existing PDF and citation attachment links.

The old author's identifier remains only in compatibility redirects, so
existing links continue working. Theme licensing and attribution remain.

## Content to confirm

1. **Insurance publication:** the original page dates it to 2008 and lists
   four authors; its existing BibTeX dates it to 2018 and lists five, including
   V. K. Dedu. Both source records are preserved pending confirmation.
2. **Awards:** VIK and teaching award dates now follow the résumé (May 2024).
   Original award links point to a 2018 department newsletter; provide current
   supporting links if those are not intended.
3. **Teaching:** updated from the owner’s October 29 clarification: OSU Fall 2025, approximately 100 students; Gustavus Fall 2026 MCS 142, two sections of approximately 24 students each, and MCS 242, one section of approximately 16 students. Teaching now has one editable source.
4. **Office hours:** the Sunday 13:00–14:00 listing and Calendly link are
   preserved. Confirm that this schedule is still appropriate.
5. **Award naming:** existing IABA Foundation Scholar labels are preserved;
   the résumé calls these IABA Achievement Awards. Confirm the official label
   before consolidating the wording.

## Verification limits

Local testing cannot verify Netlify form processing or delivery. Retained
external links and services may require authentication or host-specific
configuration. Check Netlify attachment redirects and form delivery on the
deploy preview before merging. No test inquiry has been sent.

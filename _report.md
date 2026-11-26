# NHB source texts - collection report

Collected 2026-11-26 on the owner's laptop (nhb.org.in is not reachable from the cloud).

## Counts
- Listing pages on nhb.org.in that yielded documents: 36 (advisories; notifications/regulation archives; financing_post circulars 2015-16..2026-27 - only 2015-16, 2019-20, 2020-21, 2022-23, 2023-24, 2024-25 exist, the rest 404; regulation_post notification / policy / miscellaneous / supervisory circulars and guidelines; supervision directions, master circulars, returns, penalties; refinance pages and archives; grievance pages; CRGFTLIH; PMAY-U 2.0; UIDF; SRF).
- Distinct documents on NHB listings: **351**; downloaded OK: **347**; failed: **4**.
- Downloaded and dated on/after 2019-08-09: **92**; dated before: **221**; undated: **34**.
- Plus 5 statute/background items: NHB Act (ACT-NHB), Finance (No.2) Act 2019 (+ Part VII NHB extract txt), NHB General Regulations 1988 (2 files), RBI press release 13-08-2019 (txt only).
- Text: pdftotext layer 180; local OCR (RapidOCR) 160; no text 7.
- pdf/ total 455 MB.

### By category (NHB listings, downloaded)
| category | n |
|---|---|
| advisory | 29 |
| circular | 148 |
| direction | 6 |
| grievance | 10 |
| notification | 74 |
| other | 21 |
| refinance | 54 |
| returns | 5 |

### By category, dated on/after 2019-08-09
| category | n |
|---|---|
| advisory | 29 |
| circular | 11 |
| direction | 1 |
| grievance | 1 |
| other | 14 |
| refinance | 36 |

## Failures (dead links on the NHB site)
- NHB-2014-12-10-Inspection-Forms-prior-to-10-12-2014 - https://www.nhb.org.in/Regulation/INS_FORMS.pdf - error: HTTP Error 404: Not Found (listed on https://www.nhb.org.in/notificationsregulation-archives/)
- NHB-undated-Onsite-Inspections - https://www.nhb.org.in/INS_Forms.pdf - error: HTTP Error 404: Not Found (listed on https://www.nhb.org.in/supervision/)
- NHB-2016-01-01-Booklet-January-01-2016-Download-in-English-Download-Doc-in-2 - https://www.nhb.org.in/Financial/SCB-Schemes-2015.doc - error: HTTP Error 404: Not Found (listed on https://www.nhb.org.in/financing_post/refinance-to-scheduled-commercial-banks/)
- NHB-2015-01-01-RRB-Schemes-January-01-2015-Download-in-English-Download-Doc - https://www.nhb.org.in/Financial/RRB-Schemes-2015.doc - error: HTTP Error 404: Not Found (listed on https://www.nhb.org.in/financing_post/refinance-to-regional-rural-banks-rrbs-5/)

Six further listing links had malformed hosts (e.g. `http://hb.org.in/...`, `http:nhb.org.in/...`, `http://test.nhb.org.in/...`, `scan0005.pdfhttps://...`); the same path on www.nhb.org.in returned the PDF, so those were downloaded from the corrected host and flagged in the `note` column.

## No text extracted
- NHB-2010-10-11-Revised-Guidelines-on-Know-Your-Customer-KYC-Anti-Money-Laun.doc - no-text (.doc)
- NHB-2010-10-11-Revised-Guidelines-on-Fair-Practices-Code-for-HFCs-October-1.doc - no-text (.doc)
- NHB-2010-10-11-Revised-Guidelines-on-Asset-Liability-Management-System-for.doc - no-text (.doc)
- NHB-2005-07-04-Draft-Guidelines-on-Securitization-of-Standard-Assets-Jul-04.doc - no-text (.doc)
- NHB-undated-Guidelines-for-Asset-Liability-Management-System-in-Housing.doc - no-text (.doc)
- NHB-undated-Fraudulent-Transactions-in-Housing-Finance-98-kb-228-kb.doc - no-text (.doc)
- NHB-undated-Foreign-Exchange-Management-Act-1999-Providing-housing-loan.doc - no-text (.doc)

## Withdrawn / superseded
- No NHB listing page marks any item as withdrawn or superseded.
- RBI press release 13-08-2019: HFCs to keep following NHB directions only until RBI issues a revised framework; NHB keeps supervision, returns and grievance redressal.
- The NHB "Directions" page now lists "Housing Finance Company (Reserve Bank) Directions, 2025" first, with the older NHB Directions (2010 consolidated, NCD 2014, Auditor's Report 2016, Acquisition/Transfer of Control 2016, Corporate Governance 2016) still shown on the same page and in the directions archive. Master Circulars MC01-MC07 appear on the notifications/regulation *archives* page. Treat pre-2019 NHB notifications, policy and misc circulars as archive unless a current RBI direction keeps them alive.

## Other caveats
- Dates: `date_source=listing` is the listing date; `document text (first date found; verify)` came from the first date in the PDF text for items with no listing date. Undated items keep `undated` in the file name.
- NHB Act: India Code returned HTTP 504 repeatedly from this machine, so ACT-NHB.pdf is NHB's copy "amended up to 2023". NHB's older copy "as on 25.11.2020" is also included.
- Finance (No.2) Act 2019 PDF is from thc.nic.in (High Court of Tripura), not the eGazette.
- OCR text is machine-generated (RapidOCR) and capped at 40 pages per document; Hindi/bilingual gazette pages OCR poorly.
- Excluded: tender/RFP announcement ticker shown on every page, trustee compliance reports, deposit overdue lists and research studies from "all archives", what's-new and press-release archives, lists of HFCs sanctioned refinance.

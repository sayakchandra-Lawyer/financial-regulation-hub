# NHB source texts - collection report

Collected 2026-11-26 on the owner's laptop (nhb.org.in is not reachable from the cloud).

## Counts
- Listing pages on nhb.org.in that yielded documents: 36 (advisories; notifications/regulation archives; financing_post circulars 2015-16..2026-27 - only 2015-16, 2019-20, 2020-21, 2022-23, 2023-24, 2024-25 exist, the rest 404; regulation_post notification / policy / miscellaneous / supervisory circulars and guidelines; supervision directions, master circulars, returns, penalties; refinance pages and archives; grievance pages; CRGFTLIH; PMAY-U 2.0; UIDF; SRF).
- Distinct documents on NHB listings: **351**; downloaded OK: **347**; failed: **4**.
- Downloaded and dated on/after 2019-08-09: **92**; dated before: **221**; undated: **34**.
- Plus 5 statute/background items: NHB Act (ACT-NHB), Finance (No.2) Act 2019 (+ Part VII NHB extract txt), NHB General Regulations 1988 (2 files), RBI press release 13-08-2019 (txt only).
- Text: pdftotext layer 180; local OCR (RapidOCR) 75; no text 92.
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
- NHB-2005-12-19-NHB-HFC-DIR-13-CMD-2005-dated-Dec-19-2005.pdf - scanned, no text (OCR failed/not run)
- NHB-2006-06-06-NHB-HFC-DIR-16-CMD-2006-dated-June-6-2006.pdf - scanned, no text (OCR failed/not run)
- NHB-2006-09-29-NHB-HFC-DIR-17-CMD-2006-dated-Sept-29-2006.pdf - scanned, no text (OCR failed/not run)
- NHB-2007-03-26-NHB-HFC-DIR-18-CMD-2007-dated-March-26-2007.pdf - scanned, no text (OCR failed/not run)
- NHB-2007-04-13-NHB-HFC-DIR-19-CMD-2007-dated-April-13-2007.pdf - scanned, no text (OCR failed/not run)
- NHB-2007-05-01-NHB-HFC-REG-II-CMD-2002-dated-May-1-2007.pdf - scanned, no text (OCR failed/not run)
- NHB-2007-07-06-NHB-HFC-DIR-20-CMD-2007-dated-July-6-2007.pdf - scanned, no text (OCR failed/not run)
- NHB-2007-11-30-NHB-HFC-DIR-22-CMD-2007-dated-Nov-30-2007.pdf - scanned, no text (OCR failed/not run)
- NHB-2008-04-24-NHB-HFC-DIR-23-CMD-2008-dated-April-24-2008.pdf - scanned, no text (OCR failed/not run)
- NHB-2008-12-02-NHB-HFC-DIR-24-CMD-2008-dated-Dec-2-2008.pdf - scanned, no text (OCR failed/not run)
- NHB-2009-01-05-NHB-HFC-DIR-26-CMD-2009-dated-Jan-5-2009.pdf - scanned, no text (OCR failed/not run)
- NHB-2009-09-03-NHB-HFC-DIR-27-CMD-2009-dated-Sep-3-2009.pdf - scanned, no text (OCR failed/not run)
- NHB-2010-03-29-NHB-HFC-REG-3-CMD-2010-dated-March-29th-2010.pdf - scanned, no text (OCR failed/not run)
- NHB-2010-02-03-NHB-HFC-DIR-28-CMD-2010-dated-February-3-2010.pdf - scanned, no text (OCR failed/not run)
- NHB-2010-06-10-NHB-HFC-DIR-1-CMD-2010-dated-10th-June-2010.pdf - scanned, no text (OCR failed/not run)
- NHB-2010-08-20-NHB-HFC-DIR-1-Corrigendum-Amendments-CMD-2010-dated-Aug-20-2.pdf - scanned, no text (OCR failed/not run)
- NHB-2011-08-05-No-NHB-HFC-DIR-3-CMD-2011-dated-Aug-05-2011.pdf - scanned, no text (OCR failed/not run)
- NHB-2011-06-06-No-NHB-HFC-REG-4-CMD-2011-dated-Jun-06-2011.pdf - scanned, no text (OCR failed/not run)
- NHB-2011-06-28-NHB-HFC-REG-5-CMD-2011-dated-Jun-28-2011.pdf - scanned, no text (OCR failed/not run)
- NHB-2012-01-19-NHB-HFC-DIR-4-CMD-2012-dated-Jan-19-2012.pdf - scanned, no text (OCR failed/not run)
- NHB-2012-05-28-NHB-HFC-DIR-5-CMD-2012-dated-May-28-2012.pdf - scanned, no text (OCR failed/not run)
- NHB-2012-08-01-NHB-HFC-DIR-6-CMD-2012-dated-Aug-01-2012.pdf - scanned, no text (OCR failed/not run)
- NHB-2013-03-21-NHB-HFC-DIR-7-CMD-2013-dated-Mar-21-2013.pdf - scanned, no text (OCR failed/not run)
- NHB-2013-06-24-NHB-HFC-DIR-8-CMD-2013-dated-Jun-24-2013.pdf - scanned, no text (OCR failed/not run)
- NHB-2013-09-06-NHB-HFC-DIR-9-CMD-2013-dated-Sep-06-2013.pdf - scanned, no text (OCR failed/not run)
- NHB-2015-03-13-NHB-HFC-NCD-DIR-2-CMD-2015-dated-Mar-13-2015.pdf - scanned, no text (OCR failed/not run)
- NHB-2015-03-13-NHB-HFC-DIR-15-CMD-2015-dated-Mar-13-2015.pdf - scanned, no text (OCR failed/not run)
- NHB-2010-10-11-Revised-Guidelines-on-Know-Your-Customer-KYC-Anti-Money-Laun.doc - no-text (.doc)
- NHB-2010-10-11-Revised-Guidelines-on-Fair-Practices-Code-for-HFCs-October-1.doc - no-text (.doc)
- NHB-2010-10-11-Revised-Guidelines-on-Asset-Liability-Management-System-for.doc - no-text (.doc)
- NHB-2005-07-04-Draft-Guidelines-on-Securitization-of-Standard-Assets-Jul-04.doc - no-text (.doc)
- NHB-undated-Guidelines-for-Asset-Liability-Management-System-in-Housing.doc - no-text (.doc)
- NHB-undated-Fraudulent-Transactions-in-Housing-Finance-98-kb-228-kb.doc - no-text (.doc)
- NHB-undated-Foreign-Exchange-Management-Act-1999-Providing-housing-loan.doc - no-text (.doc)
- NHB-2016-06-10-Additional-Special-Refinance-Facility-ASRF-scheme.pdf - scanned, no text (OCR failed/not run)
- NHB-2016-09-01-CRGFTLIH-Recovery-of-Guarantee-Fee-on-upfront-basis.pdf - scanned, no text (OCR failed/not run)
- NHB-2010-01-25-NHB-ND-DRS-Misc-Circular-1-2010.pdf - scanned, no text (OCR failed/not run)
- NHB-2010-04-09-NHB-ND-DRS-Misce-Cir-No-2-2009-2010.pdf - scanned, no text (OCR failed/not run)
- NHB-2010-12-28-NHB-ND-DRS-Misce-Cir-No-2-8792-2010.pdf - scanned, no text (OCR failed/not run)
- NHB-2011-04-07-NHB-ND-DRS-Misc-Circular-No-3-3986-2010-11.pdf - scanned, no text (OCR failed/not run)
- NHB-2011-08-29-NHB-ND-DRS-Misc-Circular-No-6-2011-12.pdf - scanned, no text (OCR failed/not run)
- NHB-2012-01-03-NHB-ND-DRS-Misc-Circular-No-7-2012.pdf - scanned, no text (OCR failed/not run)
- NHB-2012-06-05-NHB-ND-DRS-Misc-Circular-No-8-2012.pdf - scanned, no text (OCR failed/not run)
- NHB-2012-08-03-NHB-ND-DRS-Misc-Circular-No-9-2012.pdf - scanned, no text (OCR failed/not run)
- NHB-2012-08-21-NHB-ND-DRS-Misc-Circular-No-10-2012.pdf - scanned, no text (OCR failed/not run)
- NHB-2012-12-18-NHB-ND-DRS-Misc-Circular-No-11-2012.pdf - scanned, no text (OCR failed/not run)
- NHB-2013-05-08-NHB-ND-DRS-Misc-Circular-No-12-2013.pdf - scanned, no text (OCR failed/not run)
- NHB-2015-07-17-NHB-ND-DRS-Misc-Circular-No-15-2015-16.pdf - scanned, no text (OCR failed/not run)
- NHB-2014-09-03-NHB-ND-DRS-Policy-Circular-66-2014-15.pdf - scanned, no text (OCR failed/not run)
- NHB-2013-11-18-NHB-ND-DRS-Pol-No-58-2013-14.pdf - scanned, no text (OCR failed/not run)
- NHB-2013-07-04-NHB-ND-DRS-Pol-No-57-2012-14.pdf - scanned, no text (OCR failed/not run)
- NHB-2013-06-24-NHB-ND-DRS-Pol-No-56-2012-13.pdf - scanned, no text (OCR failed/not run)
- NHB-2013-04-16-NHB-ND-DRS-Pol-No-55-2012-13.pdf - scanned, no text (OCR failed/not run)
- NHB-2012-09-26-NHB-ND-DRS-Pol-No-52-2012-13.pdf - scanned, no text (OCR failed/not run)
- NHB-2012-05-28-NHB-ND-DRS-Pol-No-51-2012-13.pdf - scanned, no text (OCR failed/not run)
- NHB-2012-05-28-NHB-ND-DRS-Pol-No-50-2011-12.pdf - scanned, no text (OCR failed/not run)
- NHB-2012-04-09-NHB-ND-DRS-Pol-No-49-2011-12.pdf - scanned, no text (OCR failed/not run)
- NHB-2012-04-09-NHB-ND-DRS-Pol-No-48-2011-12.pdf - scanned, no text (OCR failed/not run)
- NHB-2012-03-29-NHB-ND-DRS-Pol-No-47-2011-12.pdf - scanned, no text (OCR failed/not run)
- NHB-2011-10-19-NHB-ND-DRS-Pol-No-44-2011-12.pdf - scanned, no text (OCR failed/not run)
- NHB-2011-10-19-NHB-ND-DRS-Pol-No-43-2011-12.pdf - scanned, no text (OCR failed/not run)
- NHB-2011-10-11-NHB-ND-DRS-Pol-No-42-2010-11.pdf - scanned, no text (OCR failed/not run)
- NHB-2011-05-19-NHB-ND-DRS-Pol-No-39-2010-11.pdf - scanned, no text (OCR failed/not run)
- NHB-2011-04-25-NHB-ND-DRS-Pol-No-38-2010-11.pdf - scanned, no text (OCR failed/not run)
- NHB-2010-03-16-NHB-ND-DRS-Pol-No-32-2009-10.pdf - scanned, no text (OCR failed/not run)
- NHB-2009-10-27-NHB-ND-DRS-Pol-No-31-corrg-2009.pdf - scanned, no text (OCR failed/not run)
- NHB-2009-09-23-NHB-ND-DRS-POL-No-30-2009.pdf - scanned, no text (OCR failed/not run)
- NHB-2009-06-02-NHB-ND-DRS-POL-No-29-2009.pdf - scanned, no text (OCR failed/not run)
- NHB-2009-04-15-NHB-ND-DRS-POL-No-28-2009.pdf - scanned, no text (OCR failed/not run)
- NHB-2009-04-13-NHB-ND-DRS-POL-No-27-2009.pdf - scanned, no text (OCR failed/not run)
- NHB-2009-02-20-NHB-ND-DRS-POL-No-26-2009.pdf - scanned, no text (OCR failed/not run)
- NHB-2008-07-14-NHB-ND-DRS-POL-No-25-2008.pdf - scanned, no text (OCR failed/not run)
- NHB-2008-07-14-NHB-ND-DRS-POL-No-24-2008.pdf - scanned, no text (OCR failed/not run)
- NHB-2008-04-24-NHB-ND-DRS-POL-No-23-2008.pdf - scanned, no text (OCR failed/not run)
- NHB-2007-09-27-NHB-ND-DRS-POL-No-22-2007.pdf - scanned, no text (OCR failed/not run)
- NHB-2007-04-13-NHB-ND-DRS-POL-No-21-2007.pdf - scanned, no text (OCR failed/not run)
- NHB-2007-01-17-NHB-ND-DRS-POL-No-20-2007.pdf - scanned, no text (OCR failed/not run)
- NHB-2006-09-15-NHB-ND-DRS-POL-No-19-2006.pdf - scanned, no text (OCR failed/not run)
- NHB-2006-09-05-NHB-ND-DRS-POL-No-16-2006.pdf - scanned, no text (OCR failed/not run)
- NHB-2006-07-25-NHB-ND-DRS-POL-No-15-2006.pdf - scanned, no text (OCR failed/not run)
- NHB-2006-07-25-NHB-ND-DRS-POL-No-14-2006.pdf - scanned, no text (OCR failed/not run)
- NHB-2006-04-10-NHB-ND-DRS-POL-No-13-2006.pdf - scanned, no text (OCR failed/not run)
- NHB-2006-03-16-NHB-ND-DRS-POL-No-12-2006.pdf - scanned, no text (OCR failed/not run)
- NHB-2006-03-03-NHB-ND-DRS-POL-No-11-2006.pdf - scanned, no text (OCR failed/not run)
- NHB-2005-07-04-NHB-ND-DRS-POL-No-10-2005-2006.pdf - scanned, no text (OCR failed/not run)
- NHB-2005-05-18-NHB-ND-DRS-POL-No09-2004-2005.pdf - scanned, no text (OCR failed/not run)
- NHB-2005-03-31-NHB-ND-DRS-POL-No-08-2004-2005.pdf - scanned, no text (OCR failed/not run)
- NHB-2005-03-28-NHB-ND-DRS-POL-No-07-2004-2005.pdf - scanned, no text (OCR failed/not run)
- NHB-2005-01-31-NHB-ND-DRS-POL-No-06-2004-2005.pdf - scanned, no text (OCR failed/not run)
- NHB-2013-08-05-NHB-ND-DRS-POL-No-04-2004-2005.pdf - scanned, no text (OCR failed/not run)
- NHB-2004-08-26-NHB-ND-DRS-POL-No-03-2004-2005.pdf - scanned, no text (OCR failed/not run)
- NHB-2004-08-25-NHB-ND-DRS-POl-No-02-2004-2005.pdf - scanned, no text (OCR failed/not run)

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

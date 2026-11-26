# Stock exchanges sources: collection report

Collected 26-11-2026, for the "Stock exchanges" section of financial-regulation-hub. The focus is what a listed NBFC, debt issuer or lender needs from NSE and BSE.

All texts come from official hosts only: nseindia.in / nseindia.com, nsearchives.nseindia.in / .com, bseindia.com and sebi.gov.in. NSE now serves its site from **nseindia.in**, and nseindia.com redirects there. Third-party search was used only to find BSE notice numbers and SEBI page addresses. Every text was then fetched from the official copy.

## What is in the folder

| | Count |
|---|---|
| Catalogue rows (`_catalogue.tsv`) | 354 |
| Rows with a full text file in `txt/` | 112 (SEBI 4, NSE 65, BSE 43) |
| Jun–Nov 2026 sweep rows listed without text | 242 (NSE 106, BSE 136) |
| Total size of `txt/` | about 8.3 MB |

How each text was made:

- Each `txt/<ID>.txt` starts with a short header: source, number, date, title, page and file URL.
- PDFs were converted with `pdftotext -layout`.
- For zip files, every PDF or DOCX inside was converted. Each part is marked `===== [zip member] … =====`.
- For BSE notices, the notice body is followed by its attachments, each marked `===== [attachment] … =====`.
- For short NSE covering circulars that forward a SEBI circular (the 2025–26 debt circulars, the MPS/pledge circulars and the older SOP, default and encumbrance circulars), the forwarded SEBI circular, as hosted on nsearchives, is appended in the same file.
- The SEBI Master Circular for Stock Exchanges and Clearing Corporations is published as a covering PDF plus 7 chapter PDFs. All of them are joined into `SEBI-MC-SECC.txt`.

## Coverage by theme (main IDs)

1. **Framework**
   - SEBI: `SEBI-SECC` (SECC Regulations 2018, last amended 22-11-2025), `SEBI-SECC-A4-2025`, `SEBI-MC-SECC` (Master Circular of 30-12-2024 with all chapters), `SEBI-PR-20260622` (SEBI announced a comprehensive review of the master circular).
   - NSE: `NSE-RULES` (29-06-2026), `NSE-BYELAWS` (19-06-2026), `NSE-REG-CM` (2026), `NSE-REG-WDM` (WDM trading regulations), `NSE-MC-LISTED-2026` (NSE Master Circular for Listed Companies, 30-04-2026).
   - BSE: `BSE-RULES` (compiled Rules, Bye-laws and Regulations zip), `BSE-20260430-29` (Master Circular – Listing Compliance 2026).
2. **Debt listing**
   - NSE checklists: private placement in-principle (07-08-2026), final listing, procedure and conditions (04-09-2026), public issue in-principle and final (25-06-2026), CP checklist, CP FAQs, REF guidance, uniform listing agreement.
   - NSE CP framework (26-12-2019), CP and debt re-issuance under the same ISIN, and debt listing fees (`NSE-LISTFEE-DEBT`, applicable from 01-11-2023).
   - BSE: Master Checklist 2026 (`BSE-20260430-51`), CP checklist and FAQs, CP framework notice (2019), debt listing agreement.
   - REF: `NSE-DT-CH4-20251202`, `BSE-20251127-66` and `NSE-REF-GUIDE`.
   - ISIN: `NSE-ISIN-DEBT-20261008` and `BSE-20261008-21`.
3. **EBP**
   - NSE: `NSE-EBP-OG` (NSE/DS/71301, 14-11-2025, with revised operating guidelines in Annexure I). It supersedes NSE/DS/69679 (14-08-2025) and NSE/DS/68064 (20-05-2025), which are also catalogued.
   - BSE: `BSE-EBP-OG` (BSEBOND Operational Guidelines, effective 17-11-2025) and `BSE-20251114-47`. They supersede `BSE-20250814-19` (effective 18-08-2025).
   - No EBP change was issued by either exchange in 2026.
4. **Continuous filings**
   - Integrated Filing (NSE 02-01-2025, 13-01-2025, 28-02-2025, 01-04-2025, FAQs 12-06-2026; BSE 20250102-4 and FAQs 20260612-13).
   - Single-filing API (latest NSE 19-06-2026, BSE 20260619-11).
   - XBRL Reg 50 for debt-listed entities (NSE 21-11-2025, BSE 20251121-72).
   - Record-date filing (NSE 29-04-2025 and 07-02-2025).
   - CP/NCS payment-status timeline (10-09-2024).
   - Default disclosure (21-11-2019 with SEBI text), encumbrance (08-08-2019), credit-rating system-driven disclosure (01-08-2025).
   - Reg 37/59A joint SOP for debt (31-07-2025), results formats (NSE 14-10-2026, BSE 20261014-25), LODR amendments 2026 (BSE 20260203-12, 20260722-7, 20261023-12).
   - NCS amendment 2026 (BSE 20260203-13), DT timelines, SDI disclosures, denomination, green and ESG debt, merchant-banker exemption and Credit Risk-o-Meter (Oct 2026).
5. **Penalties and enforcement**
   - NSE SOP fines circular (22-01-2020, with SEBI text).
   - NSE fine-waiver policy for commonly listed entities (26-08-2025, file of 13-01-2026).
   - MPS relaxation (NSE 07-04-2026, BSE 20260409-3).
   - BSE: SOP chapter (LODR Master Circular ch. VII, as hosted by BSE), uniform carve-out policies (equity and debt), guidance notes (equity and debt).
   - BSE high-promoter-pledge surveillance (20260902-39, repeated monthly).
6. **Secondary market**
   - NSE RFQ enhancements (16-10-2025 and 28-02-2026), RFQ T+0 timings (16-10-2026), RFQ funds settlement (NCL 04-06-2026), RFQ entity-type confirmation (30-09-2026).
   - NSE Corporate Bond Database simplification (19-05-2025), tri-party repo timings (17-09-2026).
   - NSE Clearing consolidated debt-segment circular (NCL/DS/74002, 30-04-2026) and debt formats update (13-07-2026).
   - Liquidity Window Facility: guidelines 11-02-2026 and issuer compliance 04-05-2026.
   - OBPP framework change (17-08-2026).
   - BSE: Clearing master circular for the debt segment (20260429-36), RFQ hours revision (20261019-21), RFQ Muhurat notices.
7. **Jun–Nov 2026 sweep**
   - Every NSE and BSE circular in the window that touches listed debt, CP, EBP, RFQ, LODR filings or fines is catalogued.
   - Substantive ones are fetched (see the 2026 IDs above).
   - The rest are listed with "listed only" in `note`:
     - 99 NSE and 135 BSE routine record-date or redemption trading suspensions for NCDs and CPs;
     - 6 NSE revised DVP-3 eligible corporate bond lists;
     - the member-facing copies of the Credit Risk-o-Meter circular.
   - Not catalogued on purpose: 241 NSE daily "Listing of privately placed securities on the debt market segment" circulars and the BSE company-specific debt/CP listing notices. These are issue-level admissions. They can be pulled from `nse_all` metadata if wanted.

## Superseded instruments

| Superseded | By |
|---|---|
| NSE/DS/68064 (20-05-2025), NSE/DS/69679 (14-08-2025) | NSE/DS/71301 (14-11-2025) – `NSE-EBP-OG` |
| BSE 20250814-19 (BSEBOND guidelines, 18-08-2025) | BSE 20251114-47 / BSEBOND Operational Guidelines effective 17-11-2025 |
| BSE Master Checklist 2025 (20250430-40); BSE PPDI checklist 2021 | BSE Master Checklist 2026 (20260430-51) |
| NSE Master Circular for Listed Companies 2025 | NSE Master Circular 2026 (30-04-2026) |
| NSE LWF guidelines NSE/DS/70953 (24-10-2025) | NSE/DS/72742 (11-02-2026) |
| NSE Clearing debt consolidated circular NCL/CMPT/67767 (30-04-2025) | NCL/DS/74002 (30-04-2026) |
| NSE revised Reg 37/59A SOP (29-09-2023) | Joint SOP (31-07-2025) |
| SEBI MC for SEs and CCs of 16-10-2023 | MC of 30-12-2024 (under review per SEBI press release of 22-06-2026) |

The superseded files I fetched are marked in `status`. The others are named in the `note` of the current row.

## Latest change dates

| Instrument | Latest version or change |
|---|---|
| SECC Regulations | 22-11-2025 (Fourth Amendment 2025) |
| SEBI MC for SEs/CCs | 30-12-2024; review announced 22-06-2026, no new MC found on sebi.gov.in |
| NSE Rules / Bye-laws / CM Regulations | 29-06-2026 / 19-06-2026 / 10-04-2026 |
| NSE EBP guidelines | 14-11-2025 |
| BSE EBP guidelines | 14-11-2025 (effective 17-11-2025) |
| NSE debt PP checklists | 07-08-2026 (in-principle), 04-09-2026 (procedure zip) |
| NSE debt listing fees | from 01-11-2023 (page updated 31-10-2023) |
| BSE Master Checklist / Listing Compliance MC | 30-04-2026 |
| NSE / BSE debt circulars (ISIN, Risk-o-Meter, MB exemption) | 08-10-2026 |
| RFQ timings | NSE 16-10-2026; BSE 19-10-2026 |
| Integrated Filing FAQs | 12-06-2026 (both exchanges) |
| Single-filing API | 19-06-2026 (both exchanges) |

## Failures and gaps

There were no fetch failures in the final run. NCL/DS/75187 returned 404 at first because I had the wrong file extension (it is a zip, not a pdf). I corrected it and it fetched.

Gaps:

1. **NSE website blocks plain downloads.** nseindia.in pages and APIs return 403 to scripted requests. I read the NSE listings (circular API, listed-company circular tables, rules page, debt checklist pages, listing-fee page) in a browser. The files themselves on nsearchives.nseindia.in/.com download normally. `NSE-LISTFEE-DEBT` is the text of the HTML page as shown in the browser.
2. **BSE notices search covers only 16-03-2026 onward.** BSE's notices search API (`getDataAdvance_New`) returns nothing for earlier dates. Older BSE notice numbers (2019–Feb 2026) were taken from BSE's own pages (EBP, CP, downloads, circulars-to-listed-companies, SOP non-compliance). The full 2025 BSE notice list was therefore not swept. The 2025 BSE items in the catalogue are the ones those pages link to.
3. **BSE Master Checklist 2026 is only partly in text** (`BSE-20260430-51`). The annexure DOCX (20 MB) holds the individual checklists as embedded OLE objects (Word/Acrobat "Package" objects). Only the index table converted. The original DOCX is kept locally in `pdf/BSE-20260430-51_att1.docx`. Extracting it needs an OLE extractor such as `olefile`, which is not installed.
4. **One BSE attachment not converted.** The XLS annexure of `BSE-20260902-39` (list of companies with high promoter pledge) is marked "not converted".
5. **No separate NSE or BSE 2025–26 circular revising LODR SOP fine amounts was found.** The fine schedule sits in the SEBI LODR Master Circular, already in the sebi-sources branch, as MC-LODR / MC-NCS-LODR. The exchange items here are the SOP implementation circular, the waiver/carve-out policies and the guidance notes.
6. **No standalone BSE RFQ operational-guidelines document was found.** BSE's RFQ rules are in the BSE Clearing debt master circular (20260429-36) and individual notices.
7. **The NSE EBP site (ebp.nseindia.com) was not crawled.** The guidelines are taken from the NSE/DS/71301 circular zip, whose Annexure I is the revised operating guidelines.
8. **Some documents carry no date.** They are marked `unknown` in the date column: NSE checklists, uniform listing agreement, BSE Rules zip, BSE CP FAQs, BSE SOP policies.

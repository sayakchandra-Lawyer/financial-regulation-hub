# OtherLaws-Hub fetch report ("Other relevant laws")

These are the official texts for the hub's "Other relevant laws" section: laws that bear on lending by banks, NBFCs and HFCs, covering how security is created, how it is enforced, recovery and lender conduct. Fetched 26-11-2026 from a laptop in India. Every row in `_catalogue.tsv` gives the official page opened (`detail_url`) and the exact file URL fetched (`pdf_url`). Rows whose `file` column is blank were **not fetched**. Their notes say why.

## What is here

| Folder / file | Contents |
|---|---|
| `pdf/` | Official PDFs. Only files under 5 MB are pushed to the branch. Larger ones are kept on the laptop, and their txt is pushed. |
| `txt/` | `pdftotext -layout` text of each PDF. Image-only PDFs were run through Windows OCR; their txt starts with a "MACHINE OCR" line. |
| `html/` | Empty. Every source used was a PDF. |
| `_catalogue.tsv` | One row per ID, with columns ID, title, reference_no, issue_date, effective_date, detail_url, pdf_url, file, notes. |

Sources used were India Code, sansad.in, financialservices.gov.in (DFS), enforcementdirectorate.gov.in, dolr.gov.in and state portals: IGR Maharashtra, revenue.delhi, igrsup, TN stationery/tnmoneylending/cms.tn, cra.tn, dpal.karnataka and legislative.assam.

## How the sites behaved
- **India Code:** every handle (detail) page returned HTTP 504 all day. Act PDFs were fetched from the bitstream servlet at `https://www.indiacode.nic.in/indiacode/bitstream/...`; the plain `/bitstream/...` path mostly returned 504. Bitstream URLs came from search results, never guessed. `upload.indiacode.nic.in` and `ViewFileUploaded` (where the rules files live) timed out.
- **eGazette:** refused all connections from this IP all day, in both curl and the browser. As a result:
  - no Gazette PDFs were fetched;
  - 2025-26 Gazette notifications are identified by their Gazette ID only.
- **rbidocs.rbi.org.in:** serves a human-verification CAPTCHA to scripts. It was **not bypassed**, so RBI's consolidated PDFs were not fetched (CIC Rules and Regulations as on 21-03-2024, CIC amendment regulations of 2017 and 2021, BPSS 2008 and PRB 2025 regulations). DFS copies were used where they exist.
- **legalaffairs.gov.in:** "Access Denied" (403). The DLA draft Arbitration Bill file is now 404.
- **revenuedepartment.gujarat.gov.in:** refused connections.

## Image-only files (txt is machine OCR)
STAMP-DL-AMD2007, MF-TN-GO580, MF-AS.

## Known staleness in fetched texts
- ACT-RDB: India Code "as on 15-05-2026". It does not show ss.6A and 15A as substituted by the Tribunals Reforms Act 2026 (w.e.f. 25-08-2026).
- ACT-CPA: does not show s.55(1A) as substituted by the same Act.
- ACT-PSS (DFS copy): check it for the s.10A amendment by Act 21 of 2026.
- RULES-PML: the Enforcement Directorate (ED) consolidated copy's footnotes stop at 2017. The 2023 amendments are missing, so do not rely on it as current.
- RULES-CIC and REGS-CIC: original 2006 Gazette texts, not consolidated.
- STAMP-RJ: India Code upload from 2019.

## 2025-26 changes (01-01-2025 to 26-11-2026)
Method:
- Every Bill in the sansad.in bills API with an introduction date from 01-01-2025 (344 bills) was screened by title.
- The texts of the relevant Acts as passed were searched for each Part A Act name.
- The Jan Vishwas 2026 Schedule was read serial by serial.
- eGazette could not be searched (see above), so rule amendments and commencement notifications below come from official pages where available. Otherwise they are marked "Gazette ID only, not verified".

### Central Acts passed that amend a Part A Act
| ID | What | Reference / date | In force | Source |
|---|---|---|---|---|
| AMD-RDB-20260813 (also covers CPA) | **Tribunals Reforms Act, 2026**: s.6 substitutes ss.6A (DRT Presiding Officer) and 15A (DRAT Chairperson) of the **RDB Act**; s.12 substitutes s.55(1A) of the **Consumer Protection Act, 2019**. Service conditions now governed by the 2026 Act. | Act 17 of 2026, assent 13-08-2026 | 25-08-2026 (Gazette ID CG-DL-E-25082026-275749, not fetched) | sansad.in passed text |
| AMD-PSS-20260817 | **Taxation and Other Laws (Amendment) Act, 2026**, s.2: **PSS Act s.10A**. Electronic modes are now those the Central Government notifies, no longer those under s.269SU of the Income-tax Act, 1961. | Act 21 of 2026, assent 17-08-2026 | On publication of the Act in the Gazette | sansad.in passed text |
| ACT-BBE-2026 | **Bankers' Books Evidence Act, 2026**: repeals and replaces the 1891 Act. Works alongside the BSA 2023 and IT Act. | Act 15 of 2026, assent 13-08-2026 | 01-10-2026 (notification of 10-09-2026, PIB PRID 2309122) | DFS copy of Gazette |
| ACT-REPAMD-2025 | **Repealing and Amending Act, 2025**: repeals spent amending Acts (Arbitration amendments of 2015 and 2021, NI amendment of 2018, Factoring amendment of 2021); principal Acts unchanged. Also amends **General Clauses Act s.27 and CPC**: "registered post" becomes "speed post with registration", which affects how notices are served. | Act 37 of 2025, assent 20-12-2025 | 20-12-2025 | sansad.in |
| ACT-AIRCRAFT-2025 | **Protection of Interests in Aircraft Objects Act, 2025**: Cape Town Convention security interests over aircraft objects. A new Act, not an amendment. | Act 17 of 2025, assent 16-04-2025 | Gazette ID CG-DL-E-30042025-262777, reportedly 01-05-2025; not verified | sansad.in |

### Jan Vishwas (Amendment of Provisions) Act, 2026 (Act 8 of 2026, assent 07-04-2026)
All 80 Schedule serials were checked. **None amends any Part A Act.** The Consumer Protection Act, 2019 appears only as a cross-reference inside the Legal Metrology entry. Serial 7 amends the **RBI Act, 1934**:
- **s.58B:** in the marginal heading, "Penalties" becomes "Offences", and sub-section (4AA) is omitted.
- **s.58G:** in the marginal heading, "fine" becomes "penalties".

Commencement is by notification, Act by Act; none was found.

### Regulations, rules and notifications (not fetched unless a file is listed)
| Item | Date | Status |
|---|---|---|
| PSS Act amendment creating the Payments Regulatory Board | in force 09-05-2025 | RBI press release prid=61974 |
| Payments Regulatory Board Regulations, 2025 (supersede the BPSS Regulations 2008), RBI Notification CO.DPSS.BD.No.S168/02-01-012/2025-2026 (AMD-PSS-20250520) | 20-05-2025 | on rbidocs; CAPTCHA, not fetched |
| DRTs and DRATs Electronic Filing (Amendment) Rules, 2025, G.S.R. 403(E) | 23-06-2025 | secondary reports only; eGazette blocked |
| DRT (Refund of Court Fees) Amendment Rules, 2026 | about May 2026 | secondary reports only |
| PML Rules: S.O. 4697(E) on intermediaries uploading/accessing KYC via CKYCRR | 16-10-2025 | Gazette ID CG-DL-E-16102025-266971; not verified |
| DFS S.O. 5034(E): designates CERSAI for CKYCRR integration / Aadhaar authentication | 06-11-2025 | Gazette ID CG-DL-E-06112025-267407; not verified |

### State laws, 2025-26
| What | Reference / date | In force |
|---|---|---|
| **Karnataka Micro Loan and Small Loan (Prevention of Coercive Actions) Act, 2025** (MF-KA), which replaced the 2025 Ordinance | Karnataka Act 15 of 2025, 24-03-2025 | — |
| **Karnataka Money Lenders (Amendment) Act, 2024** (ML-KA-AMD2025) | Karnataka Act 16 of 2025 | — |
| **Karnataka Prohibition of Charging Exorbitant Interest (Amendment)** (ML-KA-PCEI2025) | Karnataka Act 17 of 2025 | — |
| **Tamil Nadu Money Lending Entities (Prevention of Coercive Actions) Act, 2025** (MF-TN) | TN Act 40 of 2025, Gazette 09-06-2025 | **19-11-2025** by G.O.(Ms) No.580 |
| TN Money Lending Entities Rules, 2025 (MF-TN-RULES) | Gazette Ext. No.761 | — |
| TN notification under s.4(1) (MF-TN-2026-S4) | 16-02-2026 | — |
| TN order under s.31 (MF-TN-2026-S31) | 04-08-2026 | — |
| Maharashtra Stamp Act, consolidated (STAMP-MH) | modified to 07-04-2026 | — |
| Gujarat Stamp Act, consolidated (STAMP-GJ) | modified to 28-02-2026 | not fetched |
| Karnataka Stamp Act (STAMP-KA) | amended to Act 30 of 2025 | — |

- No 2025-26 change was found for: MF-AP, MF-AS, PID-MH, ML-MH, ML-TN, ML-GJ.
- This is not conclusive: state gazettes were not searched systematically.

### Pending or draft (official)
- **Draft Registration Bill, 2025** (DoLR, 27-05-2025; comments due by 25-06-2025): would repeal the Registration Act, 1908. The draft and DoLR's feedback summary were fetched. It had not been introduced in Parliament as of 26-11-2026.
- **Draft Arbitration and Conciliation (Amendment) Bill, 2024** (DLA, PIB 18-10-2024): the draft could not be fetched. No Bill has been introduced in Parliament.
- **Private Members' Bills, pending in Lok Sabha** (introduced 05-12-2025; fetched):
  - IT (Amendment) Bill, 2025 (No. 28)
  - Consumer Protection (Amendment) Bill, 2025 (No. 39)
  - PML (Amendment) Bill, 2025 (No. 75)
- **No government Bill to amend** any of these Acts was pending on sansad.in as of 26-11-2026: SARFAESI, RDB, Contract, TPA, Stamp, Registration, NI, Limitation, Specific Relief, BUDS, Chit Funds, CICRA or Factoring.
- Business Standard (20-01-2026) reported that a SARFAESI amendment on CERSAI control was planned. No Bill has followed.

## Retry (15:30-16:10 UTC, 26-11-2026)
- **What was retried:** every priority row, against India Code bitstream URLs taken from search results. Each try waited 25 s and was attempted 3 times.
- **Result:** every India Code bitstream returned **HTTP 504**, including files that had downloaded earlier in the day. drt.gov.in returned 503.
- **Fallbacks used:** where an official ministry or State copy existed, it was used instead. The row notes say so.

| ID | Copy used |
|---|---|
| ACT-PMLA | Enforcement Directorate (footnotes to 2019) |
| ACT-CHIT | Delhi Govt Registrar of Chit Funds (scanned; machine OCR) |
| ML-KA | Karnataka DPAL copy (2020) |
| STAMP-KA | Karnataka DPAL copy, as amended to Act 4 of 2024 |
| ML-MH | Maharashtra Law and Judiciary reprint, to 31-08-2018 |
| PID-MH | Maharashtra Home Dept copy (scanned; machine OCR) |

- **Alternates tried and rejected:**
  - legislative.gov.in for the Arbitration Act serves only an HTML shell.
  - The meity.gov.in "IT Act" link was an advisory, not the Act.
  - The DFS "beta" URLs now return 404.

## Second and third retries (17:25 and 18:20 UTC, 26-11-2026)
- **India Code:**
  - The home page loaded (200), and so did files already fetched earlier in the day, which loaded instantly.
  - Every file not fetched before still returned **504**, on both the `/bitstream/` and `/indiacode/bitstream/` paths, with 3 tries each 25 s apart.
  - It looks as if India Code is serving only cached copies while its file store is down. **No new rows were fetched.**
- **Mirrors tried:**
  - meity.gov.in: the only full-text "IT Act" PDF is the 2005 Expert Committee's *proposed amendments* draft, so it was rejected.
  - cersai.org.in: the "Acts and Rules" page returned 500, and its pages need JavaScript.
  - drt.gov.in: 503 earlier.
  - legislative.gov.in: serves only an HTML shell for the Arbitration Act PDF.
  - No India Code search result exists for the Kerala Money-Lenders Act, 1958.

## Morning retry (27-11-2026): new India Code site
- **Old site:** indiacode.nic.in still returned 504 for every missing file (3 tries, 25 s apart).
- **New site:** the new India Code (**indiacode.gov.in**, a DSpace 7 site) answered. Items were found through its public search API (`/server/api/discover/search/objects`). The PDF link for each was taken from the item's bundle listing (`/server/api/core/items/{id}/bundles`), never guessed.
- **What came down:** 27 files.
  - **Central Acts:** ARB, FRA, IT, BUDS. CHIT and PMLA were also replaced with the central India Code texts ("as on 01-07-2026" style covers), instead of the Delhi and Enforcement Directorate copies used on 26-11.
  - **Rules:** SIE (+2007 amendment), CERSAI (+2013 and 2016 amendments), DRT Procedure, BUDS, PML amendments of 2022 and 2023.
  - **State laws:**
    - Karnataka: MF-KA (+ the 2025 Ordinance) and ML-KA-PCEI2025.
    - Andhra Pradesh: MF-AP.
    - Kerala: the **Kerala Money Lenders Act 1958** (newly added to India Code on 13-10-2026) and ML-KL-PCEI.
    - Tamil Nadu: ML-TN-PCEI.
    - Gujarat: ML-GJ.
    - Rajasthan: STAMP-RJ (updated to 18-05-2026).
    - West Bengal: STAMP-WB-FA2024.
    - Bihar: two PID amendment Acts (Hindi).
- **Scans:** the SIE and CERSAI rules files are scanned Gazette copies with a poor text layer, so read the PDFs.
- **This fixes two staleness items above:**
  - RULES-PML: now partly cured by RULES-PML-AMD2022 and RULES-PML-AMD2023.
  - STAMP-RJ: now the 2026 update.

Later on 27-11 the principal Bihar PID Act 2002 (Hindi) was also found there (PID-BR).

## Missing / not fetched (after 27-11 retry)
These are the rows with a blank `file` column in `_catalogue.tsv`. The notes on each row give the reason.

| Reason | IDs |
|---|---|
| Not on the new India Code either (searched by title) | STAMP-GJ, STAMP-WB-2021, PID-TN |
| Gazette-only rules; not on the new India Code; eGazette refused connections | RULES-STAMPCOLL, RULES-CPA-JUR |
| Site blocked | DRAFT-ARB-2024 (Dept of Legal Affairs, 403) |
| rbidocs CAPTCHA (not bypassed) | AMD-PSS-20250520 |

## Row status (generated from _catalogue.tsv)

| ID | Status | Reason / source |
|---|---|---|
| ACT-ICA | fetched | India Code handle page returned HTTP 504 on every try (dynamic pages down 26-11-2026); PDF fetched from the bitstream servlet under /indiacode/bitstream/. |
| ACT-TPA | fetched | India Code handle page returned HTTP 504 on every try (dynamic pages down 26-11-2026); PDF fetched from the bitstream servlet under /indiacode/bitstream/. |
| ACT-TRUSTS | fetched | India Code handle page returned HTTP 504 on every try (dynamic pages down 26-11-2026); PDF fetched from the bitstream servlet under /indiacode/bitstream/. |
| ACT-SOGA | fetched | India Code handle page returned HTTP 504 on every try (dynamic pages down 26-11-2026); PDF fetched from the bitstream servlet under /indiacode/bitstream/. |
| ACT-SARFAESI | fetched | India Code handle page returned HTTP 504 on every try (dynamic pages down 26-11-2026); PDF fetched from the bitstream servlet under /indiacode/bitstream/. File Last-Modified 24-04-2024. |
| ACT-RDB | fetched | India Code handle page returned HTTP 504 on every try (dynamic pages down 26-11-2026); PDF fetched from the bitstream servlet under /indiacode/bitstream/. Cover says [As on the 15th May, 2026]; does NOT yet reflect Tribunals Reforms Act 2026 (ss.6A/15A substituted w.e.f. 25-08-2026, see AMD-RDB-2026 |
| ACT-ARB | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). Central item a1996-26.pdf. |
| ACT-STAMP | fetched | India Code handle page returned HTTP 504 on every try (dynamic pages down 26-11-2026); PDF fetched from the bitstream servlet under /indiacode/bitstream/. File Last-Modified 25-06-2025. |
| ACT-REG | fetched | India Code handle page returned HTTP 504 on every try (dynamic pages down 26-11-2026); PDF fetched from the bitstream servlet under /indiacode/bitstream/. File Last-Modified 20-06-2024. |
| ACT-NI | fetched | India Code handle page returned HTTP 504 on every try (dynamic pages down 26-11-2026); PDF fetched from the bitstream servlet under /indiacode/bitstream/. File Last-Modified 25-08-2023. |
| ACT-FRA | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). Cover says [As on 1st July 2026]. |
| ACT-LIM | fetched | India Code handle page returned HTTP 504 on every try (dynamic pages down 26-11-2026); PDF fetched from the bitstream servlet under /indiacode/bitstream/. |
| ACT-SRA | fetched | India Code handle page returned HTTP 504 on every try (dynamic pages down 26-11-2026); PDF fetched from the bitstream servlet under /indiacode/bitstream/. File Last-Modified 14-05-2024. |
| ACT-BSA | fetched | India Code handle page returned HTTP 504 on every try (dynamic pages down 26-11-2026); PDF fetched from the bitstream servlet under /indiacode/bitstream/. |
| ACT-CPA | fetched | India Code handle page returned HTTP 504 on every try (dynamic pages down 26-11-2026); PDF fetched from the bitstream servlet under /indiacode/bitstream/. Does not reflect s.55(1A) substitution by Tribunals Reforms Act 2026 (AMD-CPA-20260813). |
| ACT-CHIT | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). Central item; cover says [As on 1st July 2026]. Replaces the Delhi Govt scanned copy used on 26-11. Central handle 1797 has only the Hindi PDF in search results; this |
| ACT-PSS | fetched | DFS 'Acts and Policies' copy. Check for the 2023 PRB amendment (in force 09-05-2025) and s.10A amendment by Act 21 of 2026 (AMD-PSS-20260817). India Code copy: https://www.indiacode.nic.in/indiacode/bitstream/123456789/2082/4/a2007-51.pdf |
| ACT-PMLA | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). Replaces the Enforcement Directorate copy used on 26-11. |
| ACT-IT | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). |
| ACT-CICRA | fetched | DFS 'Acts and Policies' copy (uploaded 2026-06). |
| ACT-BUDS | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). |
| RULES-CIC | fetched | Original notification text, not consolidated. RBI's consolidated 'CIC Rules and Regulations 2006 (21-03-2024)' at rbidocs.rbi.org.in could not be fetched: rbidocs serves a CAPTCHA to scripts. reference_no to be read from the PDF. |
| REGS-CIC | fetched | Original text; amendments of 2017 and 2021 are on rbidocs (CAPTCHA, not fetched). |
| REGS-PSS | fetched | BPSS Regulations 2008 were superseded by the Payments Regulatory Board Regulations, 2025 (in force 20-05-2025, RBI Notification CO.DPSS.BD.No.S168/02-01-012/2025-2026); both PDFs are on rbidocs (CAPTCHA, not fetched). |
| RULES-FACT | fetched | DFS notification text dated 02-04-2012. |
| RULES-PML | fetched | Enforcement Directorate (Dept of Revenue) consolidated copy, file Last-Modified 22-11-2025, but its footnotes stop at 2017 (G.S.R. 1318(E) of 23-10-2017): later amendments (e.g. G.S.R. 745(E) of 17-10-2023) are NOT in it. 13.8 MB so PDF not pushed (txt only). |
| RULES-SIE | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). Scanned Gazette copy; text layer is poor - read the PDF. Earlier NOT FETCHED: the only official copies found are on India Code (upload.indiacode.nic.in and ViewFileUp |
| RULES-CERSAI | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). Original G.S.R. 276(E) of 31-03-2011 (scanned). Amendments 2013 and 2016 in RULES-CERSAI-AMD2013 / -AMD2016; later amendments (e.g. 2020) not on India Code. Earlier N |
| RULES-DRT | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). Amendments of 1994 and 1997 are separate India Code items (not fetched). Earlier NOT FETCHED: upload.indiacode.nic.in timed out. Text also on drt.gov.in/DebtRecoveryR |
| RULES-BUDS | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle).  Earlier NOT FETCHED: DFS beta URL now 404; India Code timed out. |
| RULES-STAMPCOLL | **missing** | NOT FETCHED: eGazette (Dept of Revenue) refused connections all day. |
| RULES-CPA-JUR | **missing** | NOT FETCHED: eGazette refused connections; consumeraffairs.nic.in not reached in time. |
| STAMP-MH | fetched | State: Maharashtra. IGR Maharashtra consolidated text incl. Schedule I; cover says modified up to 07-04-2026. |
| STAMP-KA | fetched | India Code returned 504; Karnataka DPAL copy as amended to Act 4 of 2024 used (does not show Act 30 of 2025). State: Karnataka. India Code state copy; file name says amended to Karnataka Act 30 of 2025. |
| STAMP-GJ | **missing** | State: Gujarat. NOT FETCHED: revenuedepartment.gujarat.gov.in refused connections from this IP (4 tries). |
| STAMP-RJ | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). State: Rajasthan. File name says updated up to 18-05-2026. State: Rajasthan. India Code copy uploaded 2019, so it may omit later amendments; igrs.rajasthan.gov.in act |
| STAMP-DL-SCH1A | fetched | State: Delhi. Delhi Revenue Dept copy (ss.62 onwards + Schedule I-A). Currency date not stated. |
| STAMP-DL-AMD2007 | fetched | State: Delhi. Image-only PDF; txt is machine OCR. |
| STAMP-UP-ACT | fetched | State: Uttar Pradesh. File Last-Modified 28-11-2025. |
| STAMP-UP-SCH1B | fetched | State: Uttar Pradesh. UP uses Schedule I-B. File Last-Modified 28-11-2025. |
| STAMP-TN-2023 | fetched | State: Tamil Nadu. TN amends Schedule I of the Indian Stamp Act directly; no consolidated official TN schedule was found. |
| STAMP-WB-FA2024 | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). State: West Bengal. State: West Bengal. No consolidated WB Schedule IA found; latest amending Act located. |
| STAMP-WB-2021 | **missing** | NOT FETCHED (download failed). State: West Bengal. |
| ML-MH | fetched | India Code returned 504; Maharashtra Law and Judiciary Dept reprint 'as modified up to 31-08-2018' used. State: Maharashtra. A 'text as on 22-11-2023' reprint is listed on lj.maharashtra.gov.in (not fetched). |
| ML-KA | fetched | India Code returned 504; Karnataka DPAL copy (file dated 2020) used; it predates the 2025 amendment (ML-KA-AMD2025). State: Karnataka. India Code copy uploaded 2025. |
| ML-KA-AMD2025 | fetched | State: Karnataka. 2025 amendment. |
| ML-KA-PCEI2025 | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). State: Karnataka. File 17_of_2025_(e): the Karnataka Prohibition of Charging Exorbitant Interest Act 2004 with the 2025 amendment. State: Karnataka. |
| ML-TN | fetched | State: Tamil Nadu. Co-operation Dept copy (2021 upload). |
| ML-TN-PCEI | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). State: Tamil Nadu. English Gazette text (the other file on the item is Tamil). State: Tamil Nadu. |
| ML-KL | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). State: Kerala. Item added to India Code 13-10-2026. State: Kerala. Earlier NOT FETCHED: no official full text found (lawsect.kerala.gov.in only lists it). See ML-KL-P |
| ML-KL-PCEI | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). State: Kerala. English translation published in the Kerala Gazette. State: Kerala. |
| ML-GJ | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). State: Gujarat. English text as amended by Guj. 11 of 2015 and 2 of 2018. State: Gujarat. |
| MF-KA | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). State: Karnataka. State: Karnataka. Replaced the 2025 Ordinance of the same name. |
| MF-TN | fetched | State: Tamil Nadu. TN Gazette Ext. No. 265 (09-06-2025). In force 19-11-2025 by G.O.(Ms) No.580 (MF-TN-GO580). |
| MF-TN-RULES | fetched | State: Tamil Nadu. |
| MF-TN-GO580 | fetched | State: Tamil Nadu. Image-only PDF; txt is machine OCR. |
| MF-TN-2026-S4 | fetched | State: Tamil Nadu. |
| MF-TN-2026-S31 | fetched | State: Tamil Nadu. |
| MF-TN-BILL2025 | fetched | State: Tamil Nadu. |
| MF-AP | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). State: Andhra Pradesh. State: Andhra Pradesh. |
| MF-AS | fetched | State: Assam. Image-only PDF; txt is machine OCR. |
| PID-MH | fetched | India Code returned 504; Maharashtra Home Dept copy used. Image-only, txt is machine OCR. State: Maharashtra. |
| PID-TN | **missing** | State: Tamil Nadu. NOT FETCHED: no official full-text PDF found in time (only TN Gazette orders under s.3). |
| PID-BR | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). State: Bihar. Bihar Gazette (Hindi) text of the 2002 Act; India Code item is titled 'NBFC Act 2002 & Rules 2004'. State: Bihar. |
| AMD-RDB-20260813 | fetched | Bill No. 153-F of 2026 as passed by both Houses (assent 13-08-2026). In force 25-08-2026 per notification CG-DL-E-25082026-275749 (eGazette ID; PDF not fetched because eGazette refused connections; date confirmed only by secondary reports). Also serves as AMD-CPA-20260813. |
| AMD-PSS-20260817 | fetched | s.10A: 'electronic modes of payment prescribed under s.269SU of the Income-tax Act, 1961' replaced by 'one or more electronic modes of payment as the Central Government may, by notification, specify', w.e.f. publication of the Act in the Gazette. Text is the Bill as passed (assent 17-08-2026). |
| ACT-BBE-2026 | fetched | Gazette of India Part II s.1 copy posted by DFS. In force 01-10-2026 by notification dated 10-09-2026 (PIB PRID 2309122). |
| ACT-AIRCRAFT-2025 | fetched | Security interests in aircraft objects (Cape Town Convention). Commencement notification CG-DL-E-30042025-262777 (eGazette ID, not fetched); secondary sources say w.e.f. 01-05-2025 - verify. |
| ACT-REPAMD-2025 | fetched | First Schedule repeals spent amending Acts incl. Arbitration and Conciliation (Amendment) Acts 2015 and 2021, Negotiable Instruments (Amendment) Act 2018, Factoring Regulation (Amendment) Act 2021 (principal Acts unchanged). Second Schedule amends General Clauses Act 1897 s.27 and CPC: 'registered p |
| ACT-JANVISHWAS-2026 | fetched | Gazette copy also at RBI-NBFC-Register/verify/jan_vishwas_2026.pdf (CG-DL-E-08042026-271642). Its 80-entry Schedule amends NONE of the Acts in Part A; Sl.7 amends RBI Act 1934 (ss.58B, 58G). |
| AMD-PSS-20250520 | **missing** | NOT FETCHED: rbidocs serves a CAPTCHA to scripts (not bypassed). PRB constituted under the PSS Act amendment that came into force 09-05-2025 (RBI press release prid=61974). |
| DRAFT-REG-BILL-2025 | fetched | Notice + full draft. Comments due 25-06-2025. Not introduced in Parliament as of 26-11-2026 (absent from sansad.in bills list). |
| DRAFT-REG-BILL-2025-FEEDBACK | fetched |  |
| DRAFT-ARB-2024 | **missing** | NOT FETCHED: old DLA file URL now 404 on www host; the new legalaffairs.gov.in returns 'Access Denied' (403). PIB release confirms the draft (comments by 03-11-2024). No such Bill introduced as of 26-11-2026. |
| PMB-LS28-2025-IT | fetched | Private Member's Bill; status Pending. |
| PMB-LS39-2025-CPA | fetched | Private Member's Bill; status Pending. |
| PMB-LS75-2025-PMLA | fetched | Private Member's Bill; status Pending. |
| MF-KA-ORD2025 | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). State: Karnataka. Karnataka Gazette Ext. No. 89 (12-02-2025); replaced by Act 15 of 2025 (MF-KA). |
| RULES-SIE-AMD2007 | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). Scanned Gazette copy. |
| RULES-CERSAI-AMD2013 | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). Scanned Gazette copy. |
| RULES-CERSAI-AMD2016 | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). Notification dated 22-01-2016 (scanned). |
| RULES-PML-AMD2022 | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). Gazette notification; fills part of the post-2017 gap in RULES-PML. |
| RULES-PML-AMD2023 | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). Gazette notification of 07-03-2023. |
| PID-BR-AMD2013 | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). State: Bihar. Hindi Gazette text. |
| PID-BR-AMD2017 | fetched | Fetched 27-11-2026 from the new India Code (indiacode.gov.in REST API; item found by search, file link taken from the item's bundle). State: Bihar. Hindi Gazette text. |

Fetched: 78 of 85 rows.

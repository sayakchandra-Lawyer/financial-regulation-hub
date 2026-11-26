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

## Missing / not fetched
These are the rows with a blank `file` column in `_catalogue.tsv`. The notes on each row give the reason.

| Reason | IDs |
|---|---|
| India Code bitstream returned 504 on every try; no other official copy found | ACT-ARB, ACT-FRA, ACT-IT, ACT-BUDS, STAMP-RJ, STAMP-WB-FA2024, STAMP-WB-2021, ML-KA-PCEI2025, ML-TN-PCEI, ML-KL-PCEI, ML-GJ, MF-KA, MF-AP, PID-BR |
| Only copies are on upload.indiacode.nic.in, which timed out (RULES-DRT also: drt.gov.in returned 503) | RULES-SIE, RULES-CERSAI, RULES-DRT, RULES-BUDS |
| eGazette refused connections | RULES-STAMPCOLL, RULES-CPA-JUR |
| Site unreachable or blocked | STAMP-GJ (Gujarat revenue site), DRAFT-ARB-2024 (DLA, 403) |
| rbidocs CAPTCHA (not bypassed) | AMD-PSS-20250520 |
| No official full text found | ML-KL, PID-TN |

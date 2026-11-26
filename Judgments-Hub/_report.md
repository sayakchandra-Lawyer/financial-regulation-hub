# Judgments-Hub fetch report ("Key Judgments")

These files were fetched on 26-11-2026 from a laptop in India. Everything is inside `Judgments-Hub/`. A follow-up the same day added the stay checks for VISHNU and VIRAJ and the Insurance Ombudsman award summaries (OMB1-8). The orphan branch `judgments-sources` of the hub repo carries only `_index.tsv`, `_report.md` and the official `txt/*.txt` (no PDFs, no `*.kanoon.txt`).

## What is here

| Path | Contents |
|---|---|
| `pdf/<ID>.pdf` | Official PDFs. There are 10: RHC, AVIVA, ATHENA, VISHNU, ILFS, UMANG, PUNEET, RCAP, YES-AT1 and VIRAJ. |
| `txt/<ID>.txt` | `pdftotext -layout` text of each official PDF, except AVIVA (see below). |
| `txt/OMB<n>.txt` | Insurance Ombudsman award summaries (OMB1-8), cut from CIO's public award compilations on cioins.co.in. Each file starts with the source URL and line range. |
| `txt/<ID>.kanoon.txt` | **Cross-reading copies only, not official.** They are taken from indiankanoon.org and the first line of each says so. There are 9: NEELAM, RAMLAL, JESNA, LEADER, DEEDS and HEALTH1-4. |
| `_index.tsv` | One row per ID with these columns: ID, forum, title as on order, case number, date (YYYY-MM-DD), bench, official URL, pages, note. |
| `_work/` | Scratch files: search pages, candidate PDFs and scripts. It can be deleted. |

## Every key at a glance

| Key | Forum | Case no. | Parties | Date | Official URL | Text saved? |
|---|---|---|---|---|---|---|
| RHC | NCLAT | CA(AT)(Ins) 26/2019 | HDFC Ltd v RHC Holding Pvt Ltd | 2019-07-10 | nclat.gov.in/.../11493138195d25d9f0d704d.pdf | Yes: PDF + txt |
| AVIVA | **NCLT New Delhi** (not NCLAT) | CP(IB)-1885(ND)/2019 | Apeejay Trust v Aviva Life Insurance Co India Ltd | 2019-11-04 | ibbi.gov.in/uploads/order/885b648aa53e06bc8061a68846666f9c.pdf | PDF only. It is a scan and OCR did not complete. |
| ATHENA | NCLAT | CA(AT)(Ins) 633/2020 | SBI v Athena Energy Ventures Pvt Ltd | 2020-11-24 | nclat.nic.in/.../5705615705fbcb7aea478a.pdf | Yes |
| VISHNU | NCLAT | CA(AT)(Ins) 346 & 347/2018 | Dr Vishnu Kumar Agarwal v Piramal Enterprises Ltd | 2019-01-08 | nclat.nic.in/.../2233762365c34633dbd7b3.pdf | Yes |
| ILFS | NCLAT | CA(AT) 346/2018 (+347/2018, 256/2019) | Union of India v IL&FS Ltd & Ors | 2020-03-12 | nclat.nic.in/.../4981134645e6a3679a316a.pdf | Yes |
| UMANG | NCLAT | CA(AT)(Ins) 926/2019 | Flat Buyers Assn Winter Hills-77 v Umang Realtech Pvt Ltd | 2020-02-04 | nclat.nic.in/.../18011332575e3d0b157e29a.pdf | Yes |
| PUNEET | NCLAT | CA(AT)(Ins) 390-394/2022 | Puneet Kaur v K V Developers Pvt Ltd & Ors | 2022-06-01 | efiling.nclat.gov.in/nclat/order_view.php?path=... | Yes |
| RCAP | NCLAT | CA(AT)(Ins) 132, 133, 134 & 139/2023 | **Vistra ITCL (India) Ltd v Torrent Investments** Pvt Ltd & Ors | 2023-03-02 | nclat.nic.in/display-board/view_order_pdf?fid=9910110008382023... | Yes |
| NEELAM | NCDRC | RP 4461/2012 | Neelam Chopra v LIC of India | 2018-10-08 | NOT FOUND | kanoon copy only |
| RAMLAL | NCDRC | RP 658/2012 | Ram Lal Aggarwalla v Bajaj Allianz Life Ins Co Ltd | 2013-04-23 | NOT FOUND | kanoon copy only |
| JESNA | NCDRC | RP 3333/2013 | HDFC Bank Ltd v Jesna Jose | 2020-12-21 | NOT FOUND | kanoon copy only |
| LEADER | NCDRC | FA 112/2015 | Chairman, PNB v Leader Valves Ltd | 2020-03-13 | NOT FOUND | kanoon copy only |
| DEEDS | NCDRC | CC 129/2017 | Manoj Madhusudhanan v ICICI Bank Ltd | 2023-08-31 | NOT FOUND | kanoon copy only |
| HEALTH1 | NCDRC | NC/RP/742/2022 | Religare Health Ins Co v Jarnail Singh | 2026-06-09 | NOT FOUND | kanoon copy only |
| HEALTH2 | Punjab SCDRC | FA 133/2020 | Religare Health Ins Co v Harwant Singh | 2021-02-08 | NOT FOUND | kanoon copy only |
| HEALTH3 | Gujarat SCDRC | FA 690/2017 | Dr Rikesh T Majmudar v United India Ins Co | 2023-06-30 | NOT FOUND | kanoon copy only |
| HEALTH4 | Delhi SCDRC | FA 22/2016 | Oriental Ins Co v Virender Kumar Gupta | 2023-02-01 | NOT FOUND | kanoon copy only |
| OMB1-8 | Insurance Ombudsman (Ahmedabad, Chennai, Pune, Bhopal) | see `_index.tsv` | see below | 2014-2017 | cioins.co.in compilations | Yes: summaries only |
| YES-AT1 | Supreme Court | CA 3182/2025 (Diary 6245/2023), 2026 INSC 1132 | Yes Bank Ltd v Axis Trustee Services Ltd & Ors | 2026-10-15 | api.sci.gov.in/supremecourt/2023/6245/6245_2023_6_1501_75512_Judgement_15-Oct-2026.pdf | Yes |
| VIRAJ | Bombay HC (OS) | WP 719/2020 | Viraj Chetan Shah v Union of India & Anr | 2024-04-23 | bombayhighcourt.gov.in/bhc/judgments/order-pdf/HCBM020225202019/2024-04-23/37?path=... | Yes |

`_index.tsv` has the full URLs.

## Corrections to the brief's details
- **AVIVA:** this is an **NCLT New Delhi** admission order (CP(IB)-1885(ND)/2019, 04-11-2019), not an NCLAT ruling. NCLAT's register has no Aviva entry. The case was withdrawn after settlement on 22-11-2019 (IBBI lists that order too).
- **RCAP:** the cause title is *Vistra ITCL (India) Ltd v Torrent Investments Pvt Ltd*. The appeals are CA(AT)(Ins) 132, 133 and 134 of 2023, with 139 of 2023 (IndusInd International Holdings). The order's own page footer says "135" in place of 134; this is a typo in the order.
- **ILFS:** this is a common judgment that also covers CA(AT) 347/2018 and 256/2019.
- **VISHNU, PUNEET, UMANG:** the dates and numbers in the brief were confirmed. PUNEET is a common judgment covering 390-394/2022.
- **NEELAM:** this is a **life** policy (LIC) case about undisclosed diabetes. It is not a health-insurance policy case.
- **JESNA:** the card was a prepaid Forex Plus debit card.
- **LEADER:** First Appeal 112/2015, decided 13-03-2020. **DEEDS:** Consumer Case 129/2017, decided 31-08-2023.

## What could not be found, and why

**NCDRC and State Commission official copies (NEELAM, RAMLAL, JESNA, LEADER, DEEDS, HEALTH1-4).**
- The old confonet host `cms.nic.in` no longer resolves.
- e-Jagriti puts a CAPTCHA on its case status, advance search and judgment search pages. I did not try to get past the CAPTCHA, and I stopped probing its back-end API.
- No copies were found on ncdrc.nic.in.

To finish these rows, someone needs to open https://e-jagriti.gov.in/judgement (or Case Status), enter the CAPTCHA, and save each PDF as `pdf/<ID>.pdf`. I can then do the text conversion and update the index. Case numbers for each search are in `_index.tsv`. The NCDRC "old case format" fields are: Commission = NCDRC, case type RP/FA/CC, number and year.

**Insurance Ombudsman awards from 2022 onwards.** These are not public. CIO's Annual Report 2023-24 says award downloads are limited to an OTP on the complainant's own registered mobile, for data privacy. I did not use the complainant tracker. The annual reports for 2022-23 to 2024-25 carry statistics only, no award digests. So OMB1-8 below use the latest public compilations, which stop at about 2017-18.

## Insurance Ombudsman award summaries (OMB1-8)

Source: the Council for Insurance Ombudsmen's public award compilations on cioins.co.in. These are the Ombudsman offices' own published summaries, not the signed awards. Many summaries do not print the award number or the Ombudsman's name; `_index.tsv` says so where that is the case.

| Key | Centre | Parties | Award / complaint no. | Date | Issue | Result |
|---|---|---|---|---|---|---|
| OMB1 | Ahmedabad | Kamlesh N Patel v Iffco-Tokio General | Complaint AHD-G-023-1617-1511 | 12-04-2017 | Health: non-disclosure of hypertension at portability; knee surgery | Allowed, Rs 2,06,474 |
| OMB2 | Ahmedabad | Varshaben H Mehta v United India | Complaint AHD-G-051-1718-0045 | 05-06-2017 | Health: reasonable and customary deduction (cataract lens) | Allowed, Rs 23,323 |
| OMB3 | Chennai | Rajeswari Muralidharan v Oriental | IO/CHN/A/GI/0013/2017-18 (CHN-G-050-1617-0583) | not printed (2017-18) | Health: 24-hour rule; day-care list | Dismissed |
| OMB4 | Ahmedabad | Jaimin J Patel v Oriental | Complaint AHD-G-050-1718-0228 | 22-06-2017 | Health: under 24 hours / OPD; eye injections | Allowed, Rs 45,203 |
| OMB5 | Pune | Suresh Jadhav v Bajaj Allianz Life | IO/PUN/A/LI/0104/2017-2018 (PUN-L-006-1718-0301) | 28-08-2017 | Life: early death claim, s.45 (as amended in 2015), non-disclosure without fraud | Premium refund ordered |
| OMB6 | Chennai | R. Subagaran v LIC | IO/CHN/A/LI/0002/2017-18 | 28-06-2017 | Life: 7 policies, deaths within 3 years, suppression | 1 claim payable, 6 repudiations upheld |
| OMB7 | Ahmedabad | Hemang H Trivedi v HDFC Standard Life | Case AHD-L-019-1314-0223 | 22-05-2014 | Life: mis-selling; cancellation after free-look | Allowed: cancel and refund |
| OMB8 | Bhopal | Chotu Chandrawanshi v ICICI Prudential Life | Case ICICI/336-23/02-12/RPR | 03-09-2014 | Life: alleged mis-selling; free-look not used | Dismissed |

Source files: OMB1-4 come from `https://cioins.co.in/GIC/mediclaim/Individual%20Mediclaim%20-Gen27.pdf`, OMB5-6 from `https://cioins.co.in/LIC/deathclaim/Death%20-%20Life27.pdf`, and OMB7-8 from the 1.4.2014-30.9.2014 life miscellaneous synopsis on `www.cioins.co.in/LIC/miscellanious/`. The full URLs are in `_index.tsv`.

## (a) Was NCLAT's Vishnu Kumar Agarwal ruling stayed?

In effect, yes, until the appeal ended in a settlement. The ruling was never reversed on the merits, and it is now contrary to Supreme Court law.
- Piramal appealed to the Supreme Court as **Civil Appeal No. 878 of 2019** (Diary No. 2220/2019), tagged with CA No. 1678 of 2019. The Court directed that **status quo** be maintained, by orders of 01-02-2019 and 22-02-2019 and later orders of 09-09-2020, 03-11-2020 and 12-04-2021. An official order of NCLT Jaipur records this (IA 538/JPR/2022 in CP (IB) 99/7/JPR/2019, PNB v Tirupati Balaji Enterprises, 29-03-2023), at https://nclt.gov.in/gen_pdf.php?filepath=/Efile_Document/ncltdoc/casedoc/0811101002982019/04/Order-Challenge/04_order-Challange_004_1680497085550627024642a59bd1f9b0.pdf . That is the "2023 NCLT order" mentioned in the index.
- On **16-12-2024** the appeals were disposed of on a settlement. The Bench was Hrishikesh Roy and S.V.N. Bhatti JJ, and Assets Care & Reconstruction Enterprise Ltd had been substituted for Piramal. The SC office report for that listing is at https://api.sci.gov.in/officereport/2019/2220/2220_2019_2024-12-16.pdf . The order itself was not downloaded. Its outcome is confirmed by the next point.
- In **ICICI Bank Ltd v Era Infrastructure (India) Ltd, CA No. 6094 of 2019 & connected matters, 2026 INSC 201, 26-02-2026** (Dipankar Datta and Augustine George Masih JJ), the Supreme Court says at para 75 that the appeal from *Vishnu Kumar Agarwal* "stood disposed of without expression of any opinion on the merits" (footnote 47 cites the order of 16-12-2024 in CA 878/2019). It then holds, following *BRS Ventures v SREI* (2025) 1 SCC 456, that simultaneous CIRPs against the principal borrower and the corporate guarantor are maintainable. Official PDF: https://api.sci.gov.in/supremecourt/2019/24750/24750_2019_8_1501_69159_Order_26-Feb-2026.pdf
- Takeaway for the site: cite VISHNU only as history. Its "one claim, one admitted CIRP" rule is not good law.

## (b) The Supreme Court order of Aug 2024 in Viraj Chetan Shah

- **Union of India & Ors v Viraj Chetan Shah & Ors, SLP(C) Nos. 17194-17230 of 2024** (Diary No. 27725/2024). The SLPs challenge the Bombay HC judgment of 23-04-2024 in WP 719/2020 and the connected writ petitions.
- **Order dated 12-08-2024**, Court No. 11, B.V. Nagarathna and Nongmeikapam Kotiswar Singh JJ. Official PDF: https://api.sci.gov.in/supremecourt/2024/27725/27725_2024_11_11_54690_Order_12-Aug-2024.pdf
- What the order does. It issues notice, including notice on the interim stay. It does **not** stay the HC judgment. Instead, "pending consideration of these Special Leave Petitions on the interim stay", the private respondents (the writ petitioners) must seek the High Court's permission to travel abroad. It also says the pending SLPs do not stop the Government from framing a fresh Office Memorandum. The press (e.g. ET, 15-08-2024) called this a "partial stay". Strictly, it is an interim direction, and the order does not restore the power of PSBs to request fresh LOCs.
- Status: the SLPs are still pending. They appear in the SC cause list of 16-10-2026, and an IBBI-hosted order of Aug 2026 says the HC judgment "has not attained finality". The Bombay HC has since granted travel permission case by case, e.g. IA(L) 32743/2024 in WP 3374/2022, 24-10-2024.

## Doubts about authenticity or dates
- **AVIVA** is an image-only scan, so the bench names in the index come from press reports and are not yet checked against the order. Local OCR (pdf2md) stalled at "starting" for more than 13 minutes. Re-run it later on a copy, not the original, because the converter moves PDFs it is given.
- **VISHNU:** see section (a) above. The SC status-quo orders, the settlement of 16-12-2024, and the 2026 SC ruling to the contrary mean it is not good law on simultaneous CIRPs.
- **VIRAJ:** see section (b) above. The SC order of 12-08-2024 is an interim direction, not a stay; the SLPs are pending. Its URL carries a signed token from the search result. The token worked today but may expire; the stable route is the Bombay HC judgment search with Side OS, Type WP, 719, 2020.
- **YES-AT1:** page 1 carries "Signature Not Verified", which is normal for SCI uploads. The press reports a review petition was filed in Nov 2026.
- **RCAP:** the URL is a viewer link. It auto-posts to `nclat.nic.in/display-board/view_order`, which returned the PDF. A plain GET without a browser returns only the small auto-submit page.
- **HEALTH1-4** were chosen from Indian Kanoon searches and press coverage. I did not verify that they are "widely cited". HEALTH1 (2026) is too recent to be widely cited. I could not confirm any NCDRC or State Commission ruling on the 24-hour / day-care point; the widely reported ones are Vadodara District Commission orders.
- **Cross-reading copies (`*.kanoon.txt`)** were scraped from HTML and may differ in layout and paragraph breaks from the signed originals. Do not quote from them on the site.

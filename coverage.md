# Coverage: 1 to 27 November 2026 (fetched 27-11-2026, evening IST, from a laptop in India)

308 index rows (277 documents, plus 27 cross-listed copies and 4 NPCI rows in the new `digital` section). Every row's text is in `txt/<ID>.txt`; `all.md` (4.2 MB, one file) repeats each row with its text, trimmed to 60,000 characters where longer (23 items, each marked). Only official hosts were used for texts. Nothing dated outside 1-27 November 2026 is included, except one undated lead row (SAT) and one status row (Corporate Laws Bill) whose date is the fetch date.

## Count per section

| section | rows |
|---|---|
| rbi | 53 |
| fema | 4 |
| sebi | 35 |
| irdai | 13 |
| ifsc | 22 |
| nhb | 3 |
| companies | 5 |
| ibc | 7 |
| dpdp | 1 |
| exchanges | 67 |
| other-laws | 9 |
| digital | 31 (4 NPCI rows + 27 rows cross-listed from other sections) |
| judgments | 58 |

## How to read the index

- **date** is the document date shown by the source. Where the source lists a different date, the note says so (for example RBI FEMA notification Id 13750 is dated 2 November and listed on 3 November).
- **effective date** and **comment deadline** are phrases picked out of the text by a script. They are a pointer, not a finding: check them against the text before publishing. Blank means the script found no clear phrase, not that there is none.
- **reference number** is as printed on the page or PDF. SEBI circular numbers are shown as SEBI's page prints them, including two that the page itself truncates.
- Rows whose text was not obtained say so in the note and the txt file holds a one-line explanation.

## Source by source

### 1. RBI (rbi.org.in)
- **Notifications:** `Scripts/NotificationUser.aspx` (default view and the November 2026 archive post-back) plus every `?Id=` page from 13738 to 13775. Ids 13750 to 13762 fall in the window; 13763 onward are empty. 13 rows.
  - Ids 13760 (Digital Payments - Card-based transaction Directions), 13761 (Cash Withdrawal through ATMs and PoS Directions) and 13762 (White Label ATM Operators Directions) are **PDF-only pages with no HTML text and no date on the page**. The date 27 November 2026 is taken from RBI's Master Directions listing (Payment and Settlement System group). They were not yet on the Notifications listing at fetch time. **Text not obtained** (see rbidocs below).
- **Press releases:** every `BS_PressReleaseDisplay.aspx?prid=` from 63830 to 64100. 192 ids exist in that range; the latest is 64060. 135 are dated 1-27 November: **19 kept**, **116 skipped** (92 auction, T-bill, G-sec, SDL, SGB and money-market results; 24 statistics, data releases and surveys). Kept: 2 penalties (One Mobikwik Systems, Fusion Finance), 3 CoR cancellation or surrender, 2 drafts for comment, 5 section 35A or supersession actions on co-operative banks, the D-SIB list, the securitisation and FEMA announcements, TCCFM, two Governor meetings, SAC meeting.
- **Drafts:** `Scripts/DraftNotificationsGuildelines.aspx` shows two November entries (5 and 23 November). The 10 draft Directions linked from those press releases are saved from their `bs_viewcontent.aspx` pages (Ids 5204-5208 Priority Sector Lending, 5221-5225 Responsible Business Conduct amendment on electronic banking transactions).
- **Master Directions page:** 8 consolidated Directions are marked updated in the window (seven CRR/SLR Directions "Updated as on November 27, 2026", Payment Aggregator MD "Updated as on November 11, 2026"). The PA text is saved from HTML; the seven CRR/SLR pages are PDF-only, so those rows carry no text.
- **FAQs:** 5 FAQ pages carry November dates (NBFCs 11 Nov, Banker to Government 16 Nov, IoRS 17 Nov, new Trade Regulations 20 Nov, NEFT 20 Nov). Saved in full.
- **FEMA:** `BS_FemaNotifications.aspx` shows one November item, FEMA 23(R)/(2)/2026-RB (Second Amendment), also saved from the Gazette. **A.P. (DIR Series) circulars:** the latest is No. 28 of 23-10-2026; none in the window.
- **Not reachable:** `rbidocs.rbi.org.in` (all RBI PDFs) returns a bot-check page to scripts. Not bypassed. RBI texts are therefore the HTML versions on rbi.org.in. Annexes that exist only as PDF are not included.
- Speeches not collected, as instructed.

### 2. SEBI (sebi.gov.in)
- Listing: the all-items listing (`HomeAction.do?doListingAll=yes`, AJAX `getnewslistinfo.jsp`) filtered 01-11-2026 to 27-11-2026: **286 records**, all 12 pages read. Cross-checked against the Circulars, Master Circulars, Regulations, Rules, Acts, Gazette, Guidelines, Press Releases, Public Notices, Informal Guidance and Reports-for-comment listings.
- **Kept, 35:** 12 circulars, 10 press releases, 4 consultation papers, 1 informal guidance (two PDFs), comprehensive FAQs on PIT Regulations, 1 exemption order, 3 UNSC list updates, 3 public notices.
- **Nothing in the window:** regulations or amendment regulations (the updated-regulations list shows no "last amended" date in November), master circulars (latest 28-09-2026), gazette notifications (latest 29-09-2026), board meeting.
- **Skipped (251):** 99 recovery proceedings, 3 recovery auction notices, 62 orders (49 RTI appeal orders and 13 adjudication, settlement and interim orders; none against an NBFC, debenture trustee or credit rating agency), 77 filings (offer documents, takeovers, buybacks, mutual fund scheme documents), 10 speeches.

### 3. IRDAI (irdai.gov.in)
- Listings with 100 rows each: circulars, orders, exposure drafts, press releases, warnings and penalties, regulations (consolidated and updated), guidelines, notifications, rules, notices, acts, tenders; plus the home page "What's New". The site returned HTTP 504 for about 40 minutes and then recovered.
- **13 rows:** 2 circulars (Four Layer Structure - Motor Insurance Policy; Master Circular on Registration, Capital Structure, Transfer of Shares and Amalgamation of Insurers, 2026, IRDAI/F&I/CIR/MISC/142/11/2026 of 2 November, **not in the earlier sweep**), 4 orders, 5 press releases (two of them, 2 and 6 November, not in the earlier sweep), the Star Health final order, 1 exposure draft.
- The exposure draft (document 9986094) is not on the Exposure Drafts listing at all (that listing stops at 31-07-2026). It appears only on the home page. Its date is from the document text. So the listing is not a complete record; the home page was used as the check.
- Compared with the earlier sweep's list (`Nov-2026/_found.tsv`), the Master Circular of 2 November and the press releases of 2 and 6 November are additions.
- Skipped: two monthly business-figure statistics, two tenders. Three home-page items were opened and left out as October items: two press releases whose text is dated 29 and 31 October, and circular IRDAI/HLT/CIR/MISC/141/10/2026 (October by its number; its date was not read cleanly).
- No new regulations, guidelines or gazette notifications listed in the window.

### 4. IFSCA (ifsca.gov.in)
- Listing: `Home/NewSection` (1,441 rows, newest 27-11-2026). 23 rows fall in the window: **19 kept**, 4 tenders skipped.
- Kept: 7 circulars (27, 25, 25, 12, 12 and 4 November; the requester's count of 9 could not be matched, the next older circulars are dated 27 October), 2 notifications of 4 November, 2 consultations of 9 November (comments by 30 November), FAQs of 5 November, ILS working group report of 16 November, 2 press releases, 1 informal guidance (application and reply), public comments compilation, annual report (English text saved; Hindi file has no usable text), 1 event report.
- Three further IFSC items come from the Gazette (section ifsc): S.O. 6195(E) and S.O. 6196(E) of 13 November (commodity trading as a financial service and commodity trading contract as a financial product) and CBDT S.O. 6016(E) of 4 November (TDS on dividends between aircraft-leasing IFSC units).
- No new regulations on the Legal pages in the window.

### 5. NHB (nhb.org.in)
- All 36 listing pages used in the earlier NHB sweep were re-read, plus the home page. Links to files uploaded in `/uploads/2026/11/`: 9 files, of which 7 are tenders.
- **2 rows:** the advisory of 12 November 2026 (it forwards an RBI letter of the same date on appointment of arbitrators) and the PLR notice effective 1 November 2026. A third nhb row is the Gazette notification under section 6 of the NHB Act (RBI nomination to the NHB board).
- No policy circular, refinance circular or supervisory circular dated in the window. Several listing pages took more than a minute to load but all 36 were read.

### 6. MCA (mca.gov.in)
- The site returns HTTP 403 to curl. Listings were read in a real browser from MCA's own data endpoints: Important Updates, What's New, Notices, Press Release, Reports, and the e-book lists for Notifications (835 entries), Circulars (248), Rules and Others.
- **In the window:** G.S.R. 968(E) of 3 November (Companies (Listing of equity instruments in permissible jurisdictions) Amendment Rules, 2026; text saved from the Gazette copy hosted by IFSCA), draft amendment to Schedule VII and CSR Policy Rules (11 November), NFRA service-rules consultation (20 November), one appointment order.
- **Texts not obtained** for the three non-Gazette items: PDFs cannot be downloaded by script, and the CSR draft is a 19-page scan. Their rows give the document URL as opened in the browser. **The CSR draft's comment deadline was not captured.**
- No General Circular in the window (latest: 06/2026 of 27-10-2026). No LLP notification.
- **Corporate Laws (Amendment) Bill, 2026:** sansad.in bills API shows Bill No. 85 of 2026, introduced in Lok Sabha 23-03-2026, status Pending, no committee or passage dates. One status row.

### 7. IBBI (ibbi.gov.in)
- Listings: What's New (pages 1 and 2), notifications, circulars, guidelines, rules, act, updated regulations, facilitation, press releases, IBBI orders, and the Supreme Court, NCLAT and High Court order lists.
- **7 rows:** notification of 4 November (ex-officio member), press release of 26 November (new Chairperson), 5 orders (4 Disciplinary Committee orders against insolvency professionals, 1 order on a registered valuer).
- **Nothing in the window:** regulations or amendments (latest 30-10-2026), circulars (latest 30-10-2026), guidelines, discussion papers (the discussion-paper page says the link has expired).
- Skipped: 12 RTI appeal orders; 19 NCLT resolution-plan approval orders listed under What's New.
- IBC amendment: no Act or Bill event in the window (the 2026 amendment Act and its 25-05-2026 commencement notification are earlier).

### 8. DPDP
- MeitY documents API (Acts and policies, Orders and notices, Gazette notifications, Guidelines, Publications, Press release): nothing dated in the window. Latest Acts-and-policies entry is 29-10-2026.
- **1 row:** PIB release of 14 November 2026 (PRID 2336151): the Consent Manager registration framework came into effect on 13 November 2026 and the registration portal was launched.
- **Not reachable:** the Data Protection Board site `dpbi.gov.in` returned HTTP 503 in the browser and no response to curl. No Board notification, FAQ or registration list could be checked.

### 9. Stock exchanges
- **BSE:** notices API read in a browser (curl gets HTTP 403). **720 notices** dated 1-27 November. **33 kept** (listing compliance, action for unpaid listing fees, encumbrance and price-movement measures, KYC/KRA, FATCA/CRS, broker audit and reporting reminders, settlement changes, InvIT cooling-off). Notice PDFs downloaded normally. Separate attachments were not fetched.
- **NSE:** circular API read in a browser (curl gets HTTP 403). **496 circulars** dated 1-27 November. **31 kept**, plus **3 circulars to listed entities** from the "Circulars Issued to Listed Companies" page (covering the SEBI InvIT and REIT circulars of 2 November). The debt-securities page shows nothing dated in the window. Files downloaded from nsearchives; zips were unpacked.
- Skipped on both: per-security listing, suspension, record date, redemption, corporate action, mutual fund scheme, index, derivatives contract and auction notices; forwarded SEBI and SAT orders; algo-provider empanelments; membership surrenders.
- Titles of 9 rows were cut short when the listing was copied out of the browser. 7 were completed from the "Sub:" line of the PDF itself (so they follow the PDF wording, which can differ slightly from the listing); 2 are still marked "[title truncated in listing capture]" (NSE/ISC/77595, BSE 20261116-26).

### 10. Other laws and central government
- **eGazette:** "Search by Publish Date" 01-Nov-2026 to 27-Nov-2026 reports **639 gazettes**; 617 rows were captured across 43 pages (22 rows missing, cause not found; most likely rows repeated at page boundaries). **8 saved** (2 Department of Financial Services appointments under the Actuaries Act and NABARD Act, 2 DEA notifications under the IFSCA Act, CBDT IFSC notification, RBI FEMA notification, RBI notification under section 42(6)(c) of the RBI Act, RBI notification under the NHB Act). Not saved: 16 customs/CBIC, income-tax entity notifications, G-sec auction notices, and all other ministries.
- **No new Act, commencement notification or rules** under SARFAESI, RDB Act, PMLA, CERSAI, Stamp Act, Arbitration Act, Factoring Act, BUDS Act, IT Act, Bankers' Books Evidence Act or Jan Vishwas appear in the eGazette listing for the window (Finance, Law and Justice, MeitY and MCA rows were read one by one).
- **FIU-IND:** Compliance Orders page lists one order: No. 11/DIR/FIU-IND/2026 of 12 November 2026 in the matter of Kraken under section 13 PMLA. The PDF is a scan, **no text**. No new guideline or notification; What's New for November has only a tender and a vacancy notice.
- **PIB:** all-releases view for November 2026: Finance 40, Corporate Affairs 4, Law and Justice 7, Electronics and IT 15. **6 kept** (two PSB performance releases, High-Level Committee on Banking, Cabinet decisions on Stand-Up India and the Credit Guarantee Fund for Micro Units, and the DPDP consent manager release).
- **CERT-In:** Guidelines page lists CISG-2026-04, AI Security Auditing Guidelines, 4 November 2026 (saved). No new Directions under section 70B.
- **Parliament:** the bills API holds no record with any date in November 2026; the latest introduction is 10-08-2026. No bill was introduced or passed in the window.

### 11. Judgments
- **Supreme Court (sci.gov.in):** the home page lists the latest 25 judgments, which at fetch time covered **20 to 27 November only**. 8 relevant ones saved from the official `sci-get-pdf` link, with neutral citation and bench read from the PDF: SBI v. State of Maharashtra (2026 INSC 1279), Union of India v. J. Sekar (2026 INSC 1277), UV ARC v. Gautam Sinha (2026 INSC 1263), Ramsakhi Gupta v. ICICI Lombard (2026 INSC 1276), Sukumarbai v. United India Insurance (2026 INSC 1272), Asst. General Manager v. S. Loganathan (2026 INSC 1287), Sucheta Dalal v. Union of India (2026 INSC 1282), Fenkin Infotech LLP v. Aniruddh Nikhil Makhecha (2026 INSC 1278; relevance to lending not confirmed).
- **1 to 19 November is a gap for the Supreme Court.** The date-wise and case-number searches need a CAPTCHA (not attempted) and the "Latest Judgements" page returns "No Documents found". Four Supreme Court IBC decisions of 16-17 November are saved from IBBI's official copies (Twinstar Technologies v. Bank of Maharashtra, Ganesh Benzoplast v. STC, Lulu International v. Gorinka Pratyusha, BSE v. Spice Energy; the last is a scan without text). **7 further Supreme Court decisions are lead rows only, marked "official link not obtained"**, including Subrata Bhattacharya v. SEBI (2026 INSC 1247, 19 November). Their particulars come from a third-party index and are unverified.
- **NCLAT (nclat.nic.in):** judgment search by order date, Company Appeal (AT)(Ins), 1-27 November: New Delhi 94 cases, Chennai 20 cases. Lender-related titles were picked: **32 distinct orders saved** (connected appeals decided by a common order are listed in that row's note). They include Sri Narain Aggarwal / Sangeeta Aggarwal v. Equentia Financial Service (6 November), Sunil Madhavdas Ahuja / NKAY Investment v. Jayesh Sanghrajka (6 November) and Bindu Kapoor v. Mamta Binani (6 November). Many of the 32 are short disposal orders. Company Appeal (AT) (non-insolvency) and Competition appeals were not searched. 3 more NCLAT orders and 3 High Court orders come from IBBI's lists.
- **SAT (sat.gov.in):** HTTP 503 on every attempt. Nothing collected. Tetsuya Takano v. SEBI is a lead row only, date unconfirmed.
- **High Courts:** not swept (no single official listing without CAPTCHA). Only the 3 IBC-related High Court orders hosted by IBBI are included. SARFAESI, NI Act section 138, arbitration and consumer-finance rulings of High Courts are therefore **not covered**.

### 12. Digital / direct-to-consumer platforms (section `digital`)
- 27 rows are **cross-listed copies** of items already filed under their regulator (same txt file; all.md does not repeat the text): RBI payment items (Cyber Resilience Master Directions for non-bank PSOs, Domestic Money Transfer Directions, the three 27 November Directions on cards, ATM/PoS cash withdrawal and White Label ATMs, the updated Payment Aggregator Master Direction, the Mobikwik penalty, the draft electronic-banking safeguards and their five drafts, NEFT and IoRS FAQs), the DPDP consent manager release, the CERT-In AI auditing guidelines, SEBI KYC/onboarding circulars and the social-media impersonation caution, BSE notices to investment advisers and research analysts on websites, apps and social media handles, the retail algo-trading compliance notices, and IRDAI's distribution-reform and dark-patterns items.
- **NPCI (npci.org.in):** the site returns HTTP 403 to scripts for both listings and files. Listings were read in a browser from NPCI's API for UPI (29 circulars in FY 26-27), RuPay (5), NACH (5), IMPS (5), AePS (6), NETC (11), NFS (4), CTS (1); e-RUPI and BBPS return nothing there. **The listing has no dates.** The PDF creation date was read from file metadata for the newest entries: 4 fall in the window (UPI OC 240 and OC 241, 4 November; UPI OC 242, 11 November; IMPS OC 134, 17 November). These 4 rows carry **no text** and their date is the file creation date, not the printed circular date. Listing entries with no file ("Please get in touch with your bank": UPI OC 237, OC 238, AePS OC 097A, RuPay OC052) could not be dated.
- **Nothing found in the window** for: RBI digital lending / lending service provider / default loss guarantee, account aggregator (RBI notifications and FAQs carry none; rebit.org.in shows no dated items; Sahamati is an industry body and was not used), tokenisation, authentication, PPI-specific circulars, SEBI on online MF distribution / execution-only platforms / finfluencers (no circular; only the 23 November press caution), IRDAI on web aggregators, Bima Sugam or e-commerce.
- **Not reachable:** bharat-connect.com (BBPS circulars) returns HTTP 403.

## Sources with nothing in 1-27 November 2026: their two most recent earlier items

Dates and titles are as shown on each listing saved during this sweep.

**SEBI Master Circulars**

- 2026-09-28 | Master Circular for Debenture Trustees | no reference shown on listing | https://www.sebi.gov.in/legal/master-circulars/sep-2026/master-circular-for-debenture-trustees_104743.html
- 2026-07-14 | Master Circular for Merchant Bankers | no reference shown on listing | https://www.sebi.gov.in/legal/master-circulars/jul-2026/master-circular-for-merchant-bankers_102815.html

**SEBI Gazette Notifications**

- 2026-09-29 | Gazette Notification for Renewal of Recognition of BSE Clearing Limited (BSECL) | no reference shown on listing | https://www.sebi.gov.in/legal/gazette-notification/sep-2026/gazette-notification-for-renewal-of-recognition-of-bse-clearing-limited-bsecl-_105360.html
- 2026-09-14 | Gazette Notification for Renewal of Recognition of NSE Clearing Limited (NCL) | no reference shown on listing | https://www.sebi.gov.in/legal/gazette-notification/sep-2026/gazette-notification-for-renewal-of-recognition-of-nse-clearing-limited-ncl-_105358.html

**SEBI Regulations (most recently amended, per the "last amended on" label of the updated-regulations list)**

- 2026-10-16 | Securities and Exchange Board of India (Infrastructure Investment Trusts) Regulations, 2014 [Last amended on October 16, 2026] | no reference shown on listing | https://www.sebi.gov.in/legal/regulations/oct-2026/securities-and-exchange-board-of-india-infrastructure-investment-trusts-regulations-2014-last-amended-on-october-16-2026-_105377.html
- 2026-10-15 | Securities and Exchange Board of India (Real Estate Investment Trusts) Regulations, 2014 [Last amended on October 15, 2026] | no reference shown on listing | https://www.sebi.gov.in/legal/regulations/oct-2026/securities-and-exchange-board-of-india-real-estate-investment-trusts-regulations-2014-last-amended-on-october-15-2026-_105376.html

**RBI A.P. (DIR Series) Circulars**


**IRDAI Regulations (consolidated gazette notified)**

- 2026-07-31 | Insurance Regulatory and Development Authority of India (Policyholders’ Education and Protection Fund) Regulations, 2026 | no reference shown on listing | https://irdai.gov.in/document-detail?documentId=9698497
- 2026-07-31 | IRDAI (Third Party Administrators – Health Services) (Amendment) Regulations, 2026 | no reference shown on listing | https://irdai.gov.in/document-detail?documentId=9703888

**IRDAI Guidelines**

- 2026-04-08 | IRDAI Information and Cybersecurity Guidelines, 2026 | IRDAI/GA&HR/CIR/MISC/51/4/2026 | https://irdai.gov.in/document-detail?documentId=9189223
- 2026-02-11 | Guidelines on Establishment and Closure of Liaison Office in India by an Insurance Company registered outside India | IRDAI/F&I/GDL/MISC/27/02/2026 | https://irdai.gov.in/document-detail?documentId=8752913

**IRDAI Notifications**

- 2026-09-22 | शक्ति का प्रत्यायोजन संबंधी राजपत्र अधिसूचना Gazette Notification on Delegation of Powers | no reference shown on listing | https://irdai.gov.in/document-detail?documentId=9846970
- 2026-06-22 | Notification - Amendment to Obligatory Cession Notification | no reference shown on listing | https://irdai.gov.in/document-detail?documentId=9585445

**IRDAI Exposure Drafts listing**

- 2026-07-31 | General Statement of response to public comments on IRDAI (Insurance Intermediaries) (Amendment) Regulations, 2026 | no reference shown on listing | https://irdai.gov.in/exposure-drafts
- 2026-07-31 | General statement of response to public comments on the exposure draft of the IRDAI (Insurance Surveyors and Loss Assessors) (Amendment) Regulations, 2026 (Hindi title on the listing; English wording is my reading of it) | no reference shown on listing | https://irdai.gov.in/exposure-drafts

**IBBI Circulars**

- 2026-10-30 | Introduction of revised Form CA for filing of claims by real estate allottees. | no reference shown on listing | https://ibbi.gov.in/legal-framework/circulars
- 2026-10-30 | Compliance with RERA for CDs having real estate projects and disclosure of CIRP at project and office sites of the CD. | no reference shown on listing | https://ibbi.gov.in/legal-framework/circulars

**IBBI updated Regulations**

- 2026-10-30 | IBBI (Insolvency Resolution Process for Corporate Persons) Regulations, 2016 (Amended upto 30-10-2026) | no reference shown on listing | https://ibbi.gov.in/uploads/legalframwork/e02981ba61996ccfde25af57218f5025.pdf
- 2026-09-22 | IBBI (Liquidation Process) Regulations, 2016 (Amended upto 22-09-2026) | no reference shown on listing | https://ibbi.gov.in/uploads/legalframwork/f0b29d02169e66fcc397525cf7241b94.pdf

**IBBI Guidelines**

- 2026-05-18 | The Insolvency Professionals to act as Interim Resolution Professionals, Liquidators, Resolution Professionals and Bankruptcy Trustees (Recommendation) Guidelines, 2026 issued on May 18, 2026. | no reference shown on listing | https://ibbi.gov.in/uploads/legalframwork/e5383116b116b10af0f319903ee59ee4.pdf
- 2025-11-21 | The Insolvency Professionals to act as Interim Resolution Professionals, Liquidators, Resolution Professionals and Bankruptcy Trustees (Recommendation) (Second) Guidelines, 2025 issued on November 21, 2025. | no reference shown on listing | https://ibbi.gov.in/uploads/legalframwork/e2d592498bd66c11b7e4f4ceb6156745.pdf

**MeitY Acts and Policies listing (covers IT Act and DPDP documents)**

- 2026-10-29 | Data Empowerment and Protection Architecture (DEPA) for AI Training | no reference shown on listing | https://www.meity.gov.in/static/uploads/2026/10/02d8224e4cd6c8c29be5a5198e795158.pdf
- 2026-03-30 | Draft amendments to the IT Rules, 2021 in relation to strengthening intermediary compliance with clarifications, advisories and directions issued by the Ministry and digital media oversight | no reference shown on listing | https://www.meity.gov.in/static/uploads/2026/04/ec197f1206279efb4964965f0dede6c1.pdf

**IFSCA Regulations (from the listing saved on 26-11-2026)**

- 2026-09-18 | IFSCA (ELECTRONIC TRADING PLATFORMS) REGULATIONS, 2026 | no reference shown on listing | https://ifsca.gov.in/Legal/Index (Regulations); file IFSCA__Electronic_Trading_Platforms__Regulations__2026_20260918_1130.pdf
- 2026-09-16 | IFSCA (Capital Market Intermediaries) Regulations 2025 as amended upto 05th September, 2026 | no reference shown on listing | https://ifsca.gov.in/Legal/Index (Regulations); file IFSCA__Capital_Market_Intermediaries__Regulations__2025_as_amended_up_to_05_September_2026_20260916_0112.pdf

**RBI A.P. (DIR Series) Circulars**

- 2026-10-23 | Delegation of Compounding of certain Contraventions under FEMA, 1999 to Regional Offices of the Reserve Bank | A.P. (DIR Series) Circular No. 28 | https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=13745&Mode=0
- 2026-10-12 | Risk Management and Inter-Bank Dealings | A.P. (DIR Series) Circular No. 27 | https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=13739&Mode=0

**MCA General Circulars** (from MCA's e-book Circulars list, read in a browser)

- 2026-10-27 | Relaxation of additional fee and extension of time for filing CRA-4 (Cost Audit Report in XBRL format) | General Circular No. 06/2026 | https://www.mca.gov.in/content/mca/global/en/acts-rules/ebooks/circulars.html
- 2026-10-24 | Relaxation of additional fees and extension of time for filing of Financial Statements and Annual Returns under the Companies Act, 2013 (title cut short in the capture) | General Circular No. 05/2026 | same page

**FIU-IND What's New (non-tender)**

- 2026-09-30 (as-on date) | List of Non-Compliant NBFCs which have not fulfilled their obligation under PML Act and rules relating to registration on FINnet 2.0 | no reference | https://fiuindia.gov.in/pdfs/downloads/NonCompliantNBFC30092026.pdf
- 2026-08-17 (as-on date) | List of non-compliant NBFCs (earlier edition) | no reference | https://fiuindia.gov.in/files/misc/archive.html

**CERT-In Directions under section 70B(6)** (as recorded in the earlier DPDP sweep; the Directions page shows nothing newer)

- 2022-06-27 | Extension of timelines for the 28-04-2022 Directions | no reference | https://www.cert-in.org.in/PDF/CERT-In_directions_extension_MSMEs_and_validation_27.06.2022.pdf
- 2022-04-28 | Directions No. 20(3)/2022-CERT-In | 20(3)/2022-CERT-In | https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf

**Parliament (bills)**: latest introduction in the sansad.in API is 2026-08-10, The Tribunals Reforms Bill, 2026 (Bill No. 153 of 2026). A second-latest item was not extracted.

**NPCI products with no November file:** RuPay OC051 and OC050 (RuPay Insurance Program FY 2026-27), NACH OC001 (Revision of NACH Mandate Form, file created 2026-05-21), AePS OC 097 (3 Party Cash Deposit, file created 2026-09-23), NETC OC 008 (OneTag FASTag Portability, file created 2026-09-22), NFS OC 427 (file created 2026-10-05). Listing: https://www.npci.org.in/circulars/<product>.

**Not listed here because the listing itself could not be read:** SAT orders, Data Protection Board notices, High Court rulings, NHB policy and refinance circulars (the earlier NHB sweep's two latest advisories are dated 2026-09-28, mis-selling of insurance with housing loans, and 2026-09-21, fraud monitoring return; both on https://www.nhb.org.in/advisories-issued-to-hfcs/), SEBI board meeting press release, NSE debt-segment circulars to issuers.

IBBI circular links: the two 30-10-2026 circulars are on https://ibbi.gov.in/legal-framework/circulars (the listing uses script links, so no direct file URL was captured).

## What could not be reached, in one place

| Source | Result |
|---|---|
| rbidocs.rbi.org.in (RBI PDFs) | bot-check page; not bypassed. Three new payment Directions of 27 November and seven updated CRR/SLR Directions have no text |
| mca.gov.in documents | HTTP 403 to scripts; listings read in browser, PDFs not saved |
| dpbi.gov.in (Data Protection Board) | HTTP 503 |
| sat.gov.in | HTTP 503 |
| sci.gov.in judgments for 1-19 November | CAPTCHA-only searches |
| High Court websites | not attempted |
| api.bseindia.com, nseindia.com APIs | HTTP 403 to scripts; lists read in browser, files downloaded normally |
| npci.org.in | HTTP 403 to scripts for lists and files; lists read in browser, no texts |
| bharat-connect.com | HTTP 403 |

## Scanned PDFs with no text
FIU-ORD-11-2026, JUD-IBBI-1273c92f (BSE v. Spice Energy), MCA-CSR-DRAFT (not downloaded), IFSCA-1103-18 (Hindi annual report). No OCR was run.

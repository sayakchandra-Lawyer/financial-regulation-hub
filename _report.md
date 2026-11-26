# Companies-Hub fetch report

Fetched 26 November 2026 from a laptop in India. Every row in `_catalogue.tsv` has the official URL that was actually fetched.

## What is here

| Folder / file | Contents |
|---|---|
| `pdf/` | 160 official PDFs: the Act, gazette notifications, s.462 exemptions, MCA circulars, the 2026 Bill and the JPC report |
| `html/` | 9 consolidated Rules (see the note below) |
| `txt/` | Text of every PDF and HTML file, made with `pdftotext -layout`. Rules are HTML-to-text. |
| `_catalogue.tsv` | 169 rows with columns ID, title, reference_no, issue_date, effective_date, detail_url, pdf_url, file, notes |
| `_egazette-MCA-2014-2024.tsv`, `_egazette-MCA-2025-2026.tsv` | Every Ministry of Corporate Affairs gazette entry listed by eGazette "Search by Ministry", month by month, 01-2014 to 11-2026 (882 + 86 rows). Use them to check coverage. |

### Count by type
- **Act:** ACT-CA2013, the India Code consolidated PDF. Its footnotes run up to Act 29 of 2020 and Act 33 of 2021; the latest w.e.f. date seen is 30-10-2023.
- **Consolidated Rules (MCA e-book):** RULES-CHG, -MBP, -DEP, -SCD, -PAS, -FEES, -MGT, -LAYERS and -ADJ. These are current: RULES-MBP already carries the 03-11-2025 amendment to rule 11(2).
- **Amendment notifications (eGazette), 2014–2026:** CHG 7, MBP 14, DEP 11, SCD 15, PAS 12, FEES 22, MGT 16, ADJ 3, LAYERS 1 (2025), DEFN 7 (Specification of Definitions Details amendments 2014–2025, incl. small-company thresholds G.S.R. 700(E) of 15-09-2022 and G.S.R. 880(E) of 01-12-2025).
- **Commencement:** S.O. 1833(E) brought ss.61–62 of the Companies (Amendment) Act, 2017 into force w.e.f. 07-05-2018. Those sections substitute s.185 and amend s.186. S.O. 630(E) covers the provisions commenced on 09-02-2018.
- **s.454 / adjudication:** four S.O. notifications from 2018, 2019 and 2026. The 2026 one is S.O. 698(E) of 11-02-2026.
- **s.462 exemptions:** private companies G.S.R. 464(E) and 583(E); Government companies 463(E), 582(E), S.O. 802(E) of 2018 and G.S.R. 151(E) of 2020; Section 8 companies 466(E) and 584(E); Nidhis 465(E); IFSC G.S.R. 8(E) for public companies and 9(E) for private companies, both dated 04-01-2017.
- **MCA General Circulars:** 31 in total. They cover:
  - ss.185, 186 and 180 (GC 3/2014, 4/2014, 15/2014, 4/2015, 6/2015)
  - deposits and debentures (GC 5/2015, 9/2015, 19/2014, 11/2017, 24/2020, 34/2020)
  - charge-filing relaxation schemes (GC 23/2020, 32/2020, 7/2021, 12/2021)
  - IBC professionals filing forms (GC 4/2020)
  - MGT-14 (GC 28/2014)
  - V3 migration (GC 2, 3, 4 and 5 of 2023; GC 4/2024; GC 1 and 2 of 2025)
  - every 2025–26 additional-fee relaxation circular, including GC 2/2026 on DPT-3.
- **2026 Bill:** BILL-CLAB-2026 (Bill No. 85 of 2026 as introduced), a Hindi errata sheet, and JPC-CLAB-2026 (the Joint Committee report, about 12 MB).

## Latest status of the Corporate Laws (Amendment) Bill, 2026
According to the sansad.in bills API, queried 26-11-2026:
- Bill No. 85 of 2026 was introduced in Lok Sabha on 23-03-2026. It was referred to a Joint Committee the same day.
- The Joint Committee's Report No. 1 was presented in Lok Sabha and laid in Rajya Sabha on 03-08-2026.
- Status: **Pending**. There is no Lok Sabha or Rajya Sabha passing date, no assent and no Act number. **It is not yet law.**

## What failed or needs care
1. **India Code:** the detail page for handle 123456789/2114 returned HTTP 504 on every attempt. The PDF itself downloaded from the bitstream URL. Check its footnotes against later amending Acts, such as the Jan Vishwas amendments, before you rely on it.
2. **MCA:** mca.gov.in blocks curl. Everything from MCA came through a real browser at a paced rate. The site blocked this IP once for about 20 minutes, then let it back in.
   - MCA publishes the **consolidated rules only as HTML, rule by rule** through its e-book API. Each `html/RULES-*.html` file is those official parts joined together, with footnotes showing each amendment. MCA publishes no PDF of the consolidated rules.
3. **Image-only circulars:** nine circulars are scanned images, so their `txt/` file is empty: CIR-2014-15, CIR-2014-19, CIR-2020-34, CIR-2021-07, CIR-2021-12, CIR-2025-01, CIR-2025-02, CIR-2025-07 and CIR-2026-02. Read the PDFs.
   - CIR-2025-06 and CIR-2023-02 were run through Windows OCR. Each text file is labelled as machine OCR.
4. **eGazette throttling:** after about 450 downloads eGazette began refusing connections. About 60 Section-3 notifications from 2021–2024 were never opened. Their subjects show they are outside scope: Accounts, Incorporation, CSR, IBC, institute elections, Competition Act and similar. They are listed in `_egazette-MCA-2014-2024.tsv`.
   - All in-scope titles from 2020–2024 were fetched one at a time.
5. **Scope filter:** while scanning 2014–2024, gazette entries were skipped when their subject named an obviously unrelated topic, such as Competition Act, ICAI/ICSI/ICoAI, IBC, NCLT appointments, IEPF, LLP, accounting standards and audit. A notification with a misleading subject line could have been missed.
6. **Reference numbers:** three old gazettes have no machine-readable G.S.R. number of their own: AMD-SCD-20140618, AMD-FEES-20191001 and AMD-MGT-20240715. Their `reference_no` is blank; read the number from the PDF.
   - The other numbers were taken from the English text by script. Spot-check them before you cite them.
7. **s.117(3)(g) proviso (NBFC/HFC classes):** neither the consolidated MGT Rules nor any downloaded gazette prescribes the NBFC/HFC classes "in consultation with the RBI". I found no such rule.
8. **Dates:** `issue_date` is the date of the notification. The eGazette listing sometimes shows the following day; for example, IFSC G.S.R. 8(E) and 9(E) are dated 04-01-2017 but listed under 05-01-2017.
   - `effective_date` is filled only where the text states one. Most amendments say "on the date of publication in the Official Gazette".

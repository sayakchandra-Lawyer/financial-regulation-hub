"""Rules for the 'What applies to my entity' page (/entity/).

build_entity.py reads this file with the section registers and writes entity/data/entity.json.
Every instrument id, lens id and paragraph reference here is checked at build time.

feeds:   {"sec": section id, "lens": lens node id in that section's graph, "layers": optional list of layers}
rbi_cat: RBI category node (CAT-*) used with the layer chip, as on the RBI page
adds:    {"sec", "id", "scope": which part applies (optional), "paras": [first, last] checked in RBI full text,
          "note": plain-language summary}
via:     same as adds, but the rule binds the lender and reaches the user through the contract (drawn dashed)
"""

LAYERS = [("bl", "Base", "CAT-BL"), ("ml", "Middle", "CAT-ML"), ("ul", "Upper", "CAT-UL"), ("tl", "Top", "CAT-TL")]

# RBI instruments without category tags that bind every RBI-registered NBFC or HFC
RBI_GENERAL = [
    {"sec": "rbi", "id": "ACT-RBI"}, {"sec": "rbi", "id": "ACT-CICRA"}, {"sec": "rbi", "id": "ACT-PMLA"},
    {"sec": "rbi", "id": "NOT-UAPA"}, {"sec": "rbi", "id": "ACT-BUDS"}, {"sec": "rbi", "id": "ACT-IT"},
    {"sec": "rbi", "id": "ACT-COS"},
    {"sec": "rbi", "id": "ACT-SARFAESI", "scope": "Only NBFCs and HFCs notified as financial institutions under the Act"},
]
LENDER_FEEDS = [
    {"sec": "dpdp", "lens": "ENT-LEND"}, {"sec": "ibc", "lens": "ENT-FC"},
    {"sec": "ibc", "lens": "ENT-FSP", "layers": ["ml", "ul", "tl"]},
]

# an HFC is supervised by NHB: show the NHB section through its HFC lens
NHB_FEED = [{"sec": "nhb", "lens": "ENT-HFC"}]

GROUPS = [
    {"id": "type", "label": "What is it?", "hint": "pick one", "single": True},
    {"id": "layer", "label": "Size under scale based regulation", "hint": "NBFCs and HFCs", "single": True},
    {"id": "listed", "label": "Listed on a stock exchange"},
    {"id": "lic", "label": "Licences and registrations"},
    {"id": "role", "label": "Roles for other firms", "hint": "no licence",
     "help": "Not licences. RBI rules bind the lender, which passes them to you by contract."},
    {"id": "act", "label": "What it does"},
]

def nbfc_type(i, label, cat, layers, extra=(), sectors=("lending",)):
    return {"id": i, "group": "type", "label": label, "rbi_cat": cat, "layers": list(layers), "rbi": True,
            "adds": RBI_GENERAL + list(extra), "feeds": LENDER_FEEDS, "sectors": list(sectors)}

ALL4 = ["bl", "ml", "ul", "tl"]
ATTRS = [
    nbfc_type("icc", "NBFC (Investment and Credit)", "CAT-ICC", ALL4),
    dict(nbfc_type("hfc", "Housing Finance Company", "CAT-HFC", ["ml", "ul", "tl"], [{"sec": "rbi", "id": "ACT-NHB"}], ("lending", "hfc")), feeds=LENDER_FEEDS + NHB_FEED),
    nbfc_type("cic", "Core Investment Company", "CAT-CIC", ["ml", "ul", "tl"]),
    nbfc_type("mfi", "NBFC-MFI", "CAT-MFI", ALL4),
    nbfc_type("factor", "NBFC-Factor", "CAT-FACTOR", ALL4,
              [{"sec": "rbi", "id": "ACT-FRA"}, {"sec": "rbi", "id": "REG-FACTORS"}, {"sec": "rbi", "id": "REG-ASSIGN"}]),
    nbfc_type("ifc", "NBFC-IFC", "CAT-IFC", ALL4),
    nbfc_type("idf", "IDF-NBFC", "CAT-IDF", ALL4),
    nbfc_type("p2p", "NBFC-P2P", "CAT-P2P", ["bl"]),
    nbfc_type("aa", "NBFC-AA", "CAT-AA", ["bl"]),
    {"id": "unreg", "group": "type", "label": "Company not registered with RBI", "layers": [], "adds": [],
     "feeds": [], "sectors": []},

    {"id": "bl", "group": "layer", "label": "Base", "short": "Base Layer"}, {"id": "ml", "group": "layer", "label": "Middle", "short": "Middle Layer"},
    {"id": "ul", "group": "layer", "label": "Upper", "short": "Upper Layer"}, {"id": "tl", "group": "layer", "label": "Top", "short": "Top Layer"},

    {"id": "eq", "group": "listed", "label": "Equity shares", "short": "Listed equity",
     "feeds": [{"sec": "sebi", "lens": "ENT-LE"}, {"sec": "exchanges", "lens": "ENT-EQ"}]},
    {"id": "debt", "group": "listed", "label": "Debt (NCDs, NCRPS)", "short": "Listed debt",
     "feeds": [{"sec": "sebi", "lens": "ENT-LD"}, {"sec": "exchanges", "lens": "ENT-DEBT"}]},
    {"id": "cp", "group": "listed", "label": "Commercial paper", "short": "Listed CP",
     "feeds": [{"sec": "sebi", "lens": "ENT-LD"}, {"sec": "exchanges", "lens": "ENT-DEBT"}],
     "adds": [{"sec": "rbi", "id": "MD-CPNCD", "rbi_only": True,
               "scope": "CP and NCDs of up to one year, if all fund-based bank and NBFC facilities are Standard at issue"}]},

    {"id": "ca", "group": "lic", "label": "IRDAI corporate agent",
     "feeds": [{"sec": "irdai", "lens": "ENT-CA"}, {"sec": "dpdp", "lens": "ENT-INS"}], "sectors": ["life", "health"]},
    {"id": "pa", "group": "lic", "label": "Payment aggregator (RBI)",
     "adds": [{"sec": "rbi", "id": "MD-PA"}, {"sec": "rbi", "id": "ACT-PSS"}, {"sec": "rbi", "id": "MD-AUTH"}, {"sec": "rbi", "id": "MD-EMANDATE"}]},
    {"id": "ppi", "group": "lic", "label": "PPI issuer (RBI)",
     "adds": [{"sec": "rbi", "id": "MD-PPI"}, {"sec": "rbi", "id": "ACT-PSS"}, {"sec": "rbi", "id": "MD-AUTH"}, {"sec": "rbi", "id": "MD-EMANDATE"}]},
    {"id": "dep", "group": "lic", "label": "Takes public deposits", "rbi_only": True, "rbi_cat_add": "CAT-D",
     "adds": [{"sec": "rbi", "id": "ACT-BUDS"}]},
    {"id": "ifsc", "group": "lic", "label": "IFSC unit (GIFT City)", "feeds": [{"sec": "ifsc", "lens": "ENT-FC"}]},

    {"id": "lsp", "group": "role", "label": "Lending Service Provider (LSP)", "feeds": [{"sec": "dpdp", "lens": "ENT-PROC"}],
     "via": [
        {"sec": "rbi", "id": "MD-CREDIT", "paras": [6, 30], "scope": "Chapter III, Digital Lending (paras 6-30)",
         "note": "Your lender must sign a contract with you, run due diligence on you, list you on its website and stay liable for what you do."},
        {"sec": "rbi", "id": "MD-OUTS", "scope": "Chapter III, outsourcing of financial services",
         "note": "Your lender's outsourcing policy, audit and inspection rights apply to your work."},
        {"sec": "rbi", "id": "MD-KYC", "scope": "Only if you carry out customer due diligence for the lender",
         "note": "KYC done for the lender must meet its KYC Directions; the lender stays responsible."}]},
    {"id": "dsa", "group": "role", "label": "DSA / DMA for a lender", "feeds": [{"sec": "dpdp", "lens": "ENT-PROC"}],
     "via": [
        {"sec": "rbi", "id": "MD-RBC", "paras": [98, 101], "scope": "Paras 98-101",
         "note": "Trained staff, an undertaking to follow the lender's code of conduct, and DoT telemarketer registration where you make calls."},
        {"sec": "rbi", "id": "MD-HFC", "paras": [155, 157], "scope": "Paras 155-157, if the lender is an HFC",
         "note": "Model code of conduct for DSAs / DMAs of HFCs, with inspection of your work by the HFC."}]},
    {"id": "rec", "group": "role", "label": "Recovery agent", "feeds": [{"sec": "dpdp", "lens": "ENT-PROC"}],
     "via": [
        {"sec": "rbi", "id": "MD-RBC", "paras": [92, 99], "scope": "Paras 92-99",
         "note": "Due diligence on you and your staff, an authorisation letter and notice for every visit, and your details on the lender's website."},
        {"sec": "rbi", "id": "MD-CREDIT", "paras": [9, 9], "scope": "Para 9(6), digital loans",
         "note": "The borrower is told about you by email or SMS before you make contact."},
        {"sec": "rbi", "id": "MD-HFC", "paras": [170, 170], "scope": "Para 170, if the lender is an HFC",
         "note": "Guidelines for recovery agents of HFCs, including training and limits on incentives."}]},
    {"id": "dla", "group": "role", "label": "Digital lending app operator", "feeds": [{"sec": "dpdp", "lens": "ENT-PROC"}],
     "via": [
        {"sec": "rbi", "id": "MD-CREDIT", "paras": [13, 18], "scope": "Paras 13-18, data and DLA reporting",
         "note": "Need-based data collection with explicit consent, storage in India, and reporting of the app to RBI by the lender."}]},

    {"id": "dl", "group": "act", "label": "Digital lending through LSPs", "rbi_only": True,
     "adds": [{"sec": "rbi", "id": "MD-CREDIT", "paras": [6, 30], "scope": "Chapter III, Digital Lending (paras 6-30)"}]},
    {"id": "gold", "group": "act", "label": "Gold and silver loans", "rbi_only": True,
     "adds": [{"sec": "rbi", "id": "MD-CREDIT", "paras": [30, 50], "scope": "Chapter IV, gold and silver collateral (paras 30-50)"}]},
    {"id": "colend", "group": "act", "label": "Co-lending", "rbi_only": True,
     "adds": [{"sec": "rbi", "id": "MD-TDCR", "paras": [97, 130], "scope": "Part B, Co-Lending Arrangements (paras 97-130)"}]},
    {"id": "las", "group": "act", "label": "Loans against shares",
     "feeds": [{"sec": "exchanges", "lens": "ENT-LEND"}],
     "adds": [{"sec": "rbi", "id": "MD-CREDIT", "paras": [104, 108], "rbi_only": True, "scope": "Chapter VIII (paras 104-108), including LTV for loans against shares"}]},
    {"id": "sec", "group": "act", "label": "Securitisation and loan transfers", "rbi_only": True,
     "adds": [{"sec": "rbi", "id": "MD-SEC"}, {"sec": "rbi", "id": "MD-TDCR", "paras": [13, 95], "scope": "Part A, transfer of loans (paras 13-95)"}]},
    {"id": "cards", "group": "act", "label": "Credit cards", "rbi_only": True,
     "adds": [{"sec": "rbi", "id": "MD-CARDS"}, {"sec": "rbi", "id": "MD-AUTH"}, {"sec": "rbi", "id": "MD-EMANDATE"}, {"sec": "rbi", "id": "ACT-PSS"}]},
    {"id": "ecb", "group": "act", "label": "Borrows abroad or lends to non-residents",
     "feeds_rbi": [{"sec": "fema", "lens": "ENT-NBFC"}], "feeds_other": [{"sec": "fema", "lens": "ENT-BOR"}, {"sec": "fema", "lens": "ENT-LEND"}]},
]

# Obligations that arise only from a combination of choices. Each is taken from the text; paras are checked.
COMBOS = [
    {"id": "nbfc-ca", "all": ["ca"], "any": ["icc", "mfi", "factor", "ifc", "idf"],
     "title": "An NBFC that is also an IRDAI corporate agent",
     "adds": [
        {"sec": "rbi", "id": "MD-FINSVC", "paras": [32, 33], "scope": "Paras 32-33",
         "note": "Insurance agency on a fee basis, with no risk participation, needs no RBI approval if you hold IRDAI permission as a composite corporate agent. Customers choose their own insurer for assets you finance; publicity must say insurance is voluntary, with no link to your loans; the premium goes straight to the insurer; risks of the agency business must not pass to the NBFC."},
        {"sec": "irdai", "id": "REG-CA", "note": "Registration, principal officer, trained specified persons, insurer tie-ups and conduct rules for corporate agents."}]},
    {"id": "hfc-ca", "all": ["hfc", "ca"],
     "title": "An HFC that is also an IRDAI corporate agent",
     "adds": [
        {"sec": "rbi", "id": "MD-FINSVC", "paras": [40, 49], "scope": "Paras 40 and 45-49",
         "note": "HFCs with the prescribed net owned fund may take up fee-based insurance agency without RBI approval, with IRDAI permission. A Board-approved policy on insurance distribution, customer suitability checks, no commission paid directly to staff, no forcing a particular insurer or linking insurance to a loan, and fees disclosed in the notes to accounts."},
        {"sec": "irdai", "id": "REG-CA", "note": "Registration, principal officer, trained specified persons, insurer tie-ups and conduct rules for corporate agents."}]},
    {"id": "nbfc-listed", "any2": ["eq", "debt"], "any": ["icc", "hfc", "cic", "mfi", "factor", "ifc", "idf", "p2p", "aa"],
     "title": "An NBFC with listed equity or debt",
     "adds": [
        {"sec": "rbi", "id": "MD-CRM", "paras": [13, 13], "scope": "Para 13P",
         "note": "On lending to related parties, a listed NBFC also follows the SEBI Listing Regulations, on top of the RBI rules."},
        {"sec": "sebi", "id": "REG-LODR", "note": "Related party transaction approvals and disclosures under the Listing Regulations."}]},
    {"id": "ul-unlisted", "any": ["ul"], "none": ["eq"], "because": "Upper Layer, equity not listed",
     "title": "An Upper Layer NBFC whose equity is not yet listed",
     "adds": [
        {"sec": "rbi", "id": "MD-GOV", "paras": [42, 43], "scope": "Paras 42-43",
         "note": "List equity within three years of being placed in the Upper Layer, and follow listed-company disclosure standards before listing, under a Board-approved policy. Not for Upper Layer NBFCs fully owned and controlled by Government."},
        {"sec": "rbi", "id": "MD-FS", "paras": [23, 23], "scope": "Para 23",
         "note": "A Board-approved roadmap to meet the disclosure requirements of a listed company under the SEBI Listing Regulations."}]},
]

# The same instrument summarised in two sections: show it once, under the first.
SAME_AS = [
    (("rbi", "MD-CREDIT"), ("dpdp", "RBI-DL")), (("rbi", "MD-KYC"), ("dpdp", "RBI-KYC")),
    (("rbi", "MD-OUTS"), ("dpdp", "RBI-OUTS")), (("rbi", "MD-CYBER"), ("dpdp", "RBI-CYBER")),
    (("rbi", "MD-AA"), ("dpdp", "RBI-AA")), (("rbi", "ACT-CICRA"), ("dpdp", "ACT-CICRA")),
    (("rbi", "ACT-IT"), ("dpdp", "ACT-IT")), (("sebi", "MC-CSCRF"), ("dpdp", "SEBI-CSCRF")),
    (("irdai", "REG-PPHI"), ("dpdp", "IRDAI-PPHI")), (("irdai", "MC-CYBER"), ("dpdp", "IRDAI-CYBER")),
    (("dpdp", "ACT-DPDP"), ("rbi", "ACT-DPDP")), (("ibc", "CODE"), ("rbi", "ACT-IBC")),
    (("sebi", "REG-LODR"), ("rbi", "REG-SEBI-LODR")), (("sebi", "REG-NCS"), ("rbi", "REG-SEBI-NCS")),
    (("fema", "ACT-FEMA"), ("rbi", "ACT-FEMA")), (("fema", "REG-BL"), ("rbi", "REG-FEMA-BL")),
    (("fema", "MD-FDI"), ("rbi", "MD-FEMA-FDI")), (("fema", "MD-ODI"), ("rbi", "MD-FEMA-ODI")),
    (("fema", "MD-ECB"), ("rbi", "MD-FEMA-ECB")),
]

PRESETS = [
    {"label": "NBFC · Middle Layer · listed debt · corporate agent", "sel": ["icc", "ml", "debt", "ca"]},
    {"label": "HFC · Middle Layer · corporate agent", "sel": ["hfc", "ml", "ca"]},
    {"label": "Corporate agent · LSP · DSA", "sel": ["unreg", "ca", "lsp", "dsa"]},
]

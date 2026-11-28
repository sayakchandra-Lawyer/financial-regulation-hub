"""Build the About, Feedback, Contact and Disclaimer & privacy pages.

Run from the repo root:  python3 -I tools/make_info_pages.py
Contact details shown on the site come from hub.json -> "contact".
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
idx = (ROOT / "index.html").read_text(encoding="utf-8")
VER = re.search(r"hub\.css\?v=([\w]+)", idx).group(1)
ICON = re.search(r'<link rel="icon"[^>]+>', idx).group(0)
REPO = "https://github.com/sayakchandra-lawyer/financial-regulation-hub"

PAGES = [("about", "About"), ("feedback", "Feedback"), ("contact", "Contact"), ("disclaimer", "Disclaimer & privacy")]

def side(active):
    links = "".join(f'<a class="il" href="../{k}/"{" aria-current=\"page\"" if k == active else ""}>{t}</a>' for k, t in PAGES)
    return f'''<aside>
      <div class="card"><h3>About this site</h3>{links}</div>
      <div class="card"><h3>Spotted an error?</h3><p class="tag" style="margin:0 0 12px">Tell us which page and what looks wrong. Corrections are the most useful feedback we get.</p><a class="btn p" href="../feedback/?type=error">Report an error</a></div>
    </aside>'''

def page(key, title, desc, body, script=""):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title} · Financial Regulation Hub</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,500;0,8..60,600;1,8..60,400&display=swap">
<link rel="stylesheet" href="../assets/hub.css?v={VER}">
{ICON}
</head>
<body>
<header id="top"></header>
<main class="wrap">
  <div class="ipage">
    <section class="rise">
{body}
    </section>
    {side(key)}
  </div>
</main>
<footer id="foot"></footer>
<script src="../assets/hub.js?v={VER}"></script>
<script>
(async function(){{
  const hub = await getJSON("../hub.json");
  renderChrome(hub, {{ root: "../", active: "{key}", crumb: `<a href="../">Home</a> / <b>{title.replace("&", "&amp;")}</b>` }});
  const C = hub.contact || {{}};
{script}
}})();
</script>
</body>
</html>
'''

ABOUT = '''      <div class="eyebrow">About</div>
      <h1>Financial regulation, in one place</h1>
      <p class="lede">Financial Regulation Hub brings together the rules that finance professionals work with every day: what each rule requires, who it applies to, when things are due and what happens on a breach, with a link to the official text for every point.</p>
      <h2>What it covers</h2>
      <p>Each regulator or law has its own section. Inside a section you can browse by subject, see a calendar of deadlines, read definitions and penalties, and open the full text of each instrument.</p>
      <div class="secgrid" id="secs"></div>
      <h2>Who it is for</h2>
      <ul>
        <li>Compliance, legal and risk teams at NBFCs, housing finance companies, banks, insurers, brokers, asset managers and other regulated entities.</li>
        <li>Company secretaries, auditors and consultants who advise them.</li>
        <li>Students and anyone who wants a plain-English starting point before reading the official text.</li>
      </ul>
      <h2>How to use it</h2>
      <ul>
        <li><b>Search</b> from the home page across every section, or inside one section.</li>
        <li><b>What changed this month</b> on the home page lists new and amended rules, each linked to the regulator's own notice.</li>
        <li><b>Ask Counsel’s Clerk</b> (bottom right on the home and section pages) answers questions from the texts on this site and cites the provision. Treat its answers as a pointer, not an opinion.</li>
      </ul>
      <h2>Independent and unofficial</h2>
      <p>This site is not run by, linked to or endorsed by any regulator, court or government body. It summarises public documents for general information. It is not legal advice, and it may be incomplete or out of date. Always check the official text, and take professional advice for a specific situation. See the <a class="lnk" href="../disclaimer/">disclaimer</a>.</p>
      <h2>Help us improve it</h2>
      <p>If a summary is wrong, a rule is missing or something is hard to find, please <a class="lnk" href="../feedback/">send feedback</a>.</p>'''
ABOUT_JS = '''  $("#secs").innerHTML = hub.sections.map(s => s.status === "live"
    ? `<a class="card" style="--c:var(--${s.id})" href="../${s.href}"><span class="ic">${I[s.id] || I.misc}</span><span><b>${esc(s.name)}</b><span>${esc(s.full)}</span></span></a>`
    : `<div class="card" style="--c:var(--${s.id});display:flex;gap:12px;padding:14px 16px;border-top:3px solid var(--c);opacity:.75"><span class="ic" style="color:var(--c)">${I[s.id] || I.misc}</span><span><b>${esc(s.name)}</b><span style="font-size:13px;color:var(--muted)">${esc(s.full)} · coming soon</span></span></div>`).join("");'''

FEEDBACK = '''      <div class="eyebrow">Feedback</div>
      <h1>Tell us what to fix or add</h1>
      <p class="lede">Found a mistake, a rule we have missed, or something hard to use? A few lines are enough. Please do not include personal or confidential client information.</p>
      <form class="card fform" id="fb" novalidate>
        <div><label id="tl">What is it about?</label>
          <div class="ftypes" role="radiogroup" aria-labelledby="tl">
            <input type="radio" name="type" id="t-error" value="Error in content"><label class="chip" for="t-error">Error in content</label>
            <input type="radio" name="type" id="t-missing" value="Missing rule or update"><label class="chip" for="t-missing">Missing rule or update</label>
            <input type="radio" name="type" id="t-idea" value="Suggestion"><label class="chip" for="t-idea">Suggestion</label>
            <input type="radio" name="type" id="t-bug" value="Something is broken"><label class="chip" for="t-bug">Something is broken</label>
            <input type="radio" name="type" id="t-other" value="Other" checked><label class="chip" for="t-other">Other</label>
          </div></div>
        <div><label for="fpage">Page or rule <span class="opt">(optional)</span></label><input id="fpage" name="page" placeholder="e.g. RBI › Fair Practices Code, para 4"></div>
        <div><label for="fmsg">Your feedback</label><textarea id="fmsg" name="msg" required maxlength="4000" placeholder="What is wrong or missing? If you can, add the official source (circular number or link)."></textarea></div>
        <div><label for="fname">Name or email for a reply <span class="opt">(optional)</span></label><input id="fname" name="who" autocomplete="email" placeholder="Leave blank to stay anonymous"></div>
        <div class="fsend" id="fsend"></div>
        <p class="fnote" id="fnote"></p>
      </form>'''
FEEDBACK_JS = f'''  const P = new URLSearchParams(location.search), F = $("#fb");
  const from = P.get("from"); if (from) $("#fpage").value = decodeURIComponent(from).replace(/^\\/financial-regulation-hub/, "") || "Home page";
  const t = P.get("type"); if (t && $("#t-" + t)) $("#t-" + t).checked = true;
  const REPO = "{REPO}";
  const btns = [];
  if (C.email) btns.push(`<button class="btn p" type="submit" data-via="mail">Send by email</button>`);
  btns.push(`<button class="btn ${{C.email ? "g" : "p"}}" type="submit" data-via="gh">Post on GitHub</button>`);
  $("#fsend").innerHTML = btns.join("");
  $("#fnote").innerHTML = (C.email ? "<b>Send by email</b> opens your email app with the message filled in. " : "") + "<b>Post on GitHub</b> opens a prefilled issue; it needs a free GitHub account and is <b>public</b>, so leave out anything private.";
  let via = C.email ? "mail" : "gh";
  F.addEventListener("click", e => {{ const b = e.target.closest("[data-via]"); if (b) via = b.dataset.via; }});
  F.addEventListener("submit", e => {{
    e.preventDefault();
    const msg = $("#fmsg").value.trim(); if (!msg) {{ $("#fmsg").focus(); $("#fmsg").setAttribute("aria-invalid", "true"); return; }}
    const type = (F.querySelector("input[name=type]:checked") || {{}}).value || "Other", pg = $("#fpage").value.trim(), who = $("#fname").value.trim();
    const subject = `[${{type}}] ${{pg || msg.split("\\n")[0]}}`.slice(0, 110);
    const body = `Type: ${{type}}\\nPage or rule: ${{pg || "-"}}\\n\\n${{msg}}${{who ? `\\n\\nReply to: ${{who}}` : ""}}`;
    if (via === "mail" && C.email) location.href = `mailto:${{C.email}}?subject=${{encodeURIComponent("Feedback: " + subject)}}&body=${{encodeURIComponent(body)}}`;
    else window.open(`${{REPO}}/issues/new?title=${{encodeURIComponent(subject)}}&body=${{encodeURIComponent(body.replace(/\\n\\nReply to: .*$/, ""))}}`, "_blank", "noopener");
  }});'''

CONTACT = '''      <div class="eyebrow">Contact</div>
      <h1>Get in touch</h1>
      <p class="lede">For corrections and suggestions, the feedback form is the quickest route. For anything else, use one of the options below.</p>
      <div class="cways" id="ways"></div>
      <h2>Before you write</h2>
      <ul>
        <li>This site cannot give advice on a specific transaction or dispute, and writing to us does not create any professional relationship.</li>
        <li>For a regulator's official position, contact that regulator directly. Each section links to the regulator's website.</li>
        <li>Please do not send confidential or personal information about clients or customers.</li>
      </ul>'''
CONTACT_JS = f'''  const W = [`<div class="card"><h3>Feedback and corrections</h3><p class="tag">Report an error, a missing rule or a broken page.</p><a class="btn p" href="../feedback/">Open the feedback form</a></div>`];
  if (C.email) W.push(`<div class="card"><h3>Email</h3><p class="tag">${{esc(C.email)}}</p><a class="btn g" href="mailto:${{esc(C.email)}}">Write an email</a></div>`);
  if (C.linkedin) W.push(`<div class="card"><h3>LinkedIn</h3><p class="tag">${{esc(C.name || "Message us on LinkedIn")}}</p><a class="btn g" href="${{esc(C.linkedin)}}" target="_blank" rel="noopener">Open LinkedIn</a></div>`);
  W.push(`<div class="card"><h3>GitHub</h3><p class="tag">Public issues and discussion about the site. Needs a free GitHub account.</p><a class="btn g" href="{REPO}/issues" target="_blank" rel="noopener">Open GitHub issues</a></div>`);
  $("#ways").innerHTML = W.join("");'''

DISCLAIMER = '''      <div class="eyebrow">Disclaimer &amp; privacy</div>
      <h1>Please read before relying on this site</h1>
      <p class="lede">Financial Regulation Hub is an independent, unofficial resource for general information. Using it means you accept the terms below.</p>
      <h2>Not legal advice</h2>
      <p>Nothing on this site is legal, financial, tax or other professional advice, and using it does not create a lawyer-client or any other professional relationship. Summaries, timelines, penalties and answers from Counsel’s Clerk are simplified and can be wrong or incomplete. Take advice from a qualified professional before acting on anything here.</p>
      <h2>Always check the official text</h2>
      <p>Laws, rules, directions and circulars change often, and their official versions prevail over anything on this site. Each entry links to the regulator's or the Gazette's own text; read it before you rely on a point. Court rulings are summarised for convenience; read the judgment itself and check whether it has been appealed, stayed or overruled.</p>
      <h2>No endorsement</h2>
      <p>This site is not run by, linked to or endorsed by the Reserve Bank of India, SEBI, IRDAI, IBBI, the Data Protection Board, any court, or any government body. Names of regulators and laws are used only to describe the content. Links to other websites are for convenience; we do not control them.</p>
      <h2>Not an advertisement</h2>
      <p>This site is for information only. It is not an advertisement or a solicitation of work or clients by anyone.</p>
      <h2>No liability</h2>
      <p>To the fullest extent the law allows, no one involved in this site is liable for any loss arising from its use, from reliance on its content, or from it being unavailable.</p>
      <h2 id="privacy">Privacy</h2>
      <ul>
        <li><b>No accounts, no tracking.</b> The site has no sign-in, sets no cookies and runs no analytics or advertising.</li>
        <li><b>Your preferences, saved entities, watchlist and collections stay on your device.</b> Choices such as light or dark mode, your chosen lens, the entities you save, the rules you watch and the extracts and notes in your research collections are saved in your browser's local storage. They are never sent to us. Anyone with access to this browser can see them, so avoid saving client-confidential notes on a shared device. You can clear them from your browser settings or with "Delete all my data on this browser" on My dashboard.</li>
        <li><b>Files you export are yours to keep safe.</b> A saved copy from My dashboard, or a collection you print or download, is created on your device only. Once it leaves the site, how it is stored and shared is up to you.</li>
        <li><b>Questions to Counsel’s Clerk</b> are sent, with extracts from the texts on this site, to an AI service to produce the answer. Do not type personal, client or confidential information into it. To decide which common questions to answer on the site, the number of questions on broad topics (such as KYC or co-lending) is counted each month; only the count is kept, never the question.</li>
        <li><b>Feeds.</b> RSS feeds are plain files. Your feed reader fetches them like any web page; we do not know who subscribes.</li>
        <li><b>Feedback.</b> Feedback posted on GitHub is public. Feedback sent by email is used only to reply and improve the site.</li>
        <li><b>Hosting and fonts.</b> The site is hosted on GitHub Pages and loads fonts from Google Fonts. Like any website host, they may log technical data such as your IP address under their own privacy policies.</li>
      </ul>
      <p>For questions about this notice, please use the <a class="lnk" href="../contact/">contact page</a>.</p>'''

CONTENT = {
    "about": ("About", "What Financial Regulation Hub covers, who it is for and how to use it.", ABOUT, ABOUT_JS),
    "feedback": ("Feedback", "Report an error, a missing rule or update, or suggest an improvement to Financial Regulation Hub.", FEEDBACK, FEEDBACK_JS),
    "contact": ("Contact", "How to get in touch with Financial Regulation Hub.", CONTACT, CONTACT_JS),
    "disclaimer": ("Disclaimer & privacy", "Disclaimer and privacy notice for Financial Regulation Hub: not legal advice, check official texts, no tracking.", DISCLAIMER, ""),
}
for key, (title, desc, body, js) in CONTENT.items():
    d = ROOT / key; d.mkdir(exist_ok=True)
    (d / "index.html").write_text(page(key, title, desc, body, js), encoding="utf-8")
    print("wrote", key)

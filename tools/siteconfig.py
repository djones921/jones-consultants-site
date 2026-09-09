# -*- coding: utf-8 -*-
"""
Single source of truth for jcseng.com.
Every page, JSON-LD block, sitemap entry, robots rule, llms.txt line and manifest field is
generated from this file by tools/build.py (imports tools/siteconfig.py). Edit here, run `python3 tools/build.py`, commit.

Fields marked None with a [VERIFY] comment are intentionally omitted from output until filled.
"""

SITE = "https://jcseng.com"
BRAND = "JCS Engineering"
LEGAL = "JCS Engineering PLLC"
TAGLINE = "Project engineering, design, CQV and project management for regulated manufacturing"
FOUNDING_YEAR = None          # owner prefers not to publish (founded 2026); leave None
LOCALE = "en_US"

# ---- NAP (must match Google Business Profile exactly) ------------------------------------
PHONE_DISPLAY = "(704)&nbsp;500&#8209;3033"
PHONE_PLAIN = "(704) 500-3033"
PHONE_E164 = "+17045003033"
EMAIL = "drew@jcseng.com"
ADDRESS = dict(
    street="5540 Centerview Dr, Ste 200-210",
    locality="Raleigh",
    region="NC",
    postal="27606",
    country="US",
)
GEO = dict(lat=35.762964, lng=-78.732141)   # 5540 Centerview Dr, from Google Maps
HOURS = [("Monday", "Friday", "06:00", "17:00")]   # matches Google Business Profile: Mon–Fri 6:00 AM–5:00 PM, Sat–Sun closed
SERVICE_AREA_LINE = "Serving the Research Triangle and North Carolina"
CONTENT_DATE = "2026-09-08"   # sitemap lastmod / humans.txt date; bump when content changes (keeps the build deterministic for CI)

# ---- Profiles (sameAs) — only emitted when set ---------------------------------------------
PROFILES = dict(
    linkedin_company="https://www.linkedin.com/company/jcseng/",
    linkedin_person="https://www.linkedin.com/in/drewjones2",
    google_business="https://www.google.com/maps/place/JCS+Engineering+PLLC/data=!4m2!3m1!1s0xa5d75401ea2be2d9:0x93acc8abfa3897e5",
    nc_board_lookup="https://www.ncbels.org/",   # public licence lookup portal
)

# ---- Verification tokens — only emitted when set ------------------------------------------
GOOGLE_SITE_VERIFICATION = None   # [VERIFY] content value from Search Console HTML-tag method
BING_SITE_VERIFICATION = None     # [VERIFY] content value from Bing Webmaster Tools meta-tag method
INDEXNOW_KEY = "9f3a6c2e8d4b4f1a9c7e5b2d8a6f4c3e"   # 32-hex key; file /<key>.txt is generated

# ---- Third parties -------------------------------------------------------------------------
FORMSPREE = "https://formspree.io/f/xqadzgzp"
MAP_SRC = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3234.5!2d-78.732141!3d35.762964!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xa5d75401ea2be2d9%3A0x93acc8abfa3897e5!2sJCS%20Engineering%20PLLC!5e0!3m2!1sen!2sus!4v1788914137359!5m2!1sen!2sus"

# ---- Geography ------------------------------------------------------------------------------
AREA_SERVED = [  # (name, type)  — emitted as schema.org City / AdministrativeArea / State
    ("Raleigh", "City"), ("Durham", "City"), ("Cary", "City"), ("Holly Springs", "City"), ("Clayton", "City"),
    ("Knightdale", "City"), ("Wendell", "City"), ("Zebulon", "City"), ("Garner", "City"), ("Apex", "City"),
    ("Wake Forest", "City"), ("Morrisville", "City"), ("Chapel Hill", "City"), ("Sanford", "City"), ("Wilson", "City"),
    ("Greenville", "City"), ("Research Triangle Park", "Place"),
    ("Wake County", "AdministrativeArea"), ("Johnston County", "AdministrativeArea"), ("Durham County", "AdministrativeArea"),
    ("North Carolina", "State"),
]

# ---- Principal --------------------------------------------------------------------------------
PRINCIPAL = dict(
    name="Drew W. Jones, PE", given="Drew", family="Jones", short="Drew Jones, PE",
    title="Founder &amp; Principal Engineer", pe_state="North Carolina", pe_no="062483",
    firm_lic="P-3451", school="North Carolina State University",
    education="B.S., Chemical &amp; Biomolecular Engineering — Minor in Biotechnology",
    bio=[
      "Drew Jones is the founder and principal engineer of JCS Engineering PLLC. A chemical engineer by training, he has spent his career on the owner's side of regulated manufacturing in North Carolina and Massachusetts — in process engineering roles in industrial biotechnology and sterile injectables, as an automation and process engineer and later senior project manager and engineer in inhalation and oral solid dose manufacturing, as a project manager on an API site, and as CQV lead on a large-scale biologics manufacturing site.",
      "That path runs through every phase of a capital project: writing user and functional requirements, performing process calculations, designing pressure vessels, CIP, solvent, and fluid-transfer systems, specifying equipment down to the check valve, leading FAT/SAT and IQ/OQ, administering construction, closing punch lists, and handing systems to operations for tech transfer. He was the responsible engineer for a $25M expansion that converted a single-product site into a multi-product spray-drying facility, and he has commissioned everything from –40&nbsp;°C process chillers to site-wide black utilities.",
      "Drew is a licensed Professional Engineer in North Carolina and a Lean Six Sigma Green Belt. As principal, he is accountable for every engagement the firm delivers — and for the engineers, project managers, and CQV specialists JCS Engineering brings onto larger programs.",
    ],
)

# ---- Services --------------------------------------------------------------------------------
# Each service is a page at /capabilities/<slug>/.  `page_title` <= 60 chars incl. " | JCS Engineering PLLC"
# is enforced by the build; `meta` must be 140-160 chars.
SERVICES = [
 dict(slug="project-engineering", n="01",
  title="Project Engineering &amp; Management",
  page_title="Owner's Rep &amp; Project Engineering",
  h1="Owner's Representation and Project Engineering Services for Pharmaceutical Capital Projects in North Carolina",
  meta="Owner-side project engineering and management for pharma and biotech capital projects in North Carolina — scope, budget, schedule and quality to closeout.",
  short="Owner-side engineering and project management from kickoff through closeout.",
  intro="JCS Engineering is an owner's representation firm for pharmaceutical, biotech, and advanced manufacturing capital projects in North Carolina. An owner's representative is the engineer on your side of the table — the one party on a project whose only interest is the owner's. Our owner's rep services cover defining scope, driving schedule and budget, coordinating the design firm, contractors, vendors, and quality organization, and holding every one of them to the intent of the project.",
  scope=[
   "<strong>Project definition.</strong> Business case support, scope and capacity basis, order-of-magnitude estimates, and the stage-gate structure the project will be run against.",
   "<strong>Design management.</strong> Owner-side review of the architect-engineer's work at every milestone: does it meet the user requirements, is it constructible, is it qualifiable, and does it stay inside the budget?",
   "<strong>Procurement support.</strong> Technical bid evaluation, clarification management, FAT planning, and long-lead tracking so equipment arrives sequenced to the schedule rather than discovered on site.",
   "<strong>Construction and CQV coordination.</strong> The single point of contact through the field and qualification phases — see <a href=\"/capabilities/construction-oversight/\">construction oversight</a> and <a href=\"/capabilities/cqv/\">CQV</a>.",
   "<strong>Governance.</strong> Budget and schedule tracking, a decision log, risk register, and change control, with reporting sized for site leadership and executive steering groups.",
  ],
  process="Most engagements begin with a short scoping conversation about where the project stands, followed by a written proposal. On approval we set up the project execution plan — stage gates, deliverables register, reporting cadence, and decision authority — in the first two weeks. From there the engagement runs at the intensity the phase demands: design reviews and gate packages during design, field presence during construction, protocol execution during CQV. The same engineer carries the project across phases; for larger programs we add project engineers, project managers, and CQV leads under the same accountability.",
  deliv=["Project execution plan","Stage-gate framework &amp; gate criteria","Integrated schedule &amp; budget tracking","Weekly status report &amp; decision log","Risk register &amp; change log","Closeout report &amp; lessons learned"],
  who="Pharmaceutical and biotech owners without a spare engineer to run a capital project; operations and quality leaders who cannot absorb a project on top of production; CDMOs adding capacity; site leadership who want independent eyes on the design firm and contractor; owners whose project has drifted and needs a reset.",
  why="We have held the responsible-engineer seat on the owner's side through every phase of real capital projects — including a $25M single-to-multi-product facility conversion — so we know where projects actually fail: at the handoffs between phases, and at the interfaces between systems that no vendor owns. Every engagement is led by a licensed North Carolina Professional Engineer under a licensed engineering firm, and we have no stake in the construction contract or design fee.",
  faq=[
   ("What does an owner's engineer do on a pharmaceutical project, and how is that different from the construction manager?", "The construction manager delivers the contract — schedule, cost, and scope as written. The owner's representative protects what the owner actually needs, which includes things outside any single contract: whether the design meets the user requirements, whether a change order has a compliance impact, whether qualification is being planned early enough, and whether the handover package will stand up to an inspection. The two roles are complementary; the CM works for the contract, the owner's rep works for you."),
   ("When in a project should we bring in an owner's engineer?", "As early as you can. The cheapest change on any project is the one made before drawings exist, so the greatest leverage is during concept and basis of design. That said, we regularly join projects mid-design or mid-construction; the first task is then an honest assessment of where the project stands and what is at risk."),
   ("Can JCS Engineering act as the owner's representative for a project outside North Carolina?", "Our firm is licensed in North Carolina (Firm License P-3451), and our principal has delivered projects in both North Carolina and Massachusetts. Owner's representation and project management are not themselves the practice of engineering in most states, but any engineering design or sealed work is delivered where we hold licensure. Ask us about a specific location."),
   ("How is the engagement priced?", "Around the project, not a template: an embedded engineer on a monthly basis, milestone-based oversight, or a fixed-scope deliverable. We recommend a structure after the scoping call and put fees in plain language in the proposal."),
  ],
  related=["construction-oversight","cqv","change-risk-compliance"], post="owners-engineer-pharmaceutical-capital-project"),

 dict(slug="engineering-design", n="02",
  title="Conceptual &amp; Detailed Design",
  page_title="Process &amp; Facility Design Engineering",
  h1="Conceptual and Detailed Design for cGMP Process Facilities in North Carolina",
  meta="Process and mechanical design for pharma and biotech facilities: URS, basis of design, PFDs and P&amp;IDs, calculations, equipment specs and IFC packages.",
  short="Process and mechanical design from basis of design through construction-ready packages.",
  intro="JCS Engineering carries engineering design from concept through detailed design for pharmaceutical, biotech, and advanced manufacturing facilities. The work starts with user requirements and a defensible basis of design and ends with construction-ready packages — process flow diagrams, P&amp;IDs, calculations, and equipment and instrument specifications — for process systems and the utilities and environments around them.",
  scope=[
   "<strong>Front-end design.</strong> User requirement specifications (URS), basis of design (BOD), block flow and adjacency studies, option comparison, and estimate input before capital is committed.",
   "<strong>Process design.</strong> PFDs and P&amp;IDs, heat and mass balances, flow, pressure-drop and pump calculations, line sizing, relief evaluation, and critical process parameter definition for scale-up.",
   "<strong>Systems.</strong> Formulation and pressure vessels, CIP skids, solvent handling and high-pressure fluid systems, fluid transfer, spray drying and vacuum drying, filling and inspection equipment integration.",
   "<strong>Utilities and environment.</strong> Clean utilities (WFI, clean steam, process gases), black utilities (chilled water, heating hot water, steam, soft water), process chillers, and cleanroom HVAC — air changes, pressure cascades, and equipment load.",
   "<strong>Specification.</strong> Equipment and instrument specifications and data sheets, from complete skids down to check valves, diaphragm pumps, flow meters, and regulators, selected against process parameters and cleanability.",
  ],
  process="Design is delivered against the stage gates on our <a href=\"/approach/\">Approach</a> page: concept, then front-end design, then detailed design, each closing with a reviewed package and a go/no-go decision. Requirements are written to be verifiable — every URS line traces forward to a design element and to a qualification test — which is what keeps <a href=\"/capabilities/cqv/\">CQV</a> off the critical path later. Design deliverables are produced in AutoCAD and standard engineering formats, and we coordinate with your architect-engineer, automation integrator, and construction manager rather than working in isolation.",
  deliv=["URS &amp; basis of design","Block flow diagrams &amp; adjacency studies","PFDs &amp; P&amp;IDs","Process, hydraulic &amp; relief calculations","Equipment &amp; instrument specifications and data sheets","Detailed design &amp; issued-for-construction packages"],
  who="Owners adding a line, suite, or process to an existing cGMP site; CDMOs modifying equipment for a new client process; facilities converting from single- to multi-product operation; owners who want an independent technical review of an A/E's concept before approving capital.",
  why="Our design experience comes from the owner's side of operating facilities — the same engineer who specified the check valve later executed the IQ and watched operators run the system. That produces designs that are maintainable, cleanable, and qualifiable, not just code-compliant. Design work is delivered under a licensed North Carolina engineering firm by a licensed Professional Engineer.",
  faq=[
   ("Do you produce sealed engineering drawings?", "JCS Engineering PLLC is a licensed North Carolina engineering firm (P-3451) and our principal is a North Carolina PE (No. 062483). Where a deliverable requires a professional seal in North Carolina, we provide it within our discipline; for work in other states or disciplines we coordinate with your architect-engineer of record. Confirm the requirement with us at scoping."),
   ("What is the difference between a URS and a basis of design?", "The user requirement specification says what the system must do, in the owner's and quality unit's language: capacity, product contact materials, cleanability, environmental class, data requirements. The basis of design says how the engineering will achieve it: process approach, utilities, equipment philosophy, codes and standards. The URS is the contract between owner and designer; the BOD is the designer's answer to it. Both are needed, and qualification later verifies the design against the URS."),
   ("Can you design against single-use as well as stainless platforms?", "Yes. The design consequences differ — utility loads, CIP/SIP scope, footprint, changeover, and waste — and we work through those trade-offs in the concept phase rather than after equipment is ordered."),
   ("Which standards do you design to?", "The codes and guidance that govern your facility: ISPE Baseline Guides, ASTM E2500, GAMP 5, ASME BPE, ASME B31.3 and Section VIII, ISO 14644, NFPA 30/70/497 for solvent and classified areas, ASHRAE, and 21 CFR Parts 210, 211 and 11. The full list is on our <a href=\"/approach/#standards\">Approach</a> page."),
  ],
  related=["project-engineering","cqv","optimization-tech-transfer"], post="facility-fit-gap-assessment-tech-transfer"),

 dict(slug="construction-oversight", n="03",
  title="Construction Administration &amp; Oversight",
  page_title="cGMP Construction Oversight",
  h1="Construction Administration and Oversight for cGMP Facilities in North Carolina",
  meta="Owner-side construction administration for cGMP facilities in North Carolina: submittal and RFI management, field verification, change orders and turnover.",
  short="Field coordination and verification that what's built matches what was designed.",
  intro="Drawings describe intent; construction is where intent meets a jobsite. JCS Engineering provides owner-side construction administration for pharmaceutical, biotech, and advanced manufacturing facilities: managing the submittal and RFI flow, walking the work, verifying progress and pay applications, reviewing change orders, and sequencing construction around operations that cannot stop.",
  scope=[
   "<strong>Document flow.</strong> Submittal and RFI logs, technical review and turnaround tracking, and coordination between the A/E, contractor, and equipment vendors so questions are answered once, on the record.",
   "<strong>Field verification.</strong> Regular walkdowns against drawings and specifications, observation reports, and early identification of deviations before they are covered up or built upon.",
   "<strong>Commercial control.</strong> Progress verification against the schedule and pay applications, change order review for scope, cost, schedule, and compliance impact, and an owner-side recommendation on each.",
   "<strong>Operations protection.</strong> Shutdown planning, pressure-cascade and containment controls, tie-in sequencing, and communication with production and quality so construction inside or adjacent to a GMP area does not become a deviation.",
   "<strong>Completion.</strong> Mechanical completion walkdowns, punch classification by criticality, punch closure and escalation, and review of turnover packages before acceptance.",
  ],
  process="We attend the owner-architect-contractor meetings, own the owner's action items, and report weekly on progress, open RFIs, change exposure, and risk. Field presence scales with the phase — heavier during tie-ins, equipment set, and mechanical completion — and can be full-time for a major program. Construction administration hands directly into <a href=\"/capabilities/cqv/\">commissioning and qualification</a>: the same punch list, the same turnover packages, and the same engineer.",
  deliv=["Submittal &amp; RFI logs and reviews","Field observation reports","Progress &amp; pay-application verification","Change order technical and cost review","Shutdown &amp; tie-in plans","Punch list &amp; turnover package review"],
  who="Owners building inside or next to an operating GMP facility; site engineering groups stretched across production support and capital work; owners who want a contractor's progress and invoices independently verified; projects with complex MEP, cleanroom, or process installations.",
  why="We have administered construction for facility expansions, cleanroom buildouts, solvent and utility systems, and equipment installations in operating cGMP plants — where the cost of a shutdown is measured in batches, not days. We know which submittals matter, which RFIs signal a design gap, and how to sequence work so production stays on plan.",
  faq=[
   ("How do you build inside an operating GMP facility without disrupting production?", "By planning it as a controlled activity, not a nuisance: mapping the risk to classified areas and product, establishing containment and pressure-cascade controls, scheduling tie-ins in defined shutdown windows, running changes through change control, and communicating with production and quality daily. The design phase is where most of that is decided, which is why we prefer to be involved before construction starts."),
   ("Do you replace the construction manager or general contractor?", "No. The CM or GC executes the work. We represent the owner: verifying that the work matches the design, that invoices match progress, and that changes are justified. On projects without a CM we can carry more of the coordination load, but we do not self-perform construction."),
   ("What is a punch list criticality classification?", "Not every open item blocks handover. We classify each punch item by its effect on safety, GMP compliance, and system function — items that would prevent qualification or operation are closed before turnover; cosmetic items are tracked to closure without holding up startup."),
   ("Can you review pay applications and change orders?", "Yes. Progress verification against the schedule of values and a technical and cost review of every change order — including its impact on qualification and compliance — is a standard part of the scope."),
  ],
  related=["project-engineering","cqv","change-risk-compliance"], post="owners-engineer-pharmaceutical-capital-project"),

 dict(slug="cqv", n="04",
  title="Commissioning, Qualification &amp; Validation",
  page_title="CQV Consulting for Pharma &amp; Biotech",
  h1="Commissioning, Qualification and Validation (CQV) Services in North Carolina",
  meta="CQV consulting for pharma and biotech in North Carolina: commissioning plans, impact assessments, FAT/SAT, IQ/OQ/PQ protocols, execution and turnover packages.",
  short="Planning and execution from commissioning plan through IQ, OQ, and PQ.",
  intro="Commissioning, qualification, and validation is where a construction project becomes a production asset — or stalls for months. JCS Engineering plans and executes CQV for pharmaceutical, biotech, and advanced manufacturing systems: impact and risk assessments, FAT and SAT, IQ/OQ/PQ protocols and execution, and the traceability that ties every test back to a requirement, so the handover package stands up to inspection and your teams can run the system on day one.",
  scope=[
   "<strong>Planning.</strong> Commissioning and qualification plan, system impact and component criticality assessments, risk-based test strategy (ASTM E2500 or traditional IQ/OQ/PQ, to match your quality system), and a requirements traceability matrix.",
   "<strong>Vendor testing.</strong> FAT protocol review and execution at the vendor, leveraging FAT results into qualification where your procedures allow, and SAT on receipt.",
   "<strong>Commissioning.</strong> Mechanical completion walkdowns, pre-commissioning checks, functional testing, and punch classification and closure for process, utility, automation, and HVAC systems.",
   "<strong>Qualification.</strong> IQ, OQ, and PQ protocol authoring, execution, deviation handling, and reporting for equipment, clean and black utilities, cleanrooms, filling and inspection lines, and process trains.",
   "<strong>Turnover.</strong> Turnover and validation summary packages, training support, and handover to operations and quality.",
  ],
  process="CQV succeeds or fails on planning done during design, which is why we start impact assessments and the traceability matrix while the URS is being written — see <a href=\"/capabilities/engineering-design/\">design</a>. During procurement, FAT is treated as a qualification lever rather than a formality. During construction, commissioning runs alongside mechanical completion so systems are ready for qualification the day they are turned over. We work inside your quality system and document formats, with your quality unit as the approver, and we can lead a multidiscipline CQV team — process, automation, I&amp;C, and mechanical — or execute a defined package.",
  deliv=["C&amp;Q plan &amp; risk-based test strategy","System impact &amp; component criticality assessments","Requirements traceability matrix","FAT / SAT protocols &amp; execution","IQ / OQ / PQ protocols, execution &amp; reports","Turnover &amp; validation summary packages"],
  who="Owners bringing new or modified equipment, utilities, or facilities into GMP use; validation groups thin relative to the project load; greenfield or expansion sites that need a CQV lead and execution team for a defined period; CDMOs qualifying systems for a new client process.",
  why="We have led CQV on large-scale biologics site startups — drug substance, drug product filling and inspection, and site-wide black utilities — and executed FAT, SAT, and IQ/OQ for filling, inspection, spray drying, chiller, and cleanroom systems. We plan qualification from the design phase because we have seen what happens when it starts when construction ends.",
  faq=[
   ("What is the difference between commissioning and qualification?", "Commissioning is the engineering process of verifying that a system is installed and functions as designed — an engineering activity, documented but not necessarily under the quality system. Qualification is the documented, quality-approved verification that the system is fit for its intended GMP use: installation qualification (IQ), operational qualification (OQ), and performance qualification (PQ). Good commissioning makes qualification faster because most problems are found and fixed before protocols are executed."),
   ("When should CQV planning start?", "During design. The system impact assessment, the component criticality assessment, and the traceability matrix all depend on the URS and the design, and they determine what gets tested and how. Starting CQV when construction finishes typically doubles the qualification timeline."),
   ("Do you work under ASTM E2500 or traditional IQ/OQ/PQ?", "Either, to match your quality system. ASTM E2500 risk-based verification can reduce documentation on non-critical systems; many sites still qualify with IQ/OQ/PQ. We help choose the approach during planning and document the rationale."),
   ("Can you provide a CQV lead on a contract basis for a site startup?", "Yes. We provide CQV leads and execution engineers embedded in your program for a defined period — leading multidiscipline teams through drug substance, drug product, and utilities CQV — under the firm's PE-led accountability."),
  ],
  related=["engineering-design","construction-oversight","change-risk-compliance"], post="cqv-planning-starts-in-design"),

 dict(slug="change-risk-compliance", n="05",
  title="Change, Risk &amp; Compliance Management",
  page_title="Project Change &amp; Risk Management",
  h1="Project Change Control and Risk Management for cGMP Capital Projects",
  meta="Project change control, risk registers, document control and inspection readiness for pharma and biotech capital projects — governance built in, not bolted on.",
  short="Structured change control, living risk registers, and inspection-ready documentation.",
  intro="Every capital project changes; the question is whether change is assessed, priced, approved, and documented, or absorbed silently until it appears as a schedule slip or a compliance gap. JCS Engineering builds project change control, risk management, and GMP documentation discipline into project governance so the facility is inspection-ready when it is production-ready.",
  scope=[
   "<strong>Change control.</strong> A project change procedure with a single approval path; impact assessment of each change on scope, cost, schedule, qualification, and compliance; a change log that survives the project.",
   "<strong>Risk management.</strong> A risk register that is actually reviewed — owners, triggers, mitigations, and dates — with an escalation framework so leadership sees exposure early.",
   "<strong>Document control.</strong> A document control plan for design, construction, and qualification records; version and approval discipline; traceability from requirement to design to test.",
   "<strong>Design qualification support.</strong> Documented review that the design meets the URS and applicable GMP requirements before construction — the foundation for IQ/OQ later.",
   "<strong>Inspection readiness.</strong> Gap assessment of project documentation against regulatory expectations, remediation plans, and support during pre-approval and routine inspections.",
  ],
  process="Governance is set up in the first weeks of an engagement and runs for the life of the project: a weekly risk and change review, a decision log, and gate packages that show leadership the current exposure. We work inside your quality system — your change control and document management procedures — rather than imposing a parallel one, and we coordinate with quality assurance so engineering changes and quality records stay aligned.",
  deliv=["Project change control procedure &amp; log","Risk register &amp; mitigation plans","Escalation framework","Document control plan","Design qualification report","Inspection readiness assessment &amp; remediation plan"],
  who="Owners whose project scope is evolving while work is underway; quality units who need engineering changes assessed for GMP impact; sites preparing for pre-approval inspection of a new facility; multi-vendor programs that need one approval path for change.",
  why="We have run change control and risk management on programs from targeted equipment upgrades to a $25M multi-product facility conversion, and we have prepared and reviewed the documentation that inspectors ask for — because we wrote it during the project rather than reconstructing it afterward.",
  faq=[
   ("How is project change control different from quality change control?", "Quality change control governs changes to validated systems and processes under the site's quality system. Project change control governs changes to scope, design, cost, and schedule during a capital project — and must feed the quality system whenever a change touches a GMP-impacting system. We set up the project process so the two connect rather than conflict."),
   ("What belongs in a project risk register?", "Anything with a credible chance of hurting scope, cost, schedule, quality, or safety: long-lead equipment, utility capacity, tie-in windows, vendor performance, regulatory interpretation, and staffing. Each entry has an owner, a trigger, a mitigation, and a review date. A register nobody reviews is decoration."),
   ("Can you help prepare for a pre-approval inspection of a new facility?", "Yes. We assess project documentation — design records, qualification packages, change history — against regulatory expectations, close gaps, and support the engineering side of the inspection."),
   ("Do you work inside our existing document management system?", "Yes. We use your procedures, templates, and systems wherever they exist and propose additions only where a gap would otherwise put the project at risk."),
  ],
  related=["project-engineering","cqv","construction-oversight"], post="cqv-planning-starts-in-design"),

 dict(slug="optimization-tech-transfer", n="06",
  title="Process Optimization &amp; Tech Transfer",
  page_title="Tech Transfer &amp; Process Optimization",
  h1="Process Optimization and Technology Transfer Engineering in North Carolina",
  meta="Tech transfer and process optimization engineering: facility fit-gap assessments, scale-up calculations, equipment and utility modifications, startup support.",
  short="Moving and improving processes across scales, suites, and sites — and supporting them after startup.",
  intro="Technology transfer is engineering work disguised as paperwork. Moving a process to a new scale, suite, or site means reconciling equipment differences, utility capacities, materials compatibility, cleaning strategies, and room classifications before the process runs where it has not run before. JCS Engineering provides the fit-gap assessment, scale-up engineering, and modifications that make a transfer succeed — and applies the same lens to lines already in production.",
  scope=[
   "<strong>Facility fit-gap assessment.</strong> A structured comparison of the incoming process against the receiving facility across capacity, utilities, materials of construction, environmental classification, cleaning, automation, and documentation.",
   "<strong>Scale-up engineering.</strong> Heat and mass balances, critical process parameter definition, equipment sizing (nozzles, dryers, vessels, pumps), and utility demand analysis for the new scale.",
   "<strong>Modifications.</strong> Scope, estimate, design, and execution of the equipment and utility changes the gap assessment identifies — see <a href=\"/capabilities/engineering-design/\">design</a>.",
   "<strong>Process optimization.</strong> Throughput, yield, cleaning, and reliability improvements on existing lines: CIP flow-path redesign, dosing accuracy, instrumentation, and spare-parts and maintenance strategy.",
   "<strong>Startup and stabilization.</strong> Support through engineering runs, first GMP batches, punch closure, and performance review after handover.",
  ],
  process="A transfer engagement starts with the fit-gap assessment, which produces a scored gap list, a modification scope, and an estimate — usually within a few weeks. Modifications are then executed through design, construction, and <a href=\"/capabilities/cqv/\">CQV</a> like any other capital work, and we stay through engineering and demonstration runs until the process is stable. Optimization work follows the same pattern at smaller scale: measure, diagnose, modify, verify.",
  deliv=["Facility fit-gap assessment &amp; scored gap list","Scale-up calculations &amp; critical process parameters","Process &amp; utility demand analysis","Modification scope, estimate &amp; design","Startup &amp; stabilization support","Performance review &amp; lessons learned"],
  who="CDMOs receiving a client process; owners moving a process between sites or scales; sites converting to multi-product operation; production and engineering groups with a line that under-performs on yield, cleaning, or uptime.",
  why="We have scaled spray-drying processes to drive equipment design and project scope, redesigned solvent and cleaning systems for new products, and improved filling yield and dosing accuracy on operating lines — as the responsible engineer, from calculation through validated result.",
  faq=[
   ("What does a facility fit-gap assessment cover?", "Seven categories, at minimum: capacity (batch size, throughput, storage), utilities (steam, chilled water, WFI, gases, power), materials compatibility (product contact, solvents, gaskets), environmental classification and containment, cleaning and changeover strategy, automation and data, and documentation and qualification status. Each gap is scored for impact and effort and mapped to a closing action."),
   ("How long does a tech transfer take?", "It depends on the gaps. A process that fits the receiving facility can move in months; one that needs new solvent handling, a chiller, or a cleanroom modification is a capital project with design, construction, and CQV phases. The fit-gap assessment is what tells you which case you are in, early."),
   ("Do you support scale-up calculations?", "Yes — heat and mass balances, critical process parameters, nozzle and atomization sizing for spray drying, dryer sizing to residual-solvent targets, and utility demand at the new scale."),
   ("Can you help with an existing line that is underperforming?", "Yes. Optimization engagements follow the same measure-diagnose-modify-verify approach: we have redesigned CIP flow paths, resized dosing components, and specified instrumentation to recover yield and reliability on operating lines."),
  ],
  related=["engineering-design","cqv","project-engineering"], post="facility-fit-gap-assessment-tech-transfer"),
]

# ---- Industries ------------------------------------------------------------------------------
INDUSTRIES = [
 dict(title="Pharmaceutical", body="Oral solid dose, sterile fill-finish, inhalation, and API facilities operating under cGMP, where documentation rigor, contamination control, and inspection readiness shape every engineering decision."),
 dict(title="Biotechnology", body="Upstream and downstream bioprocessing on single-use and stainless platforms, and the clean utilities and controlled environments that support them."),
 dict(title="Advanced Manufacturing", body="High-precision, highly regulated production environments — including medical device manufacturing — where uptime, traceability, and controlled change are non-negotiable."),
]

# ---- General FAQ (home + /faq/) -------------------------------------------------------------
FAQ = [
 ("What industries does JCS Engineering serve?", "Pharmaceutical, biotechnology, and advanced manufacturing — regulated environments where engineering and compliance cannot be separated."),
 ("Where is JCS Engineering located, and where do you work?", "We are based in the Raleigh, North Carolina area and serve the Research Triangle and the state's biomanufacturing corridor — Raleigh, Durham, RTP, Cary, Holly Springs, Clayton, Sanford, Wilson, and Greenville — with on-site, remote, and hybrid engagements. Our principal has also delivered projects in Massachusetts."),
 ("Is JCS Engineering a licensed engineering firm?", "Yes. JCS Engineering PLLC holds North Carolina Engineering Firm License P-3451 with the North Carolina Board of Examiners for Engineers and Surveyors, and our principal, Drew Jones, is a licensed North Carolina Professional Engineer (No. 062483)."),
 ("Do you provide on-site support?", "Yes. We work on-site, remotely, or in a hybrid arrangement depending on the phase. Construction and CQV typically warrant a field presence; design review and planning often do not."),
 ("Can you act as an owner's representative?", "Yes. Owner's representation is a core service: we serve as your single point of contact across the design firm, contractors, vendors, and quality organization to safeguard project goals, budget, schedule, and compliance."),
 ("At what stage should we engage JCS Engineering?", "Any stage — from early site planning and design through CQV execution and post-project improvement. The earlier we are engaged, the more risk and cost we can design out before it becomes rework."),
 ("Do you work on both small and large capital projects?", "Yes. We have experience with targeted facility upgrades and with major site-wide expansion projects, and we scale the engagement to fit."),
 ("How are engagements structured?", "Around the project: a defined-scope deliverable, milestone oversight, a full program, or engineers and project managers embedded in your team. We recommend a structure after a first conversation about where the project stands."),
 ("How do you minimize disruption to operations?", "By combining GMP operations knowledge with careful scheduling and disciplined change management, we execute projects that align with production needs and minimize downtime."),
]

# ---- Standards -------------------------------------------------------------------------------
STANDARDS = [
 ("Regulatory &amp; Quality", [("21 CFR Parts 210 &amp; 211","Current GMP for finished pharmaceuticals"),("21 CFR Part 11","Electronic records &amp; signatures"),("EU GMP Annex 1 &amp; Annex 15","Sterile manufacture · Qualification &amp; validation"),("ICH Q7 / Q8 / Q9 / Q10","API GMP · Development · Risk · Quality systems")]),
 ("Commissioning &amp; Qualification", [("ISPE Baseline Guide Vol. 5","Commissioning &amp; qualification"),("ASTM E2500","Specification, design &amp; verification of systems"),("ISPE GAMP 5","Computerized system validation"),("ISPE Baseline Guides Vol. 3 &amp; 4","Sterile facilities · Water &amp; steam systems")]),
 ("Mechanical &amp; Process Design", [("ASME BPE","Bioprocessing equipment"),("ASME B31.3","Process piping"),("ASME BPVC Section VIII","Pressure vessels"),("API 520 / 521","Pressure-relief sizing &amp; selection")]),
 ("Facilities, Safety &amp; Automation", [("ISO 14644","Cleanrooms &amp; controlled environments"),("NFPA 30 / 70 / 497","Flammable liquids · NEC · Classified areas"),("ASHRAE","HVAC design for controlled environments"),("ISA-5.1 / ISA-88 / ISA-95","P&amp;ID symbology · Batch · Enterprise integration")]),
]

# ---- Experience (team roles in industry; no employer names, no dates, per owner) -----------
EXPERIENCE = [
 dict(meta=["Oral Solid Dose · Spray Drying","Boston, MA"], hl="$25M Capital Expansion", slug="spray-drying-facility-expansion",
  title="Single-product site to multi-product spray-drying facility",
  role="Responsible engineer and senior project manager — full design scope, construction, qualification, and handover",
  summary="Led a facility-wide expansion converting a single-product site into a multi-product oral solid dispersion spray-drying facility. Owned the process flow diagrams, P&amp;IDs, and specifications for solvent handling, spray drying, and vacuum drying; the environmental permit revisions (Massachusetts DEP air emissions, MWRA water discharge); construction administration; and IQ/OQ execution through handover to operations for client scale-up runs.",
  scope=["<strong>Spray dryer retrofit.</strong> Redesigned an ethanol-based system for dichloromethane and methanol: solvent vapor loads, full gasket material-compatibility review, new cyclone for particle collection, PSV re-evaluation, and a new condenser sized to recirculation conditions.",
         "<strong>Solvent system expansion.</strong> New delivery platforms and skids for methanol, DCM, and acetone — high-pressure feed pumps, line sizing to hold target particle size through pressure nozzles, and a multi-solvent manifold to multiple formulation tanks.",
         "<strong>Process chiller &amp; HVAC.</strong> Designed and qualified a –40&nbsp;°C process chiller and a new chiller to cover cleanroom expansion and water-cooled equipment beyond existing 4&nbsp;°C capacity.",
         "<strong>Process design &amp; scale-up.</strong> Heat and mass balances and critical process parameters for spray-drying scale-up; nozzle sizing and atomization; 250&nbsp;L and 1,000&nbsp;L vacuum dryers designed to residual-solvent specifications.",
         "<strong>Cleanroom buildout.</strong> HVAC for ISO-classified suites — air changes, pressure cascades, equipment load impacts — integrated with chilled water and process utilities and verified at commissioning.",
         "<strong>Executive reporting.</strong> Managed and presented multiple capex budgets, forecasts, and schedules to site and executive leadership."],
  tags=["Concept","Design","Procurement","Construction","CQV","Handover","Permitting","Tech Transfer"]),
 dict(meta=["Inhalation · Sterile Fill-Finish","Morrisville, NC"], hl="Lead Engineer", slug="mdi-microvial-programs",
  title="Metered-dose inhaler and microvial programs",
  role="Automation &amp; process engineer — design, capex, FAT/SAT/IOQ, and reliability",
  summary="Engineering design for capital projects in a cGMP inhalation and sterile manufacturing environment, from user and functional requirements through commissioning and qualification. Designed mechanical and process systems including pressure vessels, formulation tanks, filling systems, CIP skids, and fluid-transfer systems, with process calculations for flow, pressure, pump capacity, valve sizing, and instrumentation.",
  scope=["<strong>MDI inspection system ($2M+ capex).</strong> Lead engineer for a canister leak-detection system: calculated acceptable leak rates over a 14-day hold and designed a continuous weigh-cell inspection system resolving sub-gram mass change — proposal, specification, installation, and validation to FDA requirements.",
         "<strong>MDI system optimization.</strong> Redesigned CIP flow paths and spray coverage with cleaning flow-rate and pressure-loss calculations verified by field samples; improved dosing accuracy by sizing new check valves, diaphragm pumps, and regulators; specified and ranged formulation-tank flow meters.",
         "<strong>Microvial filling &amp; inspection.</strong> Wrote filling and inspection specifications and executed FAT, SAT, and IOQ, verifying fill-volume precision and inspection reject rates against design criteria for release into GMP production.",
         "<strong>Automation &amp; reliability.</strong> Automation lead for the site historian, manufacturing OT network, and equipment HMI directory integration; reliability champion for spares, CMMS upgrades, and PM standards."],
  tags=["Design","Procurement","Construction","CQV","Automation","Reliability"]),
 dict(meta=["Biologics · Drug Substance &amp; Drug Product","Holly Springs, NC"], hl="CQV Lead", slug="biologics-site-startup",
  title="Large-scale biologics site startup",
  role="CQV lead (contract) — multidiscipline process, automation, I&amp;C, and mechanical team",
  summary="Led drug substance and drug product CQV on a large-scale biologics manufacturing site: protocol execution for aseptic drug product filling lines and automated visual inspection, upstream process CQV, and startup of the site's black utilities — chilled water, soft water, heating hot water, steam, and potable water — across the central utilities and drug substance buildings. Mechanical-completion walkdowns to classify punch criticality and drive closure and escalation for contractor handover.",
  scope=["<strong>Drug product.</strong> Aseptic filling lines and automated visual inspection through commissioning and qualification.",
         "<strong>Black utilities.</strong> Central utility plant and building-level systems started up and turned over as the foundation for process qualification.",
         "<strong>Upstream.</strong> Drug substance upstream systems through CQV.",
         "<strong>Handover.</strong> Punch classification, closure tracking, and escalation from mechanical completion to owner acceptance."],
  tags=["Construction","CQV","Utilities","Handover"]),
 dict(meta=["API · Fermentation, Recovery &amp; Purification","Clayton, NC"], hl="Project Manager", slug="api-site-capital-program",
  title="API site capital program",
  role="Project manager — formulation, recovery, and purification steering group",
  summary="Responsible project manager reporting to the formulation, recovery, and purification steering group with lifecycle reporting across the portfolio. Managed construction and commissioning of clean steam generators to reduce TOC to main fermentation, and led automation design and electrical construction for automated pH calibration in recovery and purification.",
  scope=["<strong>Clean steam generators.</strong> Construction and commissioning, targeting TOC reduction to fermentation.",
         "<strong>Automated pH calibration.</strong> Automation design and electrical construction through recovery and purification.",
         "<strong>Governance.</strong> Steering-group reporting and lifecycle tracking across concurrent projects."],
  tags=["Design","Construction","Commissioning","Automation","Governance"]),
 dict(meta=["Sterile Injectables &amp; Industrial Biotech","Rocky Mount &amp; Franklinton, NC"], hl="Process Engineering", slug="aseptic-processing-continuous-improvement",
  title="Aseptic processing and continuous improvement",
  role="Aseptic process engineer · Process engineer",
  summary="Foundational operations experience in two very different regulated environments: sterile injectable filling under isolator and traditional aseptic conditions, and large-scale enzyme formulation.",
  scope=["<strong>Aseptic qualification.</strong> Performed 20 media-fill simulations and 4 smoke-profile studies across aseptic and isolator sterile injectable lines; led technical sterility-assurance change controls.",
         "<strong>Operator interventions.</strong> Process improvements establishing 30 new qualified interventions for isolator filling lines.",
         "<strong>Continuous improvement.</strong> Led improvement of enzyme formulation tanks, cutting annual defects from 60% to 5%; built and delivered historian training for engineers, supervisors, and managers."],
  tags=["Operations","Sterility Assurance","Change Control","Continuous Improvement"]),
]

# ---- Service-area hubs -------------------------------------------------------------------------
HUBS = [
 ("Raleigh &amp; Wake County", "Home base. Raleigh, Cary, Apex, Garner, Knightdale, Wendell, Zebulon, Wake Forest, and Morrisville — the corporate, engineering, and contractor community that plans and staffs the region's capital projects, and the location of the state's engineering licensing board. On-site engagements anywhere in Wake County are a same-day drive."),
 ("Durham &amp; Research Triangle Park", "The original life-sciences cluster: pharmaceutical development and manufacturing, contract development and manufacturing organizations, and the research institutions that feed them. Projects here are often modifications and expansions inside operating facilities, where construction sequencing around production matters as much as the design."),
 ("Holly Springs", "One of the fastest-growing biologics manufacturing locations in the country, with large-scale drug substance and drug product campuses under construction and in startup. Demand here is for CQV leadership, black-utility and process-system startup, and owner-side project engineering at scale."),
 ("Clayton &amp; Johnston County", "A major pharmaceutical API and finished-product manufacturing concentration, with continuous capital programs across fermentation, recovery, purification, formulation, and filling. Work here is typically brownfield: steering-group governance, utilities, automation, and commissioning inside a running site."),
 ("Sanford, Wilson &amp; Greenville", "Vaccine, biologics, and sterile-injectable manufacturing along the corridor east and south of the Triangle. Greenfield builds and major expansions in these locations need embedded project engineers and CQV teams for defined program durations."),
]

# ---- Insights posts (metadata; bodies in tools/posts.py) ------------------------------------
POSTS = [
 dict(slug="owners-engineer-pharmaceutical-capital-project",
      title="What an Owner's Engineer Does on a Pharmaceutical Capital Project — and When to Bring One In",
      page_title="Owner's Engineer on Pharma Projects",
      meta="What an owner's representative does on a pharma or biotech capital project, phase by phase, how the role differs from the CM and A/E, and when it pays off.",
      date="2026-09-08", modified="2026-09-08", minutes=7, services=["project-engineering","construction-oversight"],
      excerpt="Every party on a capital project has a contract to protect. An owner's engineer is the one whose only interest is yours. Here is what the role covers, phase by phase, and how to know when you need one."),
 dict(slug="cqv-planning-starts-in-design",
      title="CQV Planning Starts in Design: Keeping Qualification Off the Critical Path",
      page_title="CQV Planning Starts in Design",
      meta="Why CQV slips on pharma projects, and the design-phase decisions — impact assessments, traceability, FAT strategy — that keep it off the critical path.",
      date="2026-09-08", modified="2026-09-08", minutes=8, services=["cqv","engineering-design"],
      excerpt="Qualification is usually the last thing to start and the first thing blamed for a late startup. Most of the delay was decided months earlier, during design. Here is how to decide it differently."),
 dict(slug="facility-fit-gap-assessment-tech-transfer",
      title="Facility Fit-Gap Assessment for Tech Transfer: A Working Checklist",
      page_title="Facility Fit-Gap Assessment Checklist",
      meta="A working checklist for assessing whether a receiving facility fits an incoming pharma process: seven gap categories, how to score them, and common surprises.",
      date="2026-09-08", modified="2026-09-08", minutes=8, services=["optimization-tech-transfer","engineering-design"],
      excerpt="Tech transfer fails on the gaps nobody assessed: a gasket, a utility, a room classification. This checklist is the one we work through before a process moves anywhere."),
]

HUB_PAGES = [
 dict(slug="holly-springs", name="Holly Springs", page_title="Engineering Firm for Holly Springs NC", h1="Engineering and CQV Services for Holly Springs, North Carolina",
  meta="Project engineering, construction oversight and CQV for the large-scale biologics manufacturing campuses being built and started up in Holly Springs, NC.",
  drive="about 25 minutes from our Raleigh office",
  what=["Holly Springs has become one of the most concentrated biologics manufacturing build-outs in the country. The work here is greenfield and large: drug substance and drug product campuses with their own central utility plants, warehouses, and quality laboratories, moving through construction, mechanical completion, and startup at the same time.",
        "That profile generates a particular kind of demand. Owners need people who can walk down hundreds of systems as they approach mechanical completion, classify punch items by criticality, start up black utilities in the right order so process CQV isn't waiting on steam or chilled water, and run multidiscipline qualification teams — process, automation, instrumentation, mechanical — through drug substance, filling, and inspection systems."],
  services=[("cqv","CQV leadership and execution across drug substance, drug product filling and inspection, and site utilities"),
            ("construction-oversight","Mechanical-completion walkdowns, punch classification and closure, turnover package review"),
            ("project-engineering","Owner-side project engineering and embedded project managers for the duration of a program"),
            ("engineering-design","Design review and modification packages for utilities, process systems and cleanroom HVAC")],
  faq=[("Do you have experience with large-scale biologics site startups?","Yes. Our principal has led drug substance and drug product CQV — aseptic filling lines, automated visual inspection, upstream systems, and site-wide black utilities including chilled water, soft water, heating hot water, steam and potable water — on a large-scale biologics manufacturing site in Holly Springs."),
       ("Can you provide a CQV lead or team on site for the length of a startup?","Yes. Engineers, CQV leads, and project managers can be embedded in your organization for a defined program period, working your procedures and reporting lines under our firm's PE-led accountability."),
       ("How quickly can you be on site?","Holly Springs is roughly 25 minutes from our Raleigh office; same-day site presence is routine.")]),
 dict(slug="clayton", name="Clayton", page_title="Engineering Firm Serving Clayton, NC", h1="Engineering and Project Management Services for Clayton and Johnston County",
  meta="Owner-side project management, utilities, automation and commissioning for API and finished-product pharmaceutical manufacturing in Clayton, NC.",
  drive="about 30 minutes from our Raleigh office",
  what=["Clayton and Johnston County hold one of the largest pharmaceutical manufacturing concentrations in the Southeast: API production by fermentation, recovery and purification, alongside formulation and finished-product filling. Unlike a greenfield campus, these are mature, operating sites with continuous capital programs — a portfolio of concurrent projects governed by steering groups and executed inside a running plant.",
        "Work here is brownfield by nature. Clean utility upgrades, automation and electrical modifications, equipment replacements, and capacity additions all have to be designed, built, and commissioned around production, with shutdown windows negotiated and change control feeding the site's quality system. Governance and reporting matter as much as engineering: leadership wants to see a portfolio, not a pile of projects."],
  services=[("project-engineering","Project management and lifecycle reporting for steering-group governed portfolios"),
            ("construction-oversight","Construction and commissioning coordination inside an operating site, sequenced around production"),
            ("change-risk-compliance","Project change control and risk registers that connect to site quality systems"),
            ("engineering-design","Utility, automation and process modification design — clean steam, pH control, tie-ins")],
  faq=[("Have you worked on an operating API site?","Yes. Our principal served as project manager on an API site in Clayton, reporting to the formulation, recovery and purification steering group — managing construction and commissioning of clean steam generators and leading automation and electrical work for automated pH calibration in recovery and purification."),
       ("How do you handle projects inside a running plant?","As controlled activities: shutdown planning, tie-in sequencing, containment and pressure-cascade controls, daily communication with production and quality, and every change through change control. See how we approach construction oversight."),
       ("Do you support portfolio-level reporting?","Yes — steering-group packages, lifecycle tracking across concurrent projects, and budget and schedule forecasts for site and executive leadership.")]),
 dict(slug="durham-rtp", name="Durham &amp; Research Triangle Park", page_title="Engineering Firm Serving Durham &amp; RTP", h1="Engineering Services for Durham and Research Triangle Park Life-Sciences Facilities",
  meta="Project engineering, design, construction oversight and CQV for pharmaceutical development and manufacturing facilities in Durham and Research Triangle Park.",
  drive="about 20 minutes from our Raleigh office",
  what=["Durham and Research Triangle Park are the original life-sciences cluster in North Carolina: pharmaceutical development and manufacturing, contract development and manufacturing organizations, inhalation and sterile fill-finish operations, and the research institutions that feed them. Facilities here span decades of construction, which means most capital work is modification and expansion inside existing cGMP space.",
        "That makes the engineering problems specific: fitting a new product into an existing suite, adding an inspection system to a running line, redesigning CIP flow paths to recover yield, reranging instrumentation for a new process, or integrating a site historian and OT network without disrupting batch records. Design, qualification, and operations have to be planned together, because there is no empty building to work in."],
  services=[("engineering-design","Process and mechanical design for modifications, equipment integration and utility upgrades"),
            ("optimization-tech-transfer","Facility fit-gap assessments and tech transfer into existing suites; CIP and dosing optimization"),
            ("cqv","FAT, SAT and IQ/OQ for filling, inspection, formulation and utility systems"),
            ("project-engineering","Owner's representation for expansions and capital programs at operating sites")],
  faq=[("What kind of projects have you done in the Durham–RTP area?","Our principal's experience in the Triangle includes inhalation and sterile fill-finish work in Morrisville — an MDI inspection-system capital project, CIP and dosing optimization, microvial filling and inspection qualification, and site historian and OT network integration — plus aseptic processing and industrial biotechnology roles elsewhere in the region."),
       ("Can you support a CDMO receiving a new client process?","Yes. A facility fit-gap assessment is the first step: capacity, utilities, materials compatibility, classification, cleaning, automation and qualification status, scored and turned into a modification scope and estimate."),
       ("Do you work on-site in RTP?","Yes — RTP and Durham are about 20 minutes from our Raleigh office. Design review and planning are often remote; construction, FAT/SAT and qualification warrant field presence.")]),
]

NAV = [("/", "Home"), ("/capabilities/", "Capabilities"), ("/approach/", "Approach"), ("/about/", "About")]
# Insights stays published (footer, home section, service pages) but is kept out of the primary nav by owner preference.
PUBLISH_EXPERIENCE = False   # owner: not public at this time. Set True to publish /experience/ and restore its links.

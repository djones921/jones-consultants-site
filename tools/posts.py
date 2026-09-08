# -*- coding: utf-8 -*-
"""Insights post bodies (HTML fragments). Metadata lives in siteconfig.POSTS. Keep to 800-1,200 words."""

POST_BODIES = {

"owners-engineer-pharmaceutical-capital-project": """
<p class="lede">Every party on a pharmaceutical capital project has a contract to protect. The architect-engineer wants the design accepted. The construction manager wants the schedule and the change orders. The equipment vendors want the skids shipped and the FAT signed. None of that is wrong — but none of it is your interest. An owner's engineer, or owner's representative, is the one party whose only interest is the owner's. Here is what the role actually covers, phase by phase, and how to know when you need one.</p>

<h2>The gap the role fills</h2>
<p>Most pharmaceutical and biotech owners do not keep a spare senior engineer on the payroll to run a capital project. When a project is approved, the work lands on someone whose day job is production support, or quality, or maintenance — people who are excellent at those jobs and who have never had to referee a dispute between a design firm and a contractor about whose scope a missing utility connection falls into.</p>
<p>The result is predictable. Design assumptions that nobody on the owner's side had time to challenge surface as RFIs, or as rework. Changes get absorbed quietly until they appear on the schedule. Qualification starts when construction ends, and the timeline doubles. Institutional knowledge about why decisions were made leaves with the contractor at closeout.</p>
<p>The owner's engineer exists to close that gap: a technically qualified person who reads every drawing, attends every meeting, and answers only to the owner.</p>

<h2>What the role covers, phase by phase</h2>
<h3>Concept and front-end design</h3>
<p>This is where the role earns the most for the least, because the cheapest change on any project is the one made before drawings exist. The owner's engineer translates operational and quality needs into a <a href="/capabilities/engineering-design/">user requirement specification and basis of design</a> that the A/E can actually design against, pressure-tests the concept for constructability and GMP flows, and makes sure the capital request carries a credible estimate and a defensible contingency.</p>
<h3>Detailed design</h3>
<p>Owner-side review at each design milestone: does the design meet the URS, is it qualifiable, is it maintainable, does it stay inside the budget? The owner's engineer also starts the commissioning and qualification planning here — impact assessments, traceability — because <a href="/insights/cqv-planning-starts-in-design/">CQV that starts in design</a> is the single largest schedule lever on the project.</p>
<h3>Procurement</h3>
<p>Technical bid evaluation, clarification management, and factory acceptance test planning. The owner's engineer makes sure long-lead equipment is sequenced against the schedule rather than discovered on site, and that FAT is treated as a qualification lever, not a formality.</p>
<h3>Construction</h3>
<p>Field presence. Submittal and RFI flow, progress verification against pay applications, change order review for scope, cost, and compliance impact, and — critically inside an operating facility — sequencing construction so production is not collateral damage. See <a href="/capabilities/construction-oversight/">construction administration and oversight</a>.</p>
<h3>Commissioning, qualification, and handover</h3>
<p>The same engineer who reviewed the design now verifies that it was built and that it works, coordinating with the quality unit so the handover package stands up to inspection and operations can run the system on day one.</p>

<h2>Owner's engineer versus construction manager versus A/E</h2>
<p>The three roles are often confused, and the confusion is expensive.</p>
<ul>
<li><strong>The architect-engineer</strong> produces the design and, under most contracts, provides construction-phase services limited to answering RFIs and reviewing submittals against their own drawings. They are not paid to question whether the design was the right one.</li>
<li><strong>The construction manager</strong> delivers the contract: the scope as drawn, on the schedule as agreed, at the cost as bid. Changes are revenue. Their incentive to challenge a design gap that produces a change order is limited.</li>
<li><strong>The owner's engineer</strong> has no stake in the design fee or the construction contract. Their job is to ask the questions nobody else is paid to ask — and to write down the answers so the record survives the project.</li>
</ul>
<p>A good CM and a good A/E make an owner's engineer's job easier, not unnecessary. The roles are complementary.</p>

<h2>When it pays for itself</h2>
<p>The economics are simple on projects above a few million dollars: a single avoided change order, a single month recovered from the qualification schedule, or a single avoided production shutdown covers the cost of the role many times over. The situations where the case is strongest:</p>
<ul>
<li>Capital is approved but there is no internal engineer with the bandwidth to own the project.</li>
<li>The project is inside or adjacent to an operating GMP facility, where the cost of disruption is measured in batches.</li>
<li>Multiple vendors and firms have scopes that must interlock — process skids, utilities, automation, cleanroom.</li>
<li>Leadership wants independent verification of the A/E and contractor.</li>
<li>A project has drifted and needs an honest reset.</li>
</ul>

<h2>What to look for</h2>
<p>Licensure and a licensed firm behind it. Experience on the <em>owner's</em> side, not only the contractor's or designer's — the instincts are different. Phase coverage: someone who has actually executed IQ/OQ will design differently than someone who has only drawn P&amp;IDs. Documentation habits, because the decision log is half the value. And a staffing model that fits: a single embedded engineer for a targeted upgrade, a coordinated team for a site-wide program.</p>
<p>If that describes what your next project needs, <a href="/contact/">tell us where it stands</a>. A first conversation is technical, not commercial: where the project is, what is at risk, and whether we are the right fit.</p>
""",

"cqv-planning-starts-in-design": """
<p class="lede">On most late pharmaceutical projects, commissioning, qualification, and validation is the last thing to start and the first thing blamed. The blame is misplaced. By the time protocols are being executed, most of the delay was decided months earlier — during design, when nobody was thinking about qualification at all. Here is how to decide it differently.</p>

<h2>Why CQV slips</h2>
<p>Qualification verifies that a system meets its requirements. That sentence contains two dependencies people routinely underestimate: there have to <em>be</em> requirements written in a testable way, and the design has to be traceable to them. When the URS is vague, the protocol author has to invent acceptance criteria and then negotiate them with quality. When the design has drifted from the URS without anyone recording why, the IQ finds discrepancies that are not deviations but look like them, and every one takes a meeting to close.</p>
<p>Layer on the practical problems — mechanical completion declared with hundreds of open punch items, FAT reports that cannot be leveraged because nobody planned to leverage them, a traceability matrix built after the fact — and the qualification phase absorbs every upstream failure of discipline. It is not slow. It is where the bill comes due.</p>

<h2>Decision one: write the URS to be tested</h2>
<p>Every user requirement should be a statement that a test can pass or fail. "The vessel shall be cleanable" is not a requirement; "the vessel shall be drainable to less than 100 mL residual and all product-contact surfaces shall be reachable by CIP spray coverage, verified by riboflavin test" is. The quality unit should co-author or approve the URS, because they will approve the protocols that verify it. A URS written this way is the first row of the traceability matrix, and it costs almost nothing compared with what it saves. See how we approach <a href="/capabilities/engineering-design/">requirements and basis of design</a>.</p>

<h2>Decision two: do the impact assessment during design, not after</h2>
<p>The system impact assessment — which systems are direct-impact, indirect, or no-impact on product quality — and the component criticality assessment determine what gets qualified and how deeply. Done during design, they let you right-size the qualification scope, decide whether ASTM E2500 risk-based verification or traditional IQ/OQ/PQ fits each system, and identify which design decisions (a shared utility header, an uncontrolled room, a non-sanitary valve) would drag a system into a higher qualification tier for no operational benefit. Done after construction, they can only describe the scope you are already stuck with.</p>

<h2>Decision three: treat FAT as a qualification lever</h2>
<p>A factory acceptance test is the cheapest place to find a problem: the vendor's shop, with the vendor's technicians, before shipping. It is also, if your quality system allows it and the protocol is written for it, a legitimate source of qualification evidence — instrument calibration, weld documentation, material certificates, functional tests that do not depend on site utilities. Planning FAT during procurement with the qualification protocol in mind can remove weeks from IQ and OQ. Planning it as a formality guarantees you repeat the work on site.</p>

<h2>Decision four: run commissioning alongside mechanical completion</h2>
<p>Commissioning — the engineering verification that a system is installed and functions as designed — is where problems should be found and fixed, under engineering control, before protocols are executed under quality control. Sites that wait for a contractor to declare mechanical completion and then begin commissioning discover the punch list twice. Sites that walk down systems as they approach completion, classify punch items by criticality, and start pre-commissioning on complete subsystems arrive at qualification with systems that actually work.</p>

<h2>Decision five: build the traceability matrix from day one</h2>
<p>A requirements traceability matrix maps each URS line to the design element that satisfies it and the test that verifies it. Built from the URS forward, it is a project management tool: it shows which requirements are not yet designed for, which tests are not yet written, and which changes have orphaned a test. Built backward from finished protocols, it is a compliance artifact that proves nothing except that someone had a spreadsheet. The difference is entirely a matter of when you start.</p>

<h2>A phase-by-phase checklist</h2>
<ul>
<li><strong>Concept:</strong> identify the quality unit's CQV expectations and the site's qualification approach (E2500 or IQ/OQ/PQ); name a CQV lead now.</li>
<li><strong>Front-end design:</strong> URS written to be tested and approved by quality; preliminary system impact assessment; traceability matrix started.</li>
<li><strong>Detailed design:</strong> component criticality assessment; design qualification review against the URS; C&amp;Q plan and test strategy approved; FAT strategy defined per system.</li>
<li><strong>Procurement:</strong> FAT protocols written to leverage into IQ/OQ; vendor documentation requirements in the purchase order; SAT scope defined.</li>
<li><strong>Construction:</strong> systems walked down as they approach completion; punch items classified; pre-commissioning on complete subsystems; protocol authoring in parallel.</li>
<li><strong>CQV:</strong> execution against approved protocols with deviations managed under quality; turnover packages assembled system by system, not at the end.</li>
</ul>

<h2>The organizational fix</h2>
<p>Every item on that list is easy to agree with and hard to do, because it requires someone whose job spans design, construction, and qualification to own it across all three. In most owner organizations that person does not exist; design belongs to engineering, construction to the project manager, and qualification to validation. The fix is a role — an <a href="/insights/owners-engineer-pharmaceutical-capital-project/">owner's engineer</a> or a CQV lead engaged from design — that carries the thread. Our <a href="/capabilities/cqv/">CQV services</a> are built on exactly that premise: qualification is planned from the first design review, because we have seen what happens when it starts when construction ends.</p>
<p>If a project of yours is heading into design, or already in it, <a href="/contact/">this is the moment to talk</a>.</p>
""",

"facility-fit-gap-assessment-tech-transfer": """
<p class="lede">Technology transfer fails on the gaps nobody assessed: a gasket that was never rated for the new solvent, a chiller that was already at capacity, a room whose classification the layout change quietly broke. A facility fit-gap assessment is the structured comparison of the incoming process against the receiving facility that finds those gaps while they are still cheap. This is the checklist we work through before a process moves anywhere.</p>

<h2>What "fit" actually means</h2>
<p>A process fits a facility when the facility can run it at the intended scale, to the intended quality, under the intended controls, without a change that would itself require design, construction, or qualification. Anything short of that is a gap — and gaps are not failures; they are the scope of the transfer project. The purpose of the assessment is to enumerate them, score them, and turn them into a plan and an estimate before anyone commits a start date.</p>
<p>The assessment needs two inputs: a complete description of the incoming process (batch records, process parameters, equipment list with materials of construction, utility demands, cleaning procedures, environmental requirements) and an honest description of the receiving facility, including what is actually available rather than what the design basis said ten years ago.</p>

<h2>The seven gap categories</h2>
<h3>1. Capacity</h3>
<p>Batch size against vessel volumes and working ranges. Throughput against line rates and shift patterns. Storage — raw material, intermediate, finished — against warehouse and cold-chain capacity. Hold times against available tankage. The most common surprise here is a vessel that is nominally large enough but whose minimum working volume is above the incoming batch size.</p>
<h3>2. Utilities</h3>
<p>Steam, chilled water, heating hot water, WFI, purified water, clean steam, compressed air, process gases, nitrogen, power, and drain capacity — each compared against the incoming demand <em>at peak, concurrently with everything else the facility runs</em>. Utility gaps are expensive to close and slow to build. A –40&nbsp;°C process step arriving at a site with only 4&nbsp;°C chilled water is a capital project, not a transfer.</p>
<h3>3. Materials compatibility</h3>
<p>Every product-contact and solvent-contact material — vessel and piping alloys, gaskets, diaphragms, hoses, filter housings, tubing — checked against the incoming process's solvents, pH, temperature, and cleaning agents. Changing a process from ethanol to dichloromethane, for instance, requires a full gasket review across every system the solvent touches, and the answer is frequently that dozens of components need to change.</p>
<h3>4. Environmental classification and containment</h3>
<p>Room grades, pressure cascades, air changes, and containment strategy against what the incoming process requires. Potent compounds, solvents that create classified electrical areas, and open-processing steps all have facility consequences that a layout drawing does not show. Check the classified-area boundaries against NFPA requirements if solvents are involved, and check HVAC capacity against any new equipment heat load.</p>
<h3>5. Cleaning and changeover</h3>
<p>The incoming process's cleaning procedure against the facility's CIP and COP capabilities, spray-device coverage, drainability, and cleaning validation status. In a multi-product facility, the changeover strategy and cross-contamination controls between the incoming product and everything else on site. Cleaning gaps often surface as yield problems months after transfer.</p>
<h3>6. Automation and data</h3>
<p>Control system capability against the incoming recipe: phases, parameters, alarms, and data requirements. Historian and batch-record integration. 21 CFR Part 11 status of any system that will hold GMP data. Instrument ranges against the incoming process parameters — a flow meter ranged for one product is often wrong for the next.</p>
<h3>7. Documentation and qualification status</h3>
<p>The current qualification status of every system the process will touch, and whether the incoming process parameters fall inside the qualified ranges. A system qualified for one operating envelope may need requalification — or only a documented assessment — for another, and the difference is weeks of schedule.</p>

<h2>Scoring and closing the gaps</h2>
<p>Each gap is scored for impact (does it block the transfer, degrade it, or merely complicate it) and for effort (procedure change, component change, equipment modification, or capital project). The scored list becomes the transfer scope. Procedure and component gaps close inside the transfer itself; equipment and utility gaps become <a href="/capabilities/engineering-design/">design</a> work with their own construction and <a href="/capabilities/cqv/">CQV</a> phases; and the estimate that comes out of the assessment is what the business uses to decide whether this facility is the right receiving site at all.</p>

<h2>The surprises that usually appear</h2>
<ul>
<li>A utility that is "available" on the design basis but already committed to another line at peak.</li>
<li>Gaskets and diaphragms rated for the outgoing solvent, not the incoming one.</li>
<li>A minimum working volume above the incoming batch size.</li>
<li>Instrumentation ranged for the previous product.</li>
<li>A classified-area boundary that moves when a new solvent is introduced.</li>
<li>Cleaning procedures that were never validated for the incoming product's residues.</li>
<li>An air-emissions or wastewater permit that does not cover the new solvent throughput.</li>
</ul>
<p>None of these is exotic. All of them are found by working the list.</p>

<h2>Who should run it</h2>
<p>The assessment needs someone who can read a batch record and a P&amp;ID, walk a utility plant, and ask the quality unit the right question about qualified ranges — and who has no stake in the answer being "it fits." That is usually not the sending site, which wants the process gone, or the receiving site's production team, which wants the business. It is engineering work, and it is the first thing we do in any <a href="/capabilities/optimization-tech-transfer/">tech transfer engagement</a>. If a process is heading your way, <a href="/contact/">the assessment is where to start</a>.</p>
""",
}

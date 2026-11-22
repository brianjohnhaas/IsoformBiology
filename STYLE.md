# Writing style

Two goals, and they pull against each other if you are careless. The prose
should read as though a working scientist wrote it, not as though a language
model produced it. And it should explain methodological machinery plainly enough
that a biologist who has never run a transcript assembler can follow the
argument.

The second goal is where most science writing turns into either condescension or
fog. The resolution here is structural: **the main read trusts the reader, and
the hand-holding lives in asides nobody is forced to open.** Never dilute a
chapter to accommodate the reader who needs more. Give that reader a door
instead.

## Voice

The book is written impersonally. No narrator, no "we", no "I". Claims are
attributed to the people who made them, and judgements the book itself makes are
stated as statements rather than as opinions held by someone.

Two reasons this was chosen over a collective "we", after writing a chapter both
ways. A collective voice asserts a consensus that a multi-author book does not
yet have, and it raises the bar for contribution, since a donated section then
has to sound like the book as well as being correct.

Impersonal prose drifts toward dry. That is its failure mode, and the first
draft of the animals chapter demonstrated it. Two rules hold it off, both
enforced by `scripts/check_style.py`:

**Keep sentences short, and keep them sentences.** Mean under 19 words, nothing
over 45, and nothing under seven either. The energy in good prose comes from
pace far more than from pronouns. Measured on the two drafts, dropping the mean
from 22.2 to 14.9 words did almost all the work that switching to "we" appeared
to do.

The lower bound was added later, and it matters as much as the upper
one. A chapter written to the mean alone drifts into four- and five-word
sentences placed for emphasis, and a run of those is the single most
recognisable mark of generated prose. "The transcripts did not change. The
question did." reads as a punchline rather than as a result. The two rules pull
against each other, and the way to satisfy both is to split a long sentence
rather than to manufacture a short one.

The lower bound does not apply to a
glossary cross-reference, a defined term standing as its own label, or an item
in a list of links. It applies to running prose.

**End sections on a claim, not
a summary.** A section that closes by restating what it just said has wasted its
most emphatic position. Close on the thing the book is willing to defend, as a
full sentence with its subject in it. "Forcing the splice choice has a large
phenotype, and tumours do not make the switch." is a verdict; "the defensible
statement is that forcing the choice has a phenotype" is the same verdict with a
hedge about who finds it defensible. Drop the hedge. A verdict needs no
narrator, only an author willing to stop qualifying.

What it must not become is
an aphorism. A paragraph that ends on a short, quotable, slightly paradoxical
line has bought emphasis it did not earn, and a chapter where most paragraphs
end that way reads as pattern rather than as argument. Fold the claim into the
sentence that carries the evidence.

This checker cannot see the last two rules.
A human has to.

See `chapters/02-animals.qmd` for the reference implementation.

## Who is reading

Assume a reader who is expert in some part of biology and not in others, and who
is probably not expert in sequencing methodology. That shape has a specific
consequence:

Do not explain their subject matter back to them. Nobody reading this book needs
isoforms defined late in the book, cells defined for a cell biologist, or reads
defined for someone who has generated them.

Do explain our machinery completely. Intron chains, FSM and ISM classification,
EM-based quantification, internal priming, template switching, read support
thresholds, PSI versus transcript-level estimates. Naming one of these is not
explaining it. A reader who cannot say what an intron chain is cannot evaluate a
claim that rests on one.

Getting this backwards fails in both directions. Explaining biology to
biologists patronises; name-dropping methodology obscures.

## Explain plainly

**Behaviour before name. Concept before token. Consequence before detail.**

A reader cannot hold an unfamiliar term in mind while also learning what it
does. Describe the thing happening in words they already have, then attach the
name to it as a label.

Find the one sentence that makes the rest follow, and lead with it. It usually
has two or three clauses and no jargon in it. For a chapter section on why short
reads cannot resolve isoforms, that sentence is close to: "You can see every
junction in the gene and still not know which junctions occurred in the same
molecule." The numbers that follow then land as confirmation rather than as the
argument itself.

Keep every number, and attach its meaning. "37% of detected transcripts used an
unannotated junction chain" is noise until the reader knows what counted as
detected and which annotation was the denominator. Then it is the point.
Dropping the number for simplicity and keeping it without its meaning are both
failures.

Analogies earn their place only when they map structurally, and you must say
where they stop mapping. The test: can the reader derive a new true statement
from the analogy? If not, cut it.

## Headings

**A heading does one of three jobs.** It names the thing the section is about,
where that thing has a name a reader would look for. It states the section's
claim, where the section has one. It asks the open question, where the section
reports a disagreement. Most good headings do the first and one of the others at
once: "Titin: splicing sets cardiac stiffness", "LZTR1 is inactivated by intron
retention".

This was the last part of the book nobody checked. Every gate strips headings
before it looks at anything, so for most of the project's life no rule reached
them, and the habits being removed from sentences sat untouched in the titles.
At the worst point 39 of 131 section headings opened with a Wh- word, "What"
alone began 18 of them, and a chapter title contained "we".

**Name the handle.** A reader who knows the field scans a sidebar for genes,
methods and consortia, and a heading that describes one without naming it hides
the section from the reader best placed to use it. This is the commonest defect
and it survived a first pass that fixed everything else, because a title can be
a perfectly good claim and still withhold the one word being looked for.

| Instead of | Write |
|---|---|
| Isoforms that set tissue mechanics | Titin: splicing sets cardiac stiffness |
| Isoform-level inactivation that exome sequencing cannot see | LZTR1 is inactivated by intron retention |
| Picking one transcript per gene | MANE and APPRIS: one transcript per gene |
| What benchmarking established | LRGASP: length for structure, depth for abundance |
| Where isoform differences actually sit | Most isoform differences sit at the transcript ends |
| Which chromosome the transcript came from | Phasing comes free with read length |
| Arrays | Arrays and the designed survey |

A bare label is right when the section surveys several findings about one named
thing: "Direct RNA sequencing", "Fungi", "STMN2". It is wrong when the label is
the whole topic of the chapter's argument and the section has a verdict it could
carry, which is what was wrong with "Arrays" and "Therapeutics".

**Do not promote the section's first sentence into its heading.** The reader
meets it twice in two lines. Moving the closing verdict up is a different move
and is encouraged.

**A claim has to say something a reader could disagree with.** "Decides",
"predicts", "records", "does work", "settles" and "moved" make a heading
claim-shaped without telling anyone what was found. Prefer the finding itself,
at the strength of its record and no stronger.

A claim in a heading is still a claim. Check it against the section's records
like any sentence, because `check_citations.py` blanks headings and will not.
Keep quantities out of headings as digits for the same reason; a gene symbol
that contains a digit, such as RPS24, CD45 or TDP-43, is a name and is fine.

**Keep the question where the section is genuinely open.** "How much of this is
functional", "Whether any of this tracks complexity" and "Does one cell use one
isoform or several" are the honest titles for sections reporting a live
disagreement, and turning them into assertions would misrepresent the evidence.
`check_style.py` therefore caps Wh- openers per chapter rather than banning them,
and caps any one repeated opening word. A cap is harder to game than a ban: a
forbidden "What X cannot do" just becomes "The things X cannot do".

Two more rules the checker enforces on headings, because they are the prose
rules and there was never a reason headings escaped them: no first person, no
banned vocabulary, no em dash.

Four rules it cannot enforce, so they need a human:

**Watch for a repeated shape as well as a repeated first word.** Sixteen
headings were once built as "X that Y cannot see", and chapter 6 carried two
ending in the same three words. The checker counts opening words and cannot see
a template.

**Keep siblings in one register, and use a parallel form on purpose where the
chapter is a list.** Chapter 2 is a sequence of cases and runs "Gene: what it
shows" throughout; chapter 4 is a sequence of methods and runs "Method and what
it gave". Both are deliberate ladders. Elsewhere, do not let the colon form
spread. If three subsections under a heading are claims, the fourth should not be
a bare noun, and a matched pair can be short, as "The five-prime leader" and "The
three-prime tail" are, provided both are.

**Do not open a heading with a comma-tail.** "Tau, and a ratio that has to be
held" and "ESTs, and the first genome-scale numbers" are the heading form of the
rhythm tic the prose rules already forbid, and dropping the comma usually fixes
them outright.

**Read a chapter's headings as a list before calling it done**, the way a reader
meets them in the sidebar. Most of the defects above are invisible one heading at
a time and obvious in a column. Keep a heading short enough not to wrap there,
which is about fifty characters; the sidebar adds a section number in front of
it.

A retitle is display text only. Never change a `{#sec-...}` identifier to match
a new title: cross-references point at the identifier, and the filenames and
identifiers in this book already record history rather than reading order.

## AI tells to avoid

These are the patterns that make prose read as generated. Most of them are
habits of emphasis, and the fix is usually to state the thing and stop.

Cut throat-clearing. No "Here's the thing", no "It's worth noting", no "In this
section we will explore". Begin with content.

Do not use the binary contrast. "Not X. Y." and "This isn't about X, it's about
Y" are the single loudest tell. State Y. Keep a negation only where X is a
position some source or some earlier chapter actually holds, so that the
sentence is correcting a real belief rather than staging a reveal.

Do not open a paragraph with an announcement of what it will contain. "Two
limitations are worth carrying forward.", "Three results are worth putting side
by side." and "The scale of the problem is measurable." all say nothing the
paragraph does not go on to say better. Start with the content.

Do not pair two sentences as mirror images. "A short read reports a fragment. A
long read reports a molecule." is one sentence pretending to be two, and the
same shape used twice in a chapter becomes conspicuous.

Do not address the reader. No "Take a gene nominated as
causal", no "The second row is worth sitting with", no "Keep this in mind".
Walkthroughs in `walkthroughs/` may use "you"; chapters may not.

Ration "rather
than", along with the forms a careless edit turns it into: "and not", ", not",
"instead of", "without doing X". Each is a useful contrast on its own and a tic
at ten to a chapter. Keep it where the rejected alternative is what a reader
would otherwise have assumed, and state the positive everywhere else.

Do not fragment for drama. "Speed. That's it. That's the tradeoff." Write the
sentence.

Do not pose a question and immediately answer it. "The result? Striking." Fold
it into a statement.

Avoid the magic adverbs and their cousins: quietly, simply, merely,
fundamentally, delve, leverage, landscape, ecosystem, tapestry, nuanced, robust
as a synonym for good. Domain terminology is different and welcome. "Intron
chain" is precise; "navigate the splicing landscape" is noise.

Avoid the participle tacked onto a sentence to editorialise: "...highlighting
the importance of isoform-level analysis", "...underscoring the need for further
study". Say the specific implication or say nothing.

No invented concept labels. Do not christen "the annotation paradox" and then
lean on it.

No stakes inflation. The case for isoform biology is strong enough on evidence;
it does not need "revolutionise" or "paradigm shift".

No em dashes. Use a comma, a period, or parentheses.

No bold-first bullets, where every list item opens with a bolded keyword. No
unicode arrows. No "In conclusion". No "Despite these challenges".

Vary rhythm. Mixed sentence lengths, two-item lists more often than three-item
ones, and paragraph endings that are not all punchy one-liners.

Prefer active voice with a named actor. "Kahles and colleagues found" beats "it
was found that". A judgement the book itself makes is stated as a statement,
without being attributed to a narrator.

Do not restate. One point per section, made once. No telling the reader what you
are about to say, saying it, then summarising it.

## Hand-holding: use the aside, not the main text

When a methodological point is genuinely worth understanding but not required to
follow the argument, put it in a collapsible aside. The main read stays tight
and the reader who wants depth gets it on demand.

For a short detour, use a collapsed callout:

```markdown
::: {.callout-note collapse="true"}
## How an intron chain is compared between two transcripts

Walk the sorted list of junction coordinates for each transcript and compare
them pairwise. Two transcripts share an intron chain when every internal
junction matches exactly, which means a difference of a single base at one
splice site makes them different chains. This is why novel-isoform counts
are sensitive to alignment quality.
:::
```

For anything longer than a few paragraphs, or anything a reader might want to
cite or link on its own, write a walkthrough in `walkthroughs/` and link to it
from the chapter in one sentence. Walkthroughs can be as patient and
step-by-step as the material needs, including worked numeric examples. That is
their job.

A chapter should read completely without opening a single aside. Check this by
reading it with all of them closed.

## Quality bar before marking a chapter done

Read it once with the asides closed, asking only whether the argument lands.

Then check for the tells: any binary contrast, any rhetorical question, any
sentence you could delete without losing information, any three consecutive
sentences of the same length, any em dash, any paragraph ending in a
manufactured punchline.

Then check the plain-description rule: does any section open on an unexplained
term, and is there a term a smart outsider to sequencing would not know, used
without a gloss?

Then confirm every number still carries its meaning and every claim still traces
to a record in `research/`.

Then read the headings on their own, as a list, and ask of each one whether it
states a claim or names an open question. A chapter can pass every mechanical
check and still have a sidebar that tells a reader nothing.

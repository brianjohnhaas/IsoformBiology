# Writing style

Two goals, and they pull against each other if you are careless. The prose should
read as though a working scientist wrote it, not as though a language model
produced it. And it should explain methodological machinery plainly enough that a
biologist who has never run a transcript assembler can follow the argument.

The second goal is where most science writing turns into either condescension or
fog. The resolution here is structural: **the main read trusts the reader, and the
hand-holding lives in asides nobody is forced to open.** Never dilute a chapter to
accommodate the reader who needs more. Give that reader a door instead.

## Who is reading

Assume a reader who is expert in some part of biology and not in others, and who
is probably not expert in sequencing methodology. That shape has a specific
consequence:

Do not explain their subject matter back to them. Nobody reading this book needs
isoforms defined in chapter 6, cells defined for a cell biologist, or reads
defined for someone who has generated them.

Do explain our machinery completely. Intron chains, FSM and ISM classification,
EM-based quantification, internal priming, template switching, read support
thresholds, PSI versus transcript-level estimates. Naming one of these is not
explaining it. A reader who cannot say what an intron chain is cannot evaluate a
claim that rests on one.

Getting this backwards fails in both directions. Explaining biology to biologists
patronises; name-dropping methodology obscures.

## Explain plainly

**Behaviour before name. Concept before token. Consequence before detail.**

A reader cannot hold an unfamiliar term in mind while also learning what it does.
Describe the thing happening in words they already have, then attach the name to
it as a label.

Find the one sentence that makes the rest follow, and lead with it. It usually has
two or three clauses and no jargon in it. For a chapter section on why short reads
cannot resolve isoforms, that sentence is close to: "You can see every junction in
the gene and still not know which junctions occurred in the same molecule." The
numbers that follow then land as confirmation rather than as the argument itself.

Keep every number, and attach its meaning. "37% of detected transcripts used an
unannotated junction chain" is noise until the reader knows what counted as
detected and which annotation was the denominator. Then it is the point. Dropping
the number for simplicity and keeping it without its meaning are both failures.

Analogies earn their place only when they map structurally, and you must say where
they stop mapping. The test: can the reader derive a new true statement from the
analogy? If not, cut it.

## AI tells to avoid

These are the patterns that make prose read as generated. Most of them are habits
of emphasis, and the fix is usually to state the thing and stop.

Cut throat-clearing. No "Here's the thing", no "It's worth noting", no "In this
section we will explore". Begin with content.

Do not use the binary contrast. "Not X. Y." and "This isn't about X, it's about Y"
are the single loudest tell. State Y.

Do not fragment for drama. "Speed. That's it. That's the tradeoff." Write the
sentence.

Do not pose a question and immediately answer it. "The result? Striking." Fold it
into a statement.

Avoid the magic adverbs and their cousins: quietly, simply, merely, fundamentally,
delve, leverage, landscape, ecosystem, tapestry, nuanced, robust as a synonym for
good. Domain terminology is different and welcome. "Intron chain" is precise;
"navigate the splicing landscape" is noise.

Avoid the participle tacked onto a sentence to editorialise: "...highlighting the
importance of isoform-level analysis", "...underscoring the need for further
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

Prefer active voice with a named actor. "Kahles and colleagues found" beats "it was
found that". Use "we" for judgements this book is making.

Do not restate. One point per section, made once. No telling the reader what you
are about to say, saying it, then summarising it.

## Hand-holding: use the aside, not the main text

When a methodological point is genuinely worth understanding but not required to
follow the argument, put it in a collapsible aside. The main read stays tight and
the reader who wants depth gets it on demand.

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

For anything longer than a few paragraphs, or anything a reader might want to cite
or link on its own, write a walkthrough in `walkthroughs/` and link to it from the
chapter in one sentence. Walkthroughs can be as patient and step-by-step as the
material needs, including worked numeric examples. That is their job.

A chapter should read completely without opening a single aside. Check this by
reading it with all of them closed.

## Quality bar before marking a chapter done

Read it once with the asides closed, asking only whether the argument lands.

Then check for the tells: any binary contrast, any rhetorical question, any
sentence you could delete without losing information, any three consecutive
sentences of the same length, any em dash, any paragraph ending in a manufactured
punchline.

Then check the plain-description rule: does any section open on an unexplained
term, and is there a term a smart outsider to sequencing would not know, used
without a gloss?

Then confirm every number still carries its meaning and every claim still traces
to a record in `research/`.

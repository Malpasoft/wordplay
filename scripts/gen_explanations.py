#!/usr/bin/env python3
"""
Generate missing EXPLANATIONS entries for worksheet.html files.
Handles A2, B1, B2, C1, C2 worksheets.
"""

import glob
import re
import sys

# ─── Grammar rule lookup by chapter name ───────────────────────────────────────

MODAL_DEFS = {
    "mustn't": "prohibition — it is <em>not allowed</em>",
    "don't have to": "no obligation — it is <em>not necessary</em>",
    "doesn't have to": "no obligation — it is <em>not necessary</em>",
    "have to": "external obligation — required",
    "has to": "external obligation — required",
    "must": "strong obligation or necessity",
    "should": "advice or recommendation",
    "ought to": "advice, similar to <em>should</em>",
    "had better": "strong advice — implies a warning",
    "shouldn't": "advice <em>against</em>",
    "needn't": "no necessity — not needed",
    "can't": "impossibility or prohibition",
    "could": "past ability or present possibility",
    "might": "weaker possibility",
    "may": "possibility or permission (formal)",
    "would": "hypothetical or habitual past",
    "used to": "past habit or state, no longer true",
    "both correct": "both options are grammatically correct here",
}

FUTURE_DEFS = {
    "will": "spontaneous decision, prediction, or promise",
    "'ll": "spontaneous decision, prediction, or promise",
    "is going to": "plan already made or prediction based on evidence",
    "are going to": "plan already made or prediction based on evidence",
    "is going to have to": "future obligation — evidence visible now",
    "will have to": "future obligation — no current evidence",
    "is checking in": "fixed future arrangement (present continuous for future)",
    "are meeting": "fixed future arrangement (present continuous for future)",
    "will continue": "prediction — no current evidence/plan",
    "'ll restart": "spontaneous offer/decision at moment of speaking",
    "'ll help": "spontaneous offer at moment of speaking",
    "'m going to take up": "decision already made before speaking",
    "'m going to restart": "plan already formed (wrong here — spontaneous offer)",
}

ADV_MANNER_RULE = (
    "Adverbs of manner modify verbs; most are formed by adding <strong>-ly</strong> to the adjective. "
    "<strong>{answer}</strong> is the adverb form."
)

COMPARATIVES_RULES = {
    "short": "one-syllable adjectives: add <strong>-er</strong>",
    "long": "two+ syllable adjectives: use <strong>more</strong> + adjective",
    "double": "short adjectives ending consonant-vowel-consonant: double the final consonant before <strong>-er</strong>",
    "irregular": "irregular comparative — must be learned: <strong>{answer}</strong>",
}

CONDITIONALS = {
    "zero": "Zero conditional: if + present simple → present simple (general/scientific truths).",
    "first": "First conditional: if + present simple → will (real/possible future situations).",
    "second": "Second conditional: if + past simple → would (hypothetical/unlikely).",
    "third": "Third conditional: if + past perfect → would have + pp (impossible — past).",
    "mixed": "Mixed conditional: past condition → present/future result.",
}


def make_explanation(chapter, q_text, answer, options):
    """Generate a concise explanation string (may contain HTML)."""
    wrong = [o for o in options if o != answer]
    w1 = wrong[0] if wrong else ""
    a = answer
    q = q_text

    # ── Adverbs of manner ────────────────────────────────────────────────────
    if "adverbs-manner" in chapter:
        adj_form = w1  # typically the adjective
        if a in ("well",):
            return (
                f"<strong>well</strong> is the irregular adverb of <em>good</em>. "
                f"Adverbs modify verbs — not adjectives."
            )
        if a.endswith("ily"):
            adj = a[:-3] + "y"
            return (
                f"Adjectives ending in <strong>-y</strong> form adverbs with <strong>-ily</strong>: "
                f"<em>{adj}</em> → <strong>{a}</strong>."
            )
        if a.endswith("ly"):
            adj = a[:-2]
            return (
                f"Use the adverb <strong>{a}</strong> (not the adjective <em>{adj}</em>) "
                f"to modify the verb."
            )
        return (
            f"Adverbs of manner modify verbs. <strong>{a}</strong> is the correct adverb form here."
        )

    # ── Comparatives / superlatives ──────────────────────────────────────────
    if "comparatives" in chapter or "superlatives" in chapter:
        if a == "better":
            return "<strong>better</strong> is the irregular comparative of <em>good</em>."
        if a == "worse":
            return "<strong>worse</strong> is the irregular comparative of <em>bad</em>."
        if a == "farther" or a == "further":
            return f"<strong>{a}</strong> is an irregular comparative — must be learned."
        if a.endswith("er") and not a.startswith("more"):
            root = a[:-2]
            if len(root) <= 3 and root[-1] == root[-2]:
                return (
                    f"Short adjectives ending CVC double the final consonant: "
                    f"<em>{root[:-1]}</em> → <strong>{a}</strong>."
                )
            return (
                f"Short adjective: add <strong>-er</strong> to form the comparative — "
                f"<strong>{a}</strong>."
            )
        if a.startswith("more"):
            adj = a[5:]
            return (
                f"Longer adjective (2+ syllables): use <strong>more</strong> + adjective — "
                f"<strong>{a}</strong> (never <em>{adj}er</em>)."
            )
        return f"<strong>{a}</strong> is the correct comparative/superlative form here."

    # ── Conjunctions ────────────────────────────────────────────────────────
    if "conjunction" in chapter:
        conj_rules = {
            "and": "addition — joining similar ideas",
            "but": "contrast — opposing ideas",
            "or": "alternative — a choice between options",
            "so": "result — consequence of the first clause",
            "because": "reason — explains why",
            "although": "contrast/concession — despite the fact that",
            "however": "contrast (formal, starts a new sentence)",
            "while": "contrast or simultaneous actions",
            "unless": "condition: 'except if'",
            "until": "up to the point in time when",
            "since": "from a point in time / because",
            "after": "sequence — later in time",
            "before": "sequence — earlier in time",
        }
        rule = conj_rules.get(a.lower(), "the appropriate linking word")
        hint = ""
        if "(contrast)" in q.lower() or "(contrast)" in q:
            hint = " The clue word <em>contrast</em> signals <strong>but</strong>."
        return f"<strong>{a}</strong> = {rule}.{hint}"

    # ── Countable / Uncountable ──────────────────────────────────────────────
    if "countable" in chapter or "uncountable" in chapter:
        rules = {
            "some": "<strong>some</strong> with uncountable nouns (positive sentences)",
            "any": "<strong>any</strong> in questions and negatives",
            "much": "<strong>much</strong> with uncountable nouns",
            "many": "<strong>many</strong> with countable nouns",
            "a lot of": "<strong>a lot of</strong> with both countable and uncountable",
            "a few": "<strong>a few</strong> with countable nouns (small number)",
            "a little": "<strong>a little</strong> with uncountable nouns (small amount)",
            "a": "<strong>a/an</strong> with singular countable nouns",
            "an": "<strong>an</strong> before vowel sounds",
        }
        rule = rules.get(a, f"<strong>{a}</strong> with this noun type")
        return f"Use {rule}. Incorrect option: <em>{w1}</em>."

    # ── Future going to ──────────────────────────────────────────────────────
    if "going-to" in chapter or ("future" in chapter and "going" in q.lower()):
        return (
            f"<strong>going to</strong> = plan made before the moment of speaking "
            f"or prediction based on visible evidence. "
            f"<em>Will</em> is for spontaneous decisions."
        )

    # ── Future will ──────────────────────────────────────────────────────────
    if chapter == "future-will" or ("future" in chapter and "will" in chapter):
        if "'ll" in a or "will" in a.lower():
            return (
                f"<strong>will / 'll</strong> = spontaneous decision, promise, or prediction "
                f"(no prior plan). Signal words: <em>I think, I promise, I'm sure</em>."
            )

    # ── Future forms (combined) ──────────────────────────────────────────────
    if "future-forms" in chapter:
        signal = ""
        q_lower = q.lower()
        if "look at" in q_lower or "evidence" in q_lower or "decided" in q_lower or "booked" in q_lower:
            signal = " There is visible evidence or a prior plan — use <em>going to</em>."
        elif "i think" in q_lower or "predict" in q_lower or "scientists" in q_lower:
            signal = " This is a prediction without current evidence — use <em>will</em>."
        elif "don't worry" in q_lower or "can't carry" in q_lower:
            signal = " Spontaneous offer at moment of speaking — use <em>'ll</em>."
        elif "arranged" in q_lower or "confirmed" in q_lower or "10am" in q_lower:
            signal = " Fixed arrangement — use present continuous for future."

        def_a = FUTURE_DEFS.get(a, f"<strong>{a}</strong> is correct here")
        return f"<strong>{a}</strong> = {def_a}.{signal}"

    # ── Modal could/might ────────────────────────────────────────────────────
    if "could" in chapter or "might" in chapter:
        defs = {
            "could": "past ability <em>or</em> present possibility",
            "might": "weaker possibility (less certain than <em>may</em>)",
            "may": "possibility or formal permission",
            "can": "present ability or permission",
            "couldn't": "impossibility in the past",
        }
        d = defs.get(a, f"<strong>{a}</strong>")
        return f"<strong>{a}</strong> = {d}. Here it expresses {('ability' if 'could' in a and w1 == 'might' else 'possibility')}."

    # ── Modal must/should ────────────────────────────────────────────────────
    if "must-should" in chapter or "modals-obligation" in chapter or "modals-advice" in chapter:
        defs = {
            "mustn't": "prohibition — it is <strong>not allowed</strong>",
            "don't have to": "no obligation — <strong>not necessary</strong> (but allowed)",
            "doesn't have to": "no obligation — <strong>not necessary</strong> (but allowed)",
            "should": "advice or recommendation — not as strong as <em>must</em>",
            "shouldn't": "advice <em>against</em> — not as strong as <em>mustn't</em>",
            "must": "strong internal obligation or logical necessity",
            "have to": "external obligation — required by rules/others",
            "has to": "external obligation — required by rules/others",
            "had to": "past obligation",
            "ought to": "advice — same as <em>should</em>",
            "had better": "strong advice — implies a warning if ignored",
            "needn't": "no necessity at all",
        }
        da = defs.get(a, f"<strong>{a}</strong>")
        dw = defs.get(w1, f"<em>{w1}</em>") if w1 else ""
        contrast = f" <em>{w1}</em> = {dw}" if dw and w1 != a else ""
        return f"<strong>{a}</strong> = {da}.{contrast}."

    # ── Object pronouns ──────────────────────────────────────────────────────
    if "object-pronoun" in chapter:
        subj_to_obj = {"I": "me", "he": "him", "she": "her", "we": "us", "they": "them", "you": "you", "it": "it"}
        obj_to_subj = {v: k for k, v in subj_to_obj.items()}
        subj = obj_to_subj.get(a, "?")
        return (
            f"Object pronoun after verbs and prepositions: subject <em>{subj}</em> → "
            f"object <strong>{a}</strong>. Never use the subject pronoun (<em>{subj}</em>) "
            f"as an object."
        )

    # ── Past continuous ──────────────────────────────────────────────────────
    if "past-continuous" in chapter:
        if "was" in a or "were" in a:
            return (
                f"<strong>{a}</strong> = past continuous: an action <em>in progress</em> "
                f"at a moment in the past. Compare: past simple = completed action."
            )
        return f"<strong>{a}</strong> is the correct past continuous form here."

    # ── Past simple ──────────────────────────────────────────────────────────
    if "past-simple" in chapter:
        if a.endswith("ed") or a.endswith("d"):
            return f"<strong>{a}</strong> is the regular past simple form."
        else:
            return f"<strong>{a}</strong> is the irregular past simple of this verb — must be learned."

    # ── Prepositions of movement ──────────────────────────────────────────────
    if "prepositions-movement" in chapter or "prepositions-of-movement" in chapter:
        prep_rules = {
            "into": "movement to the inside",
            "out of": "movement from the inside",
            "through": "movement from one side to another",
            "past": "movement alongside something without entering",
            "over": "movement above and across",
            "under": "movement below",
            "across": "movement from one side to the other (surface)",
            "along": "movement following the length of something",
            "up": "movement to a higher position",
            "down": "movement to a lower position",
            "towards": "movement in the direction of",
            "away from": "movement increasing distance from",
            "to": "movement with a destination",
            "around": "movement following a curved path",
        }
        rule = prep_rules.get(a.lower(), f"indicates direction/movement")
        return f"<strong>{a}</strong> = {rule}. <em>{w1}</em> doesn't fit the spatial context."

    # ── Present perfect intro ────────────────────────────────────────────────
    if "present-perfect" in chapter and "intro" in chapter:
        signal_words = {
            "already": "<strong>already</strong> = before expected time (positive sentences)",
            "just": "<strong>just</strong> = very recently (positive sentences)",
            "yet": "<strong>yet</strong> = up to now (questions and negatives)",
            "ever": "<strong>ever</strong> = at any time (questions)",
            "never": "<strong>never</strong> = at no time",
            "for": "<strong>for</strong> + duration (e.g. for three years)",
            "since": "<strong>since</strong> + starting point (e.g. since 2010)",
            "have": "present perfect: <em>have/has</em> + past participle",
            "has": "present perfect third person singular: <em>has</em> + past participle",
        }
        sw = signal_words.get(a)
        if sw:
            return sw + "."
        return f"<strong>{a}</strong> is correct with the present perfect tense here."

    # ── Quantifiers ──────────────────────────────────────────────────────────
    if "quantifier" in chapter:
        rules = {
            "some": "positive sentences — with uncountable or plural nouns",
            "any": "questions and negatives — with uncountable or plural nouns",
            "much": "large amount — only with uncountable nouns",
            "many": "large number — only with countable nouns",
            "a lot of": "large amount — both countable and uncountable",
            "a few": "small number — only with countable nouns",
            "a little": "small amount — only with uncountable nouns",
            "no": "zero quantity — replaces 'not any'",
            "few": "almost none — countable (negative connotation)",
            "little": "almost none — uncountable (negative connotation)",
        }
        rule = rules.get(a.lower(), "the correct quantifier for this context")
        return f"Use <strong>{a}</strong> ({rule}). <em>{w1}</em> doesn't match this noun type/sentence type."

    # ── Relative clauses basic ───────────────────────────────────────────────
    if "relative-clause" in chapter and ("basic" in chapter or "intro" in chapter):
        rules = {
            "who": "<strong>who</strong> = for people",
            "which": "<strong>which</strong> = for things/animals",
            "that": "<strong>that</strong> = for people or things",
            "where": "<strong>where</strong> = for places",
            "whose": "<strong>whose</strong> = possession",
            "when": "<strong>when</strong> = for times",
        }
        rule = rules.get(a, f"<strong>{a}</strong> is the correct relative pronoun")
        return f"{rule}. <em>{w1}</em> would be wrong: it refers to {'people' if w1 == 'who' else 'things' if w1 == 'which' else 'something else'}."

    # ── Short answers ────────────────────────────────────────────────────────
    if "short-answer" in chapter:
        return (
            f"Short answer uses the same auxiliary as the question: "
            f"<strong>{a}</strong>. Never repeat the full verb."
        )

    # ── Too / enough basic ───────────────────────────────────────────────────
    if "too-enough" in chapter:
        if "too" in a:
            return (
                f"<strong>too</strong> + adjective = more than needed/acceptable (negative). "
                f"Pattern: <em>too + adjective (+ to-infinitive)</em>."
            )
        elif "enough" in a:
            if a.startswith("enough"):
                return (
                    f"<strong>enough</strong> before nouns: <em>enough + noun</em>. "
                    f"After adjectives: <em>adjective + enough</em>."
                )
            else:
                return (
                    f"<strong>adjective + enough</strong>: <em>enough</em> comes <em>after</em> the adjective. "
                    f"Compare: <em>too + adjective</em> (before)."
                )
        return f"<strong>{a}</strong> is the correct too/enough structure here."

    # ── Word order ────────────────────────────────────────────────────────────
    if "word-order" in chapter:
        return (
            f"Correct English word order: <strong>{a}</strong>. "
            f"Remember: subject → verb → object/complement. "
            f"Adverbs of frequency go before the main verb (but after <em>be</em>)."
        )

    # ── Verb + infinitive patterns ────────────────────────────────────────────
    if "infinitive" in chapter or "verb-pattern" in chapter:
        inf_verbs = ["want", "hope", "decide", "plan", "need", "agree", "manage", "try"]
        ger_verbs = ["enjoy", "finish", "mind", "suggest", "avoid", "practise", "keep"]
        both_verbs = ["like", "love", "hate", "start", "begin", "continue"]
        if "to " in a and not a.startswith("to"):
            return f"<strong>{a}</strong>: this verb takes <em>verb + to-infinitive</em>."
        if a.endswith("ing"):
            return f"<strong>{a}</strong>: this verb takes <em>verb + -ing (gerund)</em>."
        return f"<strong>{a}</strong> is the correct verb pattern here."

    # ── Zero/first conditional ────────────────────────────────────────────────
    if "zero" in chapter and "conditional" in chapter:
        return (
            f"Zero conditional: <em>if + present simple</em> → <em>present simple</em>. "
            f"Used for facts/scientific truths. <strong>{a}</strong> is the correct present simple form."
        )
    if "first" in chapter and "conditional" in chapter:
        return (
            f"First conditional: <em>if + present simple</em> → <em>will + infinitive</em>. "
            f"Real/possible future situation. <strong>{a}</strong> is correct."
        )
    if "second" in chapter and "conditional" in chapter:
        return (
            f"Second conditional: <em>if + past simple</em> → <em>would + infinitive</em>. "
            f"Hypothetical/unlikely situation. <strong>{a}</strong> is correct."
        )
    if "conditional" in chapter:
        return (
            f"<strong>{a}</strong> is the correct conditional form. "
            f"Check the <em>if</em>-clause tense to identify the conditional type."
        )

    # ── Modal deduction ───────────────────────────────────────────────────────
    if "deduction" in chapter or "modal-deduction" in chapter:
        defs_ded = {
            "must": "<strong>must</strong> = logical certainty (positive deduction)",
            "can't": "<strong>can't</strong> = logical impossibility (negative deduction)",
            "couldn't": "<strong>couldn't</strong> = logical impossibility (past)",
            "might": "<strong>might</strong> = weak possibility (uncertain)",
            "could": "<strong>could</strong> = possibility",
            "may": "<strong>may</strong> = possibility",
            "must have": "<strong>must have</strong> + pp = past deduction (certain)",
            "can't have": "<strong>can't have</strong> + pp = past impossibility",
            "might have": "<strong>might have</strong> + pp = past possibility (uncertain)",
        }
        d = defs_ded.get(a, f"<strong>{a}</strong>")
        return f"{d}. Context clues in the sentence show the degree of certainty."

    # ── Present perfect B1 ────────────────────────────────────────────────────
    if "present-perfect" in chapter and "b1" in chapter.lower():
        return (
            f"<strong>{a}</strong>: present perfect links a past action to the present. "
            f"Use <em>for</em> + duration, <em>since</em> + start point, or signal words "
            f"<em>already, just, yet, ever, never</em>."
        )

    # ── Passive simple ────────────────────────────────────────────────────────
    if "passive" in chapter:
        if "was" in a or "were" in a or "is" in a or "are" in a or "been" in a or "be" in a:
            return (
                f"Passive voice: <em>to be</em> + past participle. "
                f"<strong>{a}</strong> is the correct passive form here. "
                f"Use passive when the agent (doer) is unknown or unimportant."
            )
        return f"<strong>{a}</strong> is the correct passive construction here."

    # ── Reported speech ───────────────────────────────────────────────────────
    if "reported-speech" in chapter:
        return (
            f"Reported speech: tenses shift back. "
            f"<strong>{a}</strong> is the correct backshifted form. "
            f"(e.g. present → past, <em>will</em> → <em>would</em>, <em>can</em> → <em>could</em>)"
        )

    # ── Past simple vs continuous ─────────────────────────────────────────────
    if "past-simple" in chapter and "continuous" in chapter:
        if "was" in a or "were" in a:
            return (
                f"<strong>{a}</strong> = past continuous: background action <em>in progress</em>. "
                f"The past simple (<em>{w1}</em>) would show a completed action interrupting it."
            )
        else:
            return (
                f"<strong>{a}</strong> = past simple: completed action that <em>interrupted</em> "
                f"the continuous background action."
            )

    # ── Relative clauses (B1/B2) ──────────────────────────────────────────────
    if "relative-clause" in chapter:
        rules = {
            "who": "<strong>who</strong> = for people",
            "which": "<strong>which</strong> = for things/ideas",
            "that": "<strong>that</strong> = people or things (defining only)",
            "where": "<strong>where</strong> = for places",
            "whose": "<strong>whose</strong> = possessive",
            "when": "<strong>when</strong> = for times",
            "whom": "<strong>whom</strong> = formal object pronoun for people",
        }
        rule = rules.get(a, f"<strong>{a}</strong> is the correct relative pronoun")
        return f"{rule}."

    # ── Ing form ─────────────────────────────────────────────────────────────
    if "ing-form" in chapter or "gerund" in chapter:
        if a.endswith("ing"):
            return (
                f"<strong>{a}</strong> (gerund/-ing form). After prepositions and certain verbs "
                f"(enjoy, avoid, suggest, finish, mind, practise), use the <em>-ing</em> form."
            )
        elif "to " in a:
            return (
                f"<strong>{a}</strong> (to-infinitive). After want, need, hope, decide, plan, manage, "
                f"agree, the <em>to-infinitive</em> is used."
            )
        return f"<strong>{a}</strong> is the correct verb form here."

    # ── Advanced tenses (C1) ──────────────────────────────────────────────────
    if "advanced-tenses" in chapter:
        tense_rules = {
            "will have": "Future Perfect: action <em>completed before</em> a future point. Signal: <em>by</em>.",
            "will be": "Future Continuous: action <em>in progress at</em> a future moment. Signal: <em>this time tomorrow / at 3pm</em>.",
            "had been": "Past Perfect Continuous: extended action <em>before</em> a past event, emphasising duration.",
            "both correct": "Both <em>would</em> and <em>used to</em> express past habits. <em>Used to</em> also expresses past states.",
            "would": "Past habit — <strong>would</strong> describes repeated past actions only (not states).",
            "used to": "<strong>used to</strong> = past habit or state no longer true.",
        }
        for key_start, rule in tense_rules.items():
            if a.startswith(key_start):
                return rule
        return f"<strong>{a}</strong> is the correct advanced tense form here."

    # ── Articles advanced (C1) ────────────────────────────────────────────────
    if "articles" in chapter:
        art_rules = {
            "Ø": "No article (<strong>Ø</strong>) with abstract nouns used in a general sense, meals, and fixed expressions like <em>in hospital</em>.",
            "the": "<strong>the</strong> = specific/unique reference, or with instruments (<em>plays the violin</em>).",
            "a": "<strong>a</strong> = first mention or one of many.",
            "an": "<strong>an</strong> = before vowel sounds; first mention.",
        }
        rule = art_rules.get(a, f"<strong>{a}</strong> is the correct article here")
        return f"{rule}"

    # ── Causative (C1) ────────────────────────────────────────────────────────
    if "causative" in chapter:
        caus_rules = {
            "made": "<strong>make</strong> someone do sth = force/compel (no to-infinitive after)",
            "let": "<strong>let</strong> someone do sth = allow (no to-infinitive after)",
            "got": "<strong>get</strong> someone to do sth = persuade (requires to-infinitive)",
            "have": "<strong>have</strong> sth done = arrange for someone else to do it",
            "had": "<strong>have</strong> sth done = arrangement (past)",
            "get": "<strong>get</strong> sth done = arrange (informal)",
        }
        rule = caus_rules.get(a, f"<strong>{a}</strong> causative pattern")
        return f"{rule}."

    # ── Vocab collocations: make/do/take/have ─────────────────────────────────
    if "collocations-make" in chapter or "make-do" in chapter or "collocations-do" in chapter:
        coll_verbs = {
            "make": "<strong>make</strong> + noun (e.g. make a decision, make a difference, make a mistake)",
            "do": "<strong>do</strong> + noun (e.g. do homework, do a course, do damage)",
            "take": "<strong>take</strong> + noun (e.g. take notes, take a break, take part)",
            "have": "<strong>have</strong> + noun (e.g. have an argument, have fun, have a look)",
            "makes": "<strong>make</strong> — fixed collocation",
            "does": "<strong>do</strong> — fixed collocation",
            "takes": "<strong>take</strong> — fixed collocation",
            "had": "<strong>have</strong> + noun (fixed collocation)",
            "did": "<strong>do</strong> + noun (fixed collocation)",
        }
        rule = coll_verbs.get(a, f"<strong>{a}</strong> = fixed collocation")
        return f"{rule}. These verb-noun pairs must be memorised."

    # ── Vocab collocations: adj+noun ──────────────────────────────────────────
    if "collocations-adj" in chapter or "adjective-noun" in chapter:
        return (
            f"<strong>{a} + {re.sub(r'___+', '', q.split('____')[1].split('.')[0].strip() if '____' in q else 'noun')}</strong> "
            f"is a fixed English collocation — this combination is the natural choice."
        )

    # ── Vocab phrasal verbs ───────────────────────────────────────────────────
    if "phrasal" in chapter:
        pv_rules = {
            "ran": "<strong>ran over</strong> = went beyond the allotted time",
            "turned": "<strong>turned down</strong> = rejected/refused; <strong>turned out</strong> = proved to be; <strong>turned up</strong> = arrived",
            "run": "<strong>run out of</strong> = exhaust supply; <strong>run into</strong> = meet by chance",
            "turn": "<strong>turn</strong> + particle = the appropriate phrasal verb for this context",
            "went": "<strong>went through</strong> = experienced; <strong>went off</strong> = exploded/rang",
            "came": "<strong>came up with</strong> = thought of; <strong>came across</strong> = found by chance",
        }
        rule = pv_rules.get(a, f"<strong>{a}</strong> forms the correct phrasal verb here")
        return f"{rule}."

    # ── Vocab: environment/society/technology etc. ────────────────────────────
    if "vocabulary" in chapter or chapter in ("society-culture", "environment-climate", "technology-media", "education-school"):
        return (
            f"<strong>{a}</strong> is the correct word for this context. "
            f"<em>{w1}</em> does not collocate/fit the meaning here."
        )

    # ── Writing (B1/B2) ───────────────────────────────────────────────────────
    if "writing" in chapter or chapter in ("story", "article", "informal-letter", "essay", "report"):
        return (
            f"<strong>{a}</strong> is the correct choice here. "
            f"Consider register, linking words, and the text type when answering."
        )

    # ── C2 grammar ────────────────────────────────────────────────────────────
    if "c2" in chapter or "c/c2" in chapter.lower():
        return (
            f"<strong>{a}</strong> is the correct advanced form here. "
            f"<em>{w1}</em> does not fit the grammatical structure of this sentence."
        )

    # ── Fallback ──────────────────────────────────────────────────────────────
    return (
        f"<strong>{a}</strong> is correct here. "
        f"<em>{w1}</em> does not fit the context."
    )


# ─── Main processing ────────────────────────────────────────────────────────────

def process_all():
    paths = sorted(glob.glob('/home/user/wordplay/**/worksheet.html', recursive=True))
    fixed_count = 0
    total_keys = 0

    for path in paths:
        with open(path) as f:
            c = f.read()

        # Find all question keys
        all_q_keys = re.findall(r'data-q="(e\d+q\d+)"', c)
        if not all_q_keys:
            continue

        exp_match = re.search(r'window\.EXPLANATIONS\s*=\s*\{', c)
        if not exp_match:
            continue

        exp_block_match = re.search(r'(window\.EXPLANATIONS\s*=\s*\{)(.*?)(\};)', c, re.DOTALL)
        if not exp_block_match:
            continue

        exp_text = exp_block_match.group(2)
        missing_keys = [k for k in all_q_keys if '"' + k + '"' not in exp_text]
        if not missing_keys:
            continue

        # Extract question data
        chapter_parts = path.replace('/home/user/wordplay/', '').split('/')
        chapter = '/'.join(chapter_parts[:4])  # e.g. a/a2/grammar/adverbs-manner

        # Parse window.ANSWERS for text-input questions
        text_answers = {}
        ans_match = re.search(r'window\.ANSWERS\s*=\s*\{(.*?)\};', c, re.DOTALL)
        if ans_match:
            for m in re.finditer(r'"?(e\d+q\d+)"?\s*:\s*\{[^}]*answer\s*:\s*"([^"]+)"', ans_match.group(1)):
                text_answers[m.group(1)] = m.group(2)

        new_entries = []
        processed_keys = set()

        # Handle choice-group (button) questions
        for cg_match in re.finditer(r'data-q="(e\d+q\d+)" data-answer="([^"]+)"(.*?)</div>', c, re.DOTALL):
            key = cg_match.group(1)
            if key not in missing_keys or key in processed_keys:
                continue
            answer = cg_match.group(2)
            opts_html = cg_match.group(3)
            options = re.findall(r'data-value="([^"]+)"', opts_html)

            pos = cg_match.start()
            preceding = c[max(0, pos - 600):pos]
            qtext_list = list(re.finditer(r'<div class="q-text">(.*?)</div>', preceding, re.DOTALL))
            qtext = ''
            if qtext_list:
                qtext = re.sub(r'<[^>]+>', '', qtext_list[-1].group(1)).strip()
                qtext = re.sub(r'\s+', ' ', qtext)

            expl = make_explanation(chapter, qtext, answer, options)
            new_entries.append(f'"{key}": "{expl}"')
            processed_keys.add(key)
            total_keys += 1

        # Handle text-input questions (data-q on <input> tags)
        for inp_match in re.finditer(r'<input[^>]+data-q="(e\d+q\d+)"', c):
            key = inp_match.group(1)
            if key not in missing_keys or key in processed_keys:
                continue
            answer = text_answers.get(key, '')
            if not answer:
                continue

            pos = inp_match.start()
            preceding = c[max(0, pos - 600):pos]
            qtext_list = list(re.finditer(r'<div class="q-text">(.*?)</div>', preceding, re.DOTALL))
            qtext = ''
            if qtext_list:
                raw = qtext_list[-1].group(1)
                raw = re.sub(r'<input[^>]+>', '___', raw)
                qtext = re.sub(r'<[^>]+>', '', raw).strip()
                qtext = re.sub(r'\s+', ' ', qtext)

            expl = make_explanation(chapter, qtext, answer, [answer])
            new_entries.append(f'"{key}": "{expl}"')
            processed_keys.add(key)
            total_keys += 1

        # Handle textarea questions (open production — show model answer from data-answer-sample)
        # Search for ALL textarea data-q occurrences
        for ta_match in re.finditer(r'<textarea\b[^>]*data-q="(e\d+q\d+)"[^>]*>', c, re.DOTALL):
            key = ta_match.group(1)
            if key not in missing_keys or key in processed_keys:
                continue
            # Extract data-answer-sample from the full tag text
            tag_text = ta_match.group(0)
            sa_m = re.search(r'data-answer-sample="((?:[^"\\]|\\.)*)?"', tag_text, re.DOTALL)
            if not sa_m:
                # The tag might span more than the captured group — search a wider context
                pos2 = ta_match.start()
                tag_end = c.find('>', pos2 + 10)
                if tag_end < 0:
                    tag_end = pos2 + 5000
                tag_full = c[pos2:tag_end+1]
                sa_m = re.search(r'data-answer-sample="([^"]*)"', tag_full, re.DOTALL)
            sample = sa_m.group(1) if sa_m else ''
            answer = sample or text_answers.get(key, '')
            if not answer:
                continue

            # Decode HTML entities in sample
            answer_clean = answer.replace('&#10;', ' ').replace('&#13;', '').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').strip()
            answer_clean = re.sub(r'\s+', ' ', answer_clean)
            # Truncate long model answers to first 120 chars
            if len(answer_clean) > 120:
                answer_clean = answer_clean[:120].rsplit(' ', 1)[0] + '…'
            # Escape for JS string
            answer_clean = answer_clean.replace('"', '&quot;').replace("'", '&#39;')

            expl = f"Model answer: <em>{answer_clean}</em>"
            new_entries.append(f'"{key}": "{expl}"')
            processed_keys.add(key)
            total_keys += 1

        if not new_entries:
            continue

        # Inject new entries at the start of EXPLANATIONS
        new_exp_text = '\n  ' + ',\n  '.join(new_entries) + ',\n  ' + exp_text.lstrip()
        new_c = (
            c[:exp_block_match.start(2)]
            + new_exp_text
            + c[exp_block_match.end(2):]
        )

        with open(path, 'w') as f:
            f.write(new_c)

        fixed_count += 1
        rel = path.replace('/home/user/wordplay/', '')
        print(f'  Fixed {len(new_entries)} keys in {rel}')

    print(f'\nDone: {fixed_count} files, {total_keys} explanation keys added.')


if __name__ == '__main__':
    process_all()

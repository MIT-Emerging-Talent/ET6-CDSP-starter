# Problem Domain

Scam detection in digital job markets is a rising problem. It involves
interactions between humans (job seekers, recruiters),
systems (job boards, ATS tools), and malicious actors (scammers) who now
leverage generative AI. Traditionally, detection relied heavily on linguistic
cues and behavioral red flags like urgency, grammar issues, and fake domains,
but AI is eroding those signals.

Our study sits at the intersection of **cybersecurity, human behavior, and NLP,**
asking: What happens when scammers have access to the same tools used to detect them.

## Problem Statement

***To What extent can job seekers and existing classifier models accurately
detect fraudulent job postings crafted by advanced AI, and how does a *"scam
score marker"* influence job seeker engagement with identified risks?***

Despite advanced detection systems and widespread warnings, job scams aren’t
just surviving, they’re thriving. According to the Federal Trade Commission,
reported losses from **job opportunity scams totaled $750.6 million in 2024**,
up nearly **$250 million from 2023**.

In a recent job readiness workshop on June 12, 2025, attended by our
[team](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-21-repo/blob/main/collaboration/README.md)
and 94+ other students, nearly every attendee had encountered a fake job posting.
This personal insight reflects a sobering national trend.

> “The number of reports for job and employment agency scams tripled from 2020 to
2024, and consumer losses jumped from $90 million to $501 million.” —
[*Federal Trade Commission*](https://www.ftc.gov/news-events/news/press-releases/2025/03/new-ftc-data-show-big-jump-reported-losses-fraud-125-billion-2024#:~:text=People%20who%20report%20to%20ReportFraud,state%20broken%20down%20by%20age.)

These statistics raise an urgent question: Are AI-generated scam texts becoming
so convincing that even experts and their tools can no longer reliably detect
them? If true, this could signal the breakdown of existing scam detection models,
and the need for a paradigm shift.

## Systems Thinking Perspective

We model this as a dynamic arms race involving three actors:

1. **Scammers**, now equipped with LLMs capable of mimicking legitimate
corporate language.
2. **Detection systems**, often trained on outdated fraud signals or
keyword-based heuristics.
3. **Human users**, whose trust, judgment, and attention span are increasingly
stretched thin.

This system is evolving. As generative AI improves, it may:

- Erase the linguistic telltales traditionally used to flag fraud.
- Exploit brand tone, corporate jargon, and trust signals with unnerving accuracy.
- Render traditional classifiers obsolete unless rethought from the ground up.

## Background Summary

Past research in scam detection has leaned heavily on:

- Linguistic feature engineering (e.g., urgency cues, poor grammar, spam words).
- ML classification using bag-of-words, TF-IDF, or shallow embeddings.
- User training and awareness-based campaigns.

However, these methods rely on the assumption that fraudulent text will deviate
in detectable ways from legitimate content. That assumption is **under threat**.

## Our Research Question

**Can LLM-generated scam job postings evade both human judgment and machine detection,
and can real-time risk indicators effectively guide job seekers away from
deceptive opportunities?**

This leads to sub-questions such as:

- How do real and AI-generated scams compare linguistically?

- Can humans detect LLM-generated scams better than machines—or vice versa?

- Are today’s best detection models still effective against LLM-generated
scam text?

- How do job seekers react to the presence and prominence of an automated risk
score on job postings, and how does this influence their likelihood of engaging
with fraudulent opportunities?

## Conclusion

Scam detection is no longer just about spam filters or “watch for typos.”
It’s now a battle of AI vs AI, with humans caught in the middle. If current
detection techniques are failing - because the threat has evolved - then the
question isn’t just how to detect, but whether detection as we know it still works.
Our goal is not just to build another model, but to stress-test the foundations
of how we classify and catch job deceptions in the age of generative AI.

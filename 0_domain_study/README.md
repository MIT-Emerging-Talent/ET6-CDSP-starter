# Domain Study

This document outlines our foundational research into the domain of Buy Now, Pay
Later (BNPL) services and their implications for credit behavior, over-indebtedness,
and financial risk modeling.

## BNPL

The rise of BNPL services has significantly changed how consumers — especially
young adults (Gen Z) — access credit. These services offer short-term installment
payments with minimal upfront verification and no interest if payments are made
on time. However, this convenience may come at the cost of untracked debt accumulation,
missed payments,and difficulty predicting long-term financial stress.

Despite growing BNPL adoption, traditional credit systems often fail to monitor
or incorporate BNPL behavior. This creates blind spots in assessing financial
risk and raises critical questions about financial inclusion and consumer protection.

## Problem Statement

BNPL services create invisible debt accumulation across multiple platforms that
neither consumers nor traditional credit monitoring systems can effectively
track, leading to unexpected financial stress and over-indebtedness among young
adults who believe they are managing their finances responsibly.

## Research Question

*How accurately can a machine learning model, using behavioral and transactional
data, predict over-indebtedness risk among Gen Z Buy Now, Pay Later (BNPL) users
within a 6-month horizon, and which features provide the most reliable early-warning
signals?*

## Findings

Our domain research revealed the following major themes and gaps:

### BNPL and Credit Behavior

There is growing discussion on BNPL’s popularity  particularly among Gen Z  and
its exclusion from traditional credit scoring systems. However, we found little
rigorous analysis on whether BNPL usage positively, negatively, or neutrally
affects long-term credit behavior (defaults, credit scores, responsible borrowing).

### Over-Indebtedness Risk Modeling in BNPL

Several papers suggest BNPL usage leads to debt overextension, but very few
provide quantifiable thresholds or methods to flag high-risk users early.
There's a notable lack of frameworks for early-warning indicators or personalized
risk profiling.

### Summary of Observed Patterns

- BNPL use is rising sharply among young adults with limited financial education.
- Users frequently hold BNPL balances across multiple platforms without
- consolidated tracking.
- Traditional credit systems do not capture BNPL activity, weakening their
- predictive value.
- Machine learning approaches can help predict financial stress with higher precision.
- Explainability tools such as SHAP can provide transparency in model predictions.

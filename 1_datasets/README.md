# Project Methodology: How We're Analyzing Chatbot Failures

## Modeling the Problem Domain

To understand why users feel mental health chatbots fail, we can't run a perfect,
controlled lab experiment. Instead, our project **models this problem by treating
public user reviews as a direct proxy for real-world user experience.**

Our core assumption is that when a user has a significantly negative experience
especially a "conversational failure" where the chatbot feels robotic, unhelpful,
or repetitive—they are motivated to share this feedback on public platforms.

### Our Data Strategy: Combining Scale and Depth

We are using a two-pronged data strategy to capture a comprehensive picture:

1. **App Store Reviews (The "Quantitative" View):** By scraping thousands of 1, 2,
and 3-star reviews from the Google Play Store, we get a large-scale view of the
most common points of frustration. This tells us *what* the biggest problems are
 *how often* they occur.

2. **Reddit Discussions (The "Qualitative" View):** By scraping forums like `r/Replika`
and `r/Wysa`, we capture deep, contextual stories. This data provides the crucial
*why* behind the failures. Users on Reddit often share detailed conversational logs
and emotional reactions that are missing from concise app reviews.

### Potential Flaws in Our Approach (Our Limitations)

This model is a powerful proxy, but it's not perfect. We acknowledge the following
limitations:

* **Selection Bias:** Users who leave negative reviews or post on Reddit are often
the most frustrated. Our data represents the "loudest voices" and may not capture
the experience of moderately dissatisfied or passive users.
* **Lack of Demographics:** We do not know the age, location
(beyond the app store country), or background of these users.
* **No Control Group:** This is an observational study. We are analyzing what
people chose to write, not conducting a controlled experiment where we give
different users different bots.

**[Real User has a bad experience] -> [Writes a review on App Store / post on Reddit]
-> [Our Scrapers Collect this Data] -> [Our Dataset] -> [Analysis of Failure Themes]**

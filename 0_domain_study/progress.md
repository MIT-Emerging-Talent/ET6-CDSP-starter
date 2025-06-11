# Team Progress

## Convergent and divergent thinking

### Problem Identification

```mermaid
---
config:
  theme: neutral
  look: neo
---
flowchart TB
 subgraph s1[" "]
        B{"Sub-domains"}
        A("Define Domain and Interests")
        BA("Environmental policy")
        BB("Solar Energy Systems")
        BC("Climate change mitigation")
        BD("Renewable Energy")
        C{"Domain"}
        D["Sustainable development"]
        nn("Start")
  end
 subgraph s[" "]
        n1["Problem Statement"]
        n2["Research questions"]
        n3["**How can the use of renewable energy help in combating the effects of
climate change?**"]
        n31["**What are the economic and environmental benefits of transitioning
to solar energy?**"]
        n32["
        **How can small-scale solar energy users in unregulated markets
        Verify product quality through digital tools or cooperative purchasing models?**"]
        n33[" "]
        n4(["Actionable Research Question"])
        n5[" "]
  end
    A --> B
    B --> BA & BB & BC & BD
    BA ~~~ C
    BB ~~~ C
    BC ~~~ C
    BD ~~~ C
    nn --> A
    C --> D
    D --> n1
    n1 --> n2
    n2 --> n3 & n31 & n32 & n33
    n3 & n31 & n32 & n33 --> n4
    n4 --> n5
    style B fill:#C8E6C9
    style A fill:#FFF9C4
    style C fill:#C8E6C9
    style n3 color:#000000
    style n4 fill:#FFF9C4

```

## Constraints

- Geographical and Seasonal Limitations
  - Limited sunlight hours and seasonal variation in some regions
- Financial Barriers
  - High initial cost of solar panel installation
- Infrastructure Challenges
  - Lack of storage infrastructure (e.g. batteries)
- Energy Access Disparities
  - Uneven access to renewable energy across urban and rural areas
- Time Constraints
  - Time limit of 12 weeks for research
- Knowledge Requirements
  - Requires basic domain knowledge in climate science and energy policy

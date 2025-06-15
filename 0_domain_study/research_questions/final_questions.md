# Problem Overview and Research Framework

## Refined Main Questions

### Primary Research Question

**Can we develop a machine learning model to predict which BNPL users
are at high risk of over-indebtedness or default,**  
**and what features serve as the best early warning indicators?**

### Secondary Research Questions

1. **Methodological Question**: Which machine learning algorithms
   (XGBoost, Random Forest, Neural Networks) perform best for BNPL
   risk prediction compared to traditional credit scoring approaches?

2. **Behavioral Pattern Question**: What BNPL usage patterns
   (payment timing, frequency, cross-platform usage) most strongly
   predict financial distress 30-90 days in advance?

3. **Feature Importance Question**: How do BNPL-specific behavioral features
   compare to traditional credit variables (FICO score, income, employment)
   in predictive power?

4. **Demographic Risk Question**: How do over-indebtedness risk patterns vary
   across age, income, and geographic demographics, and can models maintain
   fairness across these groups?

5. **Policy Application Question**: What regulatory interventions and consumer  
   protection measures would be most effective based on identified risk  
   indicators and early warning signals?

## Research Focus Areas

### 1. Technical Focus

### Machine Learning for Financial Risk Assessment

- **Algorithm Comparison**: Systematic evaluation of ensemble methods  
  vs. traditional logistic regression
- **Feature Engineering**: Development of BNPL-specific behavioral and temporal features
- **Model Interpretability**: Implementation of SHAP and LIME for regulatory compliance
- **Fairness Analysis**: Ensuring equitable performance across demographic groups
- **Early Warning Systems**: Optimizing prediction horizons (30/60/90 days)  
  for actionable interventions

### 2. Business Focus  

### BNPL Market Dynamics and Stakeholder Impact

- **Market Structure Analysis**: global market growing at a fast rate
- **Cross-Platform Risk**: 63% of users have multiple simultaneous loans  
  across different services
- **Revenue Model Impact**: How merchant fee structures influence  
  risk assessment incentives
- **Competitive Positioning**: Risk management as competitive advantage  
  vs. regulatory compliance
- **Industry Standards**: Development of responsible lending practices and  
  best practices framework

### 3. User Focus

### Consumer Protection and Financial Inclusion

- **Vulnerable Population Analysis**: Disproportionate impact on young,  
  low-income, and minority consumers
- **Behavioral Economics**: Understanding why consumers accumulate hidden debt  
  across platforms
- **Financial Literacy Gaps**: BNPL-specific risks not covered in  
  traditional financial education
- **Intervention Design**: User-friendly early warning tools and  
  consumer education strategies
- **Empowerment Tools**: Democratizing risk assessment information  
  for individual consumers

## Market Context and Problem Scope

### Market Size and Growth

- **Global Market**: $378.3 billion in 2023, projected to  
  reach $532.9 billion by 2024
- **US Market**: Expected to hit $124.8 billion by 2027, growing at 15.8% annually
- **User Base**: Over 43 million users in US alone,  
  with 8 out of 10 top markets in northwestern Europe
- **Transaction Volume**: 434% increase in "necessity" purchases  
  (gas, groceries, utilities) from 2020-2021

### Consumer Impact Indicators

- **Multi-Platform Usage**: 63% of borrowers had simultaneous loans in 2021-2022
- **Cross-Provider Risk**: 32% had loans across multiple firms simultaneously
- **Late Payment Rates**: 42% of users report having missed BNPL payments
- **Fee Revenue**: 13.4% of BNPL provider revenues come from late fees and penalties

### Regulatory Environment

- **CFPB Investigation**: Active regulatory scrutiny with multiple reports  
  since 2021
- **Consumer Protection Gaps**: BNPL operates with fewer protections  
  than traditional credit
- **Policy Timeline**: May 2024 interpretive rule treating BNPL as credit cards
  under Truth in Lending Act
- **International Responses**: UK, Australia, and EU developing comprehensive  
  regulatory frameworks

## Complete Research Question Framework

### Problem Definition

**The BNPL ecosystem creates systematic information asymmetries and
cross-platform  
debt accumulation that traditional credit risk assessment cannot address,
leading  
to preventable over-indebtedness among financially vulnerable populations who
use  
BNPL services believing they are safer than traditional credit.**

### Research Hypothesis

**BNPL-specific behavioral patterns (payment timing, usage acceleration,  
cross-platform activity) will demonstrate superior predictive power for  
over-indebtedness risk compared to traditional credit scoring variables.**  
**This will enable early warning systems that can prevent financial distress  
60-90 days before crisis points.**

### Technical Approach

**Develop ensemble machine learning models using synthetic BNPL user data that  
combines traditional credit features with novel behavioral indicators to  
predict over-indebtedness risk while maintaining interpretability for  
regulatory compliance and fairness across demographic groups.**

### Expected Contribution

**Create the first comprehensive machine learning framework
 for BNPL risk assessment that provides actionable insights
  for consumers, evidence-based recommendations for
   regulators, and practical tools for industry while advancing
    academic knowledge in fintech consumer protection.**

## Success Criteria

### Technical Success Metrics

- **Model Performance**: Achieve >80% AUC score in predicting 90-day
 over-indebtedness risk
- **Feature Discovery**: Identify 10+ statistically significant early warning indicators
- **Fairness Benchmark**: Model performance variance <5% across demographic groups
- **Interpretability Standard**: Generate clear explanations for 95% of
 high-risk predictions
- **Temporal Accuracy**: Reliable risk prediction 60+ days before financial
 distress occurs

### Academic Success Metrics  

- **Literature Contribution**: Address identified research gaps with novel methodology
- **Peer Review Quality**: Research suitable for publication in financial
 technology journals
- **Methodological Innovation**: Demonstrate new approaches to behavioral feature
 engineering
- **Reproducibility Standard**: Provide complete methodology enabling replication
 studies
- **Citation Impact**: Reference framework for future BNPL risk assessment research

### Policy Success Metrics

- **Regulatory Relevance**: Generate actionable recommendations for CFPB policy development
- **Stakeholder Value**: Insights useful for consumers, industry, and regulators
 simultaneously  
- **Implementation Feasibility**: Recommendations include practical implementation
 pathways
- **Consumer Protection**: Demonstrate measurable potential to prevent financial
 harm
- **Industry Adoption**: Framework suitable for real-world deployment by BNPL providers

### Social Impact Metrics

- **Vulnerable Population Focus**: Specific protections for high-risk demographic
 groups
- **Prevention Emphasis**: Early warning capabilities that enable proactive intervention
- **Financial Inclusion Balance**: Preserve BNPL benefits while mitigating exploitation
 risks
- **Education Value**: Generate insights useful for consumer financial literacy programs
- **Systemic Understanding**: Advance knowledge of fintech impacts on consumer welfare

## Research Constraints and Limitations

### Data Constraints

- **Privacy Limitations**: Real BNPL transaction data unavailable due to proprietary
 concerns
- **Synthetic Data Challenges**: Must validate synthetic data against published behavioral
 patterns
- **Cross-Platform Visibility**: Limited ability to observe actual multi-service
 usage patterns
- **Temporal Scope**: Analysis limited to patterns observable within 12-24 month
 timeframes

### Technical Constraints

- **Model Complexity**: Balance between predictive accuracy and regulatory interpretability
 requirements
- **Fairness Requirements**: Must avoid discriminatory outcomes while maintaining
 predictive power
- **Scalability Needs**: Models must handle real-world data volumes and real-time
 requirements
- **Feature Engineering**: Limited to features that could realistically be observed
 by BNPL providers

### Timeline Constraints

- **Time Limit**: Must prioritize highest-impact analysis within timeframe
- **Sequential Dependencies**: Literature review and data collection must precede
 modeling work
- **Validation Requirements**: Must allow sufficient time for comprehensive model
 evaluation
- **Policy Relevance**: Research must align with current regulatory investigation
 timeline

### Ethical Constraints

- **Consumer Harm Prevention**: Must not enable predatory lending or discriminatory
 practices
- **Bias Mitigation**: Proactive attention to algorithmic fairness throughout development
 process
- **Transparency Requirements**: Clear explanations of methodology and limitations
 for all
 stakeholders
- **Privacy Protection**: Synthetic data approach must maintain individual privacy
 protection

## Expected Outcomes and Applications

### For Consumers

- **Early Warning Tools**: Individual risk assessment capabilities for proactive
 financial management
- **Educational Resources**: Clear understanding of BNPL risks and cross-platform
 debt accumulation
- **Empowerment Information**: Access to risk assessment insights previously available
 only to lenders
- **Protection Advocacy**: Research support for stronger consumer protection regulations

### For Regulators  

- **Evidence-Based Policy**: Data-driven insights for BNPL regulatory framework development
- **Risk Assessment Tools**: Systematic approaches to evaluating BNPL market risks
- **Implementation Guidance**: Practical recommendations for consumer protection
 enforcement
- **Monitoring Capabilities**: Framework for ongoing oversight of BNPL market evolution

### For Industry

- **Improved Risk Management**: Enhanced tools for assessing customer
 over-indebtedness risk
- **Regulatory Compliance**: Framework for meeting evolving consumer protection standards
- **Competitive Advantage**: Superior risk assessment as differentiator in crowded
 market
- **Sustainable Growth**: Business model evolution that balances growth with consumer
 welfare

### For Academia

- **Methodological Advancement**: Novel applications of ML to emerging financial
 services
- **Research Foundation**: Baseline methodology for future BNPL and fintech risk
 studies
- **Interdisciplinary Bridge**: Connection between technical capabilities and
 social science applications
- **Policy Interface**: Model for academic research directly informing regulatory
 development

## Conclusion

This comprehensive problem overview establishes the foundation for rigorous,
 impactful research that addresses a critical gap in consumer financial
  protection while advancing the state of knowledge in financial technology and
   machine learning applications for social good. The research framework balances
    academic rigor with practical relevance, ensuring that our findings will
     contribute meaningfully to consumer protection, regulatory policy, and
      industry best practices.

The integration of personal experience with systematic analysis creates a
research approach that is both technically sophisticated and grounded in
real-world understanding of the challenges facing BNPL users. This foundation
positions our research to make significant contributions across multiple
stakeholder groups while maintaining focus on our core mission of preventing
financial harm among vulnerable populations.

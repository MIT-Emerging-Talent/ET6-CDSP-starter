# Datasets: Guide

Store your local datasets in this folder (`.csv`, `.xlsx`, `.json`, `.sqlite`,
...). You can use the README to document each dataset (where it's from, what
data & types it contains, what you use it for, ...).

One of the primary goals of this repository is that anyone can clone and
replicate your research. To make this possible **DO NOT modify or overwrite your
raw datasets**! You should keep them _exactly_ as they were when you downloaded
them, you may even want to name them `dataset.raw.ext` (eg.
`daily_temperatures.raw.csv`).

When cleaning and processing your datasets, you should save the prepared data to
a _new_ file with a descriptive name. This approach will result in many dataset
files, but that's ok!

## README.md

Use the README in this folder to document each dataset in the folder. Include
information like: where is the data from? how was it collected? how does it
relate to your problem? ...

## Types of Dataset

A dataset is "simply" a collection of related measurements or observations. To
create a good model of your problem using data you must understanding what
_kinds_ of data exist, how to understand them, and the best ways to analyze each
one. The kind of data you choose impacts:

- The tools you use for exploration and analysis
- How we visualize the data
- The statistical methods you can apply
- The type of conclusions you draw
- And how confident you are of your conclusions

Below is an overview of different kinds of dataset you will encounter:

1. [Classification by Data Type](#classification-by-data-type)
2. [Classification by Structure](#classification-by-structure)
3. [Classification by Collection Method](#classification-by-collection-method)
4. [Classification by Size and Complexity](#classification-by-size-and-complexity)
5. [Classification by Access Type](#classification-by-access-type)
6. [Classification by Purpose](#classification-by-purpose)
7. [Classification by Format](#classification-by-format)

## Classification by Data Type

### Quantitative (Numerical) Data

Data that represents quantities and can represented as numbers.

#### Continuous Data

- **Definition**: Can take any value within a range (including fractions and
  decimals)
- **Examples**: Height, weight, temperature, time, distance
- **Analysis**: Mean, median, standard deviation, histograms, scatter plots
- **Real-world example**: Recording daily temperature over a month (72.5°F,
  68.3°F, etc.)

#### Discrete Data

- **Definition**: Countable values, typically whole numbers
- **Examples**: Number of children, items sold, count of occurrences
- **Analysis**: Frequency tables, bar charts, mode
- **Real-world example**: Number of customers visiting a store each day (45, 52,
  38, etc.)

### Qualitative (Categorical) Data

Data that describes qualities or characteristics of what you want to study.

#### Nominal Data

- **Definition**: Categories with no inherent order or ranking
- **Examples**: Gender, blood type, country, color, product type
- **Analysis**: Frequency counts, mode, chi-square tests, pie charts
- **Real-world example**: Survey responses for favorite color (red, blue, green,
  etc.)

#### Ordinal Data

- **Definition**: Categories with a meaningful order or ranking
- **Examples**: Education level, satisfaction ratings (1-5), economic status
- **Analysis**: Median, percentiles, rank correlations, stacked bar charts
- **Real-world example**: Customer satisfaction ratings (very dissatisfied,
  dissatisfied, neutral, satisfied, very satisfied)

### Binary Data

- **Definition**: Data with only two possible values
- **Examples**: Yes/no questions, pass/fail outcomes, true/false conditions
- **Analysis**: Proportions, odds ratios, logistic regression
- **Real-world example**: Email spam classification (spam/not spam)

### Time Series Data

- **Definition**: Sequential data points collected at specific time intervals
- **Examples**: Stock prices, weather data, website traffic
- **Analysis**: Trend analysis, seasonal decomposition, forecasting
- **Real-world example**: Monthly sales figures over several years

## Classification by Structure

### Structured Data

- **Definition**: Organized in a consistent, predefined format
- **Examples**: Relational databases, spreadsheets, CSV files
- **Characteristics**:
  - Follows a schema
  - Easy to search and analyze
  - Typically stored in rows and columns
- **Real-world example**: Customer information in a CRM database

### Semi-structured Data

- **Definition**: Has some organizational properties but not rigid schema
- **Examples**: JSON, XML, email, HTML
- **Characteristics**:
  - Flexible format
  - Contains tags or markers to separate elements
  - Self-describing structure
- **Real-world example**: JSON response from a web API

### Unstructured Data

- **Definition**: No predefined format or organization
- **Examples**: Text documents, images, audio, video, social media posts
- **Characteristics**:
  - Difficult to process with traditional tools
  - Often requires specialized techniques (NLP, computer vision)
  - Comprises ~80-90% of all data generated
- **Real-world example**: Customer reviews or feedback in free text format

## Classification by Collection Method

### Primary Data

- **Definition**: Collected firsthand for a specific purpose
- **Examples**: Surveys, experiments, interviews, direct observations
- **Advantages**: Tailored to research needs, higher control over quality
- **Disadvantages**: Time-consuming, potentially expensive
- **Real-world example**: Market research survey designed specifically for a new
  product

### Secondary Data

- **Definition**: Data previously collected for other purposes
- **Examples**: Census data, published studies, company records
- **Advantages**: Cost-effective, time-saving, often larger sample sizes
- **Disadvantages**: May not perfectly fit current research needs
- **Real-world example**: Using government census data for demographic analysis

### [Proxy Data](https://centerforgov.gitbooks.io/benchmarking/content/Proxy.html)

- **Definition**: Data that is
- **Examples**: Tree rings to proxy historical weather patterns, tax data to
  proxy incomes
- **Advantages**: Helos you understand phenomena that are difficult or
  impossible to study directly.
- **Disadvantages**: You cannot draw conclusions with the same confidence.
- **Real-world example**: Using the stock market + unemployment rates as a proxy
  for the economy..

### Experimental Data

- **Definition**: Generated from controlled experiments with manipulated
  variables
- **Examples**: A/B tests, clinical trials, laboratory experiments
- **Characteristics**:
  - Control and treatment groups
  - Controlled conditions
  - Designed to establish causality
- **Real-world example**: Testing whether a new website design increases
  conversion rates

### Observational Data

- **Definition**: Collected through observation without direct intervention
- **Examples**: Traffic patterns, wildlife behavior, market trends
- **Characteristics**:
  - Natural setting
  - No manipulation of variables
  - Good for establishing correlation (not causation)
- **Real-world example**: Observing and recording consumer shopping behaviors in
  a store

## Classification by Size and Complexity

### Small Data

- **Definition**: Datasets manageable with traditional tools and methods
- **Characteristics**:
  - Can fit in memory of a typical computer
  - Processable with standard software (Excel, SPSS)
  - Usually under several gigabytes
- **Analysis**: Standard statistical methods, desktop tools
- **Real-world example**: Survey responses from 500 participants

### Big Data

- **Definition**: Datasets too large or complex for traditional processing
- **Characterized by the 5 Vs**:
  - **Volume**: Extremely large size
  - **Velocity**: Generated at high speed
  - **Variety**: Various formats and types
  - **Veracity**: Uncertainty and reliability concerns
  - **Value**: Extracting meaningful insights
- **Analysis**: Specialized tools (Hadoop, Spark), distributed computing
- **Real-world example**: Social media data from millions of users

### High-dimensional Data

- **Definition**: Many variables or features per observation
- **Examples**: Genomic data, image data, complex sensors
- **Challenges**:
  - Curse of dimensionality
  - Feature selection importance
  - Visualization difficulties
- **Analysis**: Dimension reduction techniques (PCA, t-SNE), specialized
  algorithms
- **Real-world example**: Gene expression data with thousands of genes measured
  for each sample

## Classification by Access Type

### Public Data

- **Definition**: Freely available to anyone
- **Examples**: Government data portals, open datasets, public research data
- **Characteristics**:
  - No access restrictions
  - Often licensed for reuse
  - May have usage guidelines
- **Real-world example**: World Bank development indicators

### Private Data

- **Definition**: Access restricted to authorized users
- **Examples**: Company internal data, personal health records, proprietary
  research
- **Characteristics**:
  - Security measures required
  - Often subject to privacy regulations
  - May require anonymization for broader use
- **Real-world example**: Patient medical records in a hospital database

### Proprietary Data

- **Definition**: Owned by organizations and often commercially valuable
- **Examples**: Nielsen ratings, credit scores, market research data
- **Characteristics**:
  - Commercial value
  - Legal protections
  - Often licensed for a fee
- **Real-world example**: Credit bureau consumer data

## Classification by Purpose

### Transactional Data

- **Definition**: Records of business or system transactions
- **Examples**: Sales records, banking transactions, server logs
- **Characteristics**:
  - High volume
  - Time-stamped
  - Operation-focused
- **Real-world example**: Point-of-sale data from retail stores

### Analytical Data

- **Definition**: Processed and organized for analysis and decision-making
- **Examples**: Data warehouses, OLAP cubes, aggregated reports
- **Characteristics**:
  - Often derived from transactional data
  - Optimized for querying and analysis
  - May include historical perspectives
- **Real-world example**: Quarterly sales performance dashboard

### Master Data

- **Definition**: Core business entities that rarely change
- **Examples**: Customer database, product catalog, employee records
- **Characteristics**:
  - Reference data
  - Shared across systems
  - Requires governance
- **Real-world example**: Product master list with SKUs, descriptions, and
  categories

### Metadata

- **Definition**: Data about data
- **Examples**: File creation dates, database schema, data dictionaries
- **Characteristics**:
  - Describes structure and context
  - Essential for data management
  - Facilitates data discovery
- **Real-world example**: Column names and descriptions for a dataset

## Classification by Format

### Tabular Data

- **Definition**: Organized in tables with rows and columns
- **Examples**: CSV, Excel files, database tables
- **Characteristics**:
  - Most common format for analysis
  - Each row is an observation, each column a variable
- **Real-world example**: Excel spreadsheet of monthly expenses

### Hierarchical Data

- **Definition**: Organized in a tree-like structure with parent-child
  relationships
- **Examples**: XML, JSON, file systems
- **Characteristics**:
  - Nested structure
  - Good for representing complex relationships
- **Real-world example**: Organization chart

### Network Data

- **Definition**: Represents connections between entities
- **Examples**: Social networks, transportation systems, web links
- **Characteristics**:
  - Consists of nodes and edges
  - Focus on relationships
- **Real-world example**: LinkedIn connections network

### Spatial Data

- **Definition**: Contains geographic or geometric information
- **Examples**: GIS data, maps, satellite imagery
- **Characteristics**:
  - Contains coordinates or shape information
  - Often requires specialized tools
- **Real-world example**: Census data with geographic coordinates

### Temporal Data

- **Definition**: Emphasizes time dimension
- **Examples**: Time series, event logs, historical records
- **Characteristics**:
  - Time-stamped
  - May show patterns over time
- **Real-world example**: Server logs with timestamp for each entry

## Key Considerations for Beginners

### Data Quality Assessment

- **Completeness**: Missing values, coverage
- **Accuracy**: Errors, outliers, validity
- **Consistency**: Internal contradictions, logical issues
- **Timeliness**: How recent is the data?

### Ethical Considerations

- **Privacy**: Personal identifiable information (PII)
- **Consent**: Was data collected with proper consent?
- **Bias**: Is the sample representative?
- **Transparency**: Can methods and sources be disclosed?

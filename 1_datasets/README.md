<!-- markdownlint-disable MD013 MD033-->
# Datasets

## Off-grid Renewable Energy Statistics 2024
- This dataset is from the International Renewable Energy Agency, which
is an intergovernmental organization that promotes the adoption and
sustainable use of renewable energy worldwide.
- It’s a quantitative dataset. The file consists of two sheets:
the first one is an ‘about’ file, and the other is the ‘data’ sheet that
contains the actual data. The data sheet consists of 16 columns, namely:
Region, UN sub-region, Country, IRENA label, ISO code, Flow, Group technology,
Sub-technology, Technology, Product code, DataType, Value, Unit, Year, Ptype, Publication.
- **How it was collected**
  - According to the [measurement and estimation](https://www.irena.org/publications/2018/Dec/Measurement-and-estimation-of-off-grid-solar-hydro-and-biogas-energy) file of IRENA
    - The data was collected from a mix of national databases, international organizations
    (like GOGLA and SNV), and online sources such as project reports and news articles.
    Where direct data was unavailable, IRENA used estimation methods (e.g.,
    trade data, technical assumptions) and peer review to validate and fill gaps.
- **Some possible flaws are**
  - There is no a direct connection between off-grid renewable energy and
   conflict countries.
  - The dataset has different unit types in the Units column, depending
   on the technology utilized.
  - It has quite a lot of zero values, especially in our targeted countries.
- **<p>How it is related to our problem?<br>**
    This dataset will be a huge asset to our research question, it’s like
    a baseline layer dataset, for example:
  - We can use the “value” column to get a sense of the deployment or
    utilization rate of different renewable energy sources and make a
    comparison between conflict and non-conflicts countries.
  - Identify whether conflicts correlate to a slowdown, shift or
    an increase in solar pv utilization.<br>
    
  However, alone, it won’t be enough; we’ll need to introduce other
  resources to showcase conflicts regions, e.g (ACLED, UDCP)</p>

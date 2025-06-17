# Domain Study: Guide

To do meaningful research, you must know what others do and don’t understand.  
Use this folder to collect your group’s knowledge of your research domain.  
Include your own summaries, PDFs, and useful links.

This folder is not like `/notes` — it contains _only_ research domain info.  
Ask yourself: _Would someone need this to understand our research?_

## README.md

Use this folder’s README to describe the notes and files inside.  
Someone should not need to read everything to find key info.

## Chosen Question

How effective is Satellite Image Analysis at Predicting Deforestation  
in Malaysia?

### Why this question?

Malaysia has vast forests, but deforestation is a serious issue.  
Global Forest Watch shows a 31% drop in tree cover since 2000.  
It is important to track and predict deforestation early.  
If satellite image analysis works, it can support conservation.  
It could also be a low-cost tool for environmental protection.

### Satellite Image Analysis

This means using satellite images to study Earth’s surface.  
We can analyze land use, vegetation, and environmental changes.

Image resolution matters. High-res images give better results  
but need more storage and processing time.

We plan to use free Landsat images from Google Earth Engine.  
They have 30m resolution and are updated every 16 days.  
This offers a balance between quality and efficiency.

There are 3m daily images from PlanetScope, but they are costly.  
They also need too many resources for our timeframe.  
They may help future studies track trees at an individual level.

### Rough Plan

- **Data Collection**:  
  - Get satellite images and vegetation data from GFW and Earth Engine.  
  - GFW makes it easy to find vegetation index data.  
  - Google Earth Engine provides free satellite images.  
    We need to create accounts and request API access.  
    We also need to write code to extract and process images.  
  - Gather other data from public sources and institutions.

- **Model Training**:  
  - Use k-means clustering with 5 time-based clusters.  
  - Combine vegetation index and image data to detect forest loss.  
  - Add more features as the project progresses.

- **Model Evaluation**:  
  - Check how well the model predicts real deforestation.  
  - Compare predicted and actual results to assess performance.

### Resources

- [Global Forest Watch](https://www.globalforestwatch.org/)  
- [Google Earth Engine](https://earthengine.google.com/)  
- [Google Earth Engine API Docs](https://developers.google.com/earth-engine)  
- [Interesting Paper](https://arxiv.org/pdf/1803.02489)  
- More resources will be added as we find them.

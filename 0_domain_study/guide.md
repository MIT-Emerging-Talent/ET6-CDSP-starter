# Domain Study: Guide

To do meaningful research in a domain, you need to learn what others already do
and don't understand in this area. Use this folder to organize your group's
understanding of your research domain including: your own summaries, helpful
PDFs, links you found helpful, ...

This folder is different from `/notes` because it contains _only_ information
about your research domain. When deciding what goes here, ask yourself this
question: _Would someone need to know this to understand our research?_

## README.md

Use this folder's README to document all the notes and resources in this folder.
Someone shouldn't need to read through _everything_ to find what they need.

## Chosen Question

How effective is Satellite Image Analysis at Predicting Deforestation in Malaysia?

### Why this question?

Malaysia is one of the largest forested countries in the world,
and deforestation has proven to be a major issue. A quick look
at the Global Forest Watch website shows that Malaysia has seen a 31% decrease
in tree cover since 2000.
The need for proactive measures to monitor and predict deforestation
is crucial for conservation efforts. If satellite image analysis
can be used to predict deforestation, it can play a significant (and cheap)
role in conservation efforts.

### Satellite Image Analysis

Satellite image analysis involves using satellite imagery to monitor and analyze
various aspects of the Earth's surface, including land use, vegetation cover,
and environmental changes.

Image resolution plays a crucial role in the effectiveness of satellite image analysis.
Higher resolution images provide more detailed information, allowing for better
and more accurate analysis. However,
they also require exponentially more storage space and processing power/time.

Likely to use Landsat images which have a resolution of 30m and
are available for free from Google Earth Engine. They are also captured
every 16 days, which is a good balance between resource
demands and accuracy for our needs.

Important to note that there are satellite images with higher resolution (3m)
captured daily, such as those by PlanetScope, but they are not free.
They would also require too many resources to fit into our timeframe.
They might be interesting for future research as 3m resolution
images can track individual trees.

### Rough Plan

- **Data Collection**: Gather satellite images and vegetation index data from Google
Earth Engine and Global Forest Watch.
  - For Vegetation index, it is pretty easy to get the data from Global Forest Watch.
  - For satellite images, we will use Google Earth Engine. We will need to make
accounts and get access to the data and API.
  We also need to write code to extract the images
  - Other data will be collected from various sources such as government
  agencies, environmental organizations, and academic institutions.
  Refer to resources for more details.

- Train a model using k-means clustering.
  - Group data into 5 clusters based on date.
  - Use vegetation index and satellite images to identify deforested areas.
  - May add more features to the model as we progress.
  - More details about the model will be added as we progress.

- Model Evaluation:
  - Evaluate the model's performance (accuracy of predictions).
  - Compare the model's predictions with actual deforestation data to assess its
  effectiveness.

### Resources

- [Global Forest Watch](https://www.globalforestwatch.org/)
- [Google Earth Engine](https://earthengine.google.com/)
- [Google Earth Engine API Documentation](https://developers.google.com/earth-engine)
- [Interesting Paper](https://arxiv.org/pdf/1803.02489)
- (Other resources as we find them)

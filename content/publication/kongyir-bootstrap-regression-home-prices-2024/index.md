---
title: "Bootstrap Regression for Investigating Macroeconomics Factors Affecting USA Home Prices"

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here 
# and it will be replaced with their full name and linked to their profile.
authors:
- admin
- Emil Agbemade

draft: false

# Author notes (optional)
# author_notes:
# - "Equal contribution"
# - "Equal contribution"

date: "2024-12-06T00:00:00Z"
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: "2024-12-06T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: 
 - "2"

# Publication name and optional abbreviated publication name.
publication: ''
publication_short: ''

abstract: This study investigates the impact of macroeconomic indicators on US home prices, underscoring the importance of understanding these dynamics due to their significant socio-economic consequences. Utilizing a dataset from Kaggle, originally collected by FRED, the research examines variables such as the Consumer Price Index, Population, Unemployment, GDP, Stock Prices, Income, and Mortgage Rates to discern their effect on housing market fluctuations. The analysis identifies multicollinearity among predictors, necessitating a shift from traditional multiple linear regression to a more robust bootstrap regression method due to violations of parametric assumptions. Key findings reveal that Real Disposable Income is a significant predictor of home prices, although the presence of multicollinearity complicates the model-building process. The bootstrap regression approach, favored for its resilience to assumption violations, confirms the influence of selected macroeconomic factors on home prices. The study concludes that bootstrap regression provides a reliable alternative to parametric methods in cases of assumption non-compliance and highlights the critical role of addressing multicollinearity in regression analysis. This research provides valuable insights for stakeholders involved in the housing market, highlighting the importance of careful econometric modeling in informing economic policy and investment decisions.

# Summary. An optional shortened abstract.
summary: ''

tags: []
categories: []

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: https://stars.library.ucf.edu/cgi/viewcontent.cgi?article=1017&context=data-science-mining
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'diagnostic plot'
  focal_point: Smart
  placement: 1
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
# projects:
# - example

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---

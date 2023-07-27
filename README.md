
# NBA Prediction

Predict future NBA games using machine learning techniques.



# How to run it

You should start with saving the dataset from :

```bash
  datasetSave.py

```
If you want a larger or smaller dataset you can change the seasonal values
```python
#----------------------------#
season = 2023
prevSeason = 2017 
```

When the process is complete, you should find a file in your folder with the following name:
> "NBAGamesBetween2017-2023.csv"。



Then you should do EDA and feature engineering on the dataset and have a machine learning model for predictions. To do this, run this file:

```bash
  modelTraining.ipynb
```

Now you should have your own "model_pkl" file. For future predictions, run the "main.py" file. From this UI you can make predictions about the future games of the NBA


  

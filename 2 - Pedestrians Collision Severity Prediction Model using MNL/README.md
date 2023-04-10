# Pedestrians Collision Severity Prediction Model using MNL

This code provides a pedestrian collision severity prediction model using Multinomial Logit (MNL) regression. The model is developed to predict the severity of pedestrian collisions based on several factors including speed, age, location, and daylight conditions. The dataset used in this model is provided in a .csv format and must have headers included in the first row. The data used for this project is from Toronto Police Services collision data. This data is managed by the Data & Analytics unit and consists of records for collisions that have occurred within the City of Toronto. You can use this code for any other datasets with the same attributes. You may need to tweak the code to account for differences between dataset. 

## Dependencies

This code requires the apollo package for MNL modeling. If not already installed, this package can be installed using the following command:

```install.packages("apollo")```

## Getting Started

1. Clone this repository to your local machine.
2. Set the working directory to the cloned repository directory.
3. Load the apollo package and the dataset.csv file provided with the code.
4. Follow the comments in the code to initialize the MNL code package, set the core controls, define the model parameters,
5. validate the input data, define the model and the likelihood function, estimate the model, and print and explore the model outputs

## References

For more information about the MNL model and the apollo package, please refer to the following sources:

* https://en.wikipedia.org/wiki/Multinomial_logistic_regression
* https://cran.r-project.org/web/packages/apollo/index.html




__Feel free to use and modify this application for your own purposes, as long as you give credit to the original author. Copyright © 2023 Saeid Tayebikhorami. All rights reserved.__ 

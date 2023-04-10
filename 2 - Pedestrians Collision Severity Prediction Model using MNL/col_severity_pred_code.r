####################################################
####################################################
## Pedestrians Collision Severity Prediction Model #
##################### MNL Model ####################
####################################################

# Remove all the objects from the workspace 
rm(list = ls())

# Install the 'Apollo' package for MNL Modeling
install.packages("apollo")
library(apollo)

# Set the working directory
setwd("F://CoT//submit")

# Read in the core dataset in .csv format 
# The first row include headers 
database <- read.csv(file="dataset.csv", header=TRUE, sep=",")


################### Step 1 #########################
# Initialize the MNL Code Package 
apollo_initialise()

################### Step 2 #########################
# Set the core controls  
# The first column include IDs
apollo_control = list(
  modelName = "Col_sev_pred",
  modelDescr = "Collision Severity Prediction",
  indivID = "ID"
)

################### Step 3 #########################
# Define the model parameters and set the starting value
apollo_beta=c(b1_speed   = 0,
              b1_age = 0,
              b1_location = 0,
              b1_daylight = 0,
              
              b2_speed   = 0,
              b2_age = 0,
              b2_location = 0,
              b2_daylight = 0,
              
              #constants
              asc_none = 0, 
              asc_minor = 0, 
              asc_major = 0 
              )

# Define the model parameters that will be fixed to the starting values
apollo_fixed = c("asc_none")

################### Step 4 #########################
# Validate the input data to ensure that there are no errors
apollo_inputs = apollo_validateInputs()

################### Step 5 #########################
# Define the model and the likelihood function
apollo_probabilities=function(apollo_beta, apollo_inputs, functionality="estimate"){
  
  ### Attach inputs and detach after function exit
  apollo_attach(apollo_beta, apollo_inputs)
  on.exit(apollo_detach(apollo_beta, apollo_inputs))
  
  ### Create list of probabilities P
  P = list()
  
  ### List of utilitiy functions: these must use the same names as in mnl_settings, order is irrelevant
  V = list()
  V[['none']]  = asc_none
          
  V[['minor']] = asc_minor + b1_speed*speed +b1_age*age + b1_location*location + b1_daylight*daylight
  
  V[['major']] = asc_major +  b2_speed*speed +b2_age*age + b2_location*location + b2_daylight*daylight
  
  
  ### Define settings for MNL model component
  mnl_settings = list(
    alternatives  = c(none=1, minor=2, major=3) ,  
    choiceVar     = severity,
    V             = V
  )
  
  ### Compute probabilities using MNL model
  P[['model']] = apollo_mnl(mnl_settings, functionality)
  
  ### Prepare and return outputs of function
  P = apollo_prepareProb(P, apollo_inputs, functionality)
  return(P)
}


################### Step 6 #########################
# Estimate the model
MNL_model = apollo_estimate(apollo_beta, apollo_fixed, apollo_probabilities, apollo_inputs,
                            estimate_settings = list (bootstrapSE = 0))

################### Step 7 #########################
# Print the model outputs
output <- apollo_modelOutput(MNL_model)

################### Step 8 #########################
### Explore the model outputs
# Print the variance-covariance matrix
varcov <-MNL_model$varcov

# Print the parameter estimates
MNL_model$estimate

# Save the model outputs
apollo_saveOutput(MNL_model)


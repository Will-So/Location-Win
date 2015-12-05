# The App
The app consists of two parts:

1. The app that end users will use in order to get advice on the best business to start. This includes:
    - A page that asks the users some questions about the business they want to start
        - Refreshes automatically with AJAX when a City or Business is changed
        - More details are available if more details is pushed
    
2. Web app that goes into more details showing descriptive stats meant to diagnose the results from (1). This includes:
    - LDA topic importance
    - A descriptive statistics pane
    - A history pane that shows what others have logged.
    - A list of features and their relative performance